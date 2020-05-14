import boto3
from googletrans import Translator

def detectar_etiquetas(foto):
    client=boto3.client('rekognition')

    with open(foto, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})   
    respuesta = response['Labels']
    return respuesta
    





