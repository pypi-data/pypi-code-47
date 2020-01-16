
from math import floor, ceil

HVal=2.0

def _normalize_vals(vals):
    if len(vals) > 5: return ''
    vals = [float(i) for i in vals]
    mn = float(min(vals))
    norm_vals = [ v-mn for v in vals ]
    starter = norm_vals[0]
    for i in range(5-len(norm_vals)):
        norm_vals.insert(0, starter)
    mx = float(max(norm_vals))
    return mx, norm_vals


def chartmoji(vals):
    mx,norm_vals = _normalize_vals(vals)
    return ":chart_ln{}:".format("".join(
        [str(int(round( (float(v)/mx) * HVal ))) for v in norm_vals ]
    ))


def barmoji(vals):
    mx,norm_vals = _normalize_vals(vals)
    return ":chart_bar{}:".format("".join(
        [str(int(round( (float(v)/mx) * HVal ))) for v in norm_vals ]
    ))


