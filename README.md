# Breast-Cancer-Classifier

## Dataset Details
The dataset, "Breast Histopathalogy Images" by Paul Mooney has been imported from Kaggle. For each patient, the data has been classified as class 0 (benign) and class 1 (malignant). The entire dataset has been seperated out as train and test data with class 0 and class 1 folders within each of the two folders. It has then been sized down from 277,524 to 48,096 as it couldn't be completely unzipped into colab.

## Stain Normalization 
The main issue with histological image is that we cannot identify the variations in colors between the images. This is due to the different slider scanners used in color responses. Also the raw materials and manufacturing materials are also responsible. Hence, we use the technique stain normalization.This is the most crucial pre-processing step, before conducting any type of analysis by using histology images. In this project, we have used Vahadane method of stain normalization which is proposed by Abhishek Vahadane. Color histograms of source image is matched with the target image following which transformation of RGB images to de-correlated LAB color space. 

![image](https://user-images.githubusercontent.com/67037615/115230264-bb227880-a131-11eb-806c-638b3cfafa7e.png)

## Pretrained Architectures
The application of CNNs pre-trained on large annotated image databases, such as ImageNet for example, to images from different modalities/domains, for various classification tasks, is referred to as transfer learning. Pre-trained CNNs can be fine-tuned on medical image data sets, enabling large networks to converge quicker and learn domain-/task-
specific features. We have used Google's Inception V3, ResNet 50 and Inception ResNet V2. The top few layers have been replaced by custom layers with SGD with nesterov momentum used for Inception V3 and Adam optimizer used for the other two models.

## Web Application using Flask
1. Set up and switch to python3 virtual environment in terminal(optional)
   - python -m venv breast-cancer
   - source breast-cancer/bin/activate
   - pip install --upgrade pip
2. Install dependencies from requirements.txt
   - pip3 install -r requirements.txt
3. cd to where the code has been saved and,
   - export FLASK_ENV=development
   - export FLASK_APP=run.py
   - flask run
4. Use the given link to open the Web application

### Note : Inception V3 has been used for predictions in the web application as, right now it has the highest accuracy.
