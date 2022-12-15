from flask import render_template, Blueprint, flash, after_this_request, current_app
from flaskats.main.forms import ApplicationForm
from flaskats.broker import Producer
from json import load
import os
from flaskats.dto import Application

main = Blueprint('main', __name__)
job = {}

@main.before_app_first_request
def _load_offer():
    print("before_request executing!")
    # Loading offer
    f = open(os.path.join(current_app.root_path,'static/offer.json'))
    global job
    job = load(f)
    f.close()

@main.route("/")
@main.route("/home")
def home(): 
    return render_template('home.html', offer=job, title='Offer')


@main.route("/apply", methods=['GET','POST'])
def application():
    form = ApplicationForm()
    if form.validate_on_submit():
        #Build payload DTOs
        application = Application(job=job['code'],
                                  name=form.name.data, 
                                  email=form.email.data)
        #Queue application
        producer = Producer() 
        producer.submit_application(application.to_json())

        flash('Your application has been sent!', 'success')
    return render_template('application.html', 
                            title='Application', 
                            form=form, 
                            offer=job)

