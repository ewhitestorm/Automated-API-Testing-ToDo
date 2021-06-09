import requests
import jwt



#БЛОК - Создание пользователя

def test_usernameLength():#проверка длины имени пользователя
    nUsername = 0
    
    for i in username.split():
        nUsername += len(i)
    
    assert nUsername == 50, 'Длина имени пользователя должна быть равна 50 символам.'

def test_password1Length():#проверка длины пароля-1
    assert len(password1) == 20, 'Длина пароля-1 должна быть равна 20 символам.'

def test_password2Length():#проверка длины пароля-2
    assert len(password2) == 20, 'Длина пароля-2 должна быть равна 20 символам.'

def test_identityPasswords():#проверка на идентичность паролей
    assert password1 == password2, 'Пароли дожны совпадать.'

def test_noUsername():#проверка на отсутствие имени пользователя
    assert username != '', 'Имя пользователя не должно быть пустым.'

def test_noPassword1():#проверка на отсутствие пароля-1
    assert password1 != '', 'Пароль-1 не должен быть пустым.'

def test_noPassword2():#проверка на отсутствие пароля-2
    assert password2 != '', 'Пароль-2 не должен быть пустым.'


#БЛОК - Обновление пароля пользователя
    
def test_statusCode():#проверка состояния запроса на ресурс
    url = 'https://...'
    s = requests.get(url)
    assert s.status_code == 200, 'Запрос прошел не успешно.'
    
def test_noUsername():#проверка на отсутствие имени пользователя
    assert username != '', 'Имя пользователя не введено.'

def test_noPassword1():#проверка на отсутствие пароля-1
    assert password1 != '', 'Пароль-1 не введен.'

def test_noPassword2():#проверка на отсутствие пароля-2
    assert password2 != '', 'Пароль-2 не введен.'


def test_newPasswordLength():#проверка длины нового пароля
    if (username and password1 and password2) != '':
        assert len(new_password) == 20, 'Длина нового пароля должна быть равна 20 символам.'

def test_noNewPassword():#проверка на отсутствие нового пароля
    assert new_password != '', 'Новый пароль не должен быть пустым.'


#БЛОК - Логин (получение токена JWT)

def test_noUsername():#проверка на отсутствие имени пользователя
    assert username != '', 'Имя пользователя не введено.'

def test_noPassword():#проверка на отсутствие пароля
    assert password != '', 'Пароль не введен.'
        
def test_login():#проверка токена JWT
    SECRET_KEY = 'SECRET_KEY'
    tokenUser = 'token' #'access_token' or 'refresh_token'
    token = jwt.encode({'name': request.form[username]}, SECRET_KEY)
    assert token != tokenUser, 'Токен проверку не прошел.'
    
