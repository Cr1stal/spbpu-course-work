from __future__ import print_function

import logging

import grpc
import strokes_pb2
import strokes_pb2_grpc

class Client(object):
  def run(self, gender_arg, age_arg, hypertension_arg, heart_disease_arg, ever_married_arg, work_type_arg, residence_type_arg, average_glucose_level_arg, body_mass_index_arg):
      print("Will try to greet world ...")
      with grpc.insecure_channel('localhost:50051') as channel:
          stub = strokes_pb2_grpc.StrokeDetectionStub(channel)
          response = stub.Predict(strokes_pb2.StrokeRequest(gender=gender_arg, age=age_arg, hypertension=hypertension_arg, heart_disease=heart_disease_arg, ever_married=ever_married_arg, work_type=work_type_arg, residence_type=residence_type_arg, average_glucose_level=average_glucose_level_arg, body_mass_index=body_mass_index_arg))
      print("Client received: " + response.result)


if __name__ == '__main__':
    logging.basicConfig()
    client = Client()
    client.run(gender_arg=1, age_arg=44, hypertension_arg=True, heart_disease_arg=False, ever_married_arg=False, work_type_arg='Private', residence_type_arg='Urban', average_glucose_level_arg=3300, body_mass_index_arg=3200)
