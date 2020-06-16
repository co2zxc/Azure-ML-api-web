import flask
import io
#import urllib.request
import urllib.request as urllib
import json
from flask import request, render_template

app = flask.Flask(__name__)

@app.route("/", methods=['GET', "POST"])
def predict():
    if flask.request.method == "GET":
        return render_template('index.html')
    else:
        data = {}
        data['make']=request.form['make']
        data['body-style']=request.form['body-style']
        data['wheel-base']=request.form['wheel-base']
        data['engine-size']=request.form['engine-size']
        data['horsepower']=request.form['horsepower']
        data['peak-rpm']=request.form['peak-rpm']
        data['highway-mpg']=request.form['highway-mpg']
        data['price']='0'
        input1=[]
        input1.append(data)
        input2={}
        input2["input1"]=input1
        input3={}
        input3["Inputs"]=input2
        
        body = str.encode(json.dumps(input3))
        print(body)
       
        url = '依據你的API填寫'
        api_key = '依據你的API填寫'
        headers = {'Accept':'application/json','Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.Request(url, body, headers) 
        
        result=''
        
        response = urllib.urlopen(req)
        result = response.read()
        result_dict = json.loads(result)
        ScoredLabels = result_dict["Results"]["output1"][0]["Scored Labels"]

        return "Scored Labels:"+ScoredLabels #flask.jsonify(result)
        

if __name__ == "__main__":
      app.run(host='0.0.0.0', port=8080)
    