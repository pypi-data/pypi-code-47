from ..cobra.simulation import FBA, ROOM
from ..cobra.variability import FVA
from .GPRtransform import gpr_transform
from math import inf


def GeneSwitch(model, target, transformed=False, reference=None, constraints=None,
               production=0.5, delta=0.1, epsilon=0.1, solutions=1, use_pool=False):
    """GeneSwitch gives minimal number of genes for which the respective enzymes need to undergo flux change
        to make phenotype switch form growth optimised to producing optimised.
        This is an adaptation of the ROOM algorithm using the GPR transformation approach (Machado et al, 2016).

    Author: Daniel Machado, Astrid Stubbusch (Original method: Paula Jouhten)

    Arguments:
        model (CBModel): a constraint-based model
        target (str): target reaction id
        transformed (booL): model is already GPR-transformed (default: False)
        reference (dict): reference flux distribution (optional)
        constraints (dict): environmental or additional constraints (optional)
        production (float): minimum fraction of maximum target production rate (default: 0.5)
        delta (float): relative tolerance (default: 0.1)
        epsilon (float): absolute tolerance (default: 0.1)
        solutions (int): number of solutions to compute (default: 1)
        use_pool (bool) use solver solution pool (default: False)

    Returns:
        dict, dict: significantly up / down regulated genes and respective ratios
    """

    mut_sol = FBA(model, objective={target: 1})
    v_max = mut_sol.values[target]
    switch = {target: (production * v_max, v_max)}

    if constraints is None:
        constraints = {}

    constraints.update(switch)

    if not transformed:
        model = gpr_transform(model, inplace=False)

    if not reference:
        reference = FVA(model, obj_frac=0.9, reactions=model.u_reactions)

    constraints = model.convert_constraints(constraints)

    sols = ROOM(model, reference=reference, constraints=constraints, reactions=model.u_reactions,
                delta=delta, epsilon=epsilon, solutions=solutions, use_pool=use_pool)

    if solutions == 1:
        sols = [sols]

    switches = []

    for sol in sols:

        up = {}
        down = {}

        for g_id in model.genes:
            if 'y_u_' + g_id[2:] not in sol.values:
                continue

            y_val = sol.values['y_u_' + g_id[2:]]
            u_mut = sol.values['u_' + g_id[2:]]
            u_wt_lb = reference['u_' + g_id[2:]][0]
            u_wt_ub = reference['u_' + g_id[2:]][1]

            if y_val > 0.5:
                if u_mut > u_wt_ub + epsilon:
                    up[g_id] = u_mut / u_wt_ub if u_wt_ub > 0 else inf
                elif u_mut < u_wt_lb - epsilon:
                    try:
                        down[g_id] = u_mut / u_wt_lb
                    except:
                        print(u_mut, u_wt_lb)

        switches.append((up, down))

    return switches, sols



