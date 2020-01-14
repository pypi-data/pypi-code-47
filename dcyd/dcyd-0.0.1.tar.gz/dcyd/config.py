import json
import os
import requests
import sys

import dcyd.utils.constants as constants

def main(account_name=None):
    """Calls the account service to get credentials."""

    # main() needs to take no args, so that it functions as an entry point.
    if account_name is None:
        account_name = sys.argv[1:]

    # Call the account service.
    r = requests.post(
        os.path.join(constants.BASE_URL, constants.KEY_ROUTE),
        data={'name': account_name}
    )

    # Save the key.
    with open(constants.KEY_FILENAME, 'w') as f:
        json.dump(r.json(), f)


if __name__ == '__main__':
    main()
