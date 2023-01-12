Итоговый проект по автоматизированому тестированию к 28 модулю SkillFactory курса QAP

В директории /tests располагается файл с тестами test_lkrt.py
В корневой директории располагается файл values.py, в котором хранятся различные тестовые данные(валидные/невалидные логины, пароли и тд)

!!!В целях безопасности, реальные данные для входа в личный кабинет пользователя(номер телефона, почта, логин и лицевой счет) были удалены.
Для корректного запуска скопа тестов необходимо ввести свои корректные данные в 4 переменные в файле value.py!!!

Для того, что решить вопрос с появлением Капчи после 3 некорректных попыток авторизации, тесты на авторизацию чередуются:
1 положительный тест - 1 отрицательный тест

Для запуска проект необходимо скачать Download.zip, разархивировать и запустить в терминале с помощью команды 
python -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe  tests\test_lkrt.py\
(указать корректное расположение драйвера)


Для тестирования использовались следующие инструменты:
- Фикстура @pytest.fixture(autouse=True). Ее основная задача заключается в подготовке окружения с заранее фиксированным/известным состоянием 
для гарантии повторяемости процесса тестирования.
- Для того, что бы тестирумая веб страница успевала загружаться используется неявное ожидание pytest.driver.implicitly_wait(10)
- Функция def filling_out_the_registration_form(): Для части тестов требовались одни и те же действия по заполнению полей формы регистрации,
 функция выполняет эту роль.
- Для поиска и определния локаторов использовался DevTools на вкладке Elements. В тестах присутствуют локаторы по ID, NAME, CSS_SELECTOR, XPATH.
- Тесты, которые фейлятся по причине баг заранее отмечены маркером @pytest.mark.xfail(ожидаемо провальный тест) 
- Для тестирования ввода пароля использовалась техника разбиения на эквивалентные классы и техника граничных значений, для тестирования
 авторизации использовались позитивные и негативные тесты.
- В некоторых тестах использовался NoSuchElementException, что бы проверить, что определенных веб-элементов нет на сайте при корректном вводе
 данных (в данном случае, сообщений об ошибках).
- Для тестирования корректного и некорректного ввода в поле Имя на странице Регистрации использовались списки имен и цикл.





