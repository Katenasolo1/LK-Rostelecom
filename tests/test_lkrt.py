import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from values import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:\chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('https://b2c.passport.rt.ru')
   pytest.driver.implicitly_wait(10)

   yield

   pytest.driver.quit()

# Заполнение формы Регистрация
def filling_out_the_registration_form():

    # Записываем в переменные основные атрибуты формы Регистрация
    zaregistrirovatsya_autorization = pytest.driver.find_element(By.ID, 'kc-register')
    zaregistrirovatsya_autorization.click()
    input_name_registration = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input')
    input_surname_registration = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input')
    input_email_registration = pytest.driver.find_element(By.ID, 'address')
    random_click = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/p[2]')

    # Заполняем поля формы Регистрация
    input_name_registration.click()
    input_name_registration.send_keys(name_registration)
    input_surname_registration.click()
    input_surname_registration.send_keys(surname_registration)
    input_email_registration.click()
    input_email_registration.send_keys(email_registration)

# Проверить визуальное отображение формы авторизации
def test_lkrt_001_visual_display_of_authorization_form():
    # Записываем в переменные основные атрибуты левой стороны страницы Авторизация
    authorization = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')  # Текст Авторизация
    telefon = pytest.driver.find_element(By.ID, 't-btn-tab-phone')  # Таб Телефон
    pochta = pytest.driver.find_element(By.ID, 't-btn-tab-mail')  # Таб Почта
    login = pytest.driver.find_element(By.ID, 't-btn-tab-login')  # Таб Логин
    licevoi_schet = pytest.driver.find_element(By.ID, 't-btn-tab-ls')  # Таб Лицевой счет
    input_mob_telefon = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')  # Поле ввода Мобильный телефон
    input_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]')  # Поле ввода Пароль
    box_remember_me = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/label/span[2]/span[1]')  # Чек-бокс Запомнить меня
    forgot_password = pytest.driver.find_element(By.ID, 'forgot_password')  # Элемент Забыл пароль
    button_voity = pytest.driver.find_element(By.ID, 'kc-login')  # Кнопка Войти
    user_agreement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/a')  # Пользовательское соглашение
    vk = pytest.driver.find_element(By.CSS_SELECTOR, '#oidc_vk > svg')  # Кнопка Вконтакте
    ok = pytest.driver.find_element(By.CSS_SELECTOR, '#oidc_ok > svg')  # Кнопка Одноклассники
    mail = pytest.driver.find_element(By.CSS_SELECTOR, '#oidc_mail > svg')  # Кнопка Мэйл.ру
    google = pytest.driver.find_element(By.CSS_SELECTOR, '#oidc_google > svg')  # Кнопка Гугл
    yandex = pytest.driver.find_element(By.CSS_SELECTOR, '#oidc_ya > svg')  # Кнопка Яндекс
    zaregistrirovatsya = pytest.driver.find_element(By.ID, 'kc-register')  # Элемент Зарегистрироваться

    # Записываем в переменные основные атрибуты правой стороны страницы Авторизация
    lk = pytest.driver.find_element(By.XPATH, '//*[@id="page-left"]/div/div[2]/h2')  # Текст Личный кабинет
    some_phrase = pytest.driver.find_element(By.XPATH, '//*[@id="page-left"]/div/div[2]/p')  #Текст Персональный помощник в цифровом мире Ростелекома

    # Проверяем соответствие основных атрибутов левой стороны страницы
    assert authorization.get_attribute("innerText") == "Авторизация"
    assert telefon.text == "Телефон"
    assert pochta.text == "Почта"
    assert login.text == "Логин"
    assert licevoi_schet.text == "Лицевой счёт"
    assert input_mob_telefon.text == "Мобильный телефон"
    assert input_password.text == "Пароль"
    assert box_remember_me.text == "Запомнить меня"
    assert forgot_password.text == "Забыл пароль"
    assert button_voity.text == "Войти"
    assert user_agreement.text == "пользовательского соглашения"
    assert vk.get_attribute("alt") == "ВКонтакте"
    assert ok.get_attribute("alt") == "Одноклассники.ru"
    assert mail.get_attribute("alt") == "Mail.ru"
    assert google.get_attribute("alt") == "Google+"
    assert yandex.get_attribute("alt") == "Yandex.ru"
    assert zaregistrirovatsya.text == "Зарегистрироваться"

    # Проверяем соответствие основных атрибутов правой стороны страницы
    assert lk.get_attribute("innerText") == "Личный кабинет"
    assert some_phrase.get_attribute("innerText") == "Персональный помощник в цифровом мире Ростелекома"

