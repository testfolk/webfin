from wtforms import Form, BooleanField, StringField, IntegerField, DateTimeField, RadioField, FloatField, SelectField, validators


class OptionForm(Form):
    spot = FloatField('Spot', [validators.Length(min=4, max=25)])
    strike = FloatField('Strike')
    tenor = FloatField('Tenor')
    rate = FloatField('Risk Free Rate', [validators.Length(min=4, max=25)])
    volatility = FloatField('Volatility', [validators.Length(min=4, max=25)])
