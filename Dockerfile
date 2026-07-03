FROM python:3.13-slim
RUN pip install aiogram
COPY workordead.py .
CMD ["python", "workordead.py"]
