# ООО INSIDE HTTP API

## Структура приложения (Файлы, папки)

#### application - папка с файлами приложения
- __init__.py - файл инициализации фабрики приложения
- fakes.py - создание временных данных
- models.py - модели приложение
- urls.py - роуты, ссылки приложения
- views.py - реализация представления

#### docker/api/ - папка для хранения сценариев докер файлов
- Dockerfile - файл сценария запуска приложения

#### test - папка с тестами приложения
- test_content_type.py - проверка типа контента
- test_missng_keys.py - проверка ключей на не существование
- test_no_token.py - проверка на не существование токена
- utils.py - файл с доп функций

#### / - корневой каталог
- .gitignore - файл игнорируемых файлов и папок для github
- app.py - файл запуска приложений
- config.cfg - конфигурационный файл
- config_example.cfg - пример конфигурационного файла
- requirements.txt - файл установленных зависимостей

-----------------------------------------------------

## Применения

Проверить работоспособность приложения можно через программу Postman.

Сгенерированных токен с главной страницы "/", надо скопировать и вставить в Postman:

- перейти на вкладку **Authorization** 
- в типе **Type** в выподающем меню выбрать **Bearer token**
- и в поле **Token** вставить скопированный токен с главной страницы
- после можно оправлять запросы на закрытые страницы, как зарегистрированный пользователь

-----------------------------------------------------

## Установка

Для работы требуется установить установить docker, docker-compose.

Само приложение хранится на github `git@github.com:velllum/test_OOO_INSIDE.git`, в ветке dev

Выберите папку для клонирования и введите команду 

`git clone git@github.com:velllum/test_OOO_INSIDE.git -b dev`

Подгрузить данные для работы через `docker-compose`, командой в терминале `docker-compose up -d`.
После загрузки всех зависимостей запустить приложение в `docker`, можно командой `docker-compose up`.

Также повторить процедуру с `docker` если были внесены какие-либо правки в коде.

`docker-compose up -d`

`docker-compose up`


Пользователей в базу можно добавить только вручную.
Вот несколько записанных пользователей для работы, что были добавлены при инициализации данных.

`{"name": "Иван", "password": 111}`

`{"name": "Алексей", "password": 222}`

`{"name": "Владимир", "password": 333}`

`{"name": "Павел", "password": 444}`

--------------------------------------------------

В самом реализации было измененно api вывода из базы сообщений, было 

`{
    name: "имя отправителя",
    message: "history 10"
}`

стало 

`{
    name: "имя отправителя",
    history: 10
}`

====================== ТЗ ТЕСТА ==============================

В БД создать пару sql табличек со связями (foreign keys)

Сделать HTTP POST эндпоинт который получает данные в json вида :

`{
    name: "имя отправителя"
    password: "пароль" 
}`

Этот эндпоинт проверяет пароль по БД и создает jwt токен 
(срок действия токена и алгоритм подписи не принципиален, 
для генерации и работе с токеном можно использовать готовую библиотечку)
в токен записывает данные: name: "имя отправителя" и отправляет токен в ответ, тоже json вида:

`{
    token: "тут сгенерированный токен" 
}`


=========================

Сервер слушает и отвечает в какой-нибудь эндпоинт в него на вход поступают данные в формате json:
Сообщения клиента-пользователя:

`{
    name:       "имя отправителя",
    message:    "текст сообщение"
}`

В заголовках указан Bearer (носитель) токен (полученный из эндпоинта выше)
Проверить токен, в случае успешной проверки токена, полученное сообщение сохранить в БД.


==========================

Если пришло сообщение вида:

`{
    name: "имя отправителя",
    history: 10
}`

проверить токен, в случае успешной проверки токена отправить отправителю 10 последних сообщений из БД

=========================

Добавить описание и инструкцию по запуску и комментарии в коде, если изменяете формат сообщений, то подробное описание ендпоинтов и их полей.

Завернуть все компоненты в докер, покрыть код тестами