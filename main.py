from flask import Flask, render_template
from datetime import datetime
import json
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request
#color of import is grey because this import is still not yet used

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


app.run(debug=True)



