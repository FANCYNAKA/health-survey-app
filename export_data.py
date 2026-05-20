from pymongo import MongoClient
import csv

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access database
db = client["healthcare_db"]

# Access collection
collection = db["survey_data"]

# Retrieve all records
data = collection.find()

# Create CSV file
with open("survey_data.csv", mode="w", newline="") as file:

    writer = csv.writer(file)

    # CSV Header
    writer.writerow([
        "Age",
        "Gender",
        "Income",
        "Utilities Amount",
        "Entertainment Amount",
        "School Fees Amount",
        "Shopping Amount",
        "Healthcare Amount"
    ])

    # Loop through MongoDB records
    for record in data:

        writer.writerow([
            record.get("age"),
            record.get("gender"),
            record.get("income"),

            record.get("utilities_amount"),
            record.get("entertainment_amount"),
            record.get("school_fees_amount"),
            record.get("shopping_amount"),
            record.get("healthcare_amount")
        ])

print("CSV File Created Successfully!")