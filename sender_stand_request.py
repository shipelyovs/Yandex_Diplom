# Шипелёв Сергей, 38-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import data
import requests

# 1.Запрос на создание заказа.
def new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, 
                        json=body)

# 2.Сохранить номер трека заказа.
def get_track():
    track_response = new_order(data.body)
    return track_response.json()["track"]

# 3.Выполнить запрос на получение заказа по треку заказа.
def get_info(get_track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER,
                        params={"t": get_track})