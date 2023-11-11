import pandas as pd

path1='C:/python_work/record_rec/App/bank_code.csv'
with open(path1, 'r') as file_object:
    lines=file_object.read()
        #print(lines)
    banks=lines.split()
    print(banks)
    for bank in banks[:]:
        df1 = pd.read_csv("bvn_data.txt.csv")

        df2 = pd.read_csv(f"icad_data{bank}.txt.csv")
        print(df1)
        print(df2)

        #checking for difference in two dataframes using a column "BVN" for the checks
        common_df = pd.merge(df1, df2, on='BVN', how='inner')
        print(common_df)
        common_df.rename(columns={'first_name_y': 'first_name'}, inplace=True)
        common_df.rename(columns={'Middle_name_y': 'Middle_name'}, inplace=True)
        common_df.rename(columns={'Surname_y': 'Surname'}, inplace=True)
        common_df.rename(columns={'DOB_y': 'DOB'}, inplace=True)
        common_df.rename(columns={'account': 'Account'}, inplace=True)
        common_df.rename(columns={'bank': 'bank'}, inplace=True)
        print(common_df)
        df = common_df.drop_duplicates(subset=['BVN']).reset_index(drop=True)
        df = df.drop(['first_name_x', 'Middle_name_x', 'Surname_x', 'DOB_x'], axis=1, inplace=False)


        print(df)

        df.to_csv(f'icad_data_final{bank}.csv', index=False)

        common_df1 = pd.merge(df1, df2, on='BVN', how='inner')
        common_df1.rename(columns={'first_name_x': 'first_name'}, inplace=True)
        common_df1.rename(columns={'Middle_name_x': 'Middle_name'}, inplace=True)
        common_df1.rename(columns={'Surname_x': 'Surname'}, inplace=True)
        common_df1.rename(columns={'DOB_x': 'DOB'}, inplace=True)
        common_df1.rename(columns={'account': 'Account'}, inplace=True)
        common_df1.rename(columns={'bank': 'bank'}, inplace=True)
        print(common_df1)
        df = common_df1.drop_duplicates(subset=['BVN']).reset_index(drop=True)

        df = df.drop(['first_name_y', 'Middle_name_y', 'Surname_y', 'DOB_y', 'Account', 'Bank'], axis=1, inplace=False)
        print(df)

        df.to_csv(f'bvn_data_final{bank}.csv', index=False)

        #checking for difference in two dataframes using a column "BVN" for the checks
        merged_df = pd.merge(df1, df2, on='BVN', how='outer', indicator=True)
        diff_df = merged_df[merged_df['_merge'] != 'both']
        print(diff_df)
        diff_df = diff_df[diff_df["_merge"]=='right_only']
        diff_df.to_csv(f'invalid_BVN_on_ICAD_{bank}.csv', index=False)

