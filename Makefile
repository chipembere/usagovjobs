test:
	poetry run pytest -vv

format-check:
	poetry run black --check usagovjobs/ tests/

black-format:
	poetry run black usagovjobs/ tests/

docker-build:
	docker build --tag usagovjobs --file Dockerfile .

docker-run:
	docker run -it -d --name usagovjobs usagovjobs

build-run: docker-build docker-run

docker-logs:
	docker logs -f usagovjobs

docker-rm-container:
	docker rm usagovjobs

docker-rm-image:
	docker rmi usagovjobs

docker-rm-both:
	docker stop usagovjobs
	docker rm usagovjobs
	docker rmi usagovjobs

docker-stop:
	docker stop usagovjobs

docker-exec:
	docker exec -it usagovjobs bash

main-extract:
	poetry run python usagovjobs/main.py -e