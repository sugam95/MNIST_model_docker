FROM jupyter/scipy-notebook
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY train.py ./train.py
COPY inference.py ./inference.py
COPY final_model.h5 ./final_model.h5
COPY sample_images ./sample_images
EXPOSE 5000
RUN python train.py
RUN python inference.py
