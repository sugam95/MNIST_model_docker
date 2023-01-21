# MNIST_model_docker
## Instructions for running api

1. Run the Dockerfile for creating the docker image

2. This Docker images will be running the model training and inference script as REST api

3. For testing the api give the POST request from POSTMAN with address as http://172.17.0.2:5000/predict_file (note ip address can be different as it depends 
of containers you can get correct ip address once you run the inference script as from docker image)

4. The body for POSTMAN request contains image path ( for now have created one test folder name as sample_images which is used for prediction) we can give images path from this folder for testing inference script.

