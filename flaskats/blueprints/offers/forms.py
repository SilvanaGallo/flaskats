from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flaskats import offers_repository


class ApplicationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Apply')


class OfferForm(FlaskForm):

    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    code = StringField('Code', validators=[DataRequired(), Length(min=2, max=10)])
    repository_id = IntegerField('External Id', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    salary_range = StringField('Salary Range', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_code(self, code):
        offer = offers_repository.get_offer_by_code(code.data)
        if offer:
            raise ValidationError('That code offer is taken. Please, choose another.')


class OfferUpdateForm(FlaskForm):

    id = HiddenField('id', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=100)])
    code = StringField('Code', validators=[DataRequired(), Length(min=2, max=10)])
    repository_id = IntegerField('External Id', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    salary_range = StringField('Salary Range', validators=[DataRequired()])
    submit = SubmitField('Submit')