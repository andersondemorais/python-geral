# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "30-jun-2021"
__version__ = ""
__status__ = ""

"""
DATETIME module
The datetime module supplies classes for manipulating dates and times.
While date and time arithmetic is supported, the focus of the implementation 
is on efficient attribute extraction for output formatting and manipulation.
Other: 
- Module calendar: General calendar related functions.
- Module time: Time access and conversions.
- Package dateutil: Third-party library with expanded time zone and parsing support.
"""

import datetime
from contextlib import suppress

""" 
CONSTANTS:
datetime.MINYEAR
datetime.MAXYEAR
"""
# output: Max year: 9999 - Min year: 1
print(f'Max year: {datetime.MAXYEAR} - Min year: {datetime.MINYEAR}')

""" TYPES """

"""
class datetime.date
    An idealized naive date, assuming the current Gregorian calendar always was, and always will be, in effect. 
    Attributes: year, month, and day.
"""
tday = datetime.date.today()
nou = datetime.datetime.now()
bck_td_fut = datetime.date(2015, 10, 21)
dt_from_timestamp = datetime.date.fromtimestamp(1234567890)

# output: Today: 2021-06-30
print(f'Today: {tday}')
# output: Today year: 2021
print(f'Today year: {tday.year}')
# output: Today month: 6
print(f'Today month: {tday.month}')
# output: Today day: 30
print(f'Today day: {tday.day}')
#
print(f'Now: {nou}')
# output: Bck to d fut: 2015-10-21
print(f'Bck to d fut: {bck_td_fut}')
# output: Date from timestamp: 2009-02-13
print(f'Date from timestamp: {dt_from_timestamp}')

# formatting datetime with strftime()
""" 
%d, %m - day and month: 01, 02, 03, ..., 31
%-d, %-m - day and month: 1, 2, 3, ..., 31)
%y: year - 2 digits
%Y: year - 4 digits
%a: week day(Mon, Tue, Wed, ...)
%A: week day(Monday, Tuesday, Wednesday, ...)
%b: month(Jan, Feb, May, ...)
%B: month(January, Feruary, May, ...)
"""
# output: 06/30/21
print(tday.strftime('%D'))
# output: 21/Jun/30
print(tday.strftime('%y/%b/%d'))
# output: Wednesday 21/Jun/30
print(tday.strftime('%A %y/%b/%d'))

"""
class datetime.time
    An idealized time, independent of any particular day, assuming that every day has exactly 24*60*60 seconds. 
    (There is no notion of “leap seconds” here.) 
    Attributes: hour, minute, second, microsecond, and tzinfo.
"""
# time(hour = 0, minute = 0, second = 0)
# output: 00:00:00
print(datetime.time.min)
# output: 23:59:59.999999
print(datetime.time.max)
# output: 0:00:00.000001
print(datetime.time.resolution)
# output: <attribute 'hour' of 'datetime.time' objects>
print(datetime.time.hour)
# output: <attribute 'minute' of 'datetime.time' objects>
print(datetime.time.minute)
# output: <attribute 'second' of 'datetime.time' objects>
print(datetime.time.second)

my_time = datetime.time(19, 33, 57)
# output: 19:33:57
print(my_time)

# ERROR! attribute 'hour' of 'datetime.time' objects is not writable
with suppress(AttributeError):
    my_time.hour = 10

my_time = my_time.replace(hour=10)
# output: 10:33:57
print(my_time)

my_time1 = datetime.time(2, 42, 59, 1036)
# output: 02:42:59.001036
print(my_time1)


"""
class datetime.datetime
    A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.
"""
# datetime(year, month, day, hour, minute, second, microsecond)
my_datetime = datetime.datetime(2020, 4, 15)
# output: 2020-04-15 00:00:00
print(my_datetime)

# difference between datetimes
my_datetime1 = datetime.datetime(1990, 12, 4)
# output: 10725 days, 0:00:00
print(my_datetime - my_datetime1)

# convert string to datetime
date_str = '01/07/2021'
date_str_datetime = datetime.datetime.strptime(date_str, '%d/%m/%Y')
print(date_str_datetime)


"""
class datetime.timedelta
    A duration expressing the difference between two date, time, or datetime instances to microsecond resolution.
"""
my_timedelta = datetime.timedelta(days=10, hours=3, minutes=29)
my_timedelta1 = datetime.timedelta(days=2, hours=12, minutes=38)

# difference between timedelta
# output: 7 days, 14:51:00
print(my_timedelta - my_timedelta1)
# output: 876540.0
print(my_timedelta.total_seconds())
# add time
my_datetime_fut = nou + my_timedelta
# output: 2021-07-12 23:43:10.092091
print(my_datetime_fut)
my_datetime_past = nou - my_timedelta
# output: 2021-06-22 16:45:10.092091
print(my_datetime_past)

"""
class datetime.tzinfo
    An abstract base class for time zone information objects. 
    These are used by the datetime and time classes to provide a customizable notion of time adjustment 
    (for example, to account for time zone and/or daylight saving time).
class datetime.timezone
    A class that implements the tzinfo abstract base class as a fixed offset from the UTC.
"""
my_timezone = datetime.timezone(datetime.timedelta(hours=-3, minutes=-30))
# output: UTC-03:30
print(my_timezone)

my_datetime_timezone = datetime.datetime.now().astimezone(my_timezone)
# output: ...-03:30
print(my_datetime_timezone)
