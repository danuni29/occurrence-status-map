# 야생멧돼지 아프리카돼지열병 발생 현황

### Africa_pig_disease_map

* [`geo.py`](./Africa_pig_disease_map/geo.py) : 네이버 지도 api를 활용해서 위경도 추가
* [`combine_csv.py`](./Africa_pig_disease_map/combine_csv.py) : 예외 항목([위경도_예외_추가.csv](./input/위경도_예외_추가.csv))과 전체 데이터 합치기
* [`map_streamlit.py`](./Africa_pig_disease_map/map_streamlit.py) : 위경도가 포함된 데이터로 스트림릿에 지도 그리기

### Result

포트번호 : 8601

![readme jpg](https://github.com/danuni29/occurrence-status-map/assets/117696370/bd57f663-0ac6-40cc-869e-8f4752bfb59a)

