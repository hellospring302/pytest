s="钟山风雨起苍黄，百万雄师过大江。\
虎踞龙盘今胜昔，天翻地覆慨而慷。\
宜将剩勇追穷寇，不可沽名学霸王。\
天若有情天亦老，人间正道是沧桑。"
lines=""
for i in range(0,len(s),8):
    lines+=s[i:i+7].center(30)+"\n"
print(lines)

