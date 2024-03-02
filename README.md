# face_converter
Generate a new image that combines features from your face and the face from animations utilizing GAN structure and machine learning techniques.

## Team member
- JiHyeok - Machine Learning
- HyungKyun - Machine Learning
- Alex - Backend
- YangHwi - Fullstack

## Design

## Setup (MacOS)

### 1. Client - ReactJS

```bash
# npm install
npm i npm@10.2.4

# library install
cd face_converter/client
npm install # !!! 꼭 client 폴더위치에서만 실행 !!!
```

### 2. Server - Django

```bash
#python install
brew update && brew install python@3.12

#virtual envrionment
cd face_cconverter/server
python3.12 -m venv venv #생성
source ./venv/bin/activate #접속

#library install
pip install --upgrade pip
pip install -r requirements.txt
```

## Run

```bash
# client(react)
cd face_converter/client && npm start

# server(django)
cd hackathon/server
python manage.py makemigrations # only when changes made in model.py
python manage.py migrate # only when changes made in model.py
python manage.py runserver
```
