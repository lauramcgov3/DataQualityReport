# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:07:44 2016

@author: laura
@student number: C12431378
@title: Assignment 1: Data Quality Report
"""

# Import all libraries needed
import pandas as pd #this is how I usually import pandas
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt

class DataQuality(object):
    
    """
    Data Quality object, used to prepare data quality reports for
    data analytics
    """
    

    def __init__(self, dataset):
        
        """
        Constructor method
        """
        #These variables are created using self.name_of_variable notation
        self.data = self.get_data(dataset) 
        self.cat = self.cat_data(self.data)
        self.cont = self.cont_data(self.data)

        
    def get_data(self, dataset):    

        """
        The get_data method takes the data set DataSet.txt and assigns
        each colum a title from the featuresNames.txt file in order to
        make the data more readable.
        """

        ins = open('./data/featureNames.txt', "r")
        
        colum_headings =[]
         
        for line in ins:
            line = line.strip()
            colum_headings.append(line)
            
        show_headers = pd.read_csv('./data/DataSet.txt', 
                                 sep=',', 
                                 header=None,
                                 names=colum_headings)
        show_headers.columns = colum_headings
        #print(show_headers)
        return(show_headers)
        

    def cat_data(self, lst):
        
        """
        The cat_data method takes the categorical data columns
        from the data set and returns a new data set with just
        the values for those colums. The returned data set is
        stored in self.cat
        """
        # Read in catFeatures.txt (text file of the categorical features)
        catFile = open('./data/catFeatures.txt', "r")
        
        # Create array to store categorical features
        cat = []
        
        # Add features to array
        for line in catFile:
            line = line.strip()
            cat.append(line)

        # Create DataFrame with columns of categorical data
        getCatData = pd.DataFrame(lst, columns=cat)
        return(getCatData)
               
    
    
    def cont_data(self, lst):
        
        """
        The cont_data method takes the continuous data columns
        from the data set and returns a new data set with just
        the values for those colums. The returned data set is
        stored in self.cont
        """        
        # Read in contFeatures.txt (text file of the continuous features)
        contFile = open('./data/contFeatures.txt', "r")
        
        # Create array to store continuous features
        cont = []
        
        # Add values to array
        for line in contFile:
            line = line.strip()
            cont.append(line)
        
        # Create DataFrame with columns of continuous data
        getContData = pd.DataFrame(lst, columns=cont)
        return(getContData)
        
        
        
def main():
    

    dataset = './data/DataSet.txt'
    My_DQR = DataQuality(dataset)


# Call main ()
if __name__ == "__main__":
    main()
        




