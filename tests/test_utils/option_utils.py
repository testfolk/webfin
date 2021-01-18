import copy


def clone_with(orig, mutations):
    cloned = copy.deepcopy(valid_solve_for_premium_data())
    cloned.update(mutations)
    return cloned


def valid_solve_for_premium_data():
    return {
        'spot': '1.3',
        'strike': '1.39',
        'tenor': '0.5',
        'rate': '0.5005',
        'volatility': '0.398',
        'solveFor': 'Premium'
    }


def valid_solve_for_vol_data():
    return clone_with(valid_solve_for_premium_data(), {
        'solveFor': 'Volatility',
        'premium': '1.334'
    })


def solve_for_vol_with_zero_premium():
    return clone_with(valid_solve_for_premium_data(), {'solveFor': 'Volatility', 'premium': '0.00'})
