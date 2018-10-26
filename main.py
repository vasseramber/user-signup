from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('infoform.html')

@app.route("/", methods=['POST'])
def valid():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
        
    if len(username) < 3 or len(username) > 20 or username=='' or str.isalpha(username)==False: 
        username_error = 'The username or password is not valid'
        username=username

    if len(password) < 3 or len(password) > 20 or password=='' or str.isalpha(password)==False:
        password_error = 'The username or password is not valid'
        password=''
    
    if verify!= password:
        verify_error = 'The username or password is not valid'
        verify=''

    if email =='':
        email=''
    else: 
        if email !='':
            if len(email) <3 or len(email) >20 or ('@' and '.' not in email):
                email_error = 'The email address is not valid'
                email=email

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("Welcome.html",username = username)
    else:
        return render_template("infoform.html", username=username, password=password, verify=verify, email=email, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)   


app.run()