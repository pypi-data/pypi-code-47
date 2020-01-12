import logging
from stevedore import driver

log = logging.getLogger()


def get_vault(config):
    """Construct a vault.

    This reads a config dict to determine how to create a vault.

    This will look for the "vault_type" key in the config, defaulting to 'fs-vault'. This indicates the name of the
    vault plugin to use.

    It will then look for the subdict with the same name as the vault type, defaulting to an empty dict if this is not
    found. This subconfig dict is passed to the plugin driver.

    Args: config: A config dict.

    Returns: A vault instance.
    """
    vault_plugin_name = config.get('vault_type', 'fs-vault')

    manager = driver.DriverManager(
        namespace='godkjenn.vault',
        name=vault_plugin_name,
        invoke_on_load=False,
        on_load_failure_callback=_log_extension_loading_failure,
    )

    vault_config = config.get('vault', {}).get(vault_plugin_name, {})

    return manager.driver(config, vault_config)


def _log_extension_loading_failure(_mgr, extension_point, err):
    # We have to log at the `error` level here as opposed to, say, `info`
    # because logging isn't configure when we reach here. We need this infor to
    # print with the default logging settings.
    log.error('Plugin load failure: extension-point="%s", err="%s"',
              extension_point, err)

