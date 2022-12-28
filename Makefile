start-mysql:
	docker run --name mysql -v data:/var/lib/mysql -d mysql

stop-mysql:
	docker stop mysql
	docker rm mysql

start:
	python main.py