@pytest.mark.xfail
# Проверить, что при вводе номера телефона/почты/логина/лицевого счета таб выбора аутентификации автоматически меняется на соответсвующий
def test_lkrt_002a_autorization_form_changes_to_the_authentication_tab_from_telefon():

    # Записываем в переменные основые атрибуты
    input_username = pytest.driver.find_element(By.XPATH, '//*[@id="username"]')
    input_password = pytest.driver.find_element(By.XPATH, '//*[@id="password"]')
    telefon = pytest.driver.find_element(By.ID, 't-btn-tab-phone')  # Таб Телефон
    pochta = pytest.driver.find_element(By.ID, 't-btn-tab-mail')  # Таб Почта
    login = pytest.driver.find_element(By.ID, 't-btn-tab-login')  # Таб Логин
    licevoi_schet = pytest.driver.find_element(By.ID, 't-btn-tab-ls')  # Таб Лицевой счет

    # В поле Мобильный телефон вводим адрес электронной почты
    input_username.send_keys(valid_email)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Почта (выделен оранжевым цветом)
    color_pochta = pochta.value_of_css_property('color')
    color_telefon = telefon.value_of_css_property('color')
    assert color_pochta == "rgba(255, 79, 18, 1)"  # Таб Почта выделен оранжевым цветом
    assert color_telefon == "rgba(16, 24, 40, 1)"  # Таб Телефон выделен черным цветом

    # В поле Мобильный телефон вводим логин
    telefon.click()
    input_username.send_keys(valid_login)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Логин (выделен оранжевым цветом)
    color_login = login.value_of_css_property('color')
    color_telefon = telefon.value_of_css_property('color')
    assert color_login == "rgba(255, 79, 18, 1)"  # Таб Логин выделен оранжевым цветом
    assert color_telefon == "rgba(16, 24, 40, 1)"  # Таб Телефон выделен черным цветом

    # В поле Мобильный телефон вводим лицевой счет
    telefon.click()
    input_username.send_keys(valid_licevoi_schet)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Лицевой счет (выделен оранжевым цветом)
    color_licevoi_schet = licevoi_schet.value_of_css_property('color')
    color_telefon = telefon.value_of_css_property('color')
    assert color_licevoi_schet == "rgba(255, 79, 18, 1)"  # Таб Лицевой счет выделен оранжевым цветом
    assert color_telefon == "rgba(16, 24, 40, 1)"  # Таб Телефон выделен черным цветом

# Проверить, что при вводе номера телефона/почты/логина/лицевого счета таб выбора аутентификации автоматически меняется на соответсвующий
def test_lkrt_002b_autorization_form_changes_to_the_authentication_tab_from_email():

    # Записываем в переменные основые атрибуты
    input_username = pytest.driver.find_element(By.XPATH, '//*[@id="username"]')
    input_password = pytest.driver.find_element(By.XPATH, '//*[@id="password"]')
    telefon = pytest.driver.find_element(By.ID, 't-btn-tab-phone')  # Таб Телефон
    pochta = pytest.driver.find_element(By.ID, 't-btn-tab-mail')  # Таб Почта
    login = pytest.driver.find_element(By.ID, 't-btn-tab-login')  # Таб Логин
    licevoi_schet = pytest.driver.find_element(By.ID, 't-btn-tab-ls')  # Таб Лицевой счет

    # В поле Почта вводим номер мобильного телефона
    pochta.click()
    input_username.send_keys(valid_telefon)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Телефон (выделен оранжевым цветом)
    color_pochta = pochta.value_of_css_property('color')
    color_telefon = telefon.value_of_css_property('color')
    assert color_pochta == "rgba(16, 24, 40, 1)"  # Таб Телефон выделен черным цветом
    assert color_telefon == "rgba(255, 79, 18, 1)"  # Таб Почта выделен оранжевым цветом

    # В поле Почта вводим логин
    pochta.click()
    input_username.send_keys(valid_login)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Логин (выделен оранжевым цветом)
    color_login = login.value_of_css_property('color')
    color_pochta = pochta.value_of_css_property('color')
    assert color_login == "rgba(255, 79, 18, 1)"  # Таб Логин выделен оранжевым цветом
    assert color_pochta == "rgba(16, 24, 40, 1)"  # Таб Почта выделен черным цветом

    # В поле Почта вводим лицевой счет
    pochta.click()
    input_username.send_keys(valid_licevoi_schet)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Лицевой счет (выделен оранжевым цветом)
    color_licevoi_schet = licevoi_schet.value_of_css_property('color')
    color_pochta = pochta.value_of_css_property('color')
    assert color_licevoi_schet == "rgba(255, 79, 18, 1)"  # Таб Лицевой счет выделен оранжевым цветом
    assert color_pochta == "rgba(16, 24, 40, 1)"  # Таб Почта выделен черным цветом

@pytest.mark.xfail
# Проверить, что при вводе номера телефона/почты/логина/лицевого счета таб выбора аутентификации автоматически меняется на соответсвующий
def test_lkrt_002c_autorization_form_changes_to_the_authentication_tab_from_login():

    # Записываем в переменные основые атрибуты
    input_username = pytest.driver.find_element(By.XPATH, '//*[@id="username"]')
    input_password = pytest.driver.find_element(By.XPATH, '//*[@id="password"]')
    telefon = pytest.driver.find_element(By.ID, 't-btn-tab-phone')  # Таб Телефон
    pochta = pytest.driver.find_element(By.ID, 't-btn-tab-mail')  # Таб Почта
    login = pytest.driver.find_element(By.ID, 't-btn-tab-login')  # Таб Логин
    licevoi_schet = pytest.driver.find_element(By.ID, 't-btn-tab-ls')  # Таб Лицевой счет

    # В поле Логин вводим номер мобильного телефона
    login.click()
    input_username.send_keys(valid_telefon)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Телефон (выделен оранжевым цветом)
    color_login = login.value_of_css_property('color')
    color_telefon = telefon.value_of_css_property('color')
    assert color_login == "rgba(16, 24, 40, 1)"  # Таб Логин выделен черным цветом
    assert color_telefon == "rgba(255, 79, 18, 1)"  # Таб Телефон выделен оранжевым цветом

    # В поле Логин вводим адрес электронной почты
    login.click()
    input_username.send_keys(valid_email)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Почта (выделен оранжевым цветом)
    color_pochta = pochta.value_of_css_property('color')
    color_login = login.value_of_css_property('color')
    assert color_pochta == "rgba(255, 79, 18, 1)"  # Таб Почта выделен оранжевым цветом
    assert color_login == "rgba(16, 24, 40, 1)"  # Таб Логин выделен черным цветом

    # В поле Логин вводим лицевой счет
    login.click()
    input_username.send_keys(valid_licevoi_schet)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Лицевой счет (выделен оранжевым цветом)
    color_licevoi_schet = licevoi_schet.value_of_css_property('color')
    color_login = login.value_of_css_property('color')
    assert color_licevoi_schet == "rgba(255, 79, 18, 1)"  # Таб Лицевой счет выделен оранжевым цветом
    assert color_login == "rgba(16, 24, 40, 1)"  # Таб Логин выделен черным цветом

