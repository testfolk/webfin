from wtforms import FloatField, SelectField, Form, validators


class OptionForm(Form):
    spot = FloatField('Spot', [validators.Length(min=3, max=25)])
    strike = FloatField('Strike', [validators.Length(min=3, max=25)])
    tenor = SelectField('Tenor', choices=[(0.083333, "1m"), (0.25, "3m"), (0.5, "6m"), (1.0, "1y"), (5.0, "5y")], coerce=float)
    rate = FloatField('Risk Free Rate', [validators.Length(min=3, max=25)])
    volatility = FloatField('Volatility', [validators.Length(min=3, max=25)])
    premium = FloatField('Premium')
    solveFor = SelectField('Solve For', choices=[('Premium', 'Premium'), ('Volatility', 'Volatility')])

    def validateSolveFor(self, extra_validators=None):
        if self.solveFor.data == 'Volatility':
            return self.valid_solve_for_vol()
        else:
            return self.valid_solve_for_premium()

    def valid_solve_for_premium(self):
        return True

    def valid_solve_for_vol(self):
        premium_val = self.premium.data
        if premium_val is None or premium_val == 0.0:
            self.form_errors.append("Solve for Impl Vol must have a valid Premium")
            return False
        else:
            return True
