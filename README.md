Python, Anacondas, Spyder, pandas, numpy and collections (Counter).

This program is used to generate a Data Quality report for Data Analytics.
The program reads in two files (DataSet.txt and featureNames.txt) from the
data directory of the project (./data).
These two files are used to create an Analytics Basics Table (abt_file)
which is stored in the other data directory of the project (./odata).

The ABT is then split into categorical and continuous data sets 
(catData.csv and contData.csv). These two data sets are then used to create 
data quality tables for both continuous and categorical data features.
Both Data Quality tables are then printed by the program and output to csv
files in the data diretory of the project (./data) in files named:
CatReport.csv
ContReport.csv