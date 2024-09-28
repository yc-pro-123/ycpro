from flask import Flask, render_template, redirect, request,Response,render_template_string
from flask_wtf import *
from wtforms import *
from bs4 import BeautifulSoup
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


from wtforms.validators import DataRequired
app = Flask(__name__)
app.secret_key = 'development key'

def remove_custom_headers(app):
    @app.before_request
    def remove_headers():
        for header in ['X-Forwarded-For', 'X-Forwarded-Host', 'X-Vercel-Deployment-Url']:
            request.headers.pop(header, None)

    @app.after_request
    def remove_headers_from_response(response):
        for header in ['X-Forwarded-For', 'X-Forwarded-Host', 'X-Vercel-Deployment-Url']:
            response.headers.pop(header, None)
        return response



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

@app.route('/t',methods=['GET'])
def twitsave():
    print(type(request.args.keys()))
    
    args=[word.lower() for word in request.args.keys()]
    
    data=request.args.get(args[0])
    data = data if (data.startswith("https://x.com") or data.startswith("https://twitter")) else "https://.x.com/"+data
    
    print("Hey",data)
    if args[0]=="e":
        print(data)
        if data[8]=="x":
            data="https://twitter."+data[data.index("com"):data.index("?")]+"/video/1"
            print("Embedding", data)
        script="<script>var data= "+data";+"""navigator.clipboard.writeText(data);  
  // Alert the copied text
  alert("Copied the text: " + data);</script>"""
        return render_template("ei.html",sdata=script,data=data)
    if args[0]!="t":
        errt="Sorry !"
        return render_template("ei.html",error=errt)
    #url ="https://twitter.com/TweetTemplates1/status/1809197143099670530"
    params={"url": data
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
        #return "<h1>Heyy</h1>"+ab
        print(w[2].find(("li")).a["href"])
        return redirect((w[2].find(("li")).a["href"]))


@app.route("/i",methods=["GET"])
def instavideosave():
    print(type(request.args.keys()))
    
    args=[word.lower() for word in request.args.keys()]
    
    errtxt=""
    if args[0]=="mp3":
        downurl="https://mp3.instavideosave.com/api?url="
    elif args[0]=="mp4":
        downurl="https://dl1.instavideosave.com/?url="
    else:
        downurl=""
        errtxt=""
        return render_template("ei.html",error=errtxt)
    
    data=request.args.get(args[0])
    data = data if data.startswith("https://www.insta") else "https://www.instagram.com/"+data
    #data="https://www.instagram.com/reel/C_ktpDXSW9l/?utm_source=ig_web_button_share_sheet"
    key ="qwertyuioplkjhgf"
    t=key.encode(encoding="utf-8")
    #print("T",list(t),"\n")
    b=data.encode()
    sz=len(b)
    bs=16
    for i in range(2,17):
        if(bs<=sz):
            bs=i*16
        else:
            break;
    #print("B",list(b),len(b),"\n")
    s=pad(b,bs)
    #print("S",list(s),len(s),"\n"
    cipher=AES.new(t,AES.MODE_ECB) 
    #ct_bytes=cipher.encrypt(pad(data,AES.block_size))
    ct_bytes=cipher.encrypt(s) 
    print(ct_bytes.hex())
    ur=ct_bytes.hex() 
    #url ="https://twitter.com/TweetTemplates1/status/1809197143099670530" #params={"url":"https://www.instagram.com/reel/C_ktpDXSW9l/?utm_source=ig_web_button_share_sheet"}
    #downurl="https://dl1.instavideosave.com/?url="
    return render_template("reel.html",type=args[0], downurl=downurl,data=data,ur=ur)
    

#return redirect (downurl+q)

#@app.route('/submit', methods=['GET', 'POST'])
#def submit():
#    form = MyForm()
#    if form.validate_on_submit():
#        return render_template('index.html')
#    return render_template('submit.html', form=form)
#if __name__ == '__main__':
   #app.run(debug = True)


#remove_custom_headers(app)
