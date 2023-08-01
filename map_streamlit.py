import streamlit as st
import pandas as pd
from datetime import datetime

def main():
    df = pd.read_csv('result_final.csv',
                     usecols=['확진일','address', 'lat', 'lng'])

    date_list = []

    for i, row in df.iterrows():
        date_list.append(row['확진일'])

    # print(date_list)
    # print(df.columns)
    # print(date_dict)

    df.columns = ['확진일', 'address', 'lat', 'lon'] # lng -> lon

    st.header('야생멧돼지 아프리카돼지열병 발생 현황')

    # choose_date = st.slider("DATE", value=datetime(2019, 10, 3),
    #                         min_value=datetime(2019, 10, 3),
    #                         max_value=datetime(2023, 6, 13),
    #                         format="YY/MM/DD")

    start_dt = datetime(2019, 10, 3)
    end_dt = datetime(2023, 6, 13)
    index_dt = datetime(2020, 10, 30)

    choose_date = st.slider('Select date range', min_value=start_dt, value=[start_dt, index_dt] ,
                            max_value=end_dt, format="YY/MM/DD")


    # print(choose_date)

    start_date = choose_date[0].strftime("%Y-%m-%d")
    end_date = choose_date[1].strftime("%Y-%m-%d")

    st.write("Selected Start Date: ", start_date)
    st.write("Selected End Date: ", end_date)
    # print(start_date)
    # print(end_date)

    selected_date_range = df[(df['확진일'] >= start_date) & (df['확진일'] <= end_date)]
    # print(selected_date_range)
    # m = folium.Map(location=[37, 127], zoom_start=6.5, min_zoom=5, max_zoom=12)

    st.map(selected_date_range, zoom=7, color="#ff333333")
    # st.map(df_geo, zoom=7)



if __name__ == '__main__':
    main()