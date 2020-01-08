import click
from .context_state import CliContextState


def quite_mode_option(func):
    def callback(ctx, _, value):
        state = ctx.ensure_object(CliContextState)
        state.quite_mode = value
        return value
    return click.option('-q', '--quite', default=False, is_flag=True, required=False, help='Run in quite mode.',
                        expose_value=False, callback=callback)(func)


def common_options(func):
    func = quite_mode_option(func)
    return func
