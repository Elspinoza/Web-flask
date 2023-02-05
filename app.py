from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('toto/index.html')

@app.route('/inheritance/home')
def inheritance_home():
    return render_template('inheritance/home.html')

@app.route('/inheritance/about')
def inheritance_about():
    return render_template('/inheritance/about.html')

@app.route('/variable')
def var():
    valeur = "Hello world !"
    users = {"Inno":"Lome","Ema":"Dosie", "Theophile":"togoville", "morris":"ville", "Yves":"Pya"}
    return render_template('variables/index2.html', my_value = valeur, my_users = users)
    

if(__name__ == '__main__'):
    app.run(debug=True, host= "0.0.0.0", port= 2000)