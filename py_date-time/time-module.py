# -*- coding: utf-8 -*-
# Using Python 3.x

__author__ = "Anderson Morais"
__date__ = "1-jul-2021"
__version__ = ""
__status__ = ""

"""
TIME module
This module provides various time-related functions.
- The epoch is the point where the time starts, and is platform dependent. 
  For Unix, the epoch is January 1, 1970, 00:00:00 (UTC). 
  To find out what the epoch is on a given platform, look at time.gmtime(0).
- The functions in this module may not handle dates and times before the epoch or far in the future. 
  The cut-off point in the future is determined by the C library; for 32-bit systems, it is typically in 2038.
- Function strptime() can parse 2-digit years when given %y format code. When 2-digit years are parsed, 
  they are converted according to the POSIX and ISO C standards: values 69–99 are mapped to 1969–1999, 
  and values 0–68 are mapped to 2000–2068.
"""

import time


"""
Clock id CONSTANTS:
time.CLOCK_BOOTTIME
time.CLOCK_HIGHRES
time.CLOCK_MONOTONIC
time.CLOCK_MONOTONIC_RAW
time.CLOCK_PROCESS_CPUTIME_ID
time.CLOCK_PROF
time.CLOCK_TAI
time.CLOCK_THREAD_CPUTIME_ID
time.CLOCK_UPTIME
time.CLOCK_UPTIME_RAW
time.CLOCK_REALTIME
Timezone CONSTANTS:
time.altzone
time.daylight
time.timezone
time.tzname
"""

print(time.CLOCK_BOOTTIME)
print(time.timezone)
print(time.tzname)

""" FUNCTIONS: """
"""
time.asctime([t])
    Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() 
    to a string of the following form: 'Sun Jun 20 23:21:05 1993'.

"""
loctime = time.localtime()
# output: Thu Jul  1 13:26:33 2021
print(time.asctime(loctime))
"""
tuple = (
    year(4 digits), 
    month(1-12), 
    day(1-31), 
    hour(0-23), 
    minute(0-59), 
    second(0-59), 
    day of week(0-6 - Monday to Sunday),
    day of year(1-366),
    DST(-1,0,1)
)
"""
my_tuple_time = (2000, 12, 8, 10, 33, 55, 4, 189, 0)
loctime1 = time.asctime(my_tuple_time)
# output: Fri Dec  8 10:33:55 2000
print(loctime1)

"""
time.ctime([secs])¶
    Convert a time expressed in seconds since the epoch to a string of a form: 
    'Sun Jun 20 23:21:05 1993' representing local time.
"""
sec_time = time.ctime(123456789)
# output: Thu Nov 29 18:33:09 1973
print(sec_time)

"""
time.gmtime([secs])
    Convert a time expressed in seconds since the epoch to a struct_time in UTC in which the dst flag is always zero. 
    If secs is not provided or None, the current time as returned by time() is used. Fractions of a second are ignored.
time.localtime([secs])
    Like gmtime() but converts to local time. If secs is not provided or None, the current time as returned by time() is used. 
    The dst flag is set to 1 when DST applies to the given time.
class time.struct_time
    The type of the time value sequence returned by gmtime(), localtime(), and strptime(). 
    It is an object with a named tuple interface: values can be accessed by index and by attribute name. 
"""
# output: time.struct_time(tm_year=1973, tm_mon=11, tm_mday=29, tm_hour=18, tm_min=33, tm_sec=9, tm_wday=3, tm_yday=333, tm_isdst=0)
loctime = time.localtime(123456789)
print(loctime)
# output: 18
print(loctime.tm_hour)
# output: 333
print(loctime.tm_yday)

"""
time.sleep(secs)
    Suspend execution of the calling thread for the given number of seconds. 
    The argument may be a floating point number to indicate a more precise sleep time.
"""
time.sleep(2.6)
# wait for 2.6 seconds
print('awaken')

"""
time.strftime(format[, t])
    Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument.
"""
loctime = time.strftime('%Z %X')
# output: -03 14:00:36
print(loctime)

"""
time.time() → float
    Return the time in seconds since the epoch as a floating point number. 
"""
# output: 1625159068.184007
print(time.time())
