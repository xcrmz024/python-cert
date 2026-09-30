FROM python:3.12-slim AS builder

WORKDIR /app

RUN pip install poetry==2.1.4

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root


FROM python:3.12-slim AS runtime

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY src ./src
COPY alembic.ini .
COPY alembic ./alembic

ENV PYTHONPATH=/app/src

EXPOSE 8000

CMD ["uvicorn", "proyecto_final_integrador.main:app", "--host", "0.0.0.0", "--port", "8000"]