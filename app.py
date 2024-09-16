from flask import Flask
app = Flask(__name__)

@app.route('/')
def devops():
 return '<center><h1><font color=red>Germinare Tech, EU AMO DEVOPS GSTTTT, I LOVE DEVOPS TECH</center>'

@app.route('/Murilo')
def murilo():
 return '<center><h1><font color=red>Germinare Tech, EU AMO DEVOPS ! EU AMO MURILO !</center>'

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')
