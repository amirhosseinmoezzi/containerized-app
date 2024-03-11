FROM python:alpine

WORKDIR /app
ADD app.py .
RUN python -m pip install flask
RUN adduser -D flask
USER flask
EXPOSE 80

CMD ["python", "app.py"]