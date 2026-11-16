FROM python:3.12-slim

RUN apt-get update \
 && apt-get upgrade -y \
 && rm -rf /var/lib/apt/lists/* \
 && pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py config.yaml ./

RUN useradd --create-home appuser
USER appuser

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
