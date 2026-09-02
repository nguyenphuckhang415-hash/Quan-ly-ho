FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN python -m pip install --no-cache-dir -r requirements.txt && python -m pip show gunicorn
ENV PYTHONUNBUFFERED=1
ENV V18_DATA_DIR=/var/data
RUN mkdir -p /var/data/uploads
EXPOSE 10000
CMD ["python","-m","gunicorn","--bind","0.0.0.0:10000","--workers","1","--threads","4","--timeout","120","app:app"]
