import requests
import json

url = 'https://ihotel.meituan.com/group/v2/poi/detail/service?utm_medium=pc&version_name=999.9&poiId=113866412&X-FOR-WITH=MgIWtDZcIg0cdMoDUvKPAJp%2FJKznaSDCU9bWjOBtxEYwaMD7QaWHic2IvX9CUe8%2Fb%2FBeYTaalfVJbPyySFDYMqcV1rZrNU7FSMaMM5vOhZufsL8rq5DQNSxe%2Fwxk4cF3WMTvDLrTLC38nF3bAinNQA%3D%3D'

url = """https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&uuid=4C4844EA1E383289F62BCF8C630947BC4DA3121E283B39A9EF152D2C34203C23%401533035086135&cityId=96&offset=20&limit=20&startDay=20180731&endDay=20180731&q=&sort=defaults&X-FOR-WITH=MgIWtDZcIg0cdMoDUvKPAJp%2FJKznaSDCU9bWjOBtxEaoGHEyTVOVtWGyk8cZsmabPFPoxPrYrkopNdwtVAxFP9%2BiEQN4JoCesIugMEnZv6a3FVF0GY2lAyNttxcS8A9n6OOzi7eIkXIaOPMBy%2FWH1w%3D%3D
"""

# response = requests.get(url)
# result = json.loads(response.text)
# print(type(result))
# for i in result['data']['searchresult']:
#     for k,v in i.items():
#         print(k,v)
#     print('-' * 100)

# 获取酒店图片
url = """https://ihotel.meituan.com/group/v1/poi/159217998/imgs?utm_medium=touch&version_name=999.9&classified=true&X-FOR-WITH=s99Eh6sbSKFk2CtgH69UM3vUAY6t0ETpasHKECThU0OOv6duCovPaszE2v8xYNb0y5tFbd0R1Bz7HxqoWbDCnlQzCaz1U%2FWG2Is1UD6ycN%2Fv5sM9vSw%2BtMe6IAQAogdarTlC3CQPD6IfxiaVmV005g%3D%3D
"""
import re

response = requests.get(url)
result = response.json()
images_list = []
for i in result['data']:
    for j in i['imgs']:
        img_url = j['urls'][0]
        img_url = re.sub('w.h', '750.0', img_url)
        images_list.append(img_url)

string = 'http://p1.meituan.net/750.0/tdchotel/dc301f99368714152275b2be4f6c6439769418.png'
print(string[-10:])