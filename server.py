import email
from ntpath import join
import random
from flask import Flask, jsonify, request
import database_helper

app = Flask(__name__)
app.debug = True


@app.route("/")
def home(): 
    return "Hello, Flask!"

@app.route("/sign_in", methods=['GET']) 
def sign_in():
    json = request.get_json()
    if("email" in json and "password" in json):
        user=database_helper.find_user(json['email'])
        print(user)
        if(user):#fråga om hur man kollar att dem är samma password
            letters = "abcdefghiklmnopqrstuvwwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            token=''.join((random.choice(letters))for x in range(36))
            print(token)
            return token, 201
        else:
            return jsonify(user), 500
    else:
        return 400

@app.route("/sign_up", methods = ['PUT'])
def sign_up():
    json = request.get_json()
    if("email" in json and "password" in json and "firstname" in json and "familyname" in json and "gender" in json and "city" in json and "country" in json):
        if(len(json['password'])>=8):
            print("jorgubb gött")
            result=database_helper.create_profile(json['email'],json['password'],json['firstname'],json['familyname'],json['gender'],json['city'],json['country'])
            print(json['email'])
            if(result==True):
                return jsonify(result), 201
            else:
                return jsonify(result), 500
    else:
        return "{}",400

@app.route("/sign_out")
def sign_out():
    
    return "kunde inte bli bättre"

@app.route("/Change_password")
def Change_password(token, oldPassword, newPassword):
    return "oj va bytt"

@app.route("/get_user_data_by_token")
def get_user_data_by_token(token):
    return "tjusigt värre"

@app.route("/get_user_data_by_email")
def get_user_data_by_email(token,email):
    return jsonify(username=g.user.username,
                   email=g.user.email,
                   id=g.user.id)
 
@app.route("/Get_user_messages_by_token")
def Get_user_messages_by_token(token):
    return "tok-igt"

@app.route("/get_user_messages_by_email")
def get_user_messages_by_email(token, email):
    return "mailmail"

@app.route("/post_message")
def post_message(token, message, email):
    return "värsta meddelandet"




if __name__=="__main__":
    app.run()