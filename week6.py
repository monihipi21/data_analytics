# Task 1
# Read the dataset bikeSharing.csv into a NumPy array.
# Write a program that compares the average number of total users (column index 15) on days that are holidays (value = 1) with those on days that are not holidays (value = 0).
# Use array selection (boolean indexing) to perform this task


'''
import numpy as np
import random as rnd

def Q1():
    
    # ewentualnie tak wywolac plik TYLKO JEST LRESC NUMERYCZNA

    # file_path = '/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv'
    # data = np.loadtxt(file_path, delimiter=',', skiprows=1) # pomijajac pierwszy wiersz z naglowkami


    data = np.genfromtxt('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv', delimiter=',')

    # Wybieramy tylko te wiersze, w których kolumna 7 ma wartość 1. (czyli dni oznaczone jako święta)
    holiday = 1
    subset = data[data[:, 7] == holiday]

    print ("Number of entries Holiday:\t", len(subset))
    print ("Mean", np.mean(subset[:, 15]))
    
    # Obliczamy średnią wartość kolumny 15 (liczba wszystkich użytkowników 'cnt') dla dni świątecznych.
    holiday = 0
    subset = data[data[:, 7] == holiday]

    print ("Number of entries Non-Holiday:\t ", len(subset))

    print ("Mean", np.mean(subset[:, 15]))

Q1()
'''


# Task 2
# Generally, on a given day, the number of registered users exceeds the number of casual users.
# Determine the percentage of days in the dataset where casual users outnumber registered users.

'''
import numpy as np
import random as rnd

def Q2():

    data = np.genfromtxt('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv', delimiter=',')

    # col 13 → casual users  (użytkownicy okazjonalni)
    # col 14 → registered users (zarejestrowani użytkownicy)

    # Tworzymy tablicę wartości logicznych (True/False):
    # True → wiersze, gdzie casual > registered
    result = data[:,13]>data[:, 14]

    # Używamy tej maski logicznej do wybrania tylko tych wierszy,
    # w których liczba użytkowników casual jest większa.
    # (czyli faktycznie filtrujemy dane)
    result = data[result] # a new array that only contains the rows where casual users are greater than registered ones.
    percentage =  (len(result))/len(data)
    print ("Percentage of time where causal users > registered", percentage )

Q2()
'''

# Task 3
# n this question, you should provide a new implementation of one of last week’s exercises using array indexing. 
# The objective is to investigate the impact of weather conditions on the popularity of bike rentals.
# The 7th column (index 6) in the dataset represents the weather condition, coded as follows:
# 1: Clear, 2: Misty, 3: Light Rain, 4: Heavy Rain.
# Calculate the average number of rented bikes for each weather condition and interpret the results

'''
import numpy as np
import random as rnd

def Q3():
    data = np.genfromtxt('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv', delimiter=',')

    # (numery odpowiadają wartościom w kolumnie "weather situation")
    conditions = {1:"Clear", 2:"Misty", 3:"Light Rain", 4:"Heavy Rain"}

    # Iteracja po wszystkich typach pogody
    for key in conditions:

        # Wybieramy tylko te wiersze, w których kolumna 6 (pogoda) = key
         subsetData = data[data[:,8]==key]

        # Obliczamy średnią liczbę wypożyczonych rowerów (kolumna 15) + wynik
         print (conditions[key],np.mean(subsetData[:, 15]))

Q3()

'''

# Task 4
# The objective of this question is to examine the relationship between temperature and the number of casual users.
# Your code should calculate the average number of casual users for each of the following temperature ranges:
'''
[1, 5] → Average number of casual users?
[6, 10] → Average number of casual users?
[11, 15] → Average number of casual users?
[16, 20] → Average number of casual users?
[21, 25] → Average number of casual users?
[26, 30] → Average number of casual users?
[31, 35] → Average number of casual users?
[36, 40] → Average number of casual users?
'''
# Please note that the temperature values in the dataset are normalised by dividing by 41.
# Therefore, you need to de-normalise them by multiplying by 41 before performing your calculations.
# Finally, interpret the results — discuss how temperature appears to affect the number of casual users


'''
import numpy as np

def Q4():
    data = np.genfromtxt('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv', delimiter=',')

    # Pętla, która tworzy zakresy temperatur: [1–5], [6–10], [11–15], itd. aż do [36–40]
    # 'range(1, 41, 5)' oznacza: zaczynamy od 1, kończymy przed 41, krok = 5
    for temp in range(1, 40, 5):

           # the temperature values stored in the array are multiplied by 41
          minValue = temp
          maxValue = temp+4
          
          # W pliku temperatura jest znormalizowana (czyli podzielona przez 41)
        # Dlatego mnożymy wartości z kolumny 9 przez 41, by uzyskać rzeczywiste temperatury w °C
          higherTempCondition = (data[:,9]*41)>=minValue
          lowerTempCondition = (data[:,9]*41)<=maxValue
    
            # Tworzymy podzbiór (subset) wierszy, które spełniają oba powyższe warunki
          subset = data[higherTempCondition & lowerTempCondition]
    
            # Z kolumny 13 (liczba użytkowników typu "casual") obliczamy średnią wartość
          meanValue = np.mean(subset[:, 13])
    
          print ("For temp in range ", minValue, "to", maxValue, ", mean  casual  is ", "{:.2f}".format(meanValue))
Q4()
'''


# Task 5
# Read the bikeSharing dataset and convert the column containing the casual users into a Pandas Series. 
# You should assign a custom index to this Series, where each index corresponds to the regular (numerical) index values but represented as strings, 
# for example: [’0’, ’1’, ’2’, ...].

'''
import pandas as pd
import numpy as np

def Q5():
    data = np.genfromtxt('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv', delimiter=',')
    
    # Note, np.arange() by default generates inter values, but values type can be changed to string as below syntax.
    
    ind = np.array(np.arange(len(data)),str)
    
    
    d = pd.Series(data[:,13], index = ind)
    # Testing it below
    print(d['1030'])
Q5()
'''

# Task 6
# Create a Pandas Series using the bikeSharing dataset such that the values represent the temperature and the labeled indexes correspond to the season. 
# Using only Pandas functions, calculate the average temperature for each season (1, 2, 3, and 4). 
# Finally, interpret the results.

'''
import pandas as pd
import numpy as np

def Q6():
    data = np.genfromtxt('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv', delimiter=',')

    d = pd.Series(data[:,9], index = data[:,1])

    # Obliczamy i wypisujemy średnie wartości z kolumny 9 dla wierszy,
    # które mają w indeksie odpowiednio 1, 2, 3 i 4.
    print(np.mean(d[1]), np.mean(d[2]), np.mean(d[3]), np.mean(d[4]))

Q6()
'''


# Task 7
# Create a Pandas Series using the bikeSharing dataset such that the values represent the humidity and the labeled indexes correspond to the month. 
# Using only Pandas functions, calculate the average humidity for each month (1 through 12). 
# Finally, interpret the results.

'''
import pandas as pd
import numpy as np

def Q7():
    data = np.genfromtxt('/home/monik/Pulpit/mtu/data_analytics/bikeSharing.csv', delimiter=',')

    d = pd.Series(data[:,11], index = data[:,3])
   
    for i in range(12):
        print(np.mean(d[i+1]))
Q7()
'''

