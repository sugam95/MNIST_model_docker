#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from numpy import argmax
import cv2
import keras
from flask import Flask,request
app = Flask(__name__)

#@app.route('/')
#def welcome():
#    return 'welcome to the page'
@app.route('/predict_file',methods=["POST"])
def run_prediction():
    data=request.json
    img_path = data['img_path']
    print('************',img_path)
    image = cv2.imread(img_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = gray_image / 255
    image = gray_image.reshape(1, 784)
    model = keras.models.load_model('final_model.h5')
    
    prediction = model.predict(image)
    prediction = argmax(prediction)
    print("predicted digit:", str(prediction))
    
    
    return {'predicted_output':str(prediction)}
    

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
    #app.run(host='0.0.0.0',port=8000)

