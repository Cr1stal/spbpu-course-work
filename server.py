from concurrent import futures
import logging

import grpc
import strokes_pb2
import strokes_pb2_grpc


class StrokeDetection(strokes_pb2_grpc.StrokeDetectionServicer):

    def Predict(self, request, context):
        return strokes_pb2.StrokeReply(result=20)


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
