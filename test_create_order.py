import sender_stand_request

# Рылина Анастасия, 14-я когорта — Финальный проект. Инженер по тестированию плюс

# Получаем актуальный трек заказа
# Сохраняем информация о заказе по треку
# Проверяем что статус заказа 200
def test_get_info_order():
    track = sender_stand_request.get_track_number()
    order_response = sender_stand_request.get_order_by_track(track)
    assert order_response.status_code == 200
    print(order_response.status_code)
