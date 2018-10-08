img=duckietown/aido1_log_processing-v3b-evaluator:latest


all: push

push: build
	docker push $(img)

build:
	docker build -t $(img) .

build-no-cache:
	docker build -t $(img) . --no-cache


define-challenge:
	dts challenges define --config ../challenge.yaml --build evaluator:.
