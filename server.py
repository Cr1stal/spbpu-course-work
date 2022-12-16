from concurrent import futures
import logging

import grpc
import strokes_pb2
import strokes_pb2_grpc

import pickle
import sklearn
import pandas as pd

class StrokeDetection(strokes_pb2_grpc.StrokeDetectionServicer):
    def __init__(self):
        super().__init__()

        f = open('RandomForestSer.pkl', 'rb')
        self.model = pickle.load(f)
        f.close()

    def Predict(self, request, context):
        data = {
            'age': request.age,
            'hypertension': int(request.hypertension),
            'heart_disease': int(request.heart_disease),
            'avg_glucose_level': request.average_glucose_level/100,
            'bmi': request.body_mass_index/100,

            'gender_Female': int(request.gender == 'female'),
            'gender_Male': int(request.gender == 'male'),

            'ever_married_No': int(request.ever_married == 'no'),
            'ever_married_Yes': int(request.ever_married == 'yes'),

            'work_type_Govt_job': int(request.work_type == 'govt_job'),
            'work_type_Never_worked': int(request.work_type == 'never'),
            'work_type_Private': int(request.work_type == 'private'),
            'work_type_Self-employed': int(request.work_type == 'self-employed'),
            'work_type_children': int(request.work_type == 'children'),

            'Residence_type_Rural': int(request.residence_type == 'Rural'),
            'Residence_type_Urban': int(request.residence_type == 'Urban'),

            'smoking_status_formerly smoked': int(request.smoking_status == 'formerly_smoked'),
            'smoking_status_never smoked': int(request.smoking_status == 'never_smoked'),
            'smoking_status_smokes': int(request.smoking_status == 'smokes'),
        }
        example = pd.DataFrame(data,index=[0])
        result = self.model.predict(example)
        return strokes_pb2.StrokeReply(result=result[0])


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    strokes_pb2_grpc.add_StrokeDetectionServicer_to_server(StrokeDetection(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
