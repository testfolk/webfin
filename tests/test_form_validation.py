import test_utils.option_utils as optutil
import webfin.web.forms as forms
import multidict


async def test_optcalc_solve_for_vol_with_zero_premium():
    data = multidict.MultiDict(optutil.solve_for_vol_with_zero_premium())
    form = forms.OptionForm(data)
    validation_result = form.validateSolveFor()
    # assert validation_result is False
    assert validation_result is False
    assert len(form.form_errors) == 1
    assert form.form_errors[0] == 'Solve for Impl Vol must have a valid Premium'
