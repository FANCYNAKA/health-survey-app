from flask import Flask, render_template, request
from pymongo import MongoClient
from user import User

# Create Flask app
app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create database
db = client["healthcare_db"]

# Create collection
collection = db["survey_data"]


# Homepage route
@app.route('/')
def home():
    return render_template('index.html')


# Form submission route
@app.route('/submit', methods=['POST'])
def submit():

    # Basic user information
    age = request.form['age']
    gender = request.form['gender']
    income = request.form['income']

    # Expense categories
    utilities = request.form.get('utilities')
    utilities_amount = request.form.get('utilities_amount')

    entertainment = request.form.get('entertainment')
    entertainment_amount = request.form.get('entertainment_amount')

    school_fees = request.form.get('school_fees')
    school_fees_amount = request.form.get('school_fees_amount')

    shopping = request.form.get('shopping')
    shopping_amount = request.form.get('shopping_amount')

    healthcare = request.form.get('healthcare')
    healthcare_amount = request.form.get('healthcare_amount')

    # Create User object
    user = User(
        age,
        gender,
        income,
        utilities_amount,
        entertainment_amount,
        school_fees_amount,
        shopping_amount,
        healthcare_amount
    )

    # Display user information
    user.display_user_info()

    # Store data in dictionary
    user_data = {

        "age": age,
        "gender": gender,
        "income": income,

        "utilities": utilities,
        "utilities_amount": utilities_amount,

        "entertainment": entertainment,
        "entertainment_amount": entertainment_amount,

        "school_fees": school_fees,
        "school_fees_amount": school_fees_amount,

        "shopping": shopping,
        "shopping_amount": shopping_amount,

        "healthcare": healthcare,
        "healthcare_amount": healthcare_amount
    }

    # Insert data into MongoDB
    collection.insert_one(user_data)

    print("Data Saved to MongoDB")

    return "Form Submitted and Saved to MongoDB!"


# Run Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
