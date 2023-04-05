from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateField, DateTimeLocalField
from wtforms.validators import DataRequired
from datetime import datetime


class TestForm(FlaskForm):
    name = StringField('Nazwa', validators=[DataRequired()])
    numder = StringField('Numer serijny', validators=[DataRequired()])
    voltage = StringField('Napięcie badania', validators=[DataRequired()])
    current = StringField('Prąd upływu', validators=[DataRequired()])
    date = DateField('Data badania', format='%Y-%m-%d')
    result = BooleanField('Tak/Nie')
    next_test = DateField('Data następnego badania', format='%Y-%m-%d')
