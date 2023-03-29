from flask import Flask, request, redirect, render_template, url_for
app = Flask(__name__)

@app.route('/mypage/me')
def me():
    title='My html page'
    return render_template("index.html", title=title)
    
    
@app.route('/mypage/contact', methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        
        return render_template("form.html")
    if request.method == 'POST':
        form_data = request.form.get("massage")
        
        print(form_data)
        print("Your massage:"+form_data)
    return render_template("form.html")

