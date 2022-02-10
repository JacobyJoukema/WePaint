export DOCKER_BUILDKIT = 1

.PHONY: help
help:
	@echo "Please use \`make <target>\` where <target> is one of"
	@echo "  build              to build all the Docker images"
	@echo "  up                 to run all the Docker containers"
	@echo "  down               to stop all the Docker containers"
	@echo "  fmt                to format the Python source files"
	@echo "  psql               to open a shell to the PostgreSQL database"

.PHONY: build
build:
	docker build srv --tag srv:latest
	docker build bot --tag bot:latest
	docker build client --tag client:latest

.PHONY: up
up:
	docker-compose --version
	docker-compose up

.PHONY: down
down:
	docker-compose down --remove-orphans

.PHONY: fmt
fmt:
	black srv
	isort srv

.PHONY: psql
psql:
	docker-compose exec db psql -U wepaint wepaint
