from flask import Flask, request
import requests

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>this the email api for pTech</h1>"

@app.route('/mail', methods=['POST'])
def send_simple_message():
    data = request.get_json()
    fname = data['fname']
    lname = data['lname']
    email = data['email']
    msg = data['msg']
    requests.post(
        "https://api.mailgun.net/v3/piranhatechnologies.com/messages",
        auth=("api", "key-774f995362ec727cc4819fa705c1313d"),
        data={"from": "P Tech <mailgun@piranhatechnologies.com>",
              "to": [ "benja.gregory2@gmail.com", "snydzllc@gmail.com"],
              "subject": "Hello",
              "text": fname + ' ' +lname + ' sent a message. They say '+ msg})
    return "<h1>Email Sent</h1>"
app.run()