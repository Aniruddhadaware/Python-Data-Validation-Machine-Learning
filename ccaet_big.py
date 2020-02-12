import pandas as pd
import datetime
#mylist = []

csv_name = sys.argv[1]
chunksize = 100000
rows = 0
column_wise_nulls = 0
total_nulls = 0
i = 0
filename = csv_name.replace(".csv","")
for chunk in pd.read_csv(csv_name, chunksize=chunksize):
	 rows = rows+ len(chunk)
	 total_nulls = total_nulls+ chunk.isna().sum().sum()
	 column_wise_nulls = column_wise_nulls+chunk.isna().sum()
	 print(chunk['YEAR'].unique())
	 if i ==0:
	 	a = len(chunk.columns)
	 	b =(chunk.iloc[[1],:])
	 	c = list(chunk)
	 	d = chunk.dtypes
	 i = 1


#Name of columns 
print('List of columns: ')
print(c)

#Print first row
print(b)

#print Number of columns 
print('Total number of columns: ')
print(a)

#print number of rows
print('Total number of rows: ')
print((rows))

#Data types of columns 
data_types = chunk.dtypes
filename_datatype = "data_type_"+filename+".csv"
data_types.to_csv(filename_datatype)

filename_column_wise_nulls = "column_wise_nulls_"+filename+".csv"
column_wise_nulls.to_csv(filename_column_wise_nulls)
		
#Total number of nulls 
print('Total number of nulls: ')
print(total_nulls)



