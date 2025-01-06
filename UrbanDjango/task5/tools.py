"""Проверяет данные пользователя для регистрации."""

def valid_user(username, password, repeat_password, age, users):
    if password != repeat_password:
        return 'Пароли не совпадают'
    elif int (age) < 18:
        return 'Вы должны быть старше 18'
    elif username in users:
        return 'Пользователь уже существует'
    return None