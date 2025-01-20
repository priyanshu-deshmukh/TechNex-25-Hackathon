from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__,template_folder="templates")

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method  == "POST":
        return "POST"



if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)

