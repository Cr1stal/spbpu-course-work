from __future__ import print_function

import logging
import random

import grpc
import strokes_pb2
import strokes_pb2_grpc

class Client(object):
  def run(self, gender_arg, age_arg, hypertension_arg, heart_disease_arg, ever_married_arg, work_type_arg, residence_type_arg, average_glucose_level_arg, body_mass_index_arg, smoking_status_arg):
      with grpc.insecure_channel('localhost:50051') as channel:
          stub = strokes_pb2_grpc.StrokeDetectionStub(channel)
          response = stub.Predict(strokes_pb2.StrokeRequest(gender=gender_arg, age=age_arg, hypertension=hypertension_arg, heart_disease=heart_disease_arg, ever_married=ever_married_arg, work_type=work_type_arg, residence_type=residence_type_arg, average_glucose_level=average_glucose_level_arg, body_mass_index=body_mass_index_arg, smoking_status=smoking_status_arg))
      return response


if __name__ == '__main__':
    logging.basicConfig()
    client = Client()
    client.run(gender_arg=random.choice(['male','female']), age_arg=44, hypertension_arg=random.choice([True, False]), heart_disease_arg=random.choice([True, False]), ever_married_arg=random.choice(['yes','no']), work_type_arg=random.choice(['govt_job','never','private','self-employed','children']), residence_type_arg=random.choice(['urban','rural']), average_glucose_level_arg=3300, body_mass_index_arg=3200, smoking_status_arg=random.choice(['formerly_smoked', 'never_smoked', 'smokes']))
