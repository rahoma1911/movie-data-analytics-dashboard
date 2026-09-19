import streamlit as st
import pandas as pd
import plotly.express as px
import os
import warnings
warnings.filterwarnings('ignore')

# Page settings
st.set_page_config(page_title="Statistical_Overview", page_icon="🎬", layout="wide")

st.markdown("""
    <style>
        div.block-container {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# The title with the local image
st.markdown("""
    <div style="display: flex; align-items: center; justify-content: center;">
        <h1 style="font-family: 'Courier New', Courier, monospace; font-weight: bold; font-size: 55px; margin-right: 0px;">Statistical Overview</h1>
    </div>
""", unsafe_allow_html=True)


# Add a logo to the sidebar
st.sidebar.image("moviel__1_-removebg-preview.png", width=200)  # Replace "path_to_logo.png" with the path to your own logo


# Load the data 
df = pd.read_csv("df1.csv")

# Sidebar filters
st.sidebar.header("Choose your filter:")


col1, col2= st.columns((2))

# Drop missing values and ensure movie_year is of integer type
df = df.dropna(subset=["movie_year"])
df["movie_year"] = df["movie_year"].astype(int)

# Keep only years > 0
df = df[df["movie_year"] > 0]

# Get sorted list of unique years
years = sorted(df["movie_year"].unique())

# Remove the last year from start_year options
start_years = years[:-1]  # all years except the last one
end_years = years          # all years are available as end

with col1:
    start_year = st.selectbox("Select Start Year", start_years, index=0)

with col2:
    end_year = st.selectbox("Select End Year", end_years, index=len(end_years)-1)

# Validate range
if start_year > end_year:
    st.warning("⚠️ Start year must be less than or equal to end year.")
    st.stop()  # stops the execution of the rest of the page

# Filter the data based on selected years
df = df[(df["movie_year"] >= start_year) & (df["movie_year"] <= end_year)].copy()

# Separator line 
st.markdown("""
    <style>
        .custom-hr {
            border: none;
            height: 2px;
            background: linear-gradient(to right, #F7418F, #FFCBCB, #3AA6B9);
            margin: 10px 0;
            border-radius: 5px;
        }
    </style>
    <hr class="custom-hr">
""", unsafe_allow_html=True)


# Filter ratings
ratings = sorted(df["user_rating"].unique())
selected_ratings = st.sidebar.multiselect("Pick Rating(s)", ratings)
if selected_ratings:
    df1 = df[df["user_rating"].isin(selected_ratings)]
else:
    df1 = df.copy()

# Filter genres
genre_columns = [
    "(no genres listed)", "Action", "Adventure", "Animation", "Children",
    "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir",
    "Horror", "IMAX", "Musical", "Mystery", "Romance", "Sci-Fi",
    "Thriller", "War", "Western"
]
selected_genres = st.sidebar.multiselect("Pick Genre(s)", genre_columns)

if selected_genres:
    genre_filter = df1[selected_genres].sum(axis=1) > 0
    filtered_df = df1[genre_filter]
else:
    filtered_df = df1.copy()

# Create Statistical Summary Table
summary_df = filtered_df.groupby(["movie_title", "movie_year"]).agg({
    "user_rating": ["count", "mean", "median", "std"],
    "movies_avg_rating": "mean"  # This will be used for Avg User Rating
}).reset_index()

# Rename columns
summary_df.columns = [
    "Movie Title", "Release Year", "Total Ratings",
    "Original User Rating Mean", "Median User Rating", "User Rating Std Dev",
    "Avg Rating"
]

# Drop "Original User Rating Mean" column
summary_df = summary_df.drop(columns=["Original User Rating Mean"])

# Display the table
st.markdown("<h3 style='text-align: center; font-size: 25px; font-family: \"Courier New\", Times, serif;'>Summary of Movies Statistical Data</h3>", unsafe_allow_html=True)
st.dataframe(summary_df.sort_values(by="Total Ratings", ascending=False).style.background_gradient(cmap="YlGnBu"))

# Download the table as CSV
csv = summary_df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download Summary", data=csv, file_name="Movie_Statistical_Summary.csv", mime='text/csv')

# Display Genre Ratings Summary by Year
st.markdown("<h3 style='text-align: center; font-size: 25px; font-family: \"Courier New\", Times, serif;'>Year-wise Genre Ratings Summary</h3>", unsafe_allow_html=True)
with st.expander("Summary Table:"):
    # Filter for genre columns
    genre_columns = [
        'Action', 'Adventure', 'Animation', 'Children', 'Comedy', 'Crime',
        'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'IMAX',
        'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western','(no genres listed)'
    ]

    # Use selected genres or all if none selected
    genres_to_use = selected_genres if selected_genres else genre_columns

    # Filter data to remove rows with year 0
    filtered_df = filtered_df[filtered_df['movie_year'] != 0]
    filtered_df["movie_year"] = filtered_df["movie_year"].astype(int)

    # Filter the data based on selected genres
    filtered_genres_df = filtered_df[["movie_year", "user_rating"] + genres_to_use]

    # Melt the dataframe to long format
    melted_df = filtered_genres_df.melt(
        id_vars=["movie_year", "user_rating"],
        value_vars=genres_to_use,
        var_name="Genre",
        value_name="is_present"
    )

    # Keep only present genres
    genre_data = melted_df[melted_df["is_present"] == 1]

    # Pivot table to calculate average ratings by genre and year
    pivot_table = pd.pivot_table(
        data=genre_data,
        values="user_rating",
        index="Genre",
        columns="movie_year",
        aggfunc="mean"
    )

    st.markdown("<h3 style='font-size: 15px; font-family: \"Courier New\", Times, serif;'>Average Rating by Genre and Year</h3>", unsafe_allow_html=True)
    st.write(pivot_table.style.background_gradient(cmap="YlGnBu"))

# Display Sample Data
st.markdown("<h3 style='text-align: center; font-size: 25px; font-family: \"Courier New\", Times, serif;'>Sample of Data</h3>", unsafe_allow_html=True)
# Display filtered data or full data if no filters applied
data_to_display = filtered_df if not filtered_df.empty else df

# Expandable section to view data
with st.expander("View Data"):
    st.write(data_to_display.head(500).style.background_gradient(cmap="Blues"))

# Download the full original data
csv = df.to_csv(index=False).encode('utf-8')
st.download_button('Download Data', data=csv, file_name="Data.csv", mime='text/csv')