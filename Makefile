.PHONY: serve
serve:
	docker-compose -f docker-compose.yml -f docker-compose.local.yml up webserver