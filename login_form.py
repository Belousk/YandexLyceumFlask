from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class EmergencyAccess(FlaskForm):
    astronaut_id = StringField('id астронавта', validators=[DataRequired()])
    astronaut_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    captain_id = StringField('id капитана')
    captain_password = PasswordField('Пароль капитана')
    submit = SubmitField('Доступ')
