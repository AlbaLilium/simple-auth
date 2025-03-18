FROM python:3.12-slim-bookworm

COPY ../requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY .. .

EXPOSE 8000

RUN chmod +x /src/entrypoint.sh

CMD ["/src/entrypoint.sh"]
