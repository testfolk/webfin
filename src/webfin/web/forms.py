from wtforms import FloatField, SelectField, Form, validators


class OptionForm(Form):
    spot = FloatField('Spot', [validators.Length(min=4, max=25)])
    strike = FloatField('Strike')
    tenor = SelectField('Tenor', choices=[(0.083333, "1m"), (0.25, "3m"), (0.5, "6m")], coerce=float)
    rate = FloatField('Risk Free Rate', [validators.Length(min=4, max=25)])
    volatility = FloatField('Volatility', [validators.Length(min=4, max=25)])
    premium = FloatField('Premium', [validators.Length(min=4, max=25)])
    solveFor = SelectField('Solve For', choices=[('Premium', 'Premium'), ('Volatility', 'Volatility')])
