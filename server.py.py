from flask import Flask, render_template, request, flash, redirect
from flask import session

app = Flask(__name__)

import authenticate as auth


@app.route('/')
@app.route('/homapage')
def index():

    user_id = session.get('username')
    loged_in = auth.user_loged_in(user_id)

    return render_template("main.html")





@app.route('/register', methods=['GET', 'POST'])
def registration():
    """
    DONE - create a username and password pair.
    password hashing for maximum security.
    If either fild is empty after push the Submit button on the registration page,
      ==> Show: "Please, fill in both fields." error message.
    

    If the username field contains a username that already exists in the database
      ==> Show: "Username already exists, please choose another one!" error message
    
    On successful registration,
      ==> Show: "Successful registration. Log in to continue."
    
    """



    if request.method == 'POST':

        new_username = request.form['input-username']
        new_email = request.form['input-email']
        new_password = request.form['input-password']
        error = None

        if new_username == "" or new_email == "" or new_password == "":
            error = "Please, fill in both fields."

        else:

            if data.get_user_by_id(new_username) is None:

                try:
                    data.user_registration(new_username, new_email, auth.hash_password(new_password))

                    error = 'Registration successfully done!'
                    
                    ## redirect back to login countdown
                    # return redirect('/')

                
                except Exception as errors:
                    print(errors)                 
                    
            else:
                error = f'User {new_username} is already registered.'

        flash(error)
            
    


    return render_template("registration.html")


        # pass



@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login with the created ID & PW
    # If the username and password pair does not match
    # ==> Show: "Wrong username or password"
    #
    # After logging in, the username is displayed in the top right corner with the text 
    # ==> Show: "Signed in as <username>"

    if request.method == 'POST':

        login_username = request.form['login-username']
        login_password = request.form['login-password']
        error = None

        user_is_exist = data.get_user_by_id(login_username)

        if login_username == "" or login_password == "":
            error = "Please, fill in both fields."

        else:

            if user_is_exist is not None:
                
                chechk_auth = auth.check_password_hash(login_password, login_username)
                if chechk_auth:
                    session['username'] = login_username

                    return redirect('/')

                else:
                    error = "Wrong username or password"

            else:
                error = "Wrong username or password"
            

        flash(error)


    return render_template("login.html")


@app.route('/logout', methods=['GET', 'POST'])
def logout():

    del session['username']
    return render_template('logout.html')




@app.route('/OBD_get_data', methods=['GET', 'POST'])
def get_data():
    

    if request.method=='POST':
        

        print(f"get data from OBD, counter ")
        return "", 200
    
    

if __name__ == '__main__':
    app.run(debug=True, port=8000)