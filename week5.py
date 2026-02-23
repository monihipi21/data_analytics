# Task 1

# In the bikeSharing file, you will notice that the following columns in the dataset are normalized:
# • temp : Normalized temperature in Celsius. The values are divided to 41 (max)
# • atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
# • hum: Normalized humidity. The values are divided to 100 (max)
# • windspeed: Normalized wind speed. The values are divided to 67 (max)

# Your objective is to produce a new NumPy array. The new NumPy array should be a copy of the old one with the real-values replacing the normalized values for each of the above columns.

# Note: You can use the below syntaxt to write a numpy array into a new CSV file: 
#  np.savetxt("deNormalized.csv", denormalized_data, fmt=’%.2f’, delimiter=’,’)

'''
import numpy as np

def DeNormalize():

    # Load the dataset into a NumPy array
    # In practice, you can use np.loadtxt() or np.genfromtxt() to load data from a CSV.

    data = np.genfromtxt('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv', delimiter=',', skip_header=1)

    # Column indices for the normalized columns
    temp_index = 9
    atemp_index = 10
    hum_index = 11
    windspeed_index = 12

    # Create a copy of the original data to preserve the original values
    denormalized_data = data.copy()

    # De-normalize the columns by multiplying them by their maximum values
    denormalized_data[:, temp_index] *= 41
    denormalized_data[:, atemp_index] *= 50
    denormalized_data[:, hum_index] *= 100
    denormalized_data[:, windspeed_index] *= 67

    # Print the resulting NumPy array with real values
    print(denormalized_data)
    np.savetxt("deNormalized.csv", denormalized_data, fmt='%.2f', delimiter=',')
DeNormalize()

'''


# Task 2
# Read the bikeshare dataset from a CSV file using NumPy. Divide the dataset into three equal sections (by rows):
# Section 1: The first one-third of the rows.
# Section 2: The second one-third of the rows.
# Section 3: The last one-third of the rows.
# Create a new NumPy array containing only Section 1 and Section 3. Save this new array into a new CSV file named newBike.csv.

'''
import numpy as np
import os

def extractFromFile():
    # Pobierz folder, w którym jest aktualny skrypt
    folder = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(folder, 'bikeSharing.csv')

    # Wczytaj plik
    data = np.loadtxt(filepath, delimiter=',', skiprows=1)

    # Podziel dane na sekcje
    total_rows = data.shape[0]
    section_size = total_rows // 3
    section1 = data[:section_size]
    section3 = data[2 * section_size:]
    newArray = np.vstack((section1, section3))

    # Zapisz nowy plik w tym samym folderze
    newfile = os.path.join(folder, 'newBike.csv')
    np.savetxt(newfile, newArray, fmt='%.2f', delimiter=',')

    print(f"New CSV file '{newfile}' created successfully!")

# Wywołanie funkcji
extractFromFile()
'''



# Task 3
# Repeat the previous question and this time, analyse the tempreture and causal users as follows:
# • Load the CSV data.
# • Split the dataset into three equal sections.
# • Calculate average temperature and average casual users for each section.
# • Return the results and print a basic interpretation

'''
import numpy as np

def analyze_bikeshare(file_path):

    temp_col_index = 9  # Index of temperature
    casual_col_index = 13  # Index of casual users

    # Step 1: Load the dataset
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)

    # Step 2: Get total rows and determine section size
    total_rows = data.shape[0]
    section_size = total_rows // 3  # integer division for three equal sections

    # Step 3: Split data into three sections
    section1 = data[:section_size]
    section2 = data[section_size:2 * section_size]
    section3 = data[2 * section_size:]

    # Step 4: Calculate averages
    averages = {
        "temperature": {
            "section1": np.mean(section1[:, temp_col_index]),
            "section2": np.mean(section2[:, temp_col_index]),
            "section3": np.mean(section3[:, temp_col_index]),
        },
        "casual_users": {
            "section1": np.mean(section1[:, casual_col_index]),
            "section2": np.mean(section2[:, casual_col_index]),
            "section3": np.mean(section3[:, casual_col_index]),
        }
    }

    # Step 5: Print results
    print("\n--- Average Temperature per Section ---")
    for sec, val in averages["temperature"].items():
        print(f"{sec.capitalize()}: {val:.2f}")
    
    print("\n--- Average Casual Users per Section ---")
    for sec, val in averages["casual_users"].items():
        print(f"{sec.capitalize()}: {val:.2f}")
    
     # Step 6: Interpret results
    casual_users = list(averages["casual_users"].values())
    if casual_users[0] < casual_users[1] < casual_users[2]:
        interpretation = "Casual users increase over time, possibly due to warmer weather or growing popularity."
    elif casual_users[0] > casual_users[1] > casual_users[2]:
        interpretation = "Casual users decrease over time, which might indicate seasonal decline or reduced demand."
    else:
        interpretation = "The pattern of casual users does not follow a simple increasing or decreasing trend."
    
    print("\n--- Interpretation ---")
    print(interpretation)

    # Step 7: Return results
    return {
        "averages": averages,
        "interpretation": interpretation
    }

    # Example usage:
result = analyze_bikeshare('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv')
'''




