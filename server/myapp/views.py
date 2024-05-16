from django.conf import settings
from django.shortcuts import render
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def process_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        image_path = f'media/{image_file.name}'
        
        with open(image_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        static_dir = os.path.join(settings.BASE_DIR, 'static')
        age_prototxt_path = os.path.join(static_dir, 'age.prototxt')
        gender_prototxt_path = os.path.join(static_dir, 'gender.prototxt')
        dex_chalearn_model_path = os.path.join(static_dir, 'dex_chalearn_iccv2015.caffemodel')
        gender_model_path = os.path.join(static_dir, 'gender.caffemodel')

        # Load the models
        age_model = cv2.dnn.readNetFromCaffe(age_prototxt_path, dex_chalearn_model_path)
        gender_model = cv2.dnn.readNetFromCaffe(gender_prototxt_path, gender_model_path)
        
        # Read and process the image
        img = cv2.imread(image_path)
        haar_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        
        def detect_faces(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = haar_detector.detectMultiScale(gray, 1.3, 5)
            return faces
        
        faces = detect_faces(img)
        for x, y, w, h in faces:
            detected_face = img[int(y):int(y+h), int(x):int(x+w)]
        
        detected_face = cv2.resize(detected_face, (224, 224))
        img_blob = cv2.dnn.blobFromImage(detected_face)
        
        age_model.setInput(img_blob)
        age_dist = age_model.forward()[0]
        
        gender_model.setInput(img_blob)
        gender_class = gender_model.forward()[0]
        
        output_indexes = np.array([i for i in range(0, 101)])
        apparent_predictions = round(np.sum(age_dist * output_indexes), 2)
        
        gender = 'Woman ' if np.argmax(gender_class) == 0 else 'Man'
        
        demography = DeepFace.analyze(image_path, actions = ['age', 'gender'])
        age = demography[0]["age"]
        ret_gender = 'Woman' if demography[0]["gender"]['Woman'] > demography[0]["gender"]['Man'] else 'Man'
        
        # Clean up the uploaded image
        os.remove(image_path)
        
        return JsonResponse({
            'age': age,
            'gender': ret_gender,
            'demography': demography[0]["gender"]
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def upload_image(request):
    return render(request, 'upload.html')