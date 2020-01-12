"""Simple file-system based implementation of a vault.
"""

from itertools import chain
from enum import Enum
from pathlib import Path


class FSVault:
    """File-system implementation of a vault.

    This just keeps accepted data in files with the "accepted" suffix and received data in files suffixed with
    "received". Id's in this vault are simply paths.

    This assumes it has complete control over the files under `root_directory`.

    Args:
        root_path: The root directory under which this will store received and accepted data.
    """

    def __init__(self, root_path: Path):
        self._root_path = root_path

    @property
    def root_path(self):
        "Root path of the vault."
        return self._root_path

    def accepted(self, test_id):
        """Get the current accepted value for `test_id`.

        Args:
            test_id: ID of the test.

        Returns: A bytes object with the accepted data for the test.

        Raises:
            KeyError: `test_id` does not have accepted data in the vault.
        """
        return self._get(test_id, _Kind.accepted)

    def accept(self, test_id):
        """Accept the current received data for `test_id`.

        Args:
            test_id: The ID of the test to accept.

        Raises:
            KeyError: There is no received data for `test_id`.
        """
        data = self.received(test_id)

        self._put(test_id, _Kind.accepted, data)

        p = self._full_path(test_id, _Kind.received)
        if p.exists():
            p.unlink()

    def received(self, test_id):
        """Get the current received value for `test_id`.

        Args:
            test_id: ID of test.

        Returns: A bytes object containing the received data `test_id`.

        Raises:
            KeyError: There is no received data for `test_id`.
        """
        return self._get(test_id, _Kind.received)

    def receive(self, test_id, value):
        """Set new received data for a test.

        Args:
            test_id: ID of the test for which to receive data.
            value: Bytes object containing received data for the test.
        """
        self._put(test_id, _Kind.received, value)

    def ids(self):
        """Get all IDs in the vault.

        This is all IDs that have either or both of accepted and received data. There is no
        order to the results. Each ID is included only once in the output, even if it has both
        received and accepted data.

        Returns: An iterable of all test IDs.
        """
        def path_to_id(path, kind):
            rel = path.relative_to(self._root_path)
            suffix_length = len(".{}".format(kind.value))
            return str(rel)[:-1 * suffix_length]

        all_ids = (
            (path_to_id(path, kind)
             for path in self._root_path.glob('**/*.{}'.format(kind.value)))
            for kind in _Kind
        )

        return set(chain(*all_ids))

    def _full_path(self, path, kind):
        return self._root_path / '{}.{}'.format(path, kind.value)

    def _get(self, path, kind):
        full_path = self._full_path(path, kind)

        if not full_path.exists():
            raise KeyError('no {} data: {}'.format(kind.value, path))

        with full_path.open(mode='rb') as handle:
            return handle.read()

    def _put(self, path, kind, value):
        full_path = self._full_path(path, kind)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with full_path.open(mode='wb') as handle:
            handle.write(value)


class _Kind(Enum):
    accepted = 'accepted'
    received = 'received'


def plugin(full_config, plugin_config):
    """Vault plugin for FSVault.

    Args:
        full_config: The full godkjenn config dict.
        plugin_config: The sub-config for the plugin.

    Returns: A new FSVault instance.
    """
    # TODO: We should give users a config option for changing .godkjenn to something else.
    return FSVault(root_path=Path(full_config['root_dir']) / '.godkjenn')
