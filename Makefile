export DOCKER_BUILDKIT = 1

build:
	docker build srv --tag srv:latest
	docker build bot --tag bot:latest

up:
	docker-compose --version
	docker-compose up

down:
	docker-compose down --remove-orphans

