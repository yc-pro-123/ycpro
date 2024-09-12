from flask import Flask, render_template, redirect, request,Response
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
    ab=request.args.get("t")
    #print("Hey",ab)
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
        #return "<h1>Heyy</h1>"+ab
        print(w[2].find(("li")).a["href"])
        return redirect((w[2].find(("li")).a["href"]))


@app.route("/i",methods=["GET"])
def instavideosave():
    ar=request.args.get("i")
    data="https://www.instagram.com/"+ar
    #data="https://www.instagram.com/reel/C_ktpDXSW9l/?utm_source=ig_web_button_share_sheet"
    key ="qwertyuioplkjhgf"
    t=key.encode(encoding="utf-8")
    #print("T",list(t),"\n")
    b=data.encode()
    #print("B",list(b),"\n")
    s=pad(b,96) #print("S",list(s),"\n")
    cipher=AES.new(t,AES.MODE_ECB) 
    #ct_bytes=cipher.encrypt(pad(data,AES.block_size))
    ct_bytes=cipher.encrypt(s) 
    print(ct_bytes.hex())
    ur=ct_bytes.hex() 
    #url ="https://twitter.com/TweetTemplates1/status/1809197143099670530" #params={"url":"https://www.instagram.com/reel/C_ktpDXSW9l/?utm_source=ig_web_button_share_sheet"}
    downurl="https://dl1.instavideosave.com/?url="
    scr=f"<h1>Yours Url:{data}\nHash :{ur}"+"""</h1><h2 id='hu'></h2><script>var downurl='https://dl1.instavideosave.com/?url='; 
    var ur = """+ur+""";
    var e={
    'Accept-Encoding': 'gzip, deflate, br', 'Accept': '*/*', 
    'Connection': 'keep-alive', 'method': 'GET', 
    'authority': 'backend.instavideosave.com', 
    'path': '/allinone', 
    'scheme': 'https', 
    'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 
    'Origin':'https://www.instavideosave.net', 
    'Pragma': 'no-cache', 
    'Referer': 'https://www.instavideosave.net/', 
    'Sec-Fetch-Dest': 'empty', 
    'Sec-Fetch-Mode': 'cors', 
    'Sec-Fetch-Site': 'cross-site', 
    'Sec-Ch-Ua': '\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"', 
    'Sec-Ch-Ua-Mobile': '?1', 
    'Sec-Ch-Ua-Platform':'\"Android\"',
    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    "Content-Type":"application/json",
    "Url":ur};
    
    let url1='https://backend.instavideosave.com/allinone';
    fetch(url1,{method:'GET',mode:'cors',headers:e})
    .then(response => response.json())
    .then(data => {
    // do whatever you want with data
    var link=data["video"][0]["video"];
    document.getElementById("hu").innerHTML=data;
    window.location.assign(downurl+encodeURIComponent(link)); });
    //window.fetch(downurl+encodeURIComponent(link));</script>"""
    return scr
    

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