@pytest.mark.xfail
# Проверить, что при вводе номера телефона/почты/логина/лицевого счета таб выбора аутентификации автоматически меняется на соответсвующий
def test_lkrt_002d_autorization_form_changes_to_the_authentication_tab_from_licevoi_schet():

    # Записываем в переменные основые атрибуты
    input_username = pytest.driver.find_element(By.XPATH, '//*[@id="username"]')
    input_password = pytest.driver.find_element(By.XPATH, '//*[@id="password"]')
    telefon = pytest.driver.find_element(By.ID, 't-btn-tab-phone')  # Таб Телефон
    pochta = pytest.driver.find_element(By.ID, 't-btn-tab-mail')  # Таб Почта
    login = pytest.driver.find_element(By.ID, 't-btn-tab-login')  # Таб Логин
    licevoi_schet = pytest.driver.find_element(By.ID, 't-btn-tab-ls')  # Таб Лицевой счет

    # В поле Лицевой счет вводим номер мобильного телефона
    licevoi_schet.click()
    input_username.send_keys(valid_telefon)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Телефон (выделен оранжевым цветом)
    color_licevoi_schet = licevoi_schet.value_of_css_property('color')
    color_telefon = telefon.value_of_css_property('color')
    assert color_licevoi_schet == "rgba(16, 24, 40, 1)"  # Таб Лицевой счет выделен черным цветом
    assert color_telefon == "rgba(255, 79, 18, 1)"  # Таб Телефон выделен оранжевым цветом

    # В поле Лицевой счет вводим адрес электронной почты
    licevoi_schet.click()
    input_username.send_keys(valid_email)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Почта (выделен оранжевым цветом)
    color_pochta = pochta.value_of_css_property('color')
    color_licevoi_schet = licevoi_schet.value_of_css_property('color')
    assert color_pochta == "rgba(255, 79, 18, 1)"  # Таб Почта выделен оранжевым цветом
    assert color_licevoi_schet == "rgba(16, 24, 40, 1)"  # Таб Лицевой счет выделен черным цветом

    # В поле Лицевой счет вводим логин
    licevoi_schet.click()
    input_username.send_keys(valid_login)
    input_password.click()

    # Проверяем, что таб метода аутентификации изменился на таб Логин (выделен оранжевым цветом)
    color_licevoi_schet = licevoi_schet.value_of_css_property('color')
    color_login = login.value_of_css_property('color')
    assert color_login == "rgba(255, 79, 18, 1)"  # Таб Логин выделен оранжевым цветом
    assert color_licevoi_schet == "rgba(16, 24, 40, 1)"  # Таб Лицевой счет выделен черным цветом

