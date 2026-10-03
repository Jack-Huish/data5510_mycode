import json
import requests
import csv

DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

# Set up variables before being looped
highest_percentage = 0
highest_state = ""
highest_summary_month = ""
highest_summary_cases = 0
highest_population = 0

lowest_percentage = 100
lowest_state = ""
lowest_summary_month = ""
lowest_summary_cases = 0
lowest_population = 0

# Month names: needed to match the assignment output
month_names = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

# Loop through all states in states.csv
with open("states.csv") as file:
    reader = csv.reader(file)

    # This skips the header row. Google helped me find this function
    next(reader)

    for state_row in reader:
        state = state_row[0]
        population = int(state_row[1])

        params = {
            "$where": f"state='{state}' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
            "$order": "end_date ASC"
        }

        req = requests.get(BASE_URL, params=params)

        # Convert the request text to Python data types
        data = json.loads(req.text)

        # Save each state's raw JSON data
        with open(f"{state}.json", "w") as file:
            json.dump(data, file)

        print(f"State name: {state}")

        # Loop through dictionaries and pull out new_cases
        new_cases = []
        highest_cases = 0
        highest_date = ""

        # Find highest number of cases in one week
        for row in data:
            cases = int(float(row["new_cases"]))
            new_cases.append(cases)

            if cases > highest_cases:
                highest_cases = cases
                highest_date = row["end_date"]
                highest_date = highest_date[:10]

        # Average cases
        average_cases = sum(new_cases) / len(new_cases)
        print(f"Average number of new weekly cases for the entire state dataset: {average_cases:.2f}")

        # Print highest new number of cases
        print(f"Date with the highest new number of covid cases: {highest_date} ({highest_cases})")

        # make months
        months = {}

        for row in data:
            date = row["end_date"]
            next_week = int(float(row["new_cases"]))

            month = date[:7]

            # If loop given in class
            if month in months:
                months[month] += next_week
            else:
                months[month] = next_week

        # Find highest month
        highest_month_cases = 0
        highest_month = ""

        for month in months:
            if months[month] > highest_month_cases:
                highest_month_cases = months[month]
                highest_month = month

        # Turn 2022-01 into January 2022
        month_name = month_names[highest_month[5:7]]
        year = highest_month[:4]
        month_and_year = month_name + " " + year

        # Print highest month
        print(f"Month and Year, with the highest new number of covid cases: {month_and_year} ({highest_month_cases})")

        # Calculate percentage of population
        percentage = (highest_month_cases / population) * 100

        print(f"Month and Year, with highest new number, percentage of population: {percentage:.2f}% (Population: {population})")

        # Check for highest percentage across all states
        if percentage > highest_percentage:
            highest_percentage = percentage
            highest_state = state
            highest_summary_month = month_and_year
            highest_summary_cases = highest_month_cases
            highest_population = population

        # Check for lowest percentage across all states. Pretty much the same thing as before
        if percentage < lowest_percentage:
            lowest_percentage = percentage
            lowest_state = state
            lowest_summary_month = month_and_year
            lowest_summary_cases = highest_month_cases
            lowest_population = population

        print("--------------------------------------------")


# Summary 
print("==================== SUMMARY ACROSS ALL STATES ====================")

print("State with HIGHEST percentage of population during its highest month:")
print(f"{highest_state} - {highest_percentage:.2f}% in {highest_summary_month} ({highest_summary_cases} cases; Population: {highest_population})")

print()

print("State with LOWEST percentage of population during its highest month:")
print(f"{lowest_state} - {lowest_percentage:.2f}% in {lowest_summary_month} ({lowest_summary_cases} cases; Population: {lowest_population})")