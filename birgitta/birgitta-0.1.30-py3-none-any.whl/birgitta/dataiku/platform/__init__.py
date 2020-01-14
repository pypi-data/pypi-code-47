"""The dataiku platform module. Has is_current_platform() returning true
if we are on dataiku().
"""

__all__ = ['is_current_platform']


def is_current_platform():
    # import dataiku
    # if (
    #         ('default_project_key' in dir(dataiku)) or
    #         ('dss_settings' in dir(dataiku))
    # ):
    #     return True
    try:
        import dataiku
        # Ensure we have the actual dataiku module and not a mock.
        # We check to different members for better robustness, in case
        # one of them is removed by DSS.
        # if (
        #         ('default_project_key' in dir(dataiku)) or
        #         ('dss_settings' in dir(dataiku))
        # ):
        #     return True
        try:
            # Ensure we have the actual dataiku module and not a mock.
            # We check to different members for better robustness, in case
            # one of them is removed by DSS.
            if (
                    ('default_project_key' in dir(dataiku)) or
                    ('dss_settings' in dir(dataiku))
            ):
                return True
            else:
                return False
        except AttributeError:
            return False
    except ModuleNotFoundError:
        return False
