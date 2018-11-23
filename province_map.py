from wxpy import *
from matplotlib.font_manager import  FontProperties
import matplotlib.pyplot as plot
bot = Bot(cache_path=True)
my_friends = bot.friends()
print(my_friends.stats_text())
FontPath = 'C:\Windows\Fonts\simsun.ttc'
Font = FontProperties(fname=FontPath)

def provinceDist(my_friends):
    province_dict = {'����': 0, '�Ϻ�': 0, '���': 0, '����': 0,
                     '�ӱ�': 0, 'ɽ��': 0, '����': 0, '����': 0, '������': 0,
                     '����': 0, '����': 0, '�ຣ': 0, 'ɽ��': 0, '����': 0,
                     '�㽭': 0, '̨��': 0, '����': 0, '����': 0, '����': 0,
                     '����': 0, '����': 0, '����': 0, '�㶫': 0, '����': 0,
                     '�Ĵ�': 0, '����': 0, '����': 0,
                     '���ɹ�': 0, '�½�': 0, '����': 0, '����': 0, '����': 0,
                     '���': 0, '����': 0, '����': 0}

    # ͳ��ʡ��
    for friend in my_friends:
        if friend.province in province_dict.keys():
            province_dict[friend.province] += 1
        if friend.province not in province_dict.keys():
            province_dict['����'] += 1

    # ����JSON Array��ʽ����
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
    plot.title('\"%s\"��΢�����ѵ����ֲ�ͳ��' % bot.self.name,fontproperties=Font)
    plot.xlabel('����',fontproperties=Font)
    plot.ylabel('�ֲ�����',fontproperties=Font)

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