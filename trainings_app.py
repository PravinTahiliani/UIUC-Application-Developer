import json
import os
from datetime import datetime, timedelta
from collections import defaultdict

# Load data from the given JSON file
def load_data(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    
    with open(file_path, 'r') as file:
        return json.load(file)

# Task 1: Count how many people have completed each training
def count_completed_trainings(data):
    training_count = defaultdict(int)
    
    for person in data:
        unique_trainings = set()
        for completion in person["completions"]:
            unique_trainings.add(completion["name"])
        for training in unique_trainings:
            training_count[training] += 1
    
    return [{"training": k, "count": v} for k, v in training_count.items()]

# Task 2: List people who completed specific trainings in a fiscal year
def list_people_completed_in_fy(data, trainings, fiscal_year):
    start_date = datetime(fiscal_year - 1, 7, 1)
    end_date = datetime(fiscal_year, 6, 30)
    
    result = defaultdict(list)
    
    for person in data:
        for completion in person["completions"]:
            training_date = datetime.strptime(completion["timestamp"], "%m/%d/%Y")
            if completion["name"] in trainings and start_date <= training_date <= end_date:
                result[completion["name"]].append(person["name"])
    
    return [{"training": training, "people": people} for training, people in result.items()]

# Task 3: List all people with expired or expiring trainings
def list_expiring_or_expired_trainings(data, reference_date):
    ref_date = datetime.strptime(reference_date, "%m/%d/%Y")
    soon_threshold = ref_date + timedelta(days=30)
    
    result = defaultdict(list)
    
    for person in data:
        for completion in person["completions"]:
            if completion["expires"]:
                expire_date = datetime.strptime(completion["expires"], "%m/%d/%Y")
                if expire_date < ref_date:
                    status = "expired"
                elif expire_date <= soon_threshold:
                    status = "expires soon"
                else:
                    continue
                result[person["name"]].append({
                    "training": completion["name"],
                    "completed_on": completion["timestamp"],
                    "expires_on": completion["expires"],
                    "status": status
                })
    
    return [{"person": person, "trainings": trainings} for person, trainings in result.items()]

# Write output to JSON files
def write_json(output_data, file_name):
    with open(file_name, 'w') as file:
        json.dump(output_data, file, indent=4)

if __name__ == "__main__":
    # Load the data from the JSON file
    data = load_data("trainings.txt")
    
    # Task 1: Generate the completed training counts
    completed_trainings = count_completed_trainings(data)
    write_json(completed_trainings, "completed_trainings.json")
    
    # Task 2: List people who completed specific trainings in the fiscal year 2024
    trainings = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]
    people_completed_fy2024 = list_people_completed_in_fy(data, trainings, 2024)
    write_json(people_completed_fy2024, "people_completed_fy2024.json")
    
    # Task 3: Find expired or soon-to-expire trainings by Oct 1st, 2023
    expiring_trainings = list_expiring_or_expired_trainings(data, "10/01/2023")
    write_json(expiring_trainings, "expiring_trainings.json")
    
    print("All tasks completed! Output saved to JSON files.")
