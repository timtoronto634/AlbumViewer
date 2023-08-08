.PHONY: serve

serve:
	python app/main.py

openapi.generate:
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/openapi.yaml -o /local/openapi/out/python -g python
