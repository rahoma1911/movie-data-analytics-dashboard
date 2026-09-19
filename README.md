# 🎬 Movie Data Analytics Dashboard

An interactive multi-page **Streamlit dashboard** for exploring and analyzing MovieLens data through interactive visualizations and statistical summaries.

The dashboard provides insights into movie releases, ratings, genres, and rating patterns over time. Users can also filter the analysis by **movie release year, rating, and genre**.

---

## 📌 Overview

This project uses the **MovieLens dataset** as the original data source.

The dataset was processed and prepared before being used in the dashboard. The final processed dataset contains movie information, user ratings, movie-level rating statistics, release years, rating date/time features, and genre-related columns.

The dashboard is built using:

* Python
* Pandas
* Streamlit
* Plotly
* Matplotlib
* Seaborn

---

## ✨ Features

### 🏠 Main Dashboard

The main dashboard provides:

* Total number of movies
* Total number of users
* Total number of ratings
* Movies released per year
* Movies per genre
* Rating distribution
* Top-rated movies
* Bottom-rated movies
* Average rating by movie release year
* Number of ratings for each rating value
* Average rating by genre
* Rating distribution by:

  * Hour
  * Year
  * Month
  * Weekday
* Number of ratings vs. average rating per movie

### 📊 Statistical Overview

The statistical overview page provides:

* Statistical summary for each movie
* Total number of ratings
* Median user rating
* User rating standard deviation
* Average movie rating
* Year-wise average rating by genre
* Filtered sample data
* Downloadable statistical summary
* Downloadable filtered dataset

### 🔎 Interactive Filters

Users can filter the dashboard by:

* Movie release year range
* User rating
* Movie genre

The visualizations update based on the selected filters.

---

## 📂 Dataset Source

The project is based on the **MovieLens dataset** provided by GroupLens Research.

The original MovieLens dataset can be obtained from:

https://grouplens.org/datasets/movielens/

The dataset used in this project was downloaded and processed before being used by the dashboard.

> **Note:** The processed dataset (`df1.csv`) is not included in this repository because of its large file size.

---

## 🔄 Data Preprocessing

The dataset used in the dashboard has undergone **data preprocessing and preparation** before being used for analysis and visualization.

The final processed dataset was prepared in a format suitable for the dashboard and follows the schema documented in the **Final Dataset Schema** section below.

```text
MovieLens Data
      │
      ▼
Data Preprocessing
      │
      ▼
Final Processed Dataset
      │
      ▼
    df1.csv
      │
      ▼
Streamlit Dashboard
```

---

## 🧾 Final Dataset Schema

The current dashboard requires the following **30 columns** from the processed dataset.

### Movie & Rating Information

| Column              | Description                 |
| ------------------- | --------------------------- |
| `movieId`           | Unique movie identifier     |
| `userId`            | Unique user identifier      |
| `user_rating`       | Rating given by the user    |
| `movie_title`       | Movie title                 |
| `movies_avg_rating` | Average rating of the movie |
| `movie_year`        | Movie release year          |

### Rating Time Information

| Column  | Description                      |
| ------- | -------------------------------- |
| `year`  | Year associated with the rating  |
| `month` | Month associated with the rating |
| `day`   | Day associated with the rating   |
| `hour`  | Hour associated with the rating  |

### Genre Features

| Column               | Description     |
| -------------------- | --------------- |
| `(no genres listed)` | Genre indicator |
| `Action`             | Genre indicator |
| `Adventure`          | Genre indicator |
| `Animation`          | Genre indicator |
| `Children`           | Genre indicator |
| `Comedy`             | Genre indicator |
| `Crime`              | Genre indicator |
| `Documentary`        | Genre indicator |
| `Drama`              | Genre indicator |
| `Fantasy`            | Genre indicator |
| `Film-Noir`          | Genre indicator |
| `Horror`             | Genre indicator |
| `IMAX`               | Genre indicator |
| `Musical`            | Genre indicator |
| `Mystery`            | Genre indicator |
| `Romance`            | Genre indicator |
| `Sci-Fi`             | Genre indicator |
| `Thriller`           | Genre indicator |
| `War`                | Genre indicator |
| `Western`            | Genre indicator |

---

## 📁 Project Structure

```text
movie-data-analytics-dashboard/
│
├── Home.py
├── moviel__1_-removebg-preview.png
├── requirements.txt
├── .gitignore
├── README.md
│
└── pages/
    ├── Statistical_Overview.py
    └── moviel__1_-removebg-preview.png
```

### Main Files

**`Home.py`**
The main Streamlit dashboard containing the interactive visualizations and filters.

**`pages/Statistical_Overview.py`**
The statistical analysis page containing summary tables, genre/year analysis, and data download options.

**`moviel__1_-removebg-preview.png`**
The dashboard logo used in the Streamlit application.

**`requirements.txt`**
Contains the Python packages required to run the dashboard.

**`df1.csv`**
The processed dataset used by the dashboard. It is not included in the GitHub repository because of its large file size.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/movie-data-analytics-dashboard.git
```

### 2. Navigate to the project directory

```bash
cd movie-data-analytics-dashboard
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Windows:

```powershell
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

---

## 📥 Prepare the Dataset

The dashboard expects a processed file named:

```text
df1.csv
```

Place the file in the project root directory:

```text
movie-data-analytics-dashboard/
│
├── Home.py
├── df1.csv
├── moviel__1_-removebg-preview.png
├── requirements.txt
└── pages/
    ├── Statistical_Overview.py
    └── moviel__1_-removebg-preview.png
```

The `df1.csv` file should contain the **Final Dataset Schema** described above.

---

## ▶️ Run the Dashboard

From the project directory, run:

```bash
streamlit run Home.py
```

The dashboard will open in your browser.

---

## 🛠️ Technologies Used

| Technology | Purpose                                   |
| ---------- | ----------------------------------------- |
| Python     | Application development and data analysis |
| Pandas     | Data manipulation and analysis            |
| Streamlit  | Interactive dashboard                     |
| Plotly     | Interactive visualizations                |
| Matplotlib | Visualization support                     |
| Seaborn    | Visualization support                     |

---

## 📌 Notes

* The dashboard is designed around the processed `df1.csv` structure documented above.
* The processed dataset is not included in the repository because of its large file size.
* The original MovieLens dataset is the source of the data used in this project.
* The processed dataset may contain additional columns that are not required by the current dashboard.
* A compatible processed dataset following the documented schema is required to run the dashboard.

---

## 👩‍💻 Project

**Movie Data Analytics Dashboard**

Built with **Python, Pandas, Streamlit, and Plotly**.
