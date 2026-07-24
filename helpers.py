import random
from datetime import datetime, timedelta


def generate_random_name():
    return random.choice(["Иван", "Мария", "Алексей", "Екатерина", "Дмитрий", "Анна"])


def generate_random_surname():
    return random.choice(["Петров", "Иванова", "Смирнов", "Козлова", "Соколов", "Михайлова"])


def generate_random_address():
    streets = ["ул. Тверская", "пр. Мира", "ул. Арбат", "ул. Ленина", "ул. Пушкина"]
    return f"{random.choice(streets)}, д. {random.randint(1, 100)}"


def generate_random_phone():
    return f"+7{random.randint(900, 999)}{random.randint(1000000, 9999999)}"


def generate_random_metro():
    return random.choice(["Сокольники", "Преображенская площадь", "Черкизовская", "Бульвар Рокоссовского", "Локомотив", "Измайловская"])


def generate_random_date():
    return (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%d.%m.%Y")


def generate_random_rental_days():
    return random.randint(1, 7)


def generate_random_color():
    return random.choice(["BLACK", "GREY"])


def generate_random_comment():
    return random.choice(["Позвонить за час", "Без комментариев", "Домофон 123", "Оставить у двери"])


def generate_order_data():
    return {
        "customer": {
            "name": generate_random_name(),
            "surname": generate_random_surname(),
            "address": generate_random_address(),
            "metro_station": generate_random_metro(),
            "phone": generate_random_phone()
        },
        "rental": {
            "date": generate_random_date(),
            "rental_days": generate_random_rental_days(),
            "color": generate_random_color(),
            "comment": generate_random_comment()
        },
        "button_position": random.choice(["header", "bottom"])
    }
