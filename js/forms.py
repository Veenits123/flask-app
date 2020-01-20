from flask_wtf import FlaskForm 
from wtforms import (StringField, SubmitField, BooleanField, DateTimeField, RadioField,
                    SelectField, TextAreaField ,TextField)
from wtforms.validators import DataRequired

# app = Flask(__name__) 



class Form(FlaskForm):
    # name = StringField('SOme label that can be accessed using fiels.label syntax', validators=[DataRequired()])
    # Age = BooleanField('18 or above?')
    # major=SelectField('CHoices', choices=[('ph','PHYSICS'),
    # ('cse','CSE'), ('mt','maths')]) 
    # #value , label
    # gen = RadioField('enter gender', choices= [('m','male'),('f','female')])
    # #value , label

    fb=TextAreaField('describe the case: ', validators=[DataRequired()])
    submit= SubmitField()