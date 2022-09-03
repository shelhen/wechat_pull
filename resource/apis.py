import requests
import random


class ApiGenertor(object):
    def get_loveword(self):
        # 整点土味情话
        contents = requests.get('https://api.1314.cool/words/api.php?return=json').json()['word']
        return contents

    def get_weather(self, locationid, appid):
        # 天气接口
        # locationid = '101020900'
        url = [
            'https://devapi.qweather.com/v7/weather/now?location='+ locationid +'&key='+ appid,
            'https://devapi.qweather.com/v7/indices/1d?type=1,3,8&location='+ locationid +'&key='+ appid
        ]
        weather = requests.get(url[0] ).json()['now']
        texts = requests.get(url[1] ).json()['daily']
        weather_list = [weather['text'], str(int(weather['temp'])-1) + '~' + weather['feelsLike'] + '℃', ]
        suggestions_list = [random.choice(texts)['name'], random.choice(texts)['text']]
        return weather_list, suggestions_list

    def get_cityid(self, location, appid):
        # 获取城市id
        url = str('https://geoapi.qweather.com/v2/city/lookup?location='+location+'&key=' + appid)
        res = requests.get(url).json()['location'][0]
        id = res['id']
        city_name = res['adm1'].rstrip('市').rstrip('省')+' '+res['name']
        return id, city_name

    def iciba(self):
        text = requests.get("http://open.iciba.com/dsapi/",timeout=10).json()
        note_en = text["content"]
        note_cn = text["note"]
        return note_cn, note_en
