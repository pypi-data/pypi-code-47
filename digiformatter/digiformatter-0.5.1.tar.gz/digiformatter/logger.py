from digiformatter import styles

__all__ = ["trace", "debug", "info", "warn", "error", "log"]

styles.create("trace", fg="grey_27")
styles.create("debug", fg="blue")
styles.create("info", fg="cyan_1")
styles.create("warn", fg="yellow")
styles.create("error", fg="red", attr="bold")


def trace(message, **kwargs):
    log(message, level="trace", **kwargs)


def debug(message, **kwargs):
    log(message, level="debug", **kwargs)


def info(message, **kwargs):
    log(message, level="info", **kwargs)


def warn(message, **kwargs):
    log(message, level="warn", **kwargs)


def error(message, **kwargs):
    log(message, level="error", **kwargs)


def log(message, level="info", showtime=True):
    styles.print(message, style=level, showtime=showtime)
