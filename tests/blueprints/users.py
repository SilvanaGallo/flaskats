from flask import session

def test_login_get(app):

    with app.test_client() as client:
        response = client.get('/sign-in')
        assert response.status_code == 200
        assert b"Login" in response.data
       
    # if current_user.is_authenticated:
    #     return redirect(url_for('offers.list_offers'))
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         login_user(user, remember=form.remember.data)
    #         next_page = request.args.get('next')
    #         return redirect(next_page) if next_page else redirect(url_for('offers.list_offers'))
    #     else:
    #         flash('Login Unsuccessful. Please, check your email and password.','danger')
    # return render_template('login.html', title='Login', form=form)

def test_login_post(app):
    with app.test_client() as client:
        client.post("/sign-in", data={"email": "flask@gmail.com", "password": "123456"})
        
        # session is still accessible
        # assert session["user_id"] == 1
        assert False

def test_logout(app):
    with app.test_client() as client:
        response = client.get('/sign-out')
        assert response.status_code == 302
