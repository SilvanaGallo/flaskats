from flask import render_template, redirect, Blueprint, flash, url_for
from flaskats.main.forms import ApplicationForm
from flaskats.broker import RabbitmqProducer
from datetime import datetime
from json import dumps

main = Blueprint('main', __name__)

job = {
    'title': 'Christmas season offer',
    'code': 'BE03-345',
    'salary_range': '2000-3000',
    'description': 'The best offer ever',
    'requirements': ['req 1',
                     'req 2',
                     'req 3',
                     'req 4']
}

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', offer=job, title='Offer')



@main.route("/apply", methods=['GET','POST'])
def application():
    form = ApplicationForm()
    if form.validate_on_submit():

        #Build payload or DTO?
        application = { 'candidate': { 'name': form.name.data,
                                       'candidate_email': form.email.data },
                        'job': job['code'],
                        'date': datetime.now().isoformat()
        }

        #Queue application
        producer = RabbitmqProducer() 
        producer.submit_application(application)

        flash('Your application has been sent!', 'success')
    return render_template('application.html', 
                            title='Application', 
                            form=form, 
                            offer=job)

