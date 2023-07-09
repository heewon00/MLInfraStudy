FROM python:3.8.13-slim-buster
WORKDIR /app
COPY ./my_app ./

RUN pip install --upgrade pip --no-cache-dir

RUN pip install -r /app/requirements.txt --no-cache-dir

# docker build -t myimage .
# docker run -p 8000:8000 myimage
# 현재 디렉토리를 기준으로 myimage 라는 태그의 이미지 빌드
# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
CMD ["gunicorn", "main_app.wsgi:application", "--bind", "0.0.0.0:8000"]