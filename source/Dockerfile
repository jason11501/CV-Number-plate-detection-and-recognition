FROM python:3.12.5

WORKDIR /Users/c/Downloads/CV-Number-plate-detection-and-recognition

COPY . .

RUN pip3 install -r /Users/c/Downloads/CV-Number-plate-detection-and-recognition/source/yolov3/License-Plate-Recognition-master-4/requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
CMD [ "python3","/Users/c/Downloads/CV-Number-plate-detection-and-recognition/source/yolov3/License-Plate-Recognition-master-4/my_api.py" ]
