# car_detector

## Запуск
```commandline
poetry run build_images
poetry run up
poetry run migrate
```
либо
```commandline
docker build -f docker/image_processor.docker -t image_processor .
docker build -f docker/detector.docker -t detector .
docker-compose -f docker/docker_compose.yml up --remove-orphans
docker-compose -f docker/docker_compose.yml exec image_processor alembic upgrade head
```

сервис будет доступен по адресу http://localhost:8080

Документация к сервису http://localhost:8080/docs

## Тестирование
Запуск тестов `poetry run tests` или `pytest -s` (контейнер с базой данных должен быть поднят)

Так же есть конфигурация для тестплана apache jmeter (файл [car_detector.jmx](car_detector.jmx))

Произведен замер производительности с помощью jmeter (результат [report.csv](report.csv)), который показал, что при 
параметрах IMAGE_PROCESSOR_WORKERS=3 и DETECTOR_WORKERS=2 пропускная способность сервиса 28.6 запросов/с
