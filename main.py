from flask import*
from flask_wtf import FlaskForm
from wtforms.validators import Email,DataRequired
from wtforms.fields import PasswordField,StringField,SubmitField,EmailField
from wtforms import validators
from wtforms import EmailField
from flask_sqlalchemy import SQLAlchemy


logged_in = False # True
user = ""


app = Flask(__name__)
app.secret_key = '4n7h4r4x'

# database stuff
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstName = db.Column(db.String(120),nullable=False)
    lastName = db.Column(db.String(120),nullable=False)
    username =db.Column(db.String(100),nullable=False,unique=True)
    email = db.Column(db.String(160),nullable=False,unique=True)
    password =  db.Column(db.String(180),nullable=False)

#db.create_all() man wtf is wrong with this bitch ....

# classes for forms
class signupForm(FlaskForm):
    firstName = StringField("first name",validators=[DataRequired()],render_kw={"placeholder":"Whats your first name ?"})
    lastName =  StringField("last name",validators=[DataRequired()],render_kw={"placeholder":"Whats your last name ?"})
    username = StringField("username",validators=[DataRequired()],render_kw={"placeholder":"Choose a username "})
    email = EmailField("email",validators=[Email(),DataRequired()],render_kw={"placeholder":"Whats your email ?"})
    password = PasswordField("password",validators=[DataRequired(),validators.Length(min=4, max=25)],render_kw={"placeholder":"Please pick a weak password"})
    submit = SubmitField("Signup")
    
class loginForm(FlaskForm):
    username = StringField("username",validators=[DataRequired()],render_kw={"placeholder":"Whats your username ?"})
    password = PasswordField("password",validators=[DataRequired(),validators.Length(min=4, max=25)],render_kw={"placeholder":"ENter your password !"})
    submit = SubmitField("Login")


class profileForm(FlaskForm):
    firstName = StringField("first name",validators=[DataRequired()],render_kw={"placeholder":"Whats your first name ?"})
    lastName =  StringField("last name",validators=[DataRequired()],render_kw={"placeholder":"Whats your last name ?"})
    username = StringField("username",validators=[DataRequired()],render_kw={"placeholder":"Choose a username "})
    email = EmailField("email",validators=[Email(),DataRequired()],render_kw={"placeholder":"Whats your email ?"})
    password = PasswordField("password",validators=[DataRequired(),validators.Length(min=4, max=25)],render_kw={"placeholder":"Please pick a weak password"})
    submit = SubmitField("Confirm Changes")

@app.route("/")
def home():
    global logged_in
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():
    global logged_in
    form = loginForm()
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        # check database
    return render_template("login.html",form=form,logged_in=logged_in)

@app.route("/signup",methods=["GET","POST"])
def signup():
    global logged_in
    form = signupForm()
    if request.method == 'POST':
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        username = request.form.get("username")
        email =request.form.get("email")
        password = request.form.get("password")

        # check db

    return render_template("signup.html",form=form,logged_in=logged_in)

@app.route("/profile",methods=["GET","POST"])
def profile():
    global logged_in
    form = profileForm()
    return render_template("profile.html",form=form,logged_in=logged_in)

@app.route("/logout")
def logout():
    if("user" in session):
        session.pop("user")
    return redirect(url_for("home"))


if __name__=="__main__":
    app.run(debug=True,port=6969)


# man i had enough of this database shit , i need to fix it then i might be able to create something good xd
# reminder : this was just a warmp up and i havent used flask for like 6 months so yeah ...
# hope fully next time ( next project  ) will be better + web pages will be prettier 
# oof .