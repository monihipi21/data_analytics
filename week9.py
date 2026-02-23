# Task 1
# Use a visualization approach and visualize the average age for each ticket class in matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
def Q1():
    titanic = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/titanic.csv', encoding = "ISO-8859-1")
    
    #plt.bar(titanic.groupby('Pclass')[['Age'].mean()])
    titanic.groupby('Pclass')['Age'].mean().plot(kind='bar')
    
    plt.title('Age Distribution by Passenger Class on Titanic', fontsize=14, fontweight='bold')
    plt.xlabel('Passenger Class', fontsize=12)
    plt.ylabel('Age', fontsize=12)
    plt.xticks([0, 1, 2], ['First Class', 'Second Class', 'Third Class'])
   
    plt.tight_layout()
    
Q1()
'''

# Task 2
# Repeat the previous question and this time use seaborn. Discuss which one is preferred and why

def Q2():
    titanic = pd.read_csv('/home/monik/Pulpit/mtu/data_analytics/titanic.csv', encoding = "ISO-8859-1")
   
   
   
    sns.barplot(data=titanic, x='Pclass', y='Age', palette="pastel")
    
    # Customize the plot
    plt.title('Age Distribution by Passenger Class on Titanic', fontsize=14, fontweight='bold')
    plt.xlabel('Passenger Class', fontsize=12)
    plt.ylabel('Age', fontsize=12)
    plt.xticks([0, 1, 2], ['First Class', 'Second Class', 'Third Class'])
    
    # Show the plot
    #plt.tight_layout()
    plt.show()
    
Q2() 

# Task 3



# Task 4



# Task 5



# Task 6



# Task 7


