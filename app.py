from flask import Flask, render_template, request, flash
import threading
from .server import start_server
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.run(debug=True, use_debugger=False, use_reloader=False)

# Create SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Messages(db.Model):
  # id = db.Column(db.Integer, primary_key=True)
  user = db.Column(db.Integer, primary_key=True)
  # user = db.Column(db.String(10000), primary_key=True)
  saved_message = db.Column(db.String(1000000))
  message_time = db.Column(db.String(1000))

# Creates all tables in SQLAlchemy
db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
  all_messaging_entries = Messages.query.all() 

  if request.method == 'POST':
    inputted_message = request.form["ComposedMessage"]

    new_message = Messages(saved_message=inputted_message, message_time=str(datetime.datetime.now()))
    db.session.add(new_message)
    db.session.commit()

    return render_template('index.html', message_list = all_messaging_entries)
  else:
    return render_template('index.html', message_list = all_messaging_entries)


# @app.route('/messages', methods=['POST', 'GET'])
# def messages():
#   if request.method == 'POST':
#     pass
#     # Save message and username into database
#     # return 200 success code message
#   else:
#     return render_template('index.html')

def run_server_file():
  start_server()

x = threading.Thread(target=run_server_file)
x.start()
print(threading.activeCount())
