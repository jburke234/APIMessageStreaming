from flask import Flask 
import redis 

app = Flask(__name__) 
 
@app.route('/') 
def print_logs():
    output = ''
    try:
        conn = redis.StrictRedis(host='redis', port=6379)
        
        start_with_vowel_count = conn.get("msg:start_with_vowel_count")
        start_with_cons_count = conn.get("msg:start_with_cons_count")
        sailor_count = conn.get("msg:sailor_count")
        window_count = conn.get("msg:window_count")
        average_word_len = conn.get("msg:average_word_len")

        start_with_vowel_count_str = str(start_with_vowel_count).replace("'","").replace("b","")
        start_with_cons_count_str = str(start_with_cons_count).replace("'","").replace("b","")
        sailor_count_str = str(sailor_count).replace("'","").replace("b","")
        window_count_str = str(window_count).replace("'","").replace("b","")
        average_word_len_str = str(average_word_len).replace("'","").replace("b","")
        
        output = "Starts with vowel count: " + start_with_vowel_count_str + "<br>"
        output += "Starts with cons count: " + start_with_cons_count_str + "<br>"
        output += "Sailor word count: " + sailor_count_str + "<br>"
        output += "Window word count: " + window_count_str + "<br>"
        output += "Average word length: " + average_word_len_str + "<br>"
		
    except Exception as ex:
        output = 'Error:' + str(ex)
    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
