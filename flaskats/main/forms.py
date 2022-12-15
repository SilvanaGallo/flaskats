from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ApplicationForm(FlaskForm):
    name = StringField('Name', 
                            validators=[DataRequired(), Length(min=2, max=100)])

    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
                                    
    submit = SubmitField('Apply')
