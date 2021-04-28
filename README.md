

docker build -t iris_classifier .
docker run -dp 5000:5000 iris_classifier #d - запуск в фоновом режиме, p - сопоставить порт контейнера с хостом

http://0.0.0.0:5000/