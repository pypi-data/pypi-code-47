import warnings


class ReducedDimensionalityWarning(Warning):
    pass


def warn_reduced_dim_after_setting_attr():
    warnings.warn('Setting attribute reduces the dimensionality of the shape.',
                  ReducedDimensionalityWarning,
                  stacklevel=2)
