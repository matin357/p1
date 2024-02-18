from flask import *

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"  # database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # binding DB and Flask App



class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    whroting = db.Column(db.String(5000), nullable=False)



@app.route("/", methods=["POST"])
def home():
    name=request.form["name_input"]
    if name in db:
        return  redirect("/white", name=name)
    else:
        return redirect("/submit_form")
    return render_template("login.html")

@app.route("/submit_form", methods=["POST"])
def submit_form():
    name = request.form["new_name"]
    new_user = User(
        password=name)
    db.session.add(new_user)
    db.session.commit()
    return render_template("register.html")

@app.route("/white")
def texting():
    name=request.form["name"]
    db["password"][name]["whrouting"]=request.form["text_holder"]
    return render_template("sfeaedf.html")



if __name__ == "__main__":
    app.run(debug=False)