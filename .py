# import needed libraries
import pandas as pd
import num
# read excel file
df = pd.read_csv('data/train_modified.csv')

# display general information of the df
display(df.info())

# display 5 random samples of our df
display(df.sample(5))


# this code was used to modify the data and add nan values to a new excel sheet
# !do not run this code 

# replace_idx = np.random.choice(df.index, size=int(len(df)*0.005), replace=False)
# col_to_replace = 'SQUARE_FT'
# df.loc[replace_idx, col_to_replace] = np.nan


# df.to_csv('data/train_modified1.csv', index=False)
# display(df)
# lets fix the nan values

for col in df.columns:
    # check if the column is of object type
    if df[col].dtype == 'object':
        # replace missing values with the most occurred string
        value = df[col].mode()[0]
    else:
        # if the values are nominal(0, 1, nan) replace with mod
        if len(df[col].unique()) == 3:
            # replace missing values with the mode value
            value = df[col].mode()[0]

        else:
            # replace missing values with the mean value
            value = df[col].mean()
            
    df[col].fillna(value, inplace = True)
            
display(df.info())


# now we need to remove the outliers
display(df.iloc[530:550, 2])
