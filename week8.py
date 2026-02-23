# Task 1
# Using the GroupBy function, write a program that calculates the average age for each country. 
# Note that some records may have missing values for age. You should clean the data first by filling the empty Age cells with the most frequent age value.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Q1():
    df = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/attacks.csv', encoding = "ISO-8859-1")

    #First make the non numerical cells empty.
    df['Age']= df['Age'].apply(pd.to_numeric, errors='coerce')

    # You can get the labeled index of a specific cell in a Series with using index as below:
    leastFreq = df['Age'].value_counts().index[0]
    print(leastFreq)
    df['Age'] = df['Age'].fillna(leastFreq)
    
    grs = df.groupby('Country')['Age'].mean()
    
    print(grs)

Q1()
'''

# Task 2
# Some countries in the attacks.csv file have multiple distinct areas, for example:
'''AUSTRALIA New South Wales
   AUSTRALIA Victoria
   ...
'''
# Write a function that counts the number of unique areas for each country. 
# Then, sort the countries based on the number of different locations and visualize the top five countries with the highest number of distinct areas.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Q2():
    df = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/attacks.csv', encoding = "ISO-8859-1")

    # Pobranie listy unikalnych krajów z kolumny 'Country'
    countries = df['Country'].unique()

    # Inicjalizacja dwóch pustych list:
    # 'indexes' - będzie przechowywać nazwy krajów (x)
    # 'value' - będzie przechowywać liczbę unikalnych obszarów (y)
    indexes = []
    value = []

    for c in countries:
         # Tworzymy maskę logiczną, która wybiera wiersze odpowiadające danemu krajowi
        cn1 = df['Country'] == c
        # Filtrowanie danych tylko dla tego kraju
        cn = df[cn1]
        # dodajemy nazwe kraju do listy indeksów
        indexes.append(c) #x
        # Znajdujemy unikalne wartości w kolumnie 'Area' dla danego kraju
        areas = pd.unique(cn['Area'])
        # Liczymy, ile różnych obszarów ma dany kraj, i zapisujemy wynik do listy 'value'
        value.append(len(areas)) # y

    # Tworzymy serię pandas, gdzie:
    # - index = nazwy krajów
    # - values = liczba unikalnych obszarów
    cnt = pd.Series(value, index = indexes)
    # Sortujemy kraje malejąco według liczby unikalnych obszarów
    cnt = cnt.sort_values(ascending=False)
    # Wybieramy 5 krajów z największą liczbą różnych obszarów
    subset = cnt[:5]

    #Note you can choose one of the two below diagrams:
    # subset.plot(kind='bar')
    # or
    subset.plot()
    # note in order to add other features, we use matplotlib directly.
    plt.xlabel("country name")
    plt.ylabel("# unique areas")
    print(subset)
    plt.show()
Q2()
'''