# Проверить, что возможно авторизоваться с помощью корректного номера телефона пользователя
def test_lkrt_003_autorization_form_correct_authentication_with_telefon():
    input_mob_telefon = pytest.driver.find_element(By.XPATH, '//*[@id="username"]')
    input_password = pytest.driver.find_element(By.XPATH, '//*[@id="password"]')
    button_voity = pytest.driver.find_element(By.ID, 'kc-login')  # Кнопка Войти

    # В поле Мобильный телефон вводим номер телефона пользователя и пароль
    input_mob_telefon.click()
    input_mob_telefon.send_keys(valid_telefon_real)
    input_password.click()
    input_password.send_keys(valid_password_real)
    button_voity.click()

    # Проверяем, что вход произведен успешно
    assert pytest.driver.current_url[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    credentials = pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[1]')
    safety = pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[2]')
    assert credentials.text == "Учетные данные"
    assert safety.text == "Безопасность"

# Проверить, что невозможно авторизоваться с помощью невалидного номера телефона
def test_lkrt_004_autorization_form_invalid_telefon():
    # Записываем в переменные основные атрибуты формы Авторизация
    input_mob_telefon = pytest.driver.find_element(By.ID, 'username')  # Поле ввода Мобильный телефон
    input_password = pytest.driver.find_element(By.ID, 'password')  # Поле ввода Пароль
    box_remember_me = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/label/span[2]/span[1]')  # Чек-бокс Запомнить меня
    forgot_password = pytest.driver.find_element(By.ID, 'forgot_password')  # Элемент Забыл пароль
    button_voity = pytest.driver.find_element(By.ID, 'kc-login')  # Кнопка Войти

    # Проверяем, что элемент Забыл пароль выделен серым цветом
    color_forgot_password = forgot_password.value_of_css_property('color')
    assert color_forgot_password == "rgba(16, 24, 40, 0.5)"  # Элемент Забыл пароль выделен серым цветом

    # Вводим данные и нажимаем кнопку Войти
    input_mob_telefon.send_keys(invalid_telefon)
    input_password.send_keys(valid_password)
    box_remember_me.click()
    button_voity.click()

    # Проверяем, что вход в личный кабинет не совершен, отображается сообщение "Неверный логин или пароль"
    # и элемент 'Забыл пароль' изменяется на оранжевый цвет.
    assert pytest.driver.current_url[:56] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions'
    message_login = pytest.driver.find_element(By.ID, 'form-error-message')
    assert message_login.text == "Неверный логин или пароль"
    forgot_password = pytest.driver.find_element(By.ID, 'forgot_password')  # Элемент Забыл пароль
    color_forgot_password = forgot_password.value_of_css_property('color')
    assert color_forgot_password == "rgba(255, 79, 18, 1)"  # Элемент Забыл пароль выделен оранжевым цветом

# Проверить, что возможно авторизоваться с помощью корректного адреса электронной почты пользователя
def test_lkrt_005_autorization_form_correct_authentication_with_email():
    # Переходим на таб Почта
    pochta = pytest.driver.find_element(By.ID, 't-btn-tab-mail')  # Таб Почта
    pochta.click()

    # В поле Почта вводим электронную почту и пароль
    input_pochta = pytest.driver.find_element(By.XPATH, '//*[@id="username"]')
    input_password = pytest.driver.find_element(By.XPATH, '//*[@id="password"]')
    button_voity = pytest.driver.find_element(By.ID, 'kc-login')  # Кнопка Войти

    input_pochta.click()
    input_pochta.send_keys(valid_email_real)
    input_password.click()
    input_password.send_keys(valid_password_real)
    button_voity.click()

    # Проверяем, что вход произведен успешно
    assert pytest.driver.current_url[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    credentials = pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[1]')
    safety = pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[2]')
    assert credentials.text == "Учетные данные"
    assert safety.text == "Безопасность"

# Проверить, что невозможно авторизоваться с помощью невалидного адреса электронной почты
def test_lkrt_006_autorization_form_invalid_email():
    # Записываем в переменные основные атрибуты формы Авторизация
    pochta = pytest.driver.find_element(By.ID, 't-btn-tab-mail')  # Таб Почта
    input_email = pytest.driver.find_element(By.ID, 'username')  # Поле ввода Электронная почта
    input_password = pytest.driver.find_element(By.ID, 'password')  # Поле ввода Пароль
    box_remember_me = pytest.driver.find_element(By.XPATH,
                                                 '//*[@id="page-right"]/div/div/div/form/div[3]/label/span[2]/span[1]')  # Чек-бокс Запомнить меня
    forgot_password = pytest.driver.find_element(By.ID, 'forgot_password')  # Элемент Забыл пароль
    button_voity = pytest.driver.find_element(By.ID, 'kc-login')  # Кнопка Войти

    # Переходим на Таб Почта
    pochta.click()

    # Проверяем, что элемент Забыл пароль выделен серым цветом
    color_forgot_password = forgot_password.value_of_css_property('color')
    assert color_forgot_password == "rgba(16, 24, 40, 0.5)"  # Элемент Забыл пароль выделен серым цветом

    # Вводим данные и нажимаем кнопку Войти
    input_email.send_keys(invalid_email)
    input_password.send_keys(valid_password)
    box_remember_me.click()
    button_voity.click()

    # Проверяем, что вход в личный кабинет не совершен, отображается сообщение "Неверный логин или пароль"
    # и элемент 'Забыл пароль' изменяется на оранжевый цвет.
    assert pytest.driver.current_url[:56] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions'
    message_login = pytest.driver.find_element(By.ID, 'form-error-message')
    assert message_login.text == "Неверный логин или пароль"
    forgot_password = pytest.driver.find_element(By.ID, 'forgot_password')  # Элемент Забыл пароль
    color_forgot_password = forgot_password.value_of_css_property('color')
    assert color_forgot_password == "rgba(255, 79, 18, 1)"  # Элемент Забыл пароль выделен оранжевым цветом

# Проверить, что возможно авторизоваться с помощью корректного логина пользователя
def test_lkrt_007_autorization_form_correct_authentication_with_login():
    # Переходим на таб Логин
    login = pytest.driver.find_element(By.ID, 't-btn-tab-login')  # Таб Логин
    login.click()

    # В поле Логин вводим логин и пароль
    input_login = pytest.driver.find_element(By.XPATH, '//*[@id="username"]')
    input_password = pytest.driver.find_element(By.XPATH, '//*[@id="password"]')
    button_voity = pytest.driver.find_element(By.ID, 'kc-login')  # Кнопка Войти

    input_login.click()
    input_login.send_keys(valid_login_real)
    input_password.click()
    input_password.send_keys(valid_password_real)
    button_voity.click()

    # Проверяем, что вход произведен успешно
    assert pytest.driver.current_url[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    credentials = pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[1]')
    safety = pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[2]')
    assert credentials.text == "Учетные данные"
    assert safety.text == "Безопасность"


# Проверить, что невозможно авторизоваться с помощью невалидного логина
def test_lkrt_008_autorization_form_invalid_login():
    # Записываем в переменные основные атрибуты формы Авторизация
    login = pytest.driver.find_element(By.ID, 't-btn-tab-login')  # Таб Логин
    input_login = pytest.driver.find_element(By.ID, 'username')  # Поле ввода Электронная почта
    input_password = pytest.driver.find_element(By.ID, 'password')  # Поле ввода Пароль
    box_remember_me = pytest.driver.find_element(By.XPATH,
                                                 '//*[@id="page-right"]/div/div/div/form/div[3]/label/span[2]/span[1]')  # Чек-бокс Запомнить меня
    forgot_password = pytest.driver.find_element(By.ID, 'forgot_password')  # Элемент Забыл пароль
    button_voity = pytest.driver.find_element(By.ID, 'kc-login')  # Кнопка Войти

    # Переходим на Таб Логин
    login.click()

    # Проверяем, что элемент Забыл пароль выделен серым цветом
    color_forgot_password = forgot_password.value_of_css_property('color')
    assert color_forgot_password == "rgba(16, 24, 40, 0.5)"  # Элемент Забыл пароль выделен серым цветом

    # Вводим данные и нажимаем кнопку Войти
    input_login.send_keys(invalid_login)
    input_password.send_keys(valid_password)
    box_remember_me.click()
    button_voity.click()

# Проверить, что возможно авторизоваться с помощью корректного лицевого счета пользователя
def test_lkrt_009_autorization_form_correct_authentication_with_licevoi_schet():
    # Переходим на таб Лицевой счет
    licevoi_schet = pytest.driver.find_element(By.ID, 't-btn-tab-ls')  # Таб Лицевой счет
    licevoi_schet.click()

    # В поле Лицевой счет вводим лицевой счет и пароль
    input_licevoi_schet = pytest.driver.find_element(By.XPATH, '//*[@id="username"]')
    input_password = pytest.driver.find_element(By.XPATH, '//*[@id="password"]')
    button_voity = pytest.driver.find_element(By.ID, 'kc-login')  # Кнопка Войти

    input_licevoi_schet.click()
    input_licevoi_schet.send_keys(valid_licevoi_schet_real)
    input_password.click()
    input_password.send_keys(valid_password_real)
    button_voity.click()

    # Проверяем, что вход произведен успешно
    assert pytest.driver.current_url[:43] == 'https://b2c.passport.rt.ru/account_b2c/page'
    credentials = pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[1]')
    safety = pytest.driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/h3[2]')
    assert credentials.text == "Учетные данные"
    assert safety.text == "Безопасность"

# Проверить, что невозможно авторизоваться с помощью невалидного номера лицевого счета
def test_lkrt_010_autorization_form_invalid_licevoi_schet():
    # Записываем в переменные основные атрибуты формы Авторизация
    licevoi_schet = pytest.driver.find_element(By.ID, 't-btn-tab-ls')  # Таб Лицевой счет
    input_licevoi_schet = pytest.driver.find_element(By.ID, 'username')  # Поле ввода Электронная почта
    input_password = pytest.driver.find_element(By.ID, 'password')  # Поле ввода Пароль
    box_remember_me = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/label/span[2]/span[1]')  # Чек-бокс Запомнить меня
    forgot_password = pytest.driver.find_element(By.ID, 'forgot_password')  # Элемент Забыл пароль
    button_voity = pytest.driver.find_element(By.ID, 'kc-login')  # Кнопка Войти

    # Переходим на Таб Лицевой счет
    licevoi_schet.click()

    # Проверяем, что элемент Забыл пароль выделен серым цветом
    color_forgot_password = forgot_password.value_of_css_property('color')
    assert color_forgot_password == "rgba(16, 24, 40, 0.5)"  # Элемент Забыл пароль выделен серым цветом

    # Вводим данные и нажимаем кнопку Войти
    input_licevoi_schet.send_keys(invalid_licevoi_schet)
    input_password.send_keys(valid_password)
    box_remember_me.click()
    button_voity.click()

    # Проверяем, что вход в личный кабинет не совершен, отображается сообщение "Неверный логин или пароль"
    # и элемент 'Забыл пароль' изменяется на оранжевый цвет.
    assert pytest.driver.current_url[:56] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions'
    message_login = pytest.driver.find_element(By.ID, 'form-error-message')
    assert message_login.text == "Неверный логин или пароль"
    forgot_password = pytest.driver.find_element(By.ID, 'forgot_password')  # Элемент Забыл пароль
    color_forgot_password = forgot_password.value_of_css_property('color')
    assert color_forgot_password == "rgba(255, 79, 18, 1)"  # Элемент Забыл пароль выделен оранжевым цветом

# Проверить, что в форме регистрации система проверяет корректность длины пароля. Пустой пароль
def test_lkrt_011a_registration_form_length_of_the_password_empty():
    filling_out_the_registration_form()

    # Указываем пустой пароль
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_empty)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_empty)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Длина пароля должна быть не менее 8 символов"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Длина пароля должна быть не менее 8 символов"
    assert message_confirm_password.text == "Длина пароля должна быть не менее 8 символов"

# Проверить, что в форме регистрации система проверяет корректность длины пароля. Один символ
def test_lkrt_011b_registration_form_length_of_the_password_one_character():
    filling_out_the_registration_form()

    # Указываем пароль 1 символ
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_one)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_one)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Длина пароля должна быть не менее 8 символов"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Длина пароля должна быть не менее 8 символов"
    assert message_confirm_password.text == "Длина пароля должна быть не менее 8 символов"

