from flask import Flask,request

app=Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    #data={'username':'mike','password':'123'}
    data = request.get_json()
    uname=data["username"]
    pas=data["password"]
    if uname=='kush' and pas=="123":
        return {"status":True,"message":"login sucessful","data":[]}
    return {"status":False,"message":"login invalid","data":[]}





if __name__=='__main__':
    app.run()