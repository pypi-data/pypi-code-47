"""
Data about a particular class time.
"""

import datetime


class Class(object):
    def __init__(self, start, length, group):
        if isinstance(start, datetime.datetime):
            self.start = start
        if isinstance(start, str):
            self.start = datetime.datetime.strptime(start, "%H:%M")

        self.end = self.start + length
        self.group = group

    def __lt__(self, other):
        return self.start.time() < other.start.time()

    def __gt__(self, other):
        return self.start.time() > other.start.time()

    def __eq__(self, other):
        return self.start.time() == other.start.time() and self.end.time() == other.end.time()

    def __repr__(self):
        return f"<Class {self.start.time()} - {self.end.time()}>"

    def __str__(self):
        return f"{self.start.time()} to {self.end.time()}"

    def in_range(self, time):
        return self.start.time() <= time.time() <= self.end.time()

    def start_time(self):
        return self.start.strftime("%H:%M")

    def end_time(self):
        return self.end.strftime("%H:%M")


SHORT_CLASS = datetime.timedelta(minutes=50)
LONG_CLASS = datetime.timedelta(minutes=75)

DATE_TO_SCHEDULE = {
    6: ["SaSu"],
    0: ["MWF", "MW/WF/MF"],
    1: ["TuTh"],
    2: ["MWF", "MW/WF/MF"],
    3: ["TuTh"],
    4: ["MWF"],
    5: ["SaSu"],
}

START_END_TIMES = {
    "SaSu": [],
    "MWF": [
        Class("08:00", SHORT_CLASS, "MWF"),
        Class("09:05", SHORT_CLASS, "MWF"),
        Class("10:10", SHORT_CLASS, "MWF"),
        Class("11:15", SHORT_CLASS, "MWF"),
        Class("12:20", SHORT_CLASS, "MWF"),
        Class("13:25", SHORT_CLASS, "MWF"),
        Class("14:30", SHORT_CLASS, "MWF"),
        Class("15:35", SHORT_CLASS, "MWF"),
        Class("16:40", SHORT_CLASS, "MWF"),
        Class("17:45", SHORT_CLASS, "MWF"),
        Class("18:50", SHORT_CLASS, "MWF"),
    ],
    "MW/WF/MF": [
        Class("07:35", LONG_CLASS, "MW/WF/MF"),
        Class("08:40", LONG_CLASS, "MW/WF/MF"),
        Class("14:30", LONG_CLASS, "MW/WF/MF"),
        Class("16:00", LONG_CLASS, "MW/WF/MF"),
        Class("17:30", LONG_CLASS, "MW/WF/MF"),
        Class("19:00", LONG_CLASS, "MW/WF/MF"),
    ],
    "TuTh": [
        Class("08:00", LONG_CLASS, "TuTh"),
        Class("09:30", LONG_CLASS, "TuTh"),
        Class("11:00", LONG_CLASS, "TuTh"),
        Class("12:30", LONG_CLASS, "TuTh"),
        Class("14:00", LONG_CLASS, "TuTh"),
        Class("15:30", LONG_CLASS, "TuTh"),
        Class("17:00", LONG_CLASS, "TuTh"),
        Class("18:30", LONG_CLASS, "TuTh"),
    ]
}


def get_classes(time):
    today = time.weekday()
    today_classes = [];

    for day in DATE_TO_SCHEDULE[today]:
        today_classes += START_END_TIMES[day]

    classes = []
    for class_time in today_classes:
        if class_time.in_range(time):
            classes.append(class_time)

    return sorted(classes)
