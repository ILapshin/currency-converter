FROM python:3.10
WORKDIR /code


RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

COPY pyproject.toml poetry.lock* ./

# Установка зависимостей
RUN poetry install --no-root --no-interaction --no-ansi

COPY ./src /code/src

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