# Проверить, что в форме регистрации система проверяет корректность длины пароля. Пять символов
def test_lkrt_011с_registration_form_length_of_the_password_five_characters():
    filling_out_the_registration_form()

    # Указываем пароль 5 символов
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    #input_password_registration.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
    input_password_registration.send_keys(password_five)
    input_password_confirm_registration.click()
    #input_password_confirm_registration.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
    input_password_confirm_registration.send_keys(password_five)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Длина пароля должна быть не менее 8 символов"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Длина пароля должна быть не менее 8 символов"
    assert message_confirm_password.text == "Длина пароля должна быть не менее 8 символов"

# Проверить, что в форме регистрации система проверяет корректность длины пароля. Семь символов
def test_lkrt_011d_registration_form_length_of_the_password_seven_characters():
    filling_out_the_registration_form()

    # Указываем пароль 7 символов
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    random_click = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/p[2]')

    input_password_registration.click()
    #input_password_registration.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
    input_password_registration.send_keys(password_seven)
    input_password_confirm_registration.click()
    #input_password_confirm_registration.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
    input_password_confirm_registration.send_keys(password_seven)
    random_click.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Длина пароля должна быть не менее 8 символов"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Длина пароля должна быть не менее 8 символов"
    assert message_confirm_password.text == "Длина пароля должна быть не менее 8 символов"

