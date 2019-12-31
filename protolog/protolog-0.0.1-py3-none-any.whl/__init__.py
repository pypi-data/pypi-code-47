import logging.config
import click
from protolog import udp
import colorama


@click.group()
def cli():
    """
    CLI to run simple protocol loggers by Palmlund Wahlgren Innovative Technology AB
    """
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {},
            "formatters": {
                "main_formatter": {
                    "format": (
                        colorama.Fore.CYAN
                        + "[{asctime}] "
                        + colorama.Style.RESET_ALL
                        + ":: {message} :: "
                        + colorama.Fore.BLUE
                        + "{host}:{port}"
                        + colorama.Style.RESET_ALL
                        + " :: "
                        + colorama.Fore.YELLOW
                        + "{data}"
                        + colorama.Style.RESET_ALL
                    ),
                    "style": "{",
                }
            },
            "handlers": {
                "console": {
                    "level": "DEBUG",
                    "filters": [],
                    "class": "logging.StreamHandler",
                    "formatter": "main_formatter",
                }
            },
            "loggers": {"": {"handlers": ["console"], "level": "DEBUG"}},
        }
    )


if __name__ == "__main__":
    cli()


cli.add_command(udp.udp)
