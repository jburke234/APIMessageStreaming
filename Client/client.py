from __future__ import print_function

import logging, grpc, words_pb2, words_pb2_grpc, redis

def run():

    with grpc.insecure_channel('server:50051') as channel:
        stub = words_pb2_grpc.WordServiceStub(channel)

        start_with_vowel_count = 0
        start_with_cons_count = 0
        
        average_word_len = 0
        total_word_count = 0
        total_word_length = 0
		
        sailor_count = 0
        window_count = 0
        
        vowels = ["a","e","i","o","u"]

        for response in stub.RequestWord(words_pb2.WordRequest(name="test")):
            
            if len(response.message) > 0:
                word_resp = str(response.message).replace('"','')
                
                word_resp = word_resp.strip()
                
                word_resp = word_resp.lower()
                
                word_resp = word_resp.replace(' ','')
				
                if word_resp.isalpha():
                
                    if word_resp[0] in vowels:
                        start_with_vowel_count = start_with_vowel_count + 1
                    else:
                        start_with_cons_count = start_with_cons_count + 1
                    
                        if word_resp == "sailor":
                            sailor_count = sailor_count + 1
                        elif word_resp == "window":
                            window_count = window_count + 1
                        				
                
                    total_word_length = total_word_length + len(word_resp)
                    total_word_count = total_word_count + 1
                
                    average_word_len = total_word_length / total_word_count
                
		
                    print("Client received: " + word_resp, flush = True)
	
                    try:
                        conn = redis.StrictRedis(host='redis', port=6379) 
                        conn.set("msg:start_with_vowel_count",start_with_vowel_count)
                        conn.set("msg:start_with_cons_count",str(start_with_cons_count))
                        conn.set("msg:sailor_count",str(sailor_count))
                        conn.set("msg:window_count",str(window_count))
                        conn.set("msg:average_word_len",str(average_word_len))
                                  
                    except Exception as ex: 
                        print('Error:', ex)


if __name__ == '__main__':
    logging.basicConfig()
    run()

    run()
