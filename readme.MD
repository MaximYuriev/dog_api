# Описание проекта
Проект представляет собой api для управления информацией о породах и собаках.
# Стек
1) DRF
2) Postgresql
3) Docker
# Описание эндпойнтов
* GET /api/v1/dogs/ &mdash; Возвращает список собак, включая информацию о среднем возрасте собак каждой породы.
* POST /api/v1/dogs/ &mdash; Используется для добавление собаки.
* GET /api/v1/dogs/\<id> &mdash; Возвращает найденную собаку, включая количество собак той же породы.
* PUT /api/v1/dogs/\<id> &mdash; Используется для изменения собаки.
* DELETE /api/v1/dogs/\<id> &mdash; Используется для удаления собаки.
* GET /api/breeds/ &mdash; Возвращает список пород, включая количество собак каждой породы.
* POST /api/breeds/ &mdash; Используется для добавления новой породы.
* GET /api/breeds/<id> &mdash; Возвращает породу.
* PUT /api/breeds/<id> &mdash; Используется для изменения породы.
* DELETE /api/breeds/<id> &mdash; Удаляет породу.
# Запуск проекта
1) Склонировать репозиторий.
2) Создать файл .env в корне проекта по аналогии .env.example: 
    ```
    POSTGRES_HOST=localhost
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=pswd
    POSTGRES_DB=dogdb
    POSTGRES_PORT=5432
    ```
3) Запустить postgresql в docker:
    ``` commandline
    docker compose --file docker-composes/storage.yml up --build  
    ```
4) Запустить проект в docker:
    ``` commandline
    docker compose --file docker-composes/app.yml up --build
    ```
5) Выполнить миграции:
    ``` commandline
    docker exec -it backend-app python dog_api/manage.py migrate
    ```