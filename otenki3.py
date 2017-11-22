#!/usr/bin/env python
import pywapi
from numpy.random import *
from twitter import *

ACCESS_TOKEN = "863556291729301504-MaPF7pwhLQtFwUrtMIzxS0gQd7wEEOC"
ACCESS_TOKEN_SECRET = "fCp80ufrYK6rMVI9lqC0SOiXE6kRlTj4T7lhw6aZdKDw1"
CONSUMER_KEY = "fSMitUng7w3UkXU4kCMYrXmC6"
CONSUMER_SECRET = "SSsyuo4tE6RW8yQLAZJLLa9795NYcd4mppLnkEDHOcv6iuSIqU"

t = Twitter(auth=OAuth(ACCESS_TOKEN,
                       ACCESS_TOKEN_SECRET,
                       CONSUMER_KEY,
                       CONSUMER_SECRET)
            )

r_num = randint(0,2,5)       #  0〜1 の整数を5個生成

t.statuses.update(status="今日寒すぎ")


result1 = pywapi.get_weather_from_weather_com('JAXX0085') 
h_tug = "#デレマス朝の天気予報"

def idlst(key_num,c_max,c_min,cp, hum, w_s):
	i_l = {0:
		{ 
		"name" : "udsuki",
		"aisatsu" : "プロデューサーのみなさん、おはようございます！島村卯月です。今日の東京の天気をお伝えします。",
		"tenki" : { 
"sunny" : "今日の天気は晴れ。気持ちのいい一日になりそうです。", 
"p_cloudy" : "今日は少し曇りますが、概ね晴れる予想です。", 
"m_cloudy" : "今日は曇り空の広がる一日となりそうです。" , 
"rainy" : "今日の天気は雨、", 
"storm" : "今日は嵐が襲ってきます。プロデューサーさん気をつけてくださいね。",
"am_rain" : "今日は午前中に雨が降る予報です。",
"pm_rain" : "今日は午後に雨が降る予報です。" ,
"shower":"今日はにわか雨が降る予報です。" ,
"else":"今日は風の強い一日となるでしょう。"},
"kion" : "最高気温は" +str(c_max) +"度、最低気温は" +str(c_min) +"度です。",
"comment" : { 
"cold" : 
{ "tf" : False , "text" : "今日は最高気温が"+str(c_max)+ "度で、肌寒い一日となります。風邪には気をつけて今日もお仕事頑張りましょう。"},
"hot" : { "tf" : False , "text" : "今日は最高気温が" + str(c_max)+ "度の暑い一日となりそうです。熱中症には気をつけてくださいね。"},
"w_rain" : { "tf" : False , "text" : "降水確率は" + str(cp) + "%、傘を持っていったほうがいいかもしれませんね。"},
"s_rain" : { "tf" : False , "text" : "降水確率は" + str(cp) + "%、傘を忘れずに持っていきましょう！"},
"dry":{"tf":False, "text":"今日は湿度が" + str(hum)+ "%を下回り乾燥するので気をつけてくださいね。"},
"strong_wind" : { "tf" : True , "text" : "時速"  + str(w_s) + "キロメートルの強い風が吹きます。"} ,
"wind_and_rain" : { "tf" : False , "text" : "降水確率は" +str(cp)+ "%、そして時速" +str(w_s) + "の強い風が吹きます。\n外に出かける際は気をつけてくださいね。"},
"nothing" : { "tf" : False , "text" : "島村卯月、今日も頑張ります！"}
}
},

1:
{ "name" : "rin" ,
"aisatsu" : "みんなおはよう。渋谷凛です。今日の東京の天気を発表するよ。",
"tenki" : { 
"sunny" : "今日の天気は晴れていい天気だよ", 
"p_cloudy" : "今日は大体晴れるって。", 
"m_cloudy" : "今日はまあまあ曇るみたい。" , 
"rainy" : "今日の天気は雨、", 
"storm" : "今日は嵐がくるよ。ハナコが心配。",
"am_rain":"今日は午前中に雨が降る予報です。",
"pm_rain":"今日は午後に雨が降る予報です。",
"shower":"今日はにわか雨が降るみたいだよ。",
"else":"今日は風の強い一日となるでしょう。"},
"kion" : "最高気温は" +str(c_max) +"度、最低気温は" +str(c_min) +"度。",
"comment" : { 
"cold" : 
{ "tf" : False , "text" : "今日は最高気温が"+str(c_max)+ "度しかないから結構寒くなるよ。"},
"hot" : { "tf" : False , "text" : "今日は最高気温が" + str(c_max)+ "を越えるから暑いって。"},
"w_rain" : { "tf" : False , "text" : "降水確率は" + str(cp) + "%、傘を持っていったほうがいいかもよ。"},
"s_rain" : { "tf" : False , "text" : "降水確率が" + str(cp) + "%だから傘は忘れないようにね。"},
"dry":{"tf":False, "text":"今日は湿度が" + str(hum)+ "%を下回り乾燥するので気をつけてくださいね。"},
"strong_wind" : { "tf" : True , "text" : "今日は時速"  + str(w_s) + "キロメートルの強い風が吹きます。"} ,
"wind_and_rain" : { "tf" : False , "text" : "降水確率は" +str(cp)+ "%、そして時速" +str(w_s) + "の強い風が吹きます。\n外に出かける際は気をつけてくださいね。"},
"nothing" : { "tf" : False , "text" : "それじゃプロデューサー、今日もよろしくね。"}
}
}
}
	return i_l[key_num]


