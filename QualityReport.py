# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:07:44 2016

@author: laura mcgovern
@student number: C12431378
@title: Assignment 1: Data Quality Report
"""

# Import all libraries needed
import pandas as pd 
from numpy import nan
from collections import Counter


class DataQuality(object):
    
    """
    Data Quality object, used to prepare data quality reports for
    data analytics
    """
    

    def __init__(self, dataset):
        
        """
        Constructor method
        
        Parameters (self, dataset)
        """
        # These variables are created using self.name_of_variable notation
        # Functions of DataQuality
        self.data = self.get_data(dataset) 
        self.catData = self.cat_data(self.data)
        self.contData = self.cont_data(self.data)
        self.cont_table()
        self.cat_table()

        
    def get_data(self, dataset):    

        """
        The get_data method takes the data set DataSet.txt and assigns
        each colum a title from the featuresNames.txt file in order to
        make the data more readable. 
        
        This method essentially creates the Analytics Basics Table.
        
        Parameters (self, dataset)
        Returns (DataFrame: abt_file)
        """
        
        ins = open('./data/featureNames.txt', "r")
        
        colum_headings =[]
         
        for line in ins:
            line = line.strip()
            colum_headings.append(line)
            
        abt_file = pd.read_csv('./data/DataSet.txt', 
                                 sep=',', 
                                 header=None,
                                 names=colum_headings)
        abt_file.columns = colum_headings
        
        abt_file.to_csv('./odata/abtFile.csv')
        return(abt_file)
        

    def cat_data(self, lst):
        
        """
        The cat_data method takes the categorical data columns
        from the data set and returns a new data set with just
        the values for those colums. The returned data set is
        stored in self.cat
        
        Parameters (self, Dataframe: lst)
        Returns (DataFrame: getCatData)
        """
        # Read in catFeatures.txt (text file of the categorical features)
        catFile = open('./odata/catFeatures.txt', "r")
        
        # Create array to store categorical features
        cat = []
        
        # Add features to array
        for line in catFile:
            line = line.strip()
            cat.append(line)
        
        # Create DataFrame with columns of categorical data
        getCatData = pd.DataFrame(lst, columns=cat)
        getCatData.to_csv('./odata/catData.csv',index=True,header=True)
        return(getCatData)
        
    
    
    def cont_data(self, lst):
        
        """
        The cont_data method takes the continuous data columns
        from the data set and returns a new data set with just
        the values for those colums. The returned data set is
        stored in self.cont
        
        Parameters (self, Dataframe: lst)
        Returns (DataFrame: getContData)
        """        
        # Read in contFeatures.txt (text file of the continuous features)
        contFile = open('./odata/contFeatures.txt', "r")
        
        # Create array to store continuous features
        cont = []
        
        # Add values to array
        for line in contFile:
            line = line.strip()
            cont.append(line)
        
        # Create DataFrame with columns of continuous data
        getContData = pd.DataFrame(lst, columns=cont)
        getContData.to_csv('./odata/contData.csv',index=True,header=True)
        return(getContData)
        
    
        
    def cont_table(self):
        
        """
        The cont_table method is used to create the continuous
        data quality table. It reads in the continuous data 
        feature names, the continuous data set and combines 
        them to create the ABT.
        
        It then performs functions to get:
            * Count
            * % Missing data
            * Cardinality
            * Minimum
            * First quartile
            * Mean
            * Median
            * Third quartile
            * Maximum
            * Standard Deviation
            
        It then prints the table and exports to a csv file.
        
        Parameters(self)
        """
            
         
        # Read in contFeatures.txt (text file of the continuous features)
        indexFile = open('./odata/contFeatures.txt', "r")
        
        # Create array to store continuous features
        contFeatures = []
        
        # Add values to array
        for line in indexFile:
            line = line.strip()
            contFeatures.append(line)
        
        inputContData = pd.read_csv('./odata/contData.csv',
                        sep=',',
                        header=0,
                        index_col=False,
                        dayfirst=True,
                        tupleize_cols=False,
                        error_bad_lines=True,
                        warn_bad_lines=True,
                        skip_blank_lines=True
                        )
        # Selects only columns wanted for report (age, fnlwgt etc)
        contData = inputContData[contFeatures]
         
        # Count 
        count = pd.DataFrame(contData.count(), columns=['Count'])
        
        # Calculate missing %        
        miss_data = contData.isnull().sum()
        miss_pct = pd.DataFrame((miss_data/count.Count)*100, columns =[' % Miss.'])
        
        # Cardinality 
        unique_value_counts = pd.DataFrame(columns=['Card.'])
        for v in list(contData.columns.values):
            unique_value_counts.loc[v] = [contData[v].nunique()]
        
        # Min
        minimum_values = pd.DataFrame(columns=['Min'])
        for v in list(contData.columns.values):
            minimum_values.loc[v] = [contData[v].min()]
            
        # 1st Quartile
        f_qrt = pd.DataFrame(columns=['1st Qrt.'])
        for v in list(contData.columns.values):
            f_qrt.loc[v] = [contData[v].quantile(.25)]
        
        # Mean        
        mean = pd.DataFrame(contData.mean(), columns=['Mean'])
        
        # Median
        median = pd.DataFrame(contData.median(), columns=['Median'])
        
        # 3rd Quartile
        t_qrt = pd.DataFrame(columns=['3rd Qrt.'])
        for v in list(contData.columns.values):
            t_qrt.loc[v] = [contData[v].quantile(.75)]
           
        # Max
        max_values = pd.DataFrame(columns=['Max'])
        for v in list(contData.columns.values):
            max_values.loc[v] = [contData[v].max()]
       
        # Standard Dev
        std_dev = pd.DataFrame(contData.std(), columns=['Std. Dev.'])
        
              
        # Final report for continuous data      
        cont_report = pd.DataFrame((count.
                                    join(miss_pct).
                                    join(unique_value_counts).
                                    join(minimum_values).
                                    join(f_qrt).join(mean).
                                    join(median).
                                    join(t_qrt).
                                    join(max_values).
                                    join(std_dev)))
                                    
        cont_report.index.name = 'Feature'
        
        # Print data report
        print("\n Continuous Features Data Quality Table \n\n")        
        print(cont_report)
        
        # Export to csv file
        cont_report.to_csv('./data/ContReport.csv')
        
    def cat_table (self):
        
        """
        The cat_table method is used to create the categorical
        data quality table. It reads in the categorical data 
        feature names, the ccategorical data set and combines 
        them to create the ABT.
        
        It then performs functions to get:
            * Count
            * % Missing data
            * Cardinality
            * Mode
            * Mode Frequency
            * Mode %
            * Second Mode
            * Second Mode Frequency
            * Second Mode %
            
        It then prints the table and exports to a csv file.
        
        Parameters(self)
        """        
        
        # Read in catFeatures.txt (text file of the categorical features)
        catFile = open('./odata/catFeatures.txt', "r")
        
        # Create array to store categorical features
        catFeatures = []
        
        # Add features to array
        for line in catFile:
            line = line.strip()
            catFeatures.append(line)
            
        # Read in catHeadings.txt (text file of the categorical table headings)
        headingsFile = open('./odata/catHeadings.txt', "r")
        
        # Create array to store categorical headings
        catHeadings = []
        
        # Add headings to array
        for line in headingsFile:
            line = line.strip()
            catHeadings.append(line)
            
        # Read in categorical data   
        inputCatData = pd.read_csv('./odata/catData.csv',
                        sep=',',
                        header=0,
                        index_col=False,
                        dayfirst=True,
                        tupleize_cols=False,
                        error_bad_lines=True,
                        warn_bad_lines=True,
                        skip_blank_lines=True,
                        names = catFeatures
                        )
                        
        
        # Selects only columns wanted for report
        catData = pd.DataFrame(inputCatData[catFeatures])
        catData.replace(to_replace='?', value=nan)
        
        # Count 
        count = pd.DataFrame(catData.count(), columns=['Count'])
        
        # Calculate missing %        
        miss_data = catData.isnull().sum()
        miss_pct = pd.DataFrame((miss_data/count.Count)*100, columns =[' % Miss.'])      
        
        # Cardinality 
        unique_value_counts = pd.DataFrame(columns=['Card.'])
        for v in list(catData.columns.values):
            unique_value_counts.loc[v] = [catData[v].nunique()]

        # Modes, modde frequencies and mode %
        
        # Number columns 
        catDataCols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        # List to store data
        catRows = list()
        
        # Loop to access all data and apply functions to get values
        for i in catDataCols:
            data = Counter(inputCatData[catFeatures[i]].tolist())
            modes = data.most_common(2)
            catRows.append(
                [catFeatures[i].upper(),#featureName
                modes[0][0],#mode, value that occurs most often
                modes[0][1],#mode freq
                round((modes[0][1] / inputCatData[catFeatures[i]].count() * 100), 4),#mode %,
                modes[1][0],#2nd mode,
                modes[1][1],#2nd mode freq,
                round((modes[1][1] / inputCatData[catFeatures[i]].count() * 100), 4)#2nd mode %,
                ]
            )
        # Structure Data    
        mode_maths = pd.DataFrame(catRows, columns = ['Feature', 'Mode', 'Mode Freq.', 'Mode %', '2nd Mode', '2nd Mode Freq.', '2nd Mode %' ], index=catFeatures)
        
        # Create DQR style structure        
        mode_values = pd.DataFrame(mode_maths[catHeadings], index=catFeatures)
        
        # Final report for continuous data      
        cat_report = pd.DataFrame((count.
                                    join(miss_pct).
                                    join(unique_value_counts).
                                    join(mode_values)))
                                    
        cat_report.index.name = 'Feature'
        
        # Print final categorical data report
        print(" \n Categorical Features Data Quality Table \n\n")        
        print(cat_report)
        
        # Export to csv
        cat_report.to_csv('./data/CatReport.csv')
        
        
         
def main():
    
    """
    Main function of program
    """
    # Original csv file 
    dataset = './data/DataSet.txt'
    
    #Call Data Quality and pass it the dataset
    DataQuality(dataset)
    


# Call main ()
if __name__ == "__main__":
    main()
        




