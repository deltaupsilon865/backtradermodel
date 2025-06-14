import pandas as pd
# ufo=pd.read_csv('https://bit.ly/uforeports')
# type(ufo)
# print(ufo.head())
# print(ufo.City)
# print(ufo['City'])
# ufo['Location']= ufo.City + ' , ' + ufo.State
# print(ufo['Location'])
# ufo.rename(columns={'City':'Place','State':'Region'}, inplace=True)
# print(ufo.columns)
# ufo_cols=['City','State','Country','Shape Reported','Duration (seconds)','Date/Time']
# ufo.columns=ufo_cols
# print(ufo.columns)
# ufo=pd.read_csv('https://bit.ly/uforeports', usecols=ufo_cols)
# print(ufo.head())
# print(ufo.drop(['City','State'],axis=1, inplace=True)) #drop columns, axis=1 means columns, axis=0 means rows
# print(ufo.head()) 
# movies=pd.read_csv('https://bit.ly/imdbratings')
# print(movies.head())
# print(movies.title.sort_values) #sort values in ascending order
# print(movies.sort_values('title')) #sort values in ascending order with entire dataframe
# print(movies.sort_values(['star_rating','genre'])) #sort values of 2 columns with entire dataframe
# boolean=[]
# for length in movies.duration:
#     if length>=200:
#         boolean.append(True)
#     else:
#         boolean.append(False)
# print(boolean[0:100])
# is_long=pd.Series(boolean)
# print(movies[is_long]) #print all movies with duration greater than 200
# is_long=movies.duration>=200 #bypasses the for loop
# print(movies[is_long]) #print all movies with duration greater than 200 
# print(movies[movies.duration>=200]) #print all movies with duration greater than 200 bypassing the previous step
# #best practice - movies.loc[movies.duration>=200]
# print(movies[(movies.duration>=200) & (movies.genre=='Drama')]) #print all movies with duration greater than 200 and genre as Drama
# print(movies[movies.genre.isin(['Drama','Action'])]) #print all movies with genre as Drama or Action in MULTIPLE OR condition
# orders=pd.read_table('https://bit.ly/chiporders')
# print(orders[orders.item_name.str.contains('Chicken').astype(int).head()]) #print all orders with item_name containing 'Chicken' into boolean 0 and 1 values

# drinks = pd.read_csv('https://bit.ly/drinksbycountry')
# drinks['beer_servings'] = drinks.beer_servings.astype(float)  # changes the data type of beer_servings to floatṇ
# # print(drinks.dtypes)  # prints the data types of all columns
# print(drinks[drinks.continent == 'Antarctica'].beer_servings.mean()) # calculates the mean of beer_servings for Asia
# print(drinks.groupby('continent').beer_servings.agg(['count', 'max', 'mean']))  # calculates the mean of beer_servings for each continent 
# movies=pd.read_csv('https://bit.ly/imdbratings')
# print(movies.genre.value_counts()) # counts the number of occurrences of each genre
# print(pd.crosstab(movies.genre, movies.star_rating)) # creates a cross tabulation of genre and star_rating
# ufo=pd.read_csv('https://bit.ly/uforeports')
# print(ufo.isnull()) 
# print(ufo.notnull())  
# print(ufo.isnull().sum())  # counts the number of null values in each column
# print(ufo.dropna(how='all')) # drops rows where all values are null
# print(ufo.dropna(subset=['City', 'Colors Reported'], how='all'))  # drops rows where any of the specified columns have null values
# print(ufo['Shape Reported'].fillna(value='MISC', inplace=True))  # fills null values in 'Shape Reported' column with 'MISC'
# print(ufo['Shape Reported'].value_counts())  # counts the number of occurrences of each value in 'Shape Reported' column
ufo=pd.read_csv('https://bit.ly/uforeports')
# print(ufo.loc[0:2,:])
# print(ufo.loc[ufo.City=='New York', 'City':'State'])
# # iloc specifies the index of the row and column
# print(ufo.head())
# print(ufo.ix[0:2, 0:2]) # ix is deprecated, use loc or iloc instead
print(ufo.drop('City', axis=1, inplace=True).head()) # drops the 'City' column and prints the first 5 rows and inplace=True means it modifies the original dataframe