# Проверить, что в форме регистрации система проверяет корректность длины пароля. Восемь символов
def test_lkrt_011e_registration_form_length_of_the_password_eight_characters():
    filling_out_the_registration_form()

    # Указываем пароль 8 символов
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    random_click = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/p[2]')

    input_password_registration.click()
    input_password_registration.send_keys(password_correct)
    input_password_confirm_registration.click()

    input_password_confirm_registration.send_keys(password_correct)
    random_click.click()

    # Проверяем, что под полями Пароль и Подтверждение пароля нет никаких ошибок и подсказок
    try:
        message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
        message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')        
    except NoSuchElementException as err:
        pass
    else:
        assert False, "Validation works incorrectly"

# Проверить, что в форме регистрации система проверяет корректность длины пароля. Пятнадцать символов
def test_lkrt_011f_registration_form_length_of_the_password_fifteen_characters():
    filling_out_the_registration_form()

    # Указываем пароль 15 символов
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    random_click = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/p[2]')

    input_password_registration.click()
    input_password_registration.send_keys(password_fifteen)
    input_password_confirm_registration.click()

    input_password_confirm_registration.send_keys(password_fifteen)
    random_click.click()

    # Проверяем, что под полями Пароль и Подтверждение пароля нет никаких ошибок и подсказок
    try:
        message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
        message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    except NoSuchElementException as err:
        pass
    else:
        assert False, "Validation works incorrectly"

# Проверить, что в форме регистрации система проверяет корректность длины пароля. Девятнадцать символов
def test_lkrt_011g_registration_form_length_of_the_password_nineteen_characters():
    filling_out_the_registration_form()

    # Указываем пароль 19 символов
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    random_click = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/p[2]')

    input_password_registration.click()
    input_password_registration.send_keys(password_nineteen)
    input_password_confirm_registration.click()

    input_password_confirm_registration.send_keys(password_nineteen)
    random_click.click()

    # Проверяем, что под полями Пароль и Подтверждение пароля нет никаких ошибок и подсказок
    try:
        message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
        message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    except NoSuchElementException as err:
        pass
    else:
        assert False, "Validation works incorrectly"

# Проверить, что в форме регистрации система проверяет корректность длины пароля. Двадцать символов
def test_lkrt_011h_registration_form_length_of_the_password_twenty_characters():
    filling_out_the_registration_form()

    # Указываем пароль 20 символов
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    random_click = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/p[2]')

    input_password_registration.click()
    input_password_registration.send_keys(password_twenty)
    input_password_confirm_registration.click()

    input_password_confirm_registration.send_keys(password_twenty)
    random_click.click()

    # Проверяем, что под полями Пароль и Подтверждение пароля нет никаких ошибок и подсказок
    try:
        message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
        message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    except NoSuchElementException as err:
        pass
    else:
        assert False, "Validation works incorrectly"

# Проверить, что в форме регистрации система проверяет корректность длины пароля. Двадцать один символов
def test_lkrt_011i_registration_form_length_of_the_password_twenty_one_characters():
    filling_out_the_registration_form()

    # Указываем пароль 21 символ
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_twenty_one)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_twenty_one)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Длина пароля должна быть не более 20 символов"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Длина пароля должна быть не более 20 символов"
    assert message_confirm_password.text == "Длина пароля должна быть не более 20 символов"

# Проверить, что в форме регистрации система проверяет корректность длины пароля. Тридцать символов
def test_lkrt_011j_registration_form_length_of_the_password_thirty_characters():
    filling_out_the_registration_form()

    # Указываем пароль 30 символ
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_thirty)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_thirty)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Длина пароля должна быть не более 20 символов"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Длина пароля должна быть не более 20 символов"
    assert message_confirm_password.text == "Длина пароля должна быть не более 20 символов"

