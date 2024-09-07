from flask import Flask, render_template, redirect 
from flask_wtf import *
from wtforms import *
from bs4 import BeautifulSoup
import requests
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
        print(form.passw.data, type(form.passw.data))
        
        if (str(form.passw.data)=="401"):
            print("Password Matched for PPT")
            #return_template('certificates.html',form=hehe)
            return redirect("https://1drv.ms/p/c/f6aa89a0d3ad01c6/EZyYlhpYVHFDtKLI_1P8e5wBSykPsm-jVLGSXQKrCCJ_xw")
        
        if (str(form.passw.data)=="449"):
            print("Password Matched for Docx")
            #return_template('certificates.html',form=hehe)
            return redirect("https://1drv.ms/w/c/f6aa89a0d3ad01c6/EfYEm2dPozBHjpP7jzNf8t8Baqy01G0G2Yt7o1JTNatcwg")
        else:
            return render_template('e.html',form=form)

    
    return render_template('e.html',form=form)



@app.route('/certifications',methods=['GET','POST'])
def certify():
    return render_template('certifications.html')
@app.route('/me', methods=['GET', 'POST'])
def submit():
    return redirect("https://github.com/yc-pro-123")
@app.route('/t/<ab>',methods=['GET'])
def twitsave():
    print("Hey",ab)
    #url ="https://twitter.com/TweetTemplates1/status/1809197143099670530"
    params={"url":"https://x.com/"+ab
 #juz_scrolling/status/1831187338044858686?t=hyBxg6bqJh6X9HlVPdP7ng&s=19"
}
    url1="https://twitsave.com/info" 
    with requests.Session() as s:
        s.headers.update({
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
    })
        r=s.get(url1,params=params)
        soup =BeautifulSoup(r.content,'html.parser')
        e=soup.prettify()
        #print(r.text,"\n\n\n")
        w=soup.find_all("ul")
        return redirect((w[2].find(("li")).a["href"]))
#@app.route('/submit', methods=['GET', 'POST'])
#def submit():
#    form = MyForm()
#    if form.validate_on_submit():
#        return render_template('index.html')
#    return render_template('submit.html', form=form)


if __name__ == '__main__':
   app.run(debug = True)
