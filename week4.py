# Task 1  done
# Write a Python script that: 
# 1) Reads the content of a .txt file. 
# 2) Splits the text into individual words using the split() function. 
# 3) Counts how many times each unique word appears. 
# 4) Displays the words with frequency higher than 3.

''' 
import string
def count_top_words(file_path, maxChar):

# Step 1: Read the file
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file ’{file_path}’ was not found.")
        return 
    
    # Step 2: Split text into words
    words = content.split()

    # Step 3: Clean the words (lowercase and remove punctuation)
    cleaned_words = [
        word.strip(string.punctuation).lower()
        for word in words if word.strip(string.punctuation)
    ] 

    # Step 4: Count word occurrences
    word_count = {}
    for word in cleaned_words:
        # Note that get method here has two argument. We use the second argument as a default v
        word_count[word] = word_count.get(word, 0) + 1

    # Step 5: Sort and get the top N most frequent words
    bigWords = [word for word in word_count if word_count[word]>maxChar]
    return bigWords

# Example usage
if __name__ == "__main__":
    file_name = "test.txt"
    top_words = count_top_words(file_name, maxChar=3)
    print(top_words)
'''
    
# Task 2 jest ok ale nie mam pliku sample.txt
# Write a program that reads every line of a text file and defines a new data type for each line with the following features:
# (a) The size of the line (number of characters)
# (b) The size of the line (number of words)
# (c) The number of integers in the line
# (d) The number of floating-point numbers in the line
# (e) The number of words that start with a capital letter
# Use an appropriate data structure to collect and store all the details for each line.
# Hint: To define a new data type, create a class that contains these features as its attributes.

'''
class LineStats:
    """
    A class to hold statistical details about a line of text.
    """
    def __init__(self, line_number, line_content):
        self.line_number = line_number
        self.content = line_content.strip()

        # Calculate stats
        self.char_count = len(self.content)
        self.word_count = self._count_words()
        self.integer_count = self._count_integers()
        self.float_count = self._count_floats()
        self.capitalized_words_count = self._count_capitalized_words()

    def _count_words(self):
        """Count words by splitting on whitespace."""
        return len(self.content.split())
    
    def _count_integers(self):
        count = 0
        for word in self.content.split():
            if word.isdigit():
                count += 1
        return count

        
    def _count_floats(self):
        """
        Count valid floating point numbers.
        A float must have one decimal point, digits before and after it.
        """
        count = 0
        for word in self.content.split():
            # Check if word has exactly one decimal point
            if word.count('.') == 1:
                left, right = word.split('.', 1)
                if left.isdigit() and right.isdigit():
                    count += 1

        return count
    def _count_capitalized_words(self):
        """Count words starting with a capital letter."""
        count = 0
        for word in self.content.split():
            if word and word[0].isupper():
                count += 1
        return count

    def __str__(self):
        return (f"Line {self.line_number}: "
            f"Characters={self.char_count}, Words={self.word_count}, "
            f"Integers={self.integer_count}, Floats={self.float_count}, "
            f"Capitalized Words={self.capitalized_words_count}")

def analyze_file(file_path):
    """
    Reads a file line by line and analyzes each line using LineStats.
    Returns a list of LineStats objects.
    """
    line_stats_list = []
    with open(file_path, 'r') as file:
        for i, line in enumerate(file, start=1):
            if line.strip(): # Ignore empty lines
                stats = LineStats(i, line)
                line_stats_list.append(stats)
    return line_stats_list

file_path = "sample.txt"

# Analyze the file
stats_list = analyze_file(file_path)

# Display results
for stats in stats_list:
    print(stats)
'''

# Task 3  
# Write a Python function that receives a textbook file and detects its genre. The genre should be defined using hard-coded keywords. 
# The function should analyze the textbook by counting the frequency of these keywords and determine the genre based on the highest keyword frequency. You may use the below keywords:
''' genres = {
"Science": ["experiment", "theory", "research", "physics",
"biology", "chemistry", "data", "analysis"],
"Mathematics": ["algebra", "geometry", "equation", "calculus",
"function", "theorem", "proof", "variable"],
"History": ["king", "war", "battle", "empire",
"revolution", "ancient", "historical", "dynasty"],
"Literature": ["poem", "novel", "character", "author",
"plot", "story", "literary", "narrative"],
"Computer Science": ["algorithm", "programming", "computer", "software",
"data", "network", "system", "code"]
} '''


'''
def detect_genre(file_path):
    # --- Step 1: Define hard-coded keywords for each genre ---
    genres = {
        "Science": ["experiment", "theory", "research", "physics",
        "biology", "chemistry", "data", "analysis"],
        "Mathematics": ["algebra", "geometry", "equation", "calculus",
        "function", "theorem", "proof", "variable"],
        "History": ["king", "war", "battle", "empire",
        "revolution", "ancient", "historical", "dynasty"],
        "Literature": ["poem", "novel", "character", "author",
        "plot", "story", "literary", "narrative"],
        "Computer Science": ["algorithm", "programming", "computer", "software",
        "data", "network", "system", "code"]
    }

    # --- Step 2: Read and clean the file content ---
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().lower()
    except FileNotFoundError:
        return "Error: File not found."
    
    # --- Step 3: Count keyword occurrences for each genre ---
    genre_scores = {}
    for genre, keywords in genres.items():
        score = 0
        for keyword in keywords:
            score += text.count(keyword) # count occurrences of each keyword
        genre_scores[genre] = score

    # --- Step 4: Determine the genre with the highest score ---
    detected_genre = max(genre_scores, key=genre_scores.get)

    # --- Step 5: Display results ---
    print("Keyword Scores by Genre:")
    for genre, score in genre_scores.items():
        print(f"{genre}: {score}")
    print(f"\nDetected Genre: {detected_genre}")
    return detected_genre

# --- Example Usage ---
if __name__ == "__main__":
    file_path = "/home/monik/Pulpit/mtu/data_analytics/Math.txt" # Replace with your file path
    detect_genre(file_path)
    '''

