from flask import Flask, render_template
from flask_wtf import *
from wtforms import *
from wtforms.validators import DataRequired
app = Flask(__name__)
app.secret_key = 'development key'

class MyForm(FlaskForm):
    passw = IntegerField('Password :',validators=[DataRequired()])
    submit = SubmitField("Send")

@app.route('/',methods=['GET','POST'])
def certificates():
    form = MyForm()
    if form.validate_on_submit():
        print("hihihi")
        print(form.passw.data)
        if (form.passw.data=="0449"):
            #return_template('certificates.html',form=hehe)
            return redirect("https://1drv.ms/w/c/f6aa89a0d3ad01c6/EfYEm2dPozBHjpP7jzNf8t8Baqy01G0G2Yt7o1JTNatcwg")
        else:
            return render_template('e.html',form=form)
    return render_template('e.html',form=form)


#@app.route('/submit', methods=['GET', 'POST'])
#def submit():
#    form = MyForm()
#    if form.validate_on_submit():
#        return render_template('index.html')
#    return render_template('submit.html', form=form)


if __name__ == '__main__':
   app.run(debug = True)