# Проверить, что система проверяет необходимость ввода заглавной буквы в пароле формы регистрации
def test_lkrt_012a_registration_form_presence_of_capital_letter_in_password_numbers():
    filling_out_the_registration_form()

    # Указываем пароль из 8 символов без букв
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_without_letters)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_without_letters)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Пароль должен содержать хотя бы одну заглавную букву"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Пароль должен содержать хотя бы одну заглавную букву"
    assert message_confirm_password.text == "Пароль должен содержать хотя бы одну заглавную букву"

# Проверить, что система проверяет необходимость ввода заглавной буквы в пароле формы регистрации
def test_lkrt_012b_registration_form_presence_of_capital_letter_in_password_with_little_letter():

    filling_out_the_registration_form()

    # Указываем пароль из 8 символов с маленькой буквой
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_with_little_letter)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_with_little_letter)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Пароль должен содержать хотя бы одну заглавную букву"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Пароль должен содержать хотя бы одну заглавную букву"
    assert message_confirm_password.text == "Пароль должен содержать хотя бы одну заглавную букву"

# Проверить, что система проверяет необходимость ввода заглавной буквы в пароле формы регистрации
def test_lkrt_012c_registration_form_presence_of_capital_letter_in_password_with_all_little_letters():

    filling_out_the_registration_form()

    # Указываем пароль из 8 символов, все маленькие буквы
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_without_numbers)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_without_numbers)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка
    # "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"
    assert message_confirm_password.text == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"

# Проверить, что система проверяет необходимость ввода пароля в форме регистрации только латинскими буквами
def test_lkrt_013a_registration_form_presence_of_latin_letters_in_password_all_russian_letters():

    filling_out_the_registration_form()

    # Указываем пароль из 8 символов с русской буквой
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_all_russian_letter)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_all_russian_letter)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Пароль должен содержать только латинские буквы"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Пароль должен содержать только латинские буквы"
    assert message_confirm_password.text == "Пароль должен содержать только латинские буквы"

# Проверить, что система проверяет необходимость ввода пароля в форме регистрации только латинскими буквами
def test_lkrt_013b_registration_form_presence_of_latin_letters_in_password_russian_letter_beginning():

    filling_out_the_registration_form()

    # Указываем пароль из 8 символов с русской буквой в начале пароля
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_one_russian_letter_beginning)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_one_russian_letter_beginning)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Пароль должен содержать только латинские буквы"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Пароль должен содержать только латинские буквы"
    assert message_confirm_password.text == "Пароль должен содержать только латинские буквы"

# Проверить, что система проверяет необходимость ввода пароля в форме регистрации только латинскими буквами
def test_lkrt_013c_registration_form_presence_of_latin_letters_in_password_russian_letter_medium():

    filling_out_the_registration_form()

    # Указываем пароль из 8 символов с русской буквой в середине пароля
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_one_russian_letter_medium)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_one_russian_letter_medium)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Пароль должен содержать только латинские буквы"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Пароль должен содержать только латинские буквы"
    assert message_confirm_password.text == "Пароль должен содержать только латинские буквы"

# Проверить, что система проверяет необходимость ввода пароля в форме регистрации только латинскими буквами
def test_lkrt_013d_registration_form_presence_of_latin_letters_in_password_russian_letter_end():

    filling_out_the_registration_form()

    # Указываем пароль из 8 символов с русской буквой в конце пароля
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_one_russian_letter_end)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_one_russian_letter_end)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Пароль должен содержать только латинские буквы"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Пароль должен содержать только латинские буквы"
    assert message_confirm_password.text == "Пароль должен содержать только латинские буквы"

@pytest.mark.xfail
# Проверить, что система проверяет необходимость ввода пароля в форме регистрации только латинскими буквами
def test_lkrt_013e_registration_form_presence_of_latin_letters_in_password_chinese_characters():

    filling_out_the_registration_form()

    # Указываем пароль содержащий китайские символы
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_chinese_characters)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_chinese_characters)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полями Пароль и Подтверждение отображается подсказка "Пароль должен содержать только латинские буквы"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'
    message_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    assert message_password.text == "Пароль должен содержать только латинские буквы"
    assert message_confirm_password.text == "Пароль должен содержать только латинские буквы"

# Проверить, что система проверяет правильность ввода пароля в форме "Подтверждение пароля"
def test_lkrt_014_registration_form_correctness_of_confirmation_password():

    filling_out_the_registration_form()

    # Указываем пароль из 8 символов с маленькой буквой
    input_password_registration = pytest.driver.find_element(By.ID, 'password')
    input_password_confirm_registration = pytest.driver.find_element(By.ID, 'password-confirm')
    zaregistrirovatsya_registration = pytest.driver.find_element(By.NAME, 'register')

    input_password_registration.click()
    input_password_registration.send_keys(password_correct)
    input_password_confirm_registration.click()
    input_password_confirm_registration.send_keys(password_incorrect_input)
    zaregistrirovatsya_registration.click()

    # Проверяем, что регистрация не завершена и под полем Подтверждение пароля отображается подсказка "Пароли не совпадают"
    assert pytest.driver.current_url[:69] == 'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/registration'   
    message_confirm_password = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')    
    assert message_confirm_password.text == "Пароли не совпадают"

# Проверить, что система проверяет корректность введенного номера телефона в форме авторизации
def test_lkrt_015_autorization_form_incorrect_telefon():
    # Записываем в переменные основные атрибуты формы Авторизация
    input_mob_telefon = pytest.driver.find_element(By.ID, 'username')  # Поле ввода Мобильный телефон
    input_password = pytest.driver.find_element(By.ID, 'password')  # Поле ввода Пароль

    # Проверяем, что отображается сообщение Неверный формат телефона
    input_mob_telefon.send_keys(incorrect_telefon)
    input_password.click()
    message_telefon = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    assert message_telefon.text == "Неверный формат телефона"