# Task 4 
# Use NumPy to generate random grades for 30 students where each student has 5 modules as follows: [’Math’, ’Science’, ’History’, ’English’, ’Art’]. Then:
# (a) Print the shape of the entire data.
# (b) Print the subjects.
# (c) Print the records of the first 5 students.
# (d) Print the average grade for each module along with the standard deviation.
# (e) Print the average grade for each student along with the sum of all marks for each student and the highest average among all students.
# (f) How many students got an average above 80 and how many got below 60?

'''
import numpy as np

def student_grade_analysis():

    # Task 1: Create grade data for 30 students across 5 subjects
    print("Part 1: Creating Grade Data ===")
    #np.random.seed(42) # For reproducible results

    # Create a 30x5 array of random grades (0-100)
    grades = np.random.randint(0, 101, size=(30, 5))
    subjects = ['Math', 'Science', 'History', 'English', 'Art']
                
    print(f"Grade matrix shape: {grades.shape}")
    print(f"Subjects: {subjects}")
    print(f"First 5 students’ grades:\n{grades[:5]}")

    # Task 2: Basic statistics
    print("\nPart 2: Basic Statistics ===")
    subject_means = np.mean(grades, axis=0)
    subject_stds = np.std(grades, axis=0)
    for i, subject in enumerate(subjects):
        print(f"{subject}: Mean = {subject_means[i]:.1f}, Std = {subject_stds[i]:.1f}")

    # Task 3: Student performance analysis
    print("\nPart 3: Student Performance ===")
    student_totals = np.sum(grades, axis=1)
    student_averages = np.mean(grades, axis=1)

    print(f"Student with highest total: Student #{np.argmax(student_totals) + 1}")
    print(f"Highest average score: {np.max(student_averages):.1f}")
    print(f"Class overall average: {np.mean(grades):.1f}")

    # Task 4: Boolean indexing and filtering
    print("\nPart 4: Filtering Students ===")
    excellent_students = grades[student_averages >= 80]
    struggling_students = grades[student_averages < 60]

    print(f"Excellent students (avg >= 80): {len(excellent_students)}")
    print(f"Struggling students (avg < 60): {len(struggling_students)}")

# Run the educational task
if __name__ == "__main__":
    student_grade_analysis()
'''
    

# Task 5 

# Write a Python function that opens a file and counts the number of positive and negative integers, 
# as well as positive and negative floating-point numbers, using the isdigit() function.

'''
def count_positive_negative_numbers(filename):

    positive_int_count = 0
    negative_int_count = 0
    positive_float_count = 0
    negative_float_count = 0

    try:
        # Read the whole file at once
        with open(filename, 'r') as file:
            content = file.read()

        # Split the entire content into words/tokens
        words = content.split()

        for word in words:
            # ---- Check for negative numbers ----
            if word.startswith('-'):
                num = word[1:]  # Remove the '-' for checking
                if num.isdigit():  
                    # Negative integer
                    negative_int_count += 1
                elif '.' in num:
                    parts = num.split('.')
                    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                        # Negative float
                        negative_float_count += 1
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return positive_int_count, negative_int_count, positive_float_count, negative_float_count

# Example usage
filename = "/home/monik/Pulpit/mtu/data_analytics/science.txt"  # Replace with your file path
result = count_positive_negative_numbers(filename)

if result:
    print(f"Positive int numbers: {result[0]}")
    print(f"Negative int numbers: {result[1]}")
    print(f"Positive float numbers: {result[2]}")
    print(f"Negative float numbers: {result[3]}")
'''

# Task 6 not done
# There is a text file containing information about some of the Olympics and World Cups. The information includes the year of the event, the start date, and the end date. 
# Read the text file line by line and create a 2D NumPy array with three columns, where each column stores a piece of information for each event.
# Once the NumPy array is created, calculate the duration of each event and add it as a fourth column in the array.
#  Finally, print the complete NumPy array.

'''
import numpy as np
from datetime import date

def load_data_to_numpy(filename):
    data = []
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            part = line.split()
            if len(part) < 3:
                raise ValueError(f"Invalid line format: {line}")
            
            year = int(part[0])
            start_date = date(*map(int, part[1].split('-')))
            end_date = date(*map(int, part[2].split('-')))
            
            data.append([year, start_date, end_date])

    # Convert to NumPy array
    numpyArray = np.array(data, dtype=object)

    # Calculate duration (End - Start)
    duration = (numpyArray[:, 2] - numpyArray[:, 1]).astype('timedelta64[D]').astype(int)

    # Reshape and append as a new column
    duration = duration.reshape(-1, 1)
    numpyArray = np.append(numpyArray, duration, axis=1)
                   
    return numpyArray

# Example usage
if __name__ == "__main__":
    filename = "/home/monik/Pulpit/mtu/data_analytics/sports.txt"
    result = load_data_to_numpy(filename)
    print(result)
'''