# Workers Salary Prediction Model

This repository contains a machine learning project for predicting workers' salaries based on features such as Age, Education Level, Years of Experience, Gender, and Job Title. The project demonstrates the full workflow, from data exploration and preprocessing to model training, evaluation, and deployment as a Flask web application.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API](#api)
- [Model Training](#model-training)
- [Visualizations](#visualizations)
- [License](#license)

---

## Overview

This project uses a salary dataset to develop a regression model that predicts salary based on various features. The workflow includes data cleaning, exploratory data analysis (EDA), feature engineering, model training (with scikit-learn), evaluation, and deployment using Flask.

The repository includes:
- Jupyter notebook (`Sal.ipynb`) for data analysis and model development.
- Flask app (`app.py`) for serving predictions via a REST API.
- Pickled model pipeline (`salary.pkl`) for deployment.

---

## Features

- **End-to-end ML pipeline**: Data cleaning, EDA, feature encoding, training, evaluation, and inference.
- **Interactive visualizations**: Explore how features like Education Level, Gender, Job Title, Age, and Years of Experience impact salary.
- **REST API**: Flask-based web app for predicting salaries from JSON input.
- **Reusable model pipeline**: Includes preprocessing and regression steps.

---

## Project Structure

```
.
├── app.py              # Flask application for serving predictions
├── Sal.ipynb           # Jupyter Notebook with data analysis and modeling
├── salary.pkl          # Saved model pipeline (pickle file)
├── templates/
│   └── index.html      # (If present) Frontend for the Flask app
├── README.md           # This file
└── (other files)
```

---

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/your_username/salary-prediction.git
    cd salary-prediction
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    _Main packages:_ `numpy`, `pandas`, `scikit-learn`, `flask`, `seaborn`, `matplotlib`, `pickle`

3. **Model File**
   - Ensure `salary.pkl` is present in the project root. If not, open `Sal.ipynb` and retrain/export the model.

4. **Run the Flask app**
    ```bash
    python app.py
    ```
    The app will run on `http://127.0.0.1:5000/`

---

## Usage

### API Example

**Endpoint**: `POST /predict`

**Request (JSON):**
```json
{
  "age": 30,
  "education_level": "Bachelor's",
  "Years of Experience": 5
}
```

**Response:**
```json
{
  "Salary": 75000.0
}
```

### Web Interface

If an `index.html` template is provided, visit `http://127.0.0.1:5000/` in your browser for a simple web UI.

---

## Model Training

All data analysis, cleaning, feature engineering, and model training steps are in the `Sal.ipynb` notebook. You can experiment with different algorithms, handle missing values, explore feature importance, and visualize relationships.

_Preprocessing includes:_
- Dropping missing and duplicate rows
- One-hot encoding categorical variables
- Linear regression modeling (can be changed)
- Model evaluation (R2, MSE, MAE)

---

## Visualizations

The notebook includes visualizations such as:
- Salary vs. Education Level
- Salary vs. Gender
- Salary vs. Job Title
- Salary vs. Years of Experience (line plot)
- Salary vs. Age (scatter plot)

These help to understand feature relationships and dataset characteristics.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- Inspired by typical ML regression pipelines.
- Sample data structure:
    - Age, Gender, Education Level, Job Title, Years of Experience, Salary

---

**Feel free to fork and adapt for your own salary or regression prediction projects!**
