import pandas as pd
import csv

''' This is a python module for the online learning community.'''

class Linkedin_lp_business(object):

    def __init__(self):
        self.df_blp = pd.read_csv('learning_path_bus.csv')

    def csv(self):
        '''This is a method that returns a CSV file of all the learning paths in the business category.'''
        return(self.df_blp)

    def courseList(self):
        '''This is a method that returns a list of all the learning paths in the business category.'''
        return(self.df_blp['name'].tolist())

    def skillsList(self):
        '''This is a method that returns a list of all the skills in the business category.'''
        return(self.df_blp.groupby('skills').count().index.tolist())

    def skillsdict(self):
        '''This is a method that returns a dictionary of skills and their learning paths in the business category.'''
        return(self.df_blp.groupby('skills')['name'].apply(list).to_dict())


class Linkedin_lp_creative(object):

    def __init__(self):
        self.df_clp = pd.read_csv('learning_path_cre.csv')

    def csv(self):
        '''This is a method that returns a CSV file of all the learning paths in the creative category.'''
        return(self.df_clp)

    def courseList(self):
        '''This is a method that returns a list of all the learning paths in the creative category.'''
        return(self.df_clp['name'].tolist())

    def skillsList(self):
        '''This is a method that returns a list of all the skills in the creative category.'''
        return(self.df_clp.groupby('skills').count().index.tolist())

    def skillsdict(self):
        '''This is a method that returns a dictionary of skills and their learning paths in the creative category.'''
        return(self.df_clp.groupby('skills')['name'].apply(list).to_dict())
