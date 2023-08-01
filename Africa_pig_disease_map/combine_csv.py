import pandas as pd

def main():
    df1 = pd.read_csv('input/total_data.csv', encoding='utf-8-sig')
    df2 = pd.read_csv('input/위경도_예외_추가.csv', encoding='euc-kr')
    df2 = df2.drop_duplicates(subset=['address'])
    df2 = df2[['address', 'lat','lng']]

    # method 1
    df_fix = pd.merge(df1, df2, how='left', on='address')
    df_fix["lat"] = df_fix["lat_x"]
    df_fix["lng"] = df_fix["lng_x"]
    df_fix.loc[df_fix["lat_x"] == "x", "lat"] = df_fix["lat_y"]
    df_fix.loc[df_fix["lng_x"] == "x", "lng"] = df_fix["lng_y"]

    df_fix = df_fix.drop(columns=["lat_x", "lat_y", "lng_x", "lng_y"])

    # method 2
    addr_dict = {}

    for i, row in df2.iterrows():
        addr_dict[row["address"]] = [row["lat"], row["lng"]]
    print(df1.columns)
    df1["lat"] = df1.apply(lambda row: addr_dict[row["address"]][0] if row["lat"] == "x" else row["lat"], axis=1)
    df1["lng"] = df1.apply(lambda row: addr_dict[row["address"]][1] if row["lng"] == "x" else row["lng"], axis=1)

    # save file
    df_fix.to_csv("result_final.csv", encoding='utf-8-sig', index=False)
    df1.to_csv("result_final2.csv", encoding='utf-8-sig', index=False)


if __name__ == '__main__':
    main()
