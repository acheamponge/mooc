import pandas as pd
import csv

''' This is a python module for the online learning community.'''

df = pd.read_csv('learning_path_bus.csv')

def linkedin_learning_path_business():
    '''This is a method that returns a CSV file of all the learning paths in the business category.'''
    return(df)

def linkedin_learning_path_business_list():
    '''This is a method that returns a list of all the learning paths in the business category.'''
    return(df['name'].tolist())

def linkedin_learning_path_business_skills():
    '''This is a method that returns a list of all the learning paths in the business category.'''
    return(df.groupby('skills').count().index.tolist())
