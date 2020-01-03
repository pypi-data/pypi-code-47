from .modwt import modwt_level_nd, imodwt_level_nd


def mra(data, levels, axes):
    a_key = 'a' * len(axes)  # Approximation coefficient key
    approx_coeff = data
    detail_coeffs = []
    for level in range(levels):
        coeff = modwt_level_nd(approx_coeff, level, axes)
        approx_coeff = coeff.pop(a_key)
        detail_coeffs.append(coeff)
    return approx_coeff, detail_coeffs


def imra(approx_coeff, detail_coeffs, axes):
    a_key = 'a' * len(axes)  # Approximation coefficient key
    for level, coeff in reversed(list(enumerate(detail_coeffs))):
        coeff[a_key] = approx_coeff
        approx_coeff = imodwt_level_nd(coeff, level, axes)
    return approx_coeff
