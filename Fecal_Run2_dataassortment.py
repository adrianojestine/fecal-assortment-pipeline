import pandas as pd
#on terminal write pip install pandas and pip install tabulate on terminal
#then write pip install tabulate on terminal (for to.markdown())

#UNLIKE THE BARCODE 1 AND 2 code; because we have used DIRECT EPI2ME OUTPUT here, we split the 'Tax' column
#into 'Type' and 'Taxa' columns. This will then be used for the rest of the code
#FOR THE BARCODE 1 AND 2 (FECAL RUN 1 CODE), the file that was read into it was already seperated like this
#so this additional step needs to be done here

#raw EPI2ME FILE, UNLIKE FECAL RUN 1 SORTING CODE (BC 1 AND BC 2)
df = pd.read_csv('Fecal_trial_run_2_with_zymo_pc.csv')

df_new_columns = df.copy()
#splitting the first columns string into its individual parts, seperated by ';'
parts = df_new_columns['tax'].str.split(';')
#extracting first part of parts into a new colum created for df called 'Type'
df_new_columns['Type'] = parts.str[0]
#extracting last part of parts into a new colum created for df called 'Tax'
#Note: -ve numbering (-1) indicates the last column
df_new_columns['Tax_new'] = parts.str[-1]

#renaming Tax_new in Tax
#reordering columns
df_new_columns = df_new_columns.rename(columns ={'Tax_new': 'Tax'})
df_new_columns = df_new_columns[['Type', 'Tax', 'barcode11', 'barcode12', 'barcode13', 'barcode14', 'total']]

#creating copies of dataframe to be filtered for barcode1 and barcode2 and edited accordingly
df_barcode11 = df_new_columns.copy() # COPY, CHANGE VARIABLE to new Dataframe
df_barcode12 = df_new_columns.copy() # COPY, CHANGE VARIABLE to new Dataframe
df_barcode13 = df_new_columns.copy()
df_barcode14 = df_new_columns.copy()

#dropping unecessary columns
df_barcode11 = df_barcode11.drop(columns=['barcode12','barcode13','barcode14','total'])
df_barcode12 = df_barcode12.drop(columns=['barcode11','barcode13','barcode14','total'])
df_barcode13 = df_barcode13.drop(columns= ['barcode11','barcode12','barcode14','total'])
df_barcode14 = df_barcode14.drop(columns= ['barcode11', 'barcode12','barcode13','total'])

#now we CALCULATE RELATIVE ABUNDANCY for Barcode 1 and 2
#defining barcode1 and barcode2 total read numbers
barcode11_reads_total = 616673
barcode12_reads_total = 653686
barcode13_reads_total = 4240
barcode14_reads_total = 215416

#calculating relative abundancy
df_barcode11['barcode11_relative_abundancies'] = (df_barcode11['barcode11']/barcode11_reads_total) * 100
df_barcode12['barcode12_relative_abundancies'] = (df_barcode12['barcode12']/barcode12_reads_total) * 100
df_barcode13['barcode13_relative_abundancies'] = (df_barcode13['barcode13']/barcode13_reads_total) * 100
df_barcode14['barcode14_relative_abundancies'] = (df_barcode14['barcode14']/barcode14_reads_total) * 100

#now SORTING RELATIVE ABUNDANCIES by user set relative abundancy threshold
#DEFINING RELATIVE THRESHOLD VALUE
#asking user to INPUT value for relative abundancies thresholds for barcode 1 and 2
relative_abundancy_threshold_barcode11_input = input('Please enter the numerical value of the relative abundancy threshold you wish to set (without % symbol), to filter barcode 11 = ')
relative_abundancy_threshold_barcode12_input = input('and barcode 12 = ')
relative_abundancy_threshold_barcode13_input = input('and barcode 13 = ')
relative_abundancy_threshold_barcode14_input = input('and barcode 14 = ')

