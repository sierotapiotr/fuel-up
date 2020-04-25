pip install -r requirements.txt
docker run --name mysql-fuelup-dev -p 127.0.0.1:13306:3306 -e MYSQL_ROOT_PASSWORD=W7bMzFgVYQh7N65Z -d mysql:latest
