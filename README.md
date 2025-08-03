# Movie Recommender System

This is a full-stack movie recommender application built with Python and Streamlit. It enables users to explore movies and receive personalized recommendations based on precomputed similarity scores.

## Features

- Browse detailed movie information fetched dynamically via API.  
- Get movie recommendations based on similarity matrices computed from movie metadata.  
- User-friendly and interactive interface powered by Streamlit.  
- Fast and efficient recommendations using preprocessed datasets.

## Getting Started

### Prerequisites

- Python 3.7 or higher  
- pip package manager

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SacSresta/movie-recommender.git
    cd movie-recommender
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate    # On Linux/macOS
    venv\Scripts\activate       # On Windows
    ```

3. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Data Files

Download and unzip the following pickle files which contain essential data for the recommender:

- `movies_dict.pkl` — Movie metadata dictionary  
- `similarity.pkl` — Movie similarity matrix  

Make sure these files are correctly placed in the project directory before running the app.

## Usage

Run the Streamlit application with:

```bash
streamlit run app.py
