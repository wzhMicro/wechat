from wxpy import *
bot=Bot()
my_friend=bot.friends()

sexdict = {'male': 0, 'female': 0, 'other': 0}

for friend in my_friend:
    if friend.sex == 1:
        sexdict['male'] += 1
    elif friend.sex == 2:
        sexdict['female'] += 1
    else:
        sexdict['other']+=1

print(sexdict)