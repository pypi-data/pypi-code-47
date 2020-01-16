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
    instant_string: relativedelta(seconds=+1),
    daily_string: relativedelta(days=+1),
    weekly_string: relativedelta(weeks=+7),
    monthly_string: relativedelta(months=+1),
    quarterly_string: relativedelta(months=+3),
    annually_string: relativedelta(years=+1),
}

frequencies = [k for k in frequency_to_delta]
