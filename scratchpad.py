
import numpy as np


def get_pik_value(k, x):
    """
    This method is used by the random_excursions method to get expected probabilities
    """
    if k == 0:
        out = 1 - 1.0 / (2 * np.abs(x))
    elif k >= 5:
        out = (1.0 / (2 * np.abs(x))) * (1 - 1.0 / (2 * np.abs(x))) ** 4
    else:
        out = (1.0 / (4 * x * x)) * (1 - 1.0 / (2 * np.abs(x))) ** (k - 1)
    return out

def get_probs_for_random_excursion(k, x):
    if k == 0:
        return 1 - (1/(2*abs(x)))
    elif k >= 5:

        return (1/(2*abs(x)))*(1-(1/(2*abs(x))))**4
    else:
        return (1/(4*(x**2)))*(1-(1/(2*abs(x))))**(k-1)
    

print(get_probs_for_random_excursion(1, 1))
print(get_pik_value(1, 1))