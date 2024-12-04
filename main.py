from locale import currency

import telebot


# Создаем объект бота
bot = telebot.TeleBot('7201389391:AAG6XvGa3fGrdB_GdZMuGIIO98X9XR4Th0A')
# Токены платежей
click = '398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065'
payme = '371317599:TEST:1733237187436'


# Обработчик команды / start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    # Отправка чека
    bot.send_invoice(user_id,
                     title='Подписка на один месяц',
                     description='Активация подписки дает доступ к просмотру кино',
                     provider_token=payme,
                     currency='uzs',
                     photo_url='https://i.postimg.cc/Y2bb0xmq/channels4-profile.jpg',
                     photo_width=416,
                     photo_height=234,
                     photo_size=416,
                     is_flexible=False,
                     prices=[telebot.types.LabeledPrice(label='Подписка на 1 месяц', amount=3000000)],
                     start_parameter='one-month-subscription',
                     invoice_payload='test-invoice-payload')


# Обработка платежа
@bot.pre_checkout_query_handler(lambda query: True)
def pre_check(pre_checkout_q):
    bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# Прием платежа
@bot.message_handler(content_types=['successful_payment'])
def successful(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Оплата прошла успешно!')

# Запуск бота
bot.polling(none_stop=True)