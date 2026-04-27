FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask requests
RUN pip install selenium
EXPOSE 5000
CMD ["python", "app.py"]