# Task 4
# Read the bikeshare dataset from a CSV file into a NumPy array. Split the dataset into multiple sections, where: Each section contains 1000 rows (records),
# Except for the last section, which may contain fewer than 1000 rows. Store all sections in a Python list.
# Use a for loop to iterate over each section and: 
# 1) Calculate the average feeling temperature for that section. 
# 2) Calculate the average number of casual users for that section. 
# 3) Print the results for each section and observe any patterns, e.g., trends or seasonal effects

'''
import numpy as np

def analyze_bikeshare_in_chunks(file_path, chunk_size=1000):

    feel_temp_col_index=10
    casual_col_index=13

    # Step 1: Load data (skip header row if CSV has one)
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)

    # Step 2: Split data into chunks
    sections = []
    for i in range(0, len(data), chunk_size):
        sections.append(data[i:i + chunk_size])

    print(f"Total sections created: {len(sections)}")

    # Step 3: Calculate averages for each section
    results = []
    for idx, section in enumerate(sections, start=1):
        avg_feel_temp = np.mean(section[:, feel_temp_col_index])
        avg_casual_users = np.mean(section[:, casual_col_index])
        
        results.append({
            "section": idx,
            "avg_feeling_temp": avg_feel_temp,
            "avg_casual_users": avg_casual_users
        })
        
        print(f"\nSection {idx}:")
        print(f"  Average Feeling Temperature: {avg_feel_temp:.2f}")
        print(f"  Average Casual Users: {avg_casual_users:.2f}")

    # Step 4: Interpretation (basic trend check for casual users)
    casual_values = [res["avg_casual_users"] for res in results]
    if casual_values == sorted(casual_values):
        print("\nPattern Observed: Casual users tend to increase over time.")
    elif casual_values == sorted(casual_values, reverse=True):
        print("\nPattern Observed: Casual users tend to decrease over time.")
    else:
        print("\nPattern Observed: Casual users show mixed or seasonal variation.")

    return results

results = analyze_bikeshare_in_chunks('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv')

'''


# Task 5
# Read the bikeshare dataset from a CSV file into a NumPy array. For each record (row), calculate the difference between registered and casual users:
# difference = registered - casual
# Store this calculated difference as a new column. Append this new column to the original data to create an updated 2D NumPy array.
# Write the updated array into a new CSV file named newBike.csv

'''
import numpy as np

def add_difference_column(file_path, outtotal_rows = data.shape[0]
    section_size = total_rows // 3put_file='newBike.csv'):

    casual_col_index = 13  # Index for casual users
    registered_col_index = 14  # Index for registered users
    
    # Step 1: Load dataset (skip the header row if present)
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)

    # Step 2: Compute the difference (registered - casual) for each record
    difference = data[:, registered_col_index] - data[:, casual_col_index]
    
    # Step 3: Reshape difference into a column vector
    difference = difference.reshape(-1, 1)

     # Step 4: Append the new column to the original data
    updated_data = np.hstack((data, difference))

    # Step 5: Save the updated data into a new CSV file
    np.savetxt(output_file, updated_data, delimiter=',', fmt='%.2f')

    print(f"Updated data saved successfully to '{output_file}'")
    return updated_data

updated_array = add_difference_column('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv', output_file='newBike.csv')
'''



# Task 6
# Read the bikeshare dataset from a CSV file into a NumPy array. Remove the first column (usually representing an index, date, or ID).
# Save the remaining data into a new CSV file named newBike.csv.

'''
import numpy as np

def remove_first_column(file_path, output_file='newBike.csv'):
    # Step 1: Load dataset (skip the header row if present)
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)

    # Step 2: Remove the first column using slicing
    updated_data = data[:, 1:]  # keep all rows, columns from index 1 onward

    # Step 3: Save the updated data into a new CSV file
    np.savetxt(output_file, updated_data, delimiter=',', fmt='%.2f')
      
    print(f"Updated data saved successfully to '{output_file}'")
    return updated_data

# Example usage:
result = remove_first_column('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv', output_file='newBike.csv')

'''


# Task 7
# Implement a Python function using NumPy to perform the following task: A text file should be analyzed so that each line is processed separately.
#  For each line, extract the following information:
    # • Number of words
    # • Number of punctuation marks
    # • Number of spaces
    # • Number of numerical components (including both integers and floats)
# The results should be stored in a CSV file, where: Each row represents one line from the text file Each column represents one of the extracted metrics listed above

# Note: NumPy has a useful function called isin() (e.g., np.isin()). This function takes two arguments, typically two arrays or lists.
# The items of the first array are checked against the items in the second array. The result is a boolean array with the same shape as the first array. 
# Each value in the boolean array is True if the corresponding value in the first array exists in the second array, and False otherwise.

# Note: If you have a boolean array, you can count how many True values exist in the array or list using the sum() function. For example:
# myArray.sum()

# Notes / Clarifications: In NumPy, True is treated as 1 and False as 0, so summing the boolean array gives the count of True values.


'''
import numpy as np
import string

# Function to check if a string is a valid number (int or float)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def analyze_text_file(input_file, output_csv):
    # Define punctuation characters
    punctuation_set = set(string.punctuation)

     # Store results for all lines
    results = []

   # Read the file line by line
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip('\n')

            # Convert line into a numpy array of characters for vectorized operations
            char_array = np.array(list(line))

            # 1. Count words
            words = line.split()
            num_words = len(words)

            # 2. Count punctuations
            num_punctuations = np.isin(char_array, list(punctuation_set)).sum()

            # 3. Count spaces
            num_spaces = line.replace(' ', '')
            num_spaces = len(line)-len(num_spaces)

            # 4. Count numerical components (tokens that are numbers)
            num_numerical_components = sum(is_number(word) for word in words)

            # Append the results for this line
            results.append([
                num_words,
                num_punctuations,
                num_spaces,
                
                num_numerical_components
            ])

    # Convert results to numpy array
    results_array = np.array(results, dtype=int)
    np.savetxt(output_csv, results_array, delimiter=',', fmt='%.2f')     

    print(f"Analysis complete. Results saved to {output_csv}")

 # Example usage
analyze_text_file('/home/monik/Pulpit/mtu/data_analytics/AnimalFarm.txt', 'output.csv')   
'''


import numpy as np

def analyze_health_data(file_path):
    # Wczytanie danych, pomijamy nagłówek
    data = np.genfromtxt(file_path, delimiter=',', dtype=str, skip_header=1)

    # Kolumny (przykładowe indeksy - dostosuj do swojego pliku!)
    ages = data[:, 0].astype(float)
    genders = data[:, 1]
    bmi = data[:, 2].astype(float)
    blood_pressure = data[:, 3].astype(float)
    cholesterol = data[:, 4].astype(float)
    blood_sugar = data[:, 5].astype(float)

    # (a) średni wiek dla płci
    male_mask = np.char.lower(genders) == 'male'
    female_mask = np.char.lower(genders) == 'female'

    avg_age_male = np.mean(ages[male_mask])
    avg_age_female = np.mean(ages[female_mask])

    print(f"Average male age: {avg_age_male:.2f}")
    print(f"Average female age: {avg_age_female:.2f}\n")

    # (b) grupy wiekowe i analiza BP i cholesterolu
    groups = {
        "Group_0_35": (ages <= 35),
        "Group_36_50": (ages >= 36) & (ages <= 50),
        "Group_51_70": (ages >= 51) & (ages <= 70),
        "Group_above_70": (ages > 70)
    }

    for name, mask in groups.items():
        if np.any(mask):
            avg_bp = np.mean(blood_pressure[mask])
            avg_chol = np.mean(cholesterol[mask])
            if avg_bp > 95 and avg_chol > 200:
                print(f"{name} matches the conditions (avg BP={avg_bp:.2f}, avg Chol={avg_chol:.2f})")

    # (c) BMI i cukier we krwi — analiza korelacji
    groups = {
        "Group_0_35": (ages <= 35),
        "Group_36_45": (ages >= 36) & (ages <= 45),
        "Group_46_55": (ages >= 46) & (ages <= 55),
        "Group_56_65": (ages >= 56) & (ages <= 65),
        "Group_66_75": (ages >= 66) & (ages <= 75),
        "Group_above_75": (ages > 75)
    }

    avg_bmi_per_group = []
    avg_sugar_per_group = []

    print("\nAverages per age group:")
    for name, mask in groups.items():
        if np.any(mask):
            avg_bmi = np.mean(bmi[mask])
            avg_sugar = np.mean(blood_sugar[mask])
            avg_bmi_per_group.append(avg_bmi)
            avg_sugar_per_group.append(avg_sugar)
            print(f"{name}: avg BMI = {avg_bmi:.2f}, avg Blood Sugar = {avg_sugar:.2f}")

    if len(avg_bmi_per_group) > 1:
        correlation = np.corrcoef(avg_bmi_per_group, avg_sugar_per_group)[0, 1]
        print(f"\nCorrelation between BMI and Blood Sugar: {correlation:.2f}")

        if correlation > 0.5:
            print("Higher BMI → higher blood sugar")
        elif correlation > 0.2:
            print("Slight correlation (higher BMI → a bit higher sugar)")
        elif correlation < -0.2:
            print("Higher BMI → lower blood sugar")
        else:
            print("No significant correlation")

# Uruchomienie
analyze_health_data('/home/monik/Pulpit/mtu/data_analytics/health.csv')


