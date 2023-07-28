from flask import Flask,render_template,request,redirect,url_for
app= Flask(__name__)
@app.route('/')
def home():
    return '<h2>Hello World</h2>'
@app.route('/welcome')
def welcome():
    return 'Welcome to the Flask tutorial'
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/success/<int:score>')
def success(score):
    return "You have passed and the score is "+str(score)
@app.route('/fail/<int:score>')
def fail(score):
    return "You have failed and your score is "+str(score)
@app.route('/calculate',methods=['GET','POST'])
def calculate():
    if request.method== 'GET':
        return render_template('calculate.html')
    else:
        maths= float(request.form['maths'])
        science= float(request.form['science'])
        history= float(request.form['history'])
        average= (maths+science+history)/3
        result= ''
        if average>= 50:
            result='success'
        else:
            result='fail'
        #return redirect(url_for(result,score=average))
        return render_template('results.html',results= average)
if __name__== '__main__':
    app.run(debug=True)