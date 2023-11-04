import telebot
from telebot import types
dict1 = {"METROPOL HOTEL" : "https://www.booking.com/hotel/am/metropol.en-gb.html",
"Ramada Hotel":"https://www.booking.com/hotel/am/ramada-suites-by-wyndham-yerevan.ru.html",
"Ani Grand Hotel":"https://www.booking.com/hotel/am/ani-grand.ru.html",
"Radisson BLU Hotel":"https://www.booking.com/hotel/am/radisson-blu-hotel-yerevan.ru.html",
"Ibis Yerevan Center":"https://www.booking.com/hotel/am/ibis-yerevan-center.ru.html",
"Holiday Inn":"https://www.booking.com/hotel/am/holiday-inn-yerevan-republic-square.ru.html",
"Caucasus Hotel":"https://www.booking.com/hotel/am/caucasus.en-gb.html",
"Paris Hotel":"https://www.booking.com/hotel/am/paris-yerevan.en-gb.html",
"Best Western Plus Congress Hotel":"https://www.booking.com/hotel/am/best-western-congress.en-gb.html",
"Yerevan Centre":"https://www.booking.com/hotel/am/yerevan-center-yerevan.en-gb.html"
}
dict2 = {"Espress It":"https://www.tripadvisor.ru/Restaurant_Review-g293932-d20091342-Reviews-Espress_It-Yerevan.html",
		 "Coffeeshop Company North":"https://www.tripadvisor.ru/Restaurant_Review-g293932-d8764075-Reviews-Coffeeshop_Company_Northern_Avenue-Yerevan.html",
		 "Coffeeshop Company Cascade":"https://www.tripadvisor.ru/Restaurant_Review-g293932-d8764075-Reviews-Coffeeshop_Company_Northern_Avenue-Yerevan.html",
		 "CRUMBS Bread Factory":"https://www.tripadvisor.ru/Restaurant_Review-g293932-d16869513-Reviews-Coffeeshop_Company_Cascade-Yerevan.html",
		 "Eat&Fit Healthy Food Cafe":"https://www.tripadvisor.ru/Restaurant_Review-g293932-d13016549-Reviews-Eat_Fit_Healthy_Food_Cafe-Yerevan.html",
		 "Coffeeshop Company":"https://www.tripadvisor.ru/Restaurant_Review-g293932-d21275035-Reviews-Coffeeshop_Company_Tumanyan-Yerevan.html",
		 "Sorriso Gelato North":"https://www.tripadvisor.ru/Restaurant_Review-g293932-d9878781-Reviews-Sorriso_Gelato_Northern_Avenue-Yerevan.html",
		 "The Green Bean":"https://www.tripadvisor.ru/Restaurant_Review-g293932-d3326692-Reviews-The_Green_Bean-Yerevan.html",
		 "LETE Cafe & Veranda":"https://www.tripadvisor.ru/Restaurant_Review-g293932-d23444246-Reviews-LETE_Cafe_Veranda-Yerevan.html",
		 "Voodoo Hookah Lounge":"https://www.tripadvisor.ru/Restaurant_Review-g293932-d13071666-Reviews-Voodoo_Hookah_Lounge-Yerevan.html"}

dict3={"Syrovarnya Yerevan":"https://www.tripadvisor.com/Restaurant_Review-g293932-d23597267-Reviews-Syrovarnya_Yerevan-Yerevan.html",
	   "Indian Mehak":"https://www.tripadvisor.com/Restaurant_Review-g293932-d10818164-Reviews-Indian_Mehak_Restaurant_Bar-Yerevan.html",
	   "American Hot Wings":"https://www.tripadvisor.com/Restaurant_Review-g293932-d23256488-Reviews-American_Hot_Wings-Yerevan.html",
	   "Yasaman":"https://www.tripadvisor.com/Restaurant_Review-g293932-d19415266-Reviews-Yasaman_Yerevan_s_Restaurant-Yerevan.html",
	   "Sherep":"https://www.tripadvisor.com/Restaurant_Review-g293932-d13157535-Reviews-Sherep_Restaurant-Yerevan.html",
	   "Buzand":"https://www.tripadvisor.com/Restaurant_Review-g293932-d23482824-Reviews-Buzand_Cafe_Restaurant-Yerevan.html",
		"India Palace":"https://www.tripadvisor.com/Restaurant_Review-g293932-d16745741-Reviews-India_Palace-Yerevan.html",
	"Lavash":"https://www.tripadvisor.com/Restaurant_Review-g293932-d12321316-Reviews-Lavash_Restaurant-Yerevan.html",
	"Dari Pandok":"https://www.tripadvisor.com/Restaurant_Review-g293932-d23638485-Reviews-Dari_Pandok-Yerevan.html",
	"Tavern Yerevan Riverside":"https://www.tripadvisor.com/Restaurant_Review-g293932-d14168426-Reviews-Tavern_Yerevan_Riverside-Yerevan.html"
}
bot = telebot.TeleBot("6318903080:AAFCMOFEJ6sb5HGBNYkzW3uwJdP7c4wVC2g")
@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton('🏨 Hotels in Yerevan')
	item2 = types.KeyboardButton('☕Cafes in Yerevan')
	item3 = types.KeyboardButton('🍴 Restaurants in Yerevan')
	markup.add(item1,item2,item3)
	bot.send_message(message.chat.id, "Hello {0.first_name}!  How can I help you?".format(message.from_user), reply_markup = markup  )
@bot.message_handler(content_types=['text'])
def bot_message(message):
	if message.chat.type == 'private':
		if message.text == '🏨 Hotels in Yerevan':
			bot.send_message(message.chat.id, f"Look! This is the list of TOP 10 Yerevan hotels. \n1. METROPOL HOTEL --> 20 000 AMD Per Night \n2. Ramada Hotel & Suites by Wyndham --> 36 900 AMD Per Night\
					\n3. Ani Grand Hotel -->  38 000 AMD Per Night \n4. Radisson BLU Hotel --> 43 000 AMD Per Night\n5. Ibis Yerevan Center --> 24 650 AMD Per Night\n6. Holiday Inn --> 41 820 AMD Per NIght\
					\n7. Caucasus Hotel --> 20 000 AMD Per Night\n8. Paris Hotel --> 40 000 AMD Per Night\n9. Best Western Plus Congress Hotel --> 40 000 AMD Per Night1\n10. Yerevan Centre --> 31 350 AMD Per Night\ ".format(message.from_user))
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item4 = types.KeyboardButton('METROPOL HOTEL')
			item5 = types.KeyboardButton('Ramada Hotel ')
			item13= types.KeyboardButton('Ani Grand Hotel')
			item6 = types.KeyboardButton('Radisson BLU Hotel')
			item7 = types.KeyboardButton('Ibis Yerevan Center')
			item8 = types.KeyboardButton('Holiday Inn')
			item9 = types.KeyboardButton('Caucasus Hotel')
			item10= types.KeyboardButton('Paris Hotel')
			item11= types.KeyboardButton('Best Western Plus Congress Hotel')
			item12= types.KeyboardButton('Yerevan Centre')
			item14= types.KeyboardButton('🔙')
			markup.add(item4,item5,item13,item6,item7,item8,item9,item10,item11,item12,item14)
			bot.send_message(message.chat.id,"Which one interested you?".format(message.from_user), reply_markup = markup)
		elif message.text in dict1:
			bot.send_message(message.chat.id, f"{dict1[message.text]}".format(message.from_user))
		elif message.text =='☕Cafes in Yerevan':
			bot.send_message(message.chat.id,f"Look! This is the list of Yerevan Cafés. \n1. Espress It \n2. Coffeeshop Company Northern Avenue\n3. Coffeeshop Company Cascade\n4. CRUMBS Bread Factory\n5. Eat&Fit Healthy Food Cafe\n6. Coffeeshop Company Tumanyan\
					\n7. Sorriso Gelato Northern Avenue\n8. The Green Bean\n9. LETE Cafe & Veranda\n10.Voodoo Hookah Lounge ".format(message.from_user))
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item4 = types.KeyboardButton('Espress It')
			item5 = types.KeyboardButton('Coffeeshop Company North')
			item13= types.KeyboardButton('Coffeeshop Company Cascade')
			item6 = types.KeyboardButton('CRUMBS Bread Factory')
			item7 = types.KeyboardButton('Eat&Fit Healthy Food Cafe')
			item8 = types.KeyboardButton('Coffeeshop Company')
			item9 = types.KeyboardButton('Sorriso Gelato North')
			item10= types.KeyboardButton('The Green Bean')
			item11= types.KeyboardButton('LETE Cafe & Veranda')
			item12= types.KeyboardButton('Voodoo Hookah Lounge')
			item14= types.KeyboardButton('🔙')
			markup.add(item4,item5,item13,item6,item7,item8,item9,item10,item11,item12,item14)
			bot.send_message(message.chat.id,"Which one interested you?".format(message.from_user), reply_markup = markup)
		elif message.text in dict2:
			bot.send_message(message.chat.id, f"{dict2[message.text]}".format(message.from_user))
		elif message.text =='🍴 Restaurants in Yerevan':
			bot.send_message(message.chat.id, f"Look! This is the list of Yerevan Restaurants.\n1. Syrovarnya Yerevan\n2. Indian Mehak Restaurant & Bar\n3. American Hot Wings\n4. Yasaman Yerevan's Restaurant\n5. Sherep Restaurant\n6. Buzand Cafe Restaurant\n7. India Palace\
					\n8. Lavash Restaurant\n9. Dari Pandok\n10. Tavern Yerevan Riverside".format(message.from_user))
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			item4 = types.KeyboardButton('Syrovarnya Yerevan')
			item5 = types.KeyboardButton('Indian Mehak')
			item13= types.KeyboardButton('American Hot Wings')
			item6 = types.KeyboardButton('Yasaman')
			item7 = types.KeyboardButton('Sherep')
			item8 = types.KeyboardButton('Buzand')
			item9 = types.KeyboardButton('India Palace')
			item10= types.KeyboardButton('Lavash')
			item11= types.KeyboardButton('Dari Pandok')
			item12= types.KeyboardButton('Tavern Yerevan Riverside')
			item14= types.KeyboardButton('🔙')
			markup.add(item4,item5,item13,item6,item7,item8,item9,item10,item11,item12,item14)
			bot.send_message(message.chat.id,"Which one interested you?".format(message.from_user), reply_markup = markup)
		elif message.text in dict3:
			bot.send_message(message.chat.id, f"{dict3[message.text]}".format(message.from_user))
		elif message.text == '🔙':
				markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
				item1 = types.KeyboardButton('🏨 Hotels in Yerevan')
				item2 = types.KeyboardButton('☕Cafes in Yerevan')
				item3 = types.KeyboardButton('🍴 Restaurants in Yerevan')
				markup.add(item1,item2,item3)
				bot.send_message(message.chat.id, "🔙",reply_markup = markup)
		

bot.infinity_polling(none_stop=True)
