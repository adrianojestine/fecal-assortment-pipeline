import pandas as pd

#on terminal write pip install pandas and then, pip install tabulate
#we install these two packages and libraries as we would use it coming ahead:

#reading the .csv file into a dataframe
df = pd.read_csv('Fecal Sample data_1.csv')

#creating copies of dataframe to be filtered for barcode1 and barcode2 and edited accordingly
df_filt_barcode1 = df.copy() # COPY, CHANGE VARIABLE to new Dataframe
df_filt_barcode2 = df.copy() # COPY, CHANGE VARIABLE to new Dataframe

#dropping unecessary columns
df_barcode1 = df_filt_barcode1.drop(columns=['barcode02 (aclf)', 'unclassified- assigned to spicies but with low confidence ', 'total'])
df_barcode2 = df_filt_barcode2.drop(columns=['barcode01(HC)', 'unclassified- assigned to spicies but with low confidence ', 'total'])


#now we CALCULATE RELATIVE ABUNDANCY for Barcode 1 and 2
#defining barcode1 and barcode2 total read numbers
barcode1_reads_total = 1118361
barcode2_reads_total = 1936286

#calculating relative abundancy
df_barcode1['barcode01_relative_abundancies'] = (df_barcode1['barcode01(HC)']/barcode1_reads_total) * 100
df_barcode2['barcode02_relative_abundancies'] = (df_barcode2['barcode02 (aclf)']/barcode2_reads_total) * 100

#printing Dataframe for barcode 1 and 2 with respective calculated relative abundancies
print('Dataframe for barcode1 with calculated relative abundancies:')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(df_barcode1.to_markdown(index = True, numalign = 'left', stralign = 'right'))
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('')
print('')

print('Dataframe for barcode2 with calculated relative abundancies:')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(df_barcode2.to_markdown(index = True, numalign = 'left', stralign = 'right'))
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('')
print('')

#now SORTING RELATIVE ABUNDANCIES by user set relative abundancy threshold
#DEFINING RELATIVE THRESHOLD VALUE
#asking user to INPUT value for relative abundancies thresholds for barcode 1 and 2
relative_abundancy_threshold_barcode1_input = input('Please enter the numerical value of the relative abundancy threshold you wish to set (without % symbol), to filter barcode 1 = ')
relative_abundancy_threshold_barcode2_input = input('and barcode 2 = ')

#converting string dataype entered by user in float dataype (accepting decimals)
relative_abundancy_threshold_barcode1 = float(relative_abundancy_threshold_barcode1_input)
relative_abundancy_threshold_barcode2 = float(relative_abundancy_threshold_barcode2_input)

#printing user inputted values for relative abundancies thresholds for barcode 1 and 2 with their datatypes
print(f'The relative abundancy threshold value you entered for barcode 1 is = {relative_abundancy_threshold_barcode1} with dataype = {type(relative_abundancy_threshold_barcode1)}')
print(f'The relative abundancy threshold value you entered for barcode 2 is = {relative_abundancy_threshold_barcode2} with dataype = {type(relative_abundancy_threshold_barcode2)}')

#creating masks for sorting relative abundancies
mask_RA_barcode1 = df_barcode1['barcode01_relative_abundancies'] >= relative_abundancy_threshold_barcode1
mask_RA_barcode2 = df_barcode2['barcode02_relative_abundancies'] >= relative_abundancy_threshold_barcode2

#applying masks to Dataframes filtered and sorted for barcode 1 and 2
df_filt_barcode1 = df_barcode1[mask_RA_barcode1]
df_filt_barcode2 = df_barcode2[mask_RA_barcode2]

#printing the masks for barcode 1 and 2
print(f'Dataframe for barcode1 sorted by {relative_abundancy_threshold_barcode1}%:')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(df_filt_barcode1.to_markdown(index = False, numalign = 'left', stralign = 'right'))
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('')
print('')

print(f'Dataframe for barcode2 sorted by {relative_abundancy_threshold_barcode2}%:')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(df_filt_barcode2.to_markdown(index = False, numalign = 'left', stralign = 'right'))
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('')
print('')


#converting Dataframes with calculated relative abundancies  into csv. files
#index is false
df_filt_barcode1.to_csv('Barcode 1 Taxonomy.csv', index = False)
df_filt_barcode2.to_csv('Barcode 2 Taxonomy.csv', index = False)

print('The Dataframe for filtering and sorting barcode 1 and 2 has been converted to .csv file!')
print('The serial numbers have been removed to use easily on further R studio steps')
print('you can find it in the panel on your left')

print('Please drag and drop these files into your RStudio Directory and change the names')