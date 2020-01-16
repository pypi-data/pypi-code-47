import pprint as pp
from loguru import logger as log
import sys
log.remove()
log.add(sys.stdout, level='INFO')
pprint = pp.pprint

leaf = None

def entry_descent(config, path, funcs, leaf=leaf):
    log.info(f'Config: {pp.pformat(config)}')
    log.info(f'Path {path}')
    descent(config, path, funcs, leaf=leaf)

def entry_traverse(config, path, funcs, leaf=leaf):
    log.info(f'Config: {pp.pformat(config)}')
    log.info(f'Path {path}')
    traverse(config, path, funcs, leaf=leaf)


# One way
def descent(config, path, funcs, leaf=leaf):
    log.info(f'Current path: {path}')
    fname = path.pop(0)
    config.update(config.get(fname, {}))
    f = funcs.get(fname)
    if isinstance(f, dict):
        funcs.update(f)
        descent(config, path, funcs)

    config[fname] = '<<Entered deleted>>'
    del config[fname]
    leaf(funcs[fname], config)
    if len(path):
        descent(config, path, funcs)

## Another way
def traverse(config, path, funcs, leaf=leaf):
    while len(path) > 0:
        this_config = config.copy()
        this_funcs = funcs.copy()

        log.info(f'Current path: {path}')
        fname = path[0]
        this_config.update(config.get(fname, {}))

        f = this_funcs.get(fname)
        if f is None: break

        path.pop(0)
        if isinstance(f, dict):
            traverse(this_config, path, this_funcs[fname], leaf=leaf)

        leaf(f, this_config)
        traverse(this_config, path, this_funcs, leaf=leaf)

        log.info(f'Renurned traverse, path: {path}')


from traverse_invoke import leaves
leaf = leaves.kwarg
