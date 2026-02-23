# For each of the following questions you will use a dataset containing information on global shark attacks (attacks.csv). 
# ttribute Information: The attributes recorded in the dataset are as follows: 
# 1. Case Number 2. Date 3. Year 4. Type 5. Country 6. Area 7. Location 8. Activity 9. Name 10. Sex 11. Age 12. Injury 13. Fatal (Y/N) 14. Time 15. Species 16. Investigator or Source

# Task 1
# What location globally has the highest number of shark attacks?

'''
import pandas as pd
import numpy as np

def Q1():
    # he encoding="ISO-8859-1" (also known as Latin-1) is used in pandas.Ten wariant jest używany, gdy plik zawiera znaki spoza ASCII
    df = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/attacks.csv', encoding = "ISO-8859-1")

    # wybiera kolumne Location i zlicza, ile razy występuje każda unikalna wartość w tej kolumnie
    locs = df['Location'].value_counts()
    print(type(locs))

    print(locs.head(1))
Q1()
'''

# Task 2
# Read the shark attack dataset into a Pandas Dataframe. Determine the six countries that have experienced the highest number of shark attacks.

'''
import pandas as pd
import numpy as np

def Q2():
    # he encoding="ISO-8859-1" (also known as Latin-1) is used in pandas.Ten wariant jest używany, gdy plik zawiera znaki spoza ASCII
    df = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/attacks.csv', encoding = "ISO-8859-1")

    locs = df['Country'].value_counts()

    print(type(locs))

    print(locs.head(6))
Q2()
'''

# Task 3
# Modify your code to print out the six countries that have experienced the highest number of fatal shark attacks.

'''
import pandas as pd
import numpy as np

def Q3():
    # he encoding="ISO-8859-1" (also known as Latin-1) is used in pandas.Ten wariant jest używany, gdy plik zawiera znaki spoza ASCII
    df = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/attacks.csv', encoding = "ISO-8859-1")

    # Sprawdzenie, jakie są możliwe wartości w kolumnie "Fatal"
    print(pd.unique(df["Fatal"]))

    # filtrowanie na Y (yes) w kolumnie Fatal
    criteria1 = df["Fatal"]=='Y'
    countries_fatal= df[criteria1]

    locs = df['Country'].value_counts()
    print(type(locs))

    print(locs.head(6))
Q3()
'''

# Task 4
# Based on the data in the Activity column, are you more likely to be attacked by a shark if you are “Surfing” or “Scuba Diving”

'''
import pandas as pd
import numpy as np

def Q4():
    df = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/attacks.csv', encoding = "ISO-8859-1")

    boolSurfAttacks = df["Activity"] == "Surfing"
    boolScubaAttacks = df["Activity"] == "Scuba diving"  

    print ("Number of attacks when surfing ", len(df[boolSurfAttacks] ))    
    print ("Number of attacks when Scuba Diving ", len(df[boolScubaAttacks]))

Q4()
'''

# Task 5
# Determine from the dataset what percentage of all recorded shark attacks were fatal

'''
import pandas as pd
import numpy as np

def Q5():
    df = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/attacks.csv', encoding = "ISO-8859-1")

    Fatals = df["Fatal"]=='Y'
    Fatal_Rows= df[Fatals]

    print(len(Fatal_Rows)*100/len(df))    
Q5()
'''   

# Task 6
# For each individual country print out the percentage of fatal shark attacks (number of fatal shark attacks expressed as a percentage of the total number of shark attacks). 
# Note that only countries that have at least one fatal-attack and at least one non-fatal attack should be included in the analysis.

import pandas as pd
import numpy as np

def Q6():
    df = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/attacks.csv', encoding = "ISO-8859-1")

     # Pobranie listy unikalnych krajów występujących w kolumnie "Country".
    countries =  pd.unique(df["Country"])

    # Iteracja po każdym kraju osobno
    for c in countries:
        # Utworzenie maski logicznej wybierającej wiersze dla danego kraju.
        country = df['Country'] == c

        # Maska logiczna dla ataków śmiertelnych (Fatal == 'Y').
        fatal = df["Fatal"] == 'Y'

        # Maska logiczna dla ataków nieśmiertelnych (Fatal == 'N').
        Non_Fatal = df["Fatal"] == 'N'

        # Filtrowanie danych — wybór tylko tych wierszy, gdzie kraj = c i atak był śmiertelny.
        country_fatal = df[country & fatal]

        # Filtrowanie danych — wybór tylko tych wierszy, gdzie kraj = c i atak był nieśmiertelny.
        country_Non_Fatal = df[country & Non_Fatal]
        
        # Sprawdzenie, czy kraj ma przynajmniej jeden śmiertelny i jeden nieśmiertelny atak.
        if len(country_fatal) > 0 and len(country_Non_Fatal) > 0:
            # Obliczenie procentu śmiertelnych ataków:
            # (liczba śmiertelnych / (śmiertelne + nieśmiertelne)) * 100
            print(f'The percentage of fatal attacks: ',c, len(country_fatal)*100/(len(country_fatal)+len(country_Non_Fatal)))  

Q6()

    




Q6()











# Task 7










# Task 8











# Task 9








# Task 10
