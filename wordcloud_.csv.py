from wxpy import *
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pandas import DataFrame

bot = Bot(cache_path=True)
friends = bot.friends(update=False)

#提取好友签名，并去掉span，class，emoj等的字段
my_signatures = []
for i in friends[1:]:
    signature = i.signature.strip().replace("span", "").replace("class", "").replace("emoji", "")

    rep = re.compile("[^\u4e00-\u9fa5^]")
    signature = rep.sub("", signature)
    my_signatures.append(signature)
# 拼接字符串
text = "".join(my_signatures)
# jieba分词
wordlist = jieba.cut(text, cut_all=True)
result = " ".join(wordlist)

# wordcloud词云
wordcloud = WordCloud(background_color="white",
                         max_words=2000,
                         max_font_size=1000,
                         random_state=42,
                         font_path='C:\Windows\Fonts\simsun.ttc').generate(result)

wordcloud.to_file('output.jpg')
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

def get_var(User):
    User_dict = {}
    User_dict["Name"] = User.name if User.name else "NaN"
    User_dict["City"] = User.city if User.city else "NaN"
    User_dict["Sex"] = User.sex if User.sex else 0
    User_dict["Signature"] = User.signature if User.signature else "NaN"
    User_dict["Province"] = User.province if User.province else "NaN"
    return User_dict


friends_list = [get_var(i) for i in friends]
frame = DataFrame(friends_list)
frame.to_csv('data.csv', index=True, encoding='utf-8-sig')