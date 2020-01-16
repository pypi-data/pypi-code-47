# metadata fields
from datetime import timedelta

from dateutil.relativedelta import relativedelta

id_string = "id"
calculated_string = "calculated"
frequency_string = "frequency"
min_value_string = "minValue"
max_value_string = "maxValue"
start_time_string = "startTime"
is_integer_string = "isInteger"
delay_string = "delay"

# frequencies
instant_string = "instant"
daily_string = "daily"
weekly_string = "weekly"
monthly_string = "monthly"
quarterly_string = "quarterly"
annually_string = "annually"

frequency_to_delta = {
    instant_string: timedelta(seconds=+1),
    daily_string: timedelta(days=+1),
    weekly_string: timedelta(weeks=+7),
    monthly_string: timedelta(months=+1),
    quarterly_string: timedelta(months=+3),
    annually_string: timedelta(years=+1),
}

frequencies = [k for k in frequency_to_delta]
