import pandas as pd
import csv

''' This is a python module for the online learning community.'''

df_blp = pd.read_csv('learning_path_bus.csv')

def linkedin_learning_path_business():
    '''This is a method that returns a CSV file of all the learning paths in the business category.'''
    return(df_blp)

def linkedin_learning_path_business_list():
    '''This is a method that returns a list of all the learning paths in the business category.'''
    return(df_blp['name'].tolist())

def linkedin_learning_path_business_skills():
    '''This is a method that returns a list of all the skills in the business category.'''
    return(df_blp.groupby('skills').count().index.tolist())

def linkedin_learning_path_business_authors():
    '''This is a method that returns a dictionary of skills and their learning paths in the business category.'''
    return(df_blp.groupby('skills')['name'].apply(list).to_dict())
