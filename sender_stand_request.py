import configuration
import requests
import data

#Функция создания заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.headers)

# Функция получения трека заказа
def get_track_number():
    track = post_new_order().json()["track"]
    return track

# Функция получения информации заказа по треку
def get_order_by_track(track):
    params = {
        't': track
    }
    url = configuration.URL_SERVICE + configuration.GET_ORDER
    return requests.get(url,
                         params=params,
                         headers=data.headers)