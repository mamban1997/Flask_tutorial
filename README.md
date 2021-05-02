Запуск через докер.
Перейти в папку с проектом и выполнить команды:

$docker build -t iris_classifier .

$docker run -pp 5000:5000 --name web_iris iris_classifier
#d - запуск в фоновом режиме, p - сопоставить порт контейнера с хостом, -name - присвоить собственное имя контейнеру

Для остановки:
$docker stop web_iris 

Для повторного запуска:
$docker start web_iris

Перейти по ссылке:
http://0.0.0.0:5000/

https://iris-classifier555.herokuapp.com/