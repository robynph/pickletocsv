from sklearn.externals import joblib

#define paths
path_pickle = "myPickleFile.pkl"
path_csv = "myCSVOutput.csv"

#load data from pickle file into dataframe
df_output = joblib.load(path_pickle)

#print dataframe, check to see if you're printing the right data 
print(df_output)

#output to csv
rules.to_csv(path_csv, sep='\t')
