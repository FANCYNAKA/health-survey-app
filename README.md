# Healthcare Survey App

## Project Overview
This project is a healthcare survey web application developed using Flask, MongoDB, Pandas, and Jupyter Notebook.

The application collects user information including:
- Age
- Gender
- Income
- Expense categories

Expense categories include:
- Utilities
- Entertainment
- School Fees
- Shopping
- Healthcare

Each category includes a spending amount field.

---

## Technologies Used
- Python
- Flask
- MongoDB
- Pandas
- Matplotlib
- Jupyter Notebook

---

## Features
- User data collection through Flask web forms
- MongoDB database storage
- CSV export functionality
- Data analysis using Pandas
- Data visualization using Matplotlib

---

## Files Included

| File | Description |
|---|---|
| app.py | Main Flask application |
| export_data.py | Exports MongoDB data to CSV |
| user.py | User class definition |
| survey_data.csv | Exported survey dataset |
| analysis.ipynb | Data analysis notebook |
| index.html | HTML form template |

---

## Visualizations
The notebook includes:
1. Average Income by Age
2. Gender Distribution Across Spending Categories

---

## How to Run

### Install Dependencies
```bash
pip install flask pymongo pandas matplotlib notebook
```

### Run Flask App
```bash
python app.py
```

### Run Export Script
```bash
python export_data.py
```

### Open Jupyter Notebook
```bash
jupyter notebook
```

---

## Author
Jane Fancy
