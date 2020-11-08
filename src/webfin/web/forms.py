from wtforms import Form, BooleanField, StringField, IntegerField, DateTimeField , RadioField,FloatField,SelectField,validators

class EvalForm(Form):
    spot     = StringField('Spot', [validators.Length(min=4, max=25)])
    strike = FloatField('Strike')
    tenor = SelectField('Tenor', choices=[('1M','1m'),('3m','3m'),('6m','6m'), ('1y','1y')])
    riskFreeRate = StringField('Risk Free Rate', [validators.Length(min=4, max=25)])
    callPut = SelectField('C/P', choices=[('Call','Call'),('Put','Put')])
    volatility = StringField('Volatility', [validators.Length(min=4, max=25)])
    premium = StringField('Premium', [validators.Length(min=4, max=25)])
    solveFor = RadioField(label="Solve For", choices = ["Premium", "Volatility"])








