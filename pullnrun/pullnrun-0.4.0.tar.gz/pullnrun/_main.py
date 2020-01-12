from ._utils import as_list, validate_dict
from ._log import Log

from ._pull import pull
from ._push import push
from ._run import run

FUNCTION_MAPPINGS = {
    'pull': pull,
    'run': run,
    'push': push,
}

def main(input_dict, quiet=False):
    validate_dict(input_dict, 'input')

    log_targets = input_dict.get('log')
    log = Log(quiet, log_targets)
    log.start()

    success, error = (0, 0, )

    for stage, function in FUNCTION_MAPPINGS.items():
        for action in as_list(input_dict.get(stage)):
            ok = function(log=log, id=log.id, **action)
            if ok:
                success += 1
            else:
                error += 1

    log.end(success, error)
    return (success, error, )
