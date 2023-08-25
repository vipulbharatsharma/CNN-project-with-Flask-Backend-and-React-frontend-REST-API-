from flask import Flask, request
import pickle
import tensorflow as tf
from keras.preprocessing import image
import  numpy as np
import os
import base64
from io import BytesIO
from PIL import Image
from db import get_employee
from tensorflow.keras.models import load_model
from waitress import serve
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


#model = tf.keras.models.load_model('model')



mydir = os.path.dirname(__file__)
pickle_file_path = os.path.join(mydir, 'model.pkl')

#with open(pickle_file_path, 'rb') as pickle_file:
    #model = pickle.load(pickle_file)

model = load_model('model.keras')

mydir = os.path.dirname(__file__)
pickle_file_path = os.path.join(mydir, 'ResultMap.pkl')

with open(pickle_file_path, 'rb') as pickle_file:
    ResultMap = pickle.load(pickle_file)



@app.route('/test', methods = ['POST', 'GET'])
@cross_origin()
def predict():

    if request.method == 'GET':
        return {'Conntection': 'True'}

    dat = request.get_json()


    file = dat['file']
    starter = file.find(',')
    image_data = file[starter+1:]
    image_data = bytes(image_data, encoding="ascii")
    im = Image.open(BytesIO(base64.b64decode(image_data)))
    im.save('recieved/image.jpg')
    

    image_path = "recieved/image.jpg"
    
        

 
    test_image = image.load_img(image_path, target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)
    final = ResultMap[np.argmax(result)]

    _id = get_id(final)
    employee = get_employee(_id)
    #print(employee[0][0])

    os.remove(image_path)
    
    return {
        'id': employee[0][0],
        'name': employee[0][1],
        'designation' : employee[0][2],
        'salary': employee[0][3]
    }

def get_id(face):
    res = ''
    for a in face:
        if a.isdigit():
            res += a
    return int(res)

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port = '5000')