def get_weather(result,t):
	date = result["forecasts"][t]["date"]
	tenki = result["forecasts"][t]["day"]["text"]
	c_max = result["forecasts"][t]["high"]
	c_min = result["forecasts"][t]["low"]
	cp = result["forecasts"][t]["day"]["chance_precip"]
	hum = result["forecasts"][t]["day"]["humidity"]
	wind_speed = result["forecasts"][t]["day"]["wind"]["speed"]
	return ( date , tenki , c_max , c_min , cp , hum ,wind_speed )


def tweet(g_w,r_n):
	date = g_w[0]
	tenki = g_w[1]
	c_max = g_w[2]
	c_min = g_w[3]
	cp = g_w[4]
	
	
	i_l = idlst(r_num[0],c_max,c_min,cp,g_w[5],g_w[6])
	rain_s = False
	wind_s = False
	
	#tenki文の決定
	if "Sunny" in g_w[1]:
		key = "sunny"
	elif "Partly Cloudy" in g_w[1]:
		key = "p_cloudy"
	elif "Cloudy" in g_w[1]:
		key = "m_cloudy"
	elif "AM Rain" in g_w[1]:
		key = "am_rain"
		rain_s = True
	elif "PM Rain" in g_w[1]:
		key = "pm_rain"
		rain_s = True
	elif "Rain" in g_w[1]:
		key = "rainy"
		rain_s = True
	elif "Storm" in g_w[1]:
		key = "storm"
		rain_s = True
	elif "Showers" in g_w[1]:
		key = "shower"
		rain_s = True
	else:
		key = "else"
	
	if type(g_w[6]) == int:
		if int(g_w[6]) >= 20:
			wind_s = True
	
	#comment文の決定
	if wind_s == True and rain_s == True:
		key2 = "wind_and_rain"
	elif rain_s == True:
		if int(cp) >= 30:
			i_l["comment"]["s_rain"]["tf"] = True
			key2 = "s_rain"
		elif int(cp) > 0:
			i_l["comment"]["w_rain"]["tf"] = True
			key2 = "w_rain"
		else:
			key2 = "nothing"
	elif wind_s == True:
		key2 = "strong_wind"
		
	else:
		key2_s = []
		if int(c_max) <= 10:
			i_l["comment"]["cold"]["tf"] = True
			key2_s.append("cold")
		if int(c_max) >= 30:
			i_l["comment"]["hot"]["tf"] = True
			key2_s.append("hot")
		if int(g_w[5]) <= 30:
			i_l["comment"]["dry"]["tf"] = True
			key2_s.append("dry")
		
		if key2_s == []:
			key2 = "nothing"
		else:
			r_com = randint(0,len(key2_s))
			key2 = key2_s[r_com]
			
			
	print("今日は", date , "日です。")
	print(i_l["aisatsu"])
	print(i_l["tenki"][key])
	print(i_l["kion"])
	print(i_l["comment"][key2]["text"])
	print(h_tug)

#main_loop
if __name__ == "__main__":
	for i in range(5):
		tweet(get_weather(result1,i),r_num)