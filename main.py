from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("disease.pkl","rb"))
dic_a=pickle.load(open("diseasedic_a1.pkl","rb"))
dic_b=pickle.load(open("diseasedic_b.pkl" , "rb"))
dic_c=pickle.load(open("diseasedic_c.pkl" , "rb"))
pre_dic= pickle.load(open("pre_dic.pkl","rb"))



def getList(listA):
  predl=[]
  array=list(np.zeros(17))
  for i in range(len(listA)):
    array[i]=dic_b[listA[i]]
  predl.append(array)
  return predl


@app.route('/',methods=['GET','POST'])
def home():
    json_ = request.json
    dict1=dict(json_)
    listA=list(dict1.values())
    print(listA)
    pred_res = model.predict(getList(listA))
    prediction=dic_c[pred_res[0]]
    precaution=pre_dic[prediction]
    return jsonify({"Prediction":prediction,"Precaution":precaution})

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
   





