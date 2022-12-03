FROM python:3.8.15
WORKDIR /Project/demo

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

CMD ["python", "main.py"]
#CMD ["gunicorn", "main:app", "-c", "./gunicorn.conf"]