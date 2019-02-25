s="钟山风雨起苍黄，百万雄师过大江。\
虎踞龙盘今胜昔，天翻地覆慨而慷。\
宜将剩勇追穷寇，不可沽名学霸王。\
天若有情天亦老，人间正道是沧桑。"
ls=[]
for i in range(0,len(s),8):
    ls.append(s[i:i+8])
ls.reverse()
for item in ls:
    print(item,end="")
