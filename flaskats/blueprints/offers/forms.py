from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired, Length, Email, ValidationError, Optional
from flaskats.repositories import SQLAlchemyOffersRepository


offers_repository = SQLAlchemyOffersRepository()


class ApplicationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Apply')


class OfferForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    code = StringField('Code')
    repository_id = IntegerField('External Id', validators=[Optional()])
    description = TextAreaField('Description', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    salary_range = StringField('Salary Range', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_code(self, code):
        offer = offers_repository.get_offer_by_code(code.data)
        if offer:
            raise ValidationError('That code offer is taken. Please, choose another.')


class OfferUpdateForm(FlaskForm):

    id = IntegerField(widget=HiddenInput())
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    code = StringField('Code')
    repository_id = IntegerField('External Id', validators=[Optional()])
    description = TextAreaField('Description', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    salary_range = StringField('Salary Range', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_code(form, code):
        offer = offers_repository.get_offer_by_code(code.data)
        if 'id' in form:
            id = form.id.data
        else:
            id = None
        if offer and (id is None or id != offer.id):
            raise ValidationError('That code offer is taken. Please, choose another.')
