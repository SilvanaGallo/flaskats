
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from flaskats.blueprints.offers import OfferForm, OfferUpdateForm, ApplicationForm
from flaskats.dtos import Offer, Application
from flaskats import offers_repository
from flaskats.services import Producer


offers = Blueprint('offers', __name__)


@offers.route("/", methods=['GET'])
def list_offers():
    offers = []
    page = request.args.get('page', 1, type=int)
    if current_user.is_authenticated:
        offers = offers_repository.get_offers(per_page=10, page=page)
        return render_template('administrate_offers.html', title='Job Offers', offers=offers)
    else:
        offers = offers_repository.get_published_offers(per_page=10, page=page)
        return render_template('published_offers.html', title='Published Job Offers', offers=offers)


@offers.route("/offer", methods=['GET', 'POST'])
@login_required
def create_offer():
    form = OfferForm()
    if form.validate_on_submit():
        offer = Offer(title=form.title.data, code=form.code.data,
                    repository_id=form.repository_id.data,
                    description=form.description.data,
                    requirements=form.requirements.data,
                    salary_range=form.salary_range.data)
        offers_repository.create_offer(offer)
        flash('The job offer has been created!', 'success')
        return redirect(url_for('offers.list_offers'))
    return render_template('create_offer.html', title='New Job Offer', form=form)


@offers.route("/offer/<int:id>/update", methods=['GET', 'POST'])
@login_required
def update_offer(id):
    offer = offers_repository.get_offer(id)
    form = OfferUpdateForm()
    if form.validate_on_submit():
        offer.id = form.id.data
        offer.title = form.title.data
        offer.code = form.code.data
        offer.repository_id = form.repository_id.data
        offer.description = form.description.data
        offer.requirements = form.requirements.data
        offer.salary_range = form.salary_range.data
        offers_repository.update_offer(offer)
        flash('The job offer has been updated!', 'success')
        return redirect(url_for('offers.list_offers'))
    elif request.method == 'GET':
        form.id.data = offer.id
        form.title.data = offer.title
        form.code.data = offer.code
        form.repository_id.data = offer.repository_id
        form.description.data = offer.description
        form.requirements.data = offer.requirements
        form.salary_range.data = offer.salary_range
    return render_template('update_offer.html', title='Update Offer', form=form)


@offers.route("/offer/<int:id>/publish", methods=['GET'])
@login_required
def publish_offer(id):
    offers_repository.publish_offer(id)
    flash('The job offer has been published!', 'success')
    return redirect(url_for('offers.list_offers'))


@offers.route("/offer/<string:offer_code>", methods=['GET'])
def show_offer(offer_code):
    offer = offers_repository.get_offer_by_code(offer_code)
    return render_template('show_offer.html', title='Offer', offer=offer)


@offers.route("/offer/<string:offer_code>/delete", methods=['POST'])
@login_required
def delete_offer(offer_code):
    offers_repository.delete_offer(offer_code)

    flash('The job offer has been deleted!', 'success')
    return redirect(url_for('offers.list_offers'))


@offers.route("/apply", methods=['GET', 'POST'])
def application():
    params = request.args.to_dict()
    offer = offers_repository.get_offer_by_code(params['code_offer'])

    form = ApplicationForm()
    if form.validate_on_submit():
        # Build payload DTO
        application = Application(job=offer.repository_id,
                                  name=form.name.data,
                                  email=form.email.data)
        # Queue application
        producer = Producer(queue='application')
        producer.submit_event(application)

        flash('Your application has been sent!', 'success')
    return render_template('application.html',
                            title='Application',
                            form=form,
                            offer=offer)
