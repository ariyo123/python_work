import pandas as pd

# the SQL that will return what i want
# SELECT name, email FROM mytable LEFT JOIN myothertable ON mytable.id = myothertable.id WHERE mytable.id = 1234 AND myothertable.id IS NULL;

# # Load the first DataFrame
path1='C:/python_work/record_rec/bank_code.csv'
with open(path1, 'r') as file_object:
    lines=file_object.read()
        #print(lines)
    banks=lines.split()
    print(banks)
    for bank in banks[:]:
        df = pd.read_csv("icad_data_final.csv")
        dfo=df.sort_values(by='BVN')
        dfoo=dfo.reset_index(drop=True)
        #add leading Zero to the accont column
        dfoo['Account']=df['Account'].apply(lambda x: '{0:0>12}'.format(x))
        #dfoo['bank']=df['bank'].apply(lambda x: '{0:0>5}'.format(x))
        # rename column each of the out puted columns to the ones below
        dfoo.rename(columns={'BVN': 'BVN_ICAD'}, inplace=True)
        dfoo.rename(columns={'first_name': 'first_name_CAD'}, inplace=True)
        dfoo.rename(columns={'Middle_name': 'Middle_nameICAD'}, inplace=True)
        dfoo.rename(columns={'Surname': 'Surname_ICAD'}, inplace=True)
        dfoo.rename(columns={'DOB': 'DOB_ICAD'}, inplace=True)
        dfoo.rename(columns={'account': 'Account_ICAD'}, inplace=True)
        dfoo.rename(columns={'bank': 'bank_ICAD'}, inplace=True)
        #dfoo.round()
        # drop columns that are not needed so that the two dataframes to be compared has same number of columns
        df1=df.drop(['Account'], axis=1)
        df1=df1.drop(['Bank'], axis=1)
        # # Load the second DataFrame
        df2 = pd.read_csv("bvn_data_final.csv")


        # Sort the dataframe so that the comparism cam be equivalent in field position
        df11=df1.sort_values(by='BVN')
        df21=df2.sort_values(by='BVN')

        #after sorting the index positioning would have changed Hence,
        # we reset the index labels to default integers before comparing the dataframes.

        df111=df11.reset_index(drop=True)
        df211=df21.reset_index(drop=True)

        # create a boolean mask indicating which values are equal
        mask = df111== df211
        #mask=df211[~df211.isin(df111)].dropna()

        # rename column each of the out puted columns to the ones below

        mask.rename(columns={'BVN': 'BVN correct on ICAD?'}, inplace=True)
        mask.rename(columns={'first_name': 'first_name correct on ICAD?'}, inplace=True)
        mask.rename(columns={'Middle_name': 'Middle_name correct on ICAD?'}, inplace=True)
        mask.rename(columns={'Surname': 'Surname correct on ICAD?'}, inplace=True)
        mask.rename(columns={'DOB': 'DOB correct on ICAD?'}, inplace=True)

        # print(df)
        print(mask)

        # use the mask to extract the rows with equal values
        # equal_rows = df1[mask]
        # print(equal_rows)

        df_merged = pd.concat([df211, mask,dfoo], axis=1)
        #df_merged['bank_ICAD'].astype(int)
        print(df_merged)
        df_merged.to_csv(f'Comparism_report_{bank}.csv', index=False)