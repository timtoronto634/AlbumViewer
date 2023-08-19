.PHONY: serve

serve:
	python app/main.py

openapi.generate:
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli:v6.6.0 generate -i /local/openapi.yaml -o /local/openapi/out/python -g python
