The trainings_app.py Python script processes training completion data from a JSON file (trainings.txt) and generates output in the following ways:

Task 1: Counts how many people have completed each unique training and stores the count in completed_trainings.json.
Task 2: For a specified list of trainings, it lists all people who completed each training during the fiscal year 2024 (defined as July 1st, 2023 – June 30th, 2024). Results are stored in people_completed_fy2024.json.
Task 3: Identifies people whose trainings have expired or will expire soon (within one month of a given date, in this case October 1st, 2023) and stores the results in expiring_trainings.json.

**File Structure**
Here’s the structure of the project:

trainings_app.py: The Python script that performs all the tasks.
trainings.txt: The JSON file containing training data (input).
completed_trainings.json: Output for Task 1, listing each training with the count of how many people completed it.
people_completed_fy2024.json: Output for Task 2, listing people who completed specific trainings during fiscal year 2024.
expiring_trainings.json: Output for Task 3, listing people whose trainings have expired or will expire soon (as of October 1st, 2023).

Explanation of the Tasks
**Task 1**: Count Completed Trainings
The application reads the trainings.txt file, which contains a list of people and their training completion records. For each unique training, it calculates how many people have completed it and writes the results to completed_trainings.json.

**Task 2**: List People Who Completed Trainings in Fiscal Year 2024
The application checks which people completed specific trainings (e.g., "Electrical Safety for Labs", "X-Ray Safety", and "Laboratory Safety Training") during fiscal year 2024, which runs from July 1st, 2023 to June 30th, 2024. The results are saved to people_completed_fy2024.json.

Task 3: Find Expired or Expiring Trainings
The application looks for trainings that either:
Have expired before October 1st, 2023.
Will expire within one month of October 1st, 2023.
It lists people whose trainings match these criteria and indicates whether the training is "expired" or "expires soon." The results are saved to expiring_trainings.json.

How to Run the Application
Prerequisites:
Ensure that you have Python 3.x installed on your system.
Steps:
Clone the repository:

bash
Copy code
git clone https://github.com/PravinTahiliani/UIUC-Application-Developer.git
cd UIUC-Application-Developer
Ensure that you have the correct files:

trainings_app.py (script)
trainings.txt (input data)
Run the script: To execute the application and generate the output files:

bash
Copy code
python trainings_app.py
Check the output: After running the script, the following JSON files will be generated in the same directory:

completed_trainings.json
people_completed_fy2024.json
expiring_trainings.json
Example Output
1. completed_trainings.json (Task 1):
This file lists each training with the number of people who completed it.

json
Copy code
[
    {
        "training": "Electrical Safety for Labs",
        "count": 1
    },
    {
        "training": "X-Ray Safety",
        "count": 2
    },
    ...
]
2. people_completed_fy2024.json (Task 2):
This file lists the people who completed specific trainings in fiscal year 2024.

json
Copy code
[
    {
        "training": "X-Ray Safety",
        "people": ["Asia Duke"]
    }
]
3. expiring_trainings.json (Task 3):
This file lists people whose trainings have expired or will expire soon.

json
Copy code
[
    {
        "person": "Cason Gross",
        "trainings": [
            {
                "training": "Using Hazardous Chemicals in an Animal Care Facility",
                "completed_on": "8/19/2023",
                "expires_on": "8/18/2024",
                "status": "expires soon"
            }
        ]
    }
]
Notes
The script can handle different training data in the same format as trainings.txt.
You can modify the fiscal year or date as needed for tasks 2 and 3 by adjusting the values within the script.
This README.md provides an overview of the project, explanation of the tasks, instructions for running the application, and expected outputs.
