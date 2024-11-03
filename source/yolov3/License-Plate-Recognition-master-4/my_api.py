from flask import Flask, render_template, request, url_for
from flask_cors import CORS, cross_origin
import os
import cv2
from src.lp_recognition import E2E

app = Flask(__name__)

# Apply flask CORS
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = 'static'

# Create upload directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

yolov3_model = E2E()

@app.route('/', methods=['POST', 'GET'])
@cross_origin(origin='*')
def predict_yolov3():
    image_path = None
    if request.method == 'POST':
        # Lấy file gửi lên
        image = request.files['file']
        if image:
            # Lưu file
            path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            print("save=", path_to_save)
            image.save(path_to_save)

            # Nhận diện
            frame = cv2.imread(path_to_save)
            frame = yolov3_model.predict(frame)
            cv2.imwrite(path_to_save, frame)
            del frame
            image_path = image.filename

    return render_template('index.html', image_path=image_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6868', debug=True)