def test_lkrt_016a_registration_form_correct_name():
    zaregistrirovatsya_autorization = pytest.driver.find_element(By.ID, 'kc-register')
    zaregistrirovatsya_autorization.click()
    
    input_name_registration = pytest.driver.find_element(By.NAME, 'firstName')
    input_password_registration = pytest.driver.find_element(By.NAME, 'lastName')
    
    name_list = ["Катя", "Ия", "Ева", "Александра", "Саша", "Евгений", "Иван", "Санта-Лючия",
        "ЭфиопияКаролинаТуапсеВеледаМар", "Айгуль", "Семён", "Наталья"]
    for each_name in name_list:
        input_name_registration.send_keys(each_name)
        input_password_registration.click()
        try:
            message_name = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
        except NoSuchElementException as err:
            pass
        else:
            assert False, "Validation works incorrectly"        
        input_name_registration.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)


def test_lkrt_016b_registration_form_incorrect_name():
    zaregistrirovatsya_autorization = pytest.driver.find_element(By.ID, 'kc-register')
    zaregistrirovatsya_autorization.click()

    input_name_registration = pytest.driver.find_element(By.NAME, 'firstName')
    input_password_registration = pytest.driver.find_element(By.NAME, 'lastName')

    name_list = ["|\/!@#$%^&*()-_=+`~?№;:[]{}", "Ekaterina", "的一是不了人我在有他这为之大来以个中上们", "Эфиопия Каролина",
                 "Иван-Иван-Иван", "ЭфиопияКаролинаТуапсеВеледаМара", "-Екатерина", "Санта-Lючия"]
    for each_name in name_list:
        input_name_registration.send_keys(each_name)
        input_password_registration.click()
        message_name = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
        assert message_name.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
        input_name_registration.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)

# Проверить, что возможен переход на страницу соцсети (Вконтакте) по кнопке на странице авторизации
def test_lkrt_017_autorization_form_vk_button():
    # Нажимаем на кнопку VK
    vk = pytest.driver.find_element(By.CSS_SELECTOR, '#oidc_vk > svg')  # Кнопка Вконтакте
    vk.click()

    # Проверить, что совершается переход на страницу Вконтакте
    current_url = pytest.driver.current_url
    assert 'vk.com' in current_url

# Проверить, что возможен переход на страницу соцсети (Одноклассники) по кнопке на странице авторизации
def test_lkrt_018_autorization_form_ok_button():
    # Нажимаем на кнопку Одноклассники(человечек)
    ok = pytest.driver.find_element(By.CSS_SELECTOR, '#oidc_ok > svg')  # Кнопка Одноклассники
    ok.click()

    # Проверить, что совершается переход на страницу Одноклассники
    current_url = pytest.driver.current_url
    assert 'ok.ru' in current_url

# Проверить, что возможен переход на страницу соцсети (Мой Мир Мэйл.ру) по кнопке на странице авторизации
def test_lkrt_019_autorization_form_mail_button():
    # Нажимаем на кнопку "@"
    mail = pytest.driver.find_element(By.CSS_SELECTOR, '#oidc_mail > svg')  # Кнопка Мэйл.ру
    mail.click()

    # Проверить, что совершается переход на страницу Мой Мир Мэйл.ру
    current_url = pytest.driver.current_url
    assert 'mail.ru' in current_url

# Проверить, что возможен переход на страницу соцсети (Google) по кнопке на странице авторизации
def test_lkrt_020_autorization_form_google_button():
    # Нажимаем на кнопку "G"
    google = pytest.driver.find_element(By.CSS_SELECTOR, '#oidc_google > svg')  # Кнопка Гугл
    google.click()

    # Проверить, что совершается переход на страницу Google
    current_url = pytest.driver.current_url
    time.sleep(10)
    assert 'google.com' in current_url

# Проверить, что возможен переход на страницу соцсети (Яндекс) по кнопке на странице авторизации
def test_lkrt_021_autorization_form_yandex_button():
    # Нажимаем на кнопку "Я"
    yandex = pytest.driver.find_element(By.CSS_SELECTOR, '#oidc_ya > svg')  # Кнопка Яндекс
    yandex.click()

    # Проверить, что совершается переход на страницу Яндекс
    current_url = pytest.driver.current_url
    assert 'yandex.ru' in current_url

# Проверить, что возможно ознакомиться с пользовательским соглашением на странице авторизации
def test_lkrt_022_autorization_form_user_agreement():
    # Нажимаем на элемент "пользовательского соглашения"
    user_agreement = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/a')  # Пользовательское соглашение
    user_agreement.click()

    # Проверить, что открывается новое окно с Публичной офертой о заключении Пользовательского соглашения
    # на использование Сервиса «Ростелеком ID»
    main_page = pytest.driver.current_window_handle
    for handle in pytest.driver.window_handles:
        if handle != main_page:
            user_agreement_page = handle
    pytest.driver.switch_to.window(user_agreement_page)
    assert pytest.driver.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"
    user_agreement_titlle = pytest.driver.find_element(By.ID, 'title')
    assert user_agreement_titlle.text == "Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»"





