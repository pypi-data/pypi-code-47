"""
"""

import datetime

import click
import tabulate

from . import classes


@click.command()
@click.option(
    "-t", "--time",
    type=click.DateTime(["%H:%M", "%Y-%m-%d %H:%M"]),
    default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
)
@click.option(
    "-f", "--format",
    type=click.Choice(tabulate.tabulate_formats),
    default="plain",
)
@click.option(
    "-s", "--simple",
    is_flag=True,
    default=False,
)
def main(time, format, simple):
    fifteen_minutes = datetime.timedelta(minutes=15)
    classes_now = classes.get_classes(time)

    if not classes_now:
        classes_now = classes.get_classes(time + fifteen_minutes)

    table_data = [[c.start_time(), c.end_time(), c.group] for c in classes_now]
    table_headers = ["Start Time", "End Time", "Meets On"]

    if simple:
        if not classes_now:
            print("")
        else:
            print(classes_now[0].end_time())
    else:
        if classes_now:
            print("Times for classes currently in session")
            table = tabulate.tabulate(
                table_data,
                headers=table_headers,
                tablefmt=format
            )
            print(table)
        else:
            print("No classes are currently in session")


if __name__ == '__main__':
    main()
