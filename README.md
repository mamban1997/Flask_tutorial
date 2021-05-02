# Определение ирисов
Определение ирисов из популярного датасета [iris](https://ru.wikipedia.org/wiki/%D0%98%D1%80%D0%B8%D1%81%D1%8B_%D0%A4%D0%B8%D1%88%D0%B5%D1%80%D0%B0 "Википедия").

https://iris-classifier555.herokuapp.com/ - ссылка на рабочий проект на heroku.

### Запуск через docker
Перейти в папку с проектом и выполнить команды:

$docker build -t iris_classifier .

$docker run -dp 5000:5000 --name web_iris iris_classifier
#d - запуск в фоновом режиме, p - сопоставить порт контейнера с хостом, -name - присвоить собственное имя контейнеру

Для остановки:
$docker stop web_iris 

Для повторного запуска:
$docker start web_iris

Перейти по ссылке:
http://0.0.0.0:5000/

### Деплой на heroku
Перейти в папку с проектом и выполнить команды:

$heroku container:login

$heroku create <your_app_name> #(iris-classifier555)

$heroku container:push web --app <your_app_name> #(iris-classifier555)

$heroku container:release web --app <your_app_name> #(iris-classifier555)

Рабочая ссылка:

https://iris-classifier555.herokuapp.com/


### Ссылки
https://atrium.ai/resources/build-and-deploy-a-docker-containerized-python-machine-learning-model-on-heroku/

https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask
