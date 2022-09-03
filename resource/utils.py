import random
import config
from datetime import datetime


def generateColor():
    randomColor = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
    color_list = randomColor(100)
    return random.choice(color_list)


def get_times():
    now = datetime.now()
    week_dict = {
        'Monday': '星期一',
        'Tuesday': '星期二',
        'Wednesday': '星期三',
        'Thursday': '星期四',
        'Friday': '星期五',
        'Saturday': '星期六',
        'Sunday': '星期日'
    }
    date = now.strftime(f"%Y年%m月%d日 {week_dict[str(now.strftime('%A'))]}")
    commemoration = config.commemoration
    girl_birthday = config.girl_birthday
    boy_birthday = config.boy_birthday
    meet_day = config.meet_day
    # 计算在一起总时常
    day_long = str(now - commemoration)[:4]
    # 计算距离恋爱纪念日还有多少天
    dst1 = str(commemoration.replace(year=datetime.now().year+1)-now)[:3]
    # 计算距离女孩生日还有多少天
    dst2 = str(girl_birthday.replace(year=datetime.now().year+1)-now)[:3]
    # 计算距离男孩生日还有多少天
    dst3 = str(boy_birthday.replace(year=datetime.now().year + 1) - now)[:3]
    # 计算距离下次见面还有多少天
    dst4 = str(meet_day- now)[:2]
    return [date, day_long, dst1, dst2, dst3, dst4]