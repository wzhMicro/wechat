from wxpy import *
from matplotlib.font_manager import  FontProperties
import matplotlib.pyplot as plot
bot = Bot(cache_path=True)
my_friends = bot.friends()
print(my_friends.stats_text())
FontPath = 'C:\Windows\Fonts\simsun.ttc'
Font = FontProperties(fname=FontPath)

def provinceDist(my_friends):
    province_dict = {'北京': 0, '上海': 0, '天津': 0, '重庆': 0,
                     '河北': 0, '山西': 0, '吉林': 0, '辽宁': 0, '黑龙江': 0,
                     '陕西': 0, '甘肃': 0, '青海': 0, '山东': 0, '福建': 0,
                     '浙江': 0, '台湾': 0, '河南': 0, '湖北': 0, '湖南': 0,
                     '江西': 0, '江苏': 0, '安徽': 0, '广东': 0, '海南': 0,
                     '四川': 0, '贵州': 0, '云南': 0,
                     '内蒙古': 0, '新疆': 0, '宁夏': 0, '广西': 0, '西藏': 0,
                     '香港': 0, '澳门': 0, '其他': 0}

    # 统计省份
    for friend in my_friends:
        if friend.province in province_dict.keys():
            province_dict[friend.province] += 1
        if friend.province not in province_dict.keys():
            province_dict['其他'] += 1

    # 生成JSON Array格式数据
    data = []
    for key, value in province_dict.items():
        data.append({'name': key, 'value': value})

    print(data)

    all_dict = {}
    for friend in my_friends:
        province = friend.province if friend.province.strip() else 'other'
        if province in all_dict :
            all_dict[province] += 1
        else:
            all_dict[province] = 1


    plot.figure(1, figsize=[10, 6])
    plot.title('\"%s\"的微信朋友地区分布统计' % bot.self.name,fontproperties=Font)
    plot.xlabel('城市',fontproperties=Font)
    plot.ylabel('分布人数',fontproperties=Font)

    x = range(0, len(all_dict .keys()))
    plot.bar(left=x,
             height=list(all_dict .values()),
             align='center',
             )

    plot.xticks(x, list(all_dict .keys()), rotation=90,fontproperties=Font)

    for (x, key) in enumerate(all_dict .keys()):
        plot.text(x - 0.25, all_dict [key] + 1.5, '%d' % all_dict [key], rotation=90,fontproperties=Font)
    provinceDistImg = 'province.png'
    plot.savefig(provinceDistImg)
    plot.close('all')
    return provinceDistImg
if __name__ == '__main__':
    provinceDist(my_friends)