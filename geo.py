import time

from geopy.geocoders import Nominatim
import pandas as pd
import tqdm
from urllib import parse
from urllib.request import Request
from urllib.error import HTTPError
from urllib.request import urlopen
import json

# naver api
client_id = 'fdlzw4zacp'    # 본인이 할당받은 ID 입력
client_pw = 'IndKXhMmW6FoJfHDlGvxPMGHGjOfhdiyyq1wXIJx'    # 본인이 할당받은 Secret 입력

api_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='

def geocoding(address):
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    geo = geolocoder.geocode(address)
    crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}


    return crd

# crd = geocoding("파주 군내면 읍내리 511")
# print(crd['lat'])
# print(crd['lng'])

def naver_geocode(add):
    add_urlenc = parse.quote(add)   # 주소를 URL에서 사용할 수 있도록 URL Encoding
    url = api_url + add_urlenc
    request = Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_pw)
    try:
        response = urlopen(request)
    except HTTPError as e:
        print('HTTP Error!')
        latitude = None
        longitude = None
    else:
        rescode = response.getcode()  # 정상이면 200 리턴
        if rescode == 200:
            response_body = response.read().decode('utf-8')
            response_body = json.loads(response_body)   # json
            if 'addresses' in response_body:
                # print(add, response_body['addresses'])
                if len(response_body['addresses']) > 0:
                    latitude = response_body['addresses'][0]['y']
                    longitude = response_body['addresses'][0]['x']
                else:
                    latitude = 'x'
                    longitude = 'x'
                # print("Success!")
            else:
                print("'result' not exist!")
                latitude = None
                longitude = None
        else:
            print('Response error code : %d' % rescode)
            latitude = None
            longitude = None

    time.sleep(0.5)

    return (latitude, longitude)

def main():
    df = pd.read_excel('야생멧돼지 아프리카돼지열병 발생 현황.xlsx')
    df = df.loc[:, '구분':'주 소']
    # print(df)
    # print(df['시군구'] + ' ' + df['주 소'])
    df['address'] = df['시군구'] + ' ' + df['주 소']

    lats = []
    lngs = []

    geolocoder = Nominatim(user_agent='South Korea', timeout=None)

    for addr in tqdm.tqdm(df['address']):

        try:
            # latlon = geolocoder.geocode(i)
            # lat = latlon.latitude
            # lng = latlon.longitude
            latlon = naver_geocode(addr)
            lat = latlon[0]
            lng = latlon[1]
            # lat = geo_dic['lat']
            # lng = geo_dic['lng']
            lats.append(lat)
            lngs.append(lng)

        except AttributeError:
            # print(i)
            lats.append('x')
            lngs.append('x')

    df['lat'] = lats
    df['lng'] = lngs
    #
    # print(df)
    #

    # df['lat'] = df['address'].apply(geocoding)['lat']
    print(df)

    df.to_csv("test.csv", index = False, encoding='utf-8-sig')


if __name__ == '__main__':
    main()