# Task 3
# There are some cells in the attacks.csv file with missing values (empty or NaN). Repeat the previous task, but this time create a plot that contains two visual objects:
# 1) One plot without data cleaning,
# 2) The other plot after cleaning the data (e.g., removing rows where the Area column has no value, such as NaN or empty cells).
# Use different markers and colors for each visual object to distinguish between the two.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Q3():
    df = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/attacks.csv', encoding = "ISO-8859-1")

    # Utworzenie kopii danych po oczyszczeniu — usuwamy wiersze, w których kolumna 'Area'
    df_clean = df.dropna(subset=['Area'])
    # wyszukanie unikatowych wartosci w kolumnjie z krajami
    countries = pd.unique(df['Country'])

    # inicjalizacja pustych list
    indexes = []
    values_clean = []
    value = []

    for c in countries:
        cn1 = df['Country'] == c
        # Dane tylko dla danego kraju (bez czyszczenia)
        cn = df[cn1]
        #  Dane tylko dla danego kraju (z czyszczeniem)
        cn_clean = df_clean[cn1]

        # dodajemy nazwe kraju do listy index'ów
        indexes.append(c)

        # Liczymy unikalne obszary przed czyszczeniem danych
        areas = pd.unique(cn['Area'])
        value.append(len(areas))

        # Liczymy unikalne obszary po czyszczeniu danych
        areas_clean = pd.unique(cn_clean['Area'])
        values_clean.append(len(areas_clean))

    # Tworzymy dwie serie pandas:
    # cnt — liczba unikalnych obszarów przed czyszczeniem
    # cnt_clean — liczba unikalnych obszarów po czyszczeniu
    cnt = pd.Series(value, index = indexes)
    cnt_clean = pd.Series(values_clean, index = indexes)
    # Sortujemy dane malejąco
    cnt = cnt.sort_values(ascending=False)
    cnt_clean = cnt_clean.sort_values(ascending=False)
    # wybieramy 5 krajów z nawieksza liczba obszarów
    subset = cnt[:5]
    subset_clean = cnt_clean[:5]

    # Tworzymy 2 wykresy - przed oczyszczenie i po oczyszczeniu
    subset.plot(marker = '*', linestyle='-', color='purple')
    subset_clean.plot(marker = 's', linestyle='-', color='green')
    # note in order to add other features, we use matplotlib directly.
    plt.xlabel("country name")
    plt.ylabel("# unique areas")
    plt.show()
    print(subset)

Q3()
'''

# Task 4
# Write a program that calculates the average age for each year in the attack dataset.
# Note that some cells in the age column contain noise. For instance, some cells are empty, some contain extra spaces (e.g., ’2 3’), and some contain non-numerical values (e.g., ’20s’). 
# You first need to clean the required column and then calculate the average age for each year. 
# Visualize the data for the last 50 years and see if there is any pattern. Explain your findings.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Q4():
    df = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/attacks.csv', encoding = "ISO-8859-1")

    # Czyszczenie kolumny 'Age':
    # Funkcja apply(pd.to_numeric, errors='coerce') próbuje przekonwertować każdą wartość na liczbę
    # Jeśli w komórce są niepoprawne dane (np. "20s", "2 3", puste pola), zostaną zamienione na null
    df['Age']= df['Age'].apply(pd.to_numeric, errors='coerce')
   
    # Usuwamy wszystkie wiersze, w których kolumna 'Age' ma wartość null
    df = df.dropna(subset=['Age'])

   # grupowanie według roku ataku
    yrs = df.groupby('Year')

    # obliczanie średniego wieku dla każdego roku
    averg = yrs['Age'].mean()
    # Wybranie ostatnich 50 lat z danych
    sortedSeries = averg.tail(50)
    
    # tworzenie wykresu 
    sortedSeries.plot(marker = '*', linewidth=8.5, linestyle='-', color='pink')
    plt.show()

Q4()
'''

# Task 5
# ou may notice that there is a column named Name, which contains both first and last names separated by a space. 
# Create a new DataFrame from the attacks dataset that includes only two columns: First Name and Surname.
# You can use the following code snippet to split the column:
'''a = df[’Name’].str.split(expand=True)'''
# In the above code, a is a new DataFrame created by splitting the values of the Name column wherever a space occurs.
# The number of columns (M ) in this new DataFrame corresponds to the maximum number of space-separated components found in any entry of df[’Name’].
# For instance, if the longest name in the dataset contains two spaces (e.g., “John Michael Smith”), then M = 3. Typically, the first two components represent the person’s first name and surname.
# The expand argument determines whether the split results should be expanded into separate columns (True) or kept as a list within a single column (False).

def Q5():
    df = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/attacks.csv', encoding = "ISO-8859-1")

    a = df['Name'].str.split(expand=True) 
    """
    Note that a is a new DataFrame. The number of columns in this DataFrame depends on the entry with the largest number of spaces in it.
    We can assume that the first two components after splitting by space represent the first name and surname of the person.
    """
    names = pd.DataFrame({'First Name': a[0], 'Second Name': a[1]})
    print((names))

#Q5()


# Task 6

# Task 7

# Task 8

# Task 9


