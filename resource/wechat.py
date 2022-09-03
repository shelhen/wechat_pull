# -*- coding: utf-8 -*-
import requests
import config


class WeChat(object):

    def __init__(self):
        pass

    def getAccessToken(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": config.appID,
            "secret": config.appSecret,
        }
        accessToken =requests.get(url, params=params, timeout=30).json()["access_token"]
        return accessToken

    def senMsg(self, data):
        accessToken = self.getAccessToken()
        if accessToken:
            url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + accessToken
            for user in config.toUser:
                payload = {
                    "touser": user,
                    "template_id": config.templateId,
                    "url": "http://weixin.qq.com/download",
                    "color": "#FF0000",
                    # "data": json.dumps(data, ensure_ascii=False),
                    "data": data
                }
                requests.post(url, json=payload, timeout=30)