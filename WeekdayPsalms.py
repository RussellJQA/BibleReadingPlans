"""
Create a Bible reading plan with readings from the Psalms for each weekday.
"""

import calendar
import datetime
import os

from bible_books import bible_books
from rmm_psalm_readings import rmm_modified_260_psalm_readings
from create_bible_plan import (
    create_plan_with_playlists,
    get_weekday_delta,
    process_reading,
)

bible_books_list = list(bible_books.keys())


def WeekdayPsalms(daily_readings, year):  # Weekday Worship (Psalms)

    date = datetime.datetime(year, 1, 1)  # January 1
    while date.strftime("%a") in ("Sat", "Sun"):
        date += datetime.timedelta(days=1)  # Increment until first weekday

    # TODO: Add needed extra readings.
    #       For years other than 2020, the readings themselves may need to be adjusted.
    # extra_readings = 0
    # if (get_weekday(datetime.datetime(year, 12, 31)) not in ('Sat', 'Sun')):
    #     extra_readings += 1  # Increment if December 31 is a weekday
    # if (calendar.isleap(year) and
    #     (get_weekday(datetime.datetime(year, 12, 30)) not in ('Sat', 'Sun'))):
    #     extra_readings += 1  # Increment if leap year & December 30 is a weekday
    # print(f'For {year}, {extra_readings} extra WeekdayPsalms() readings are needed.')

    for count, psalm_ref in enumerate(rmm_modified_260_psalm_readings):
        datedelta = get_weekday_delta(date)
        (daily_readings, date) = process_reading(
            daily_readings, date, "Psa", psalm_ref, datedelta
        )

    return daily_readings


def main():
    daily_readings = {}
    YEAR = 2020
    WeekdayPsalms(daily_readings, YEAR)
    # for cal_date, full_refs in sorted(daily_readings.items()):
    #     print(cal_date, full_refs)  # Useful for debugging
    create_plan_with_playlists("WeekdayPsalms", daily_readings)


if __name__ == "__main__":
    main()