#converting string datatype entered by user in float dataype (accepting decimals)
relative_abundancy_threshold_barcode11 = float(relative_abundancy_threshold_barcode11_input)
relative_abundancy_threshold_barcode12 = float(relative_abundancy_threshold_barcode12_input)
relative_abundancy_threshold_barcode13 = float(relative_abundancy_threshold_barcode13_input)
relative_abundancy_threshold_barcode14 = float(relative_abundancy_threshold_barcode14_input)

#printing user inputted values for realtive abundancies thresholds for barcode 1 and 2 with their datatypes
print(f'The relative abundancy threshold value you entered for barcode 11 is = {relative_abundancy_threshold_barcode11} with dataype = {type(relative_abundancy_threshold_barcode11)}')
print(f'The relative abundancy threshold value you entered for barcode 12 is = {relative_abundancy_threshold_barcode12} with dataype = {type(relative_abundancy_threshold_barcode12)}')
print(f'The relative abundancy threshold value you entered for barcode 13 is = {relative_abundancy_threshold_barcode13} with dataype = {type(relative_abundancy_threshold_barcode13)}')
print(f'The relative abundancy threshold value you entered for barcode 14 is = {relative_abundancy_threshold_barcode14} with dataype = {type(relative_abundancy_threshold_barcode14)}')

#creating masks for sorting relative abundancies
mask_RA_barcode11 = df_barcode11['barcode11_relative_abundancies'] >= relative_abundancy_threshold_barcode11
mask_RA_barcode12 = df_barcode12['barcode12_relative_abundancies'] >= relative_abundancy_threshold_barcode12
mask_RA_barcode13 = df_barcode13['barcode13_relative_abundancies'] >= relative_abundancy_threshold_barcode13
mask_RA_barcode14 = df_barcode14['barcode14_relative_abundancies'] >= relative_abundancy_threshold_barcode14

#applying masks to Dataframes filtered and sorted for barcode 1 and 2
df_filt_barcode11 = df_barcode11[mask_RA_barcode11]
df_filt_barcode12 = df_barcode12[mask_RA_barcode12]
df_filt_barcode13 = df_barcode13[mask_RA_barcode13]
df_filt_barcode14 = df_barcode14[mask_RA_barcode14]

#printing the masks for barcode 11, 12, 13 and 14
print(f'Dataframe for barcode11 sorted by {relative_abundancy_threshold_barcode11}%:')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(df_filt_barcode11.to_markdown(index = False, numalign = 'left', stralign = 'right'))
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('')
print('')

print(f'Dataframe for barcode12 sorted by {relative_abundancy_threshold_barcode12}%:')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(df_filt_barcode12.to_markdown(index = False, numalign = 'left', stralign = 'right'))
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('')
print('')

print(f'Dataframe for barcode13 sorted by {relative_abundancy_threshold_barcode13}%:')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(df_filt_barcode13.to_markdown(index = False, numalign = 'left', stralign = 'right'))
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('')
print('')

print(f'Dataframe for barcode14 sorted by {relative_abundancy_threshold_barcode14}%:')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(df_filt_barcode14.to_markdown(index = False, numalign = 'left', stralign = 'right'))
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('')
print('')

#converting Dataframes with calculated relative abundancies  into csv. files
#index is false
df_filt_barcode11.to_csv('Barcode 11 Taxonomy.csv', index = False)
df_filt_barcode12.to_csv('Barcode 12 Taxonomy.csv', index = False)
df_filt_barcode13.to_csv('Barcode 13 Taxonomy.csv', index = False)
df_filt_barcode14.to_csv('Barcode 14 Taxonomy.csv', index = False)

print('The Dataframe for filtering and sorting barcode 11, 12, 13 and 14 has been converted to .csv file!')
print('The serial numbers have been removed to use easily on further R studio steps')
print('you can find it in the panel on your left')

print('Please drag and drop these files into your RStudio Directory and change the names')