import pandas as pd
# import os
# # Load the first DataFrame
df = pd.read_csv("icad_data.txt.csv")
dfo=df.sort_values(by='count')
dfoo=dfo.reset_index(drop=True)
#add leading Zero to the accont column
dfoo['account']=df['account'].apply(lambda x: '{0:0>12}'.format(x))
#dfoo['bank']=df['bank'].apply(lambda x: '{0:0>5}'.format(x))
# rename column each of the out puted columns to the ones below
dfoo.rename(columns={'AGT MGT INST NAME': 'AGT MGT INST NAME_ICAD'}, inplace=True)
dfoo.rename(columns={'AGENT CODE': 'AGENT CODE_CAD'}, inplace=True)
dfoo.rename(columns={'count': 'count_ICAD'}, inplace=True)
dfoo.rename(columns={'Actual_Pay': 'Actual_Pay_ICAD'}, inplace=True)
dfoo.rename(columns={'account': 'Account_ICAD'}, inplace=True)
dfoo.rename(columns={'bank': 'bank_ICAD'}, inplace=True)
# drop columns that are not needed so that the two dataframes to be compared has same number of columns
df1=df.drop(['account'], axis=1)
df1=df1.drop(['bank'], axis=1)
# # Load the second DataFrame
df2 = pd.read_csv("bvn_data.txt.csv")


# Sort the dataframe so that the comparism cam be equivalent in field position
df11=df1.sort_values(by='count')
df21=df2.sort_values(by='count')

#after sorting the index positioning would have changed Hence,
# we reset the index labels to default integers before comparing the dataframes.

df111=df11.reset_index(drop=True)
df211=df21.reset_index(drop=True)

# create a boolean mask indicating which values are equal
mask = df111== df211

# rename column each of the out puted columns to the ones below
mask.rename(columns={'AGT MGT INST NAME': 'AGT MGT INST NAME correct on ICAD?'}, inplace=True)
mask.rename(columns={'AGENT CODE': 'AGENT CODE correct on ICAD?'}, inplace=True)
mask.rename(columns={'count': 'count correct on ICAD?'}, inplace=True)
mask.rename(columns={'Actual_Pay': 'Actual_Pay correct on ICAD?'}, inplace=True)
# print(df)
print(mask)

# use the mask to extract the rows with equal values
# equal_rows = df1[mask]
# print(equal_rows)

df_merged = pd.concat([df211,mask,dfoo], axis=1)
print(df_merged)
df_merged.to_csv(f'report.csv', index=False)