class Constants:
    URL_COURIER = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    URL_LOGIN = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    URL_DELETE = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/'
    URL_ORDERS = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
    BODY_SUCCESS_REG = {"ok": True}
    BODY_NO_FIELD = {"code": 400,
    "message": "Недостаточно данных для создания учетной записи"}
    BODY_SAME_LOG = {"code": 409,
    "message": "Этот логин уже используется. Попробуйте другой."}
    BODY_NO_FIELD_LOG = {"code": 400,
    "message": "Недостаточно данных для входа"}
    BODY_WRONG_PASS = {"code": 404,
    "message": "Учетная запись не найдена"}