# Phát hiện và nhận dạng biển số (Number plate detection and recognition)
# Tiến độ 60%
 ## Install environments
**Công cụ (Tool):**<br>
* Jupyter Notebook or Google Colab
* Visual Studio Code (chạy main.py và my_api.py)

**Ngôn ngữ (Language):**<br>
* Python 3.12.5

## real-time
https://github.com/Hung-3008/LPDR


## deploy
Các bạn có thể clone repo này về. Open VSCode, run my_api.py :
```
cd CV-Number-plate-detection-and-recognition
/usr/local/bin/python3.12 /Users/c/Downloads/CV-Number-plate-detection-and-recognition/source/yolov3/License-Plate-Recognition-master-4/my_api.py
```
/static

/templates

/my_api

/requirement txt

Trước khi dùng cmd bất kì cmd docker nào, run:
```
export PATH="$PATH:/Applications/Docker.app/Contents/Resources/bin/"
```

build image named jason/number_plate
```
docker build -f /Users/c/Downloads/CV-Number-plate-detection-and-recognition/source/Dockerfile -t jason/number_plate .
```
run image in a container named abcxyz
```
docker run --name abcxyz jason/number_plate
```
