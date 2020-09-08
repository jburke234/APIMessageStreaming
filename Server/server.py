import re   
from concurrent import futures
from datetime import datetime
import logging, grpc, words_pb2, words_pb2_grpc, time

class Listener(words_pb2_grpc.WordServiceServicer):

    def __init__(self):
        self.word_file = open("ToTheLighthouse.txt", "r",encoding="ISO-8859-1")
        self.lines = self.word_file.readlines()
    
    def RequestWord(self, request, context):
        time_diff = 0
        line_count = len(self.lines)

        for i in range(line_count):
            
            words = self.lines[i].split(" ")
            word_count = len(words)
                
            for x in range(word_count):
                word = words[x].lower().replace(" ","")
        
                word = re.sub(r'[^\w]', ' ',word)
                
                self.word = word
                
                response = words_pb2.WordReply(message=str(self.word))
           
                time.sleep(time_diff)

                yield response

def serve():
 	    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
 	    words_pb2_grpc.add_WordServiceServicer_to_server(Listener(), server)
 	    server.add_insecure_port('[::]:50051')
 	    server.start()
 	    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
