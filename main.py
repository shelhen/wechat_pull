from resource import utils
from resource import config
from resource.wechat import WeChat
from resource.apis import ApiGenertor
from apscheduler.executors.pool import ThreadPoolExecutor as ApsThreadPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler


class ExctorMain(object):
    def __init__(self):
        self.appid = config.appid
        self.api = ApiGenertor()
        self.wechat = WeChat()
        # self.wework = Wework()

    def run_wechat(self):
        print("当前执行微信公众测试号推送")
        datelist = utils.get_times()
        # boy_cityCode, boy_city_name = self.api.get_cityid(config.boy_cityName, self.appid)
        girl_cityCode, girl_city_name = self.api.get_cityid(config.girl_cityName, self.appid)
        werther_list_g, su_list_g = self.api.get_weather(girl_cityCode, self.appid)
        # werther_list_b, su_list_b = self.api.get_weather(boy_cityCode, self.appid)
        content = self.api.get_loveword()
        note_cn, note_en = self.api.iciba()
        # 自定义消息模板的变量必须是全部小写
        msg = {
            "date": {"value": datelist[0], "color": utils.generateColor()},
            "city": {"value": girl_city_name, "color": utils.generateColor()},
            "weather": {"value": werther_list_g[0], "color": utils.generateColor()},
            "temp": {"value": werther_list_g[1], "color": utils.generateColor()},
            "loveDays": {"value": datelist[1], "color": utils.generateColor()},
            "loveDay": {"value": datelist[2], "color": utils.generateColor()},
            "girlBirthday": {"value": datelist[3], "color": utils.generateColor()},
            "boyBirthday": {"value": datelist[4], "color": utils.generateColor()},
            "meetDay": {"value": datelist[5], "color": utils.generateColor()},
            "noteEn": {"value": note_en, "color": utils.generateColor()},
            "noteCh": {"value": note_cn, "color": utils.generateColor()},
            "loveWord": {"value": content, "color": utils.generateColor()},
            "health": {"value": su_list_g[1], "color": utils.generateColor()}
        }
        self.wechat.senMsg(msg)
        print('执行完毕！')

    def run_wework(self):
        print("当前执行企业推送")

        # text = []
        # text.append("【亲爱的老婆, 你好呀!】")
        # text.append("\n")
        # text.append("今天是:  {} {}".format(today, week))
        # text.append("城市:  {}".format(config.conf["CityInfo"]["cityName"]))
        # text.append("天气:  {}".format(weather))
        # text.append("气温:  {}℃".format(temperature))
        # text.append("今天是我们恋爱的第   [{}] 天".format(love_days))
        # text.append("同时也是我们结婚的第 [{}] 天".format(marry_days))
        # text.append("距离小宝生日还有 [{}] 天".format(girlBirthday))
        # text.append("距离我的生日还有 [{}] 天".format(boyBirthday))
        # logger.info("\n".join(text))
        # wework.sendMsg(text="\n".join(text))


if __name__ == '__main__':
    main = ExctorMain()
    main.run_wechat()

    # executors = {
    #     "default": ApsThreadPoolExecutor(max_workers=3)
    # }
    # scheduler = BlockingScheduler(executors=executors, timezone='Asia/Shanghai')
    # scheduler.add_job(func=main.run_wechat(), trigger="cron", hour=17, minute=34)
    # scheduler.start()