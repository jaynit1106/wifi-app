from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is my first API call!'

@app.route('/post', methods=["POST"])
def testpost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'text':input_json['text']}
     answerr=str(dictToReturn)
     file = open('read.txt', 'a')
     file.write("\n")
     file.write("\n")
     file.close()
     file = open('read.txt', 'a')
     file.write(answerr)
     file.close()

     return jsonify(dictToReturn)