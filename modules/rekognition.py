# -*- coding:utf-8 -*-
import boto3

client = boto3.client('rekognition')


def detect_labels(key, max_labels=10):
    with open(key, 'rb') as image:
        try:
            response = client.detect_labels(
                Image={
                    'Bytes': image.read()
                }
            )
            return response['Labels']

        except Exception as e:
            return e



# def detect_labels(key, max_labels=10):
#     with open(key, 'rb') as image:
#         response = client.detect_labels(
#             Image={
#                 'Bytes': image.read()
#             }
#         )
#         return response['Labels']
