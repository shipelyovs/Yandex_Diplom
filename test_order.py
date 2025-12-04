# Шипелёв Сергей, 38-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

# Функция для проверки
def positive_assert(get_track):
    order_response = sender_stand_request.get_info(get_track)
    assert order_response.status_code == 200

# Проверяется, что по треку заказа можно получить данные о заказе
def test_get_order_track_response():
    track_number = sender_stand_request.get_track()
    positive_assert(track_number)