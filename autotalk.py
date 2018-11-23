from wxpy import *
bot=Bot()

xiaoi=XiaoI('key','secret')
my_friend=bot.friends()

@bot.register(my_friend,TEXT)
def reply(msg):
    xiaoi.do_reply(msg)

embed()
