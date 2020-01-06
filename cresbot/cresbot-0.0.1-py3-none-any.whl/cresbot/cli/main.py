#

"""
"""


@click.group("cresbot")
def main():
    """Tools for interacting with the RuneScape Wiki.
	"""


@main.command("hiscore-counts")
def hiscore_counts():
    """Update the hiscore counts module on RuneScape Wiki.
	"""


@main.command("exchange-migrate")
def exchange_migrate():
    """
	"""
