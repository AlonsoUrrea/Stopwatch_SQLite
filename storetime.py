from __future__ import annotations
import re


class Time:
    class WrongFormatError(Exception):
        pass
    #end class

    REGEX = "(?P<H>\d+):(?P<M>[0-5]\d):(?P<s>[0-5]\d)"
    MINUTES_PER_HOUR = 60
    SECONDS_PER_MINUTE = 60

    def __init__(self, hours:int=0, minutes:int=0, seconds:int=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    #end def

    def __add__(self, other: Time):
        new_time = Time()
        new_time.addSeconds(self.seconds() + other.seconds())
        new_time.addMinutes(self.minutes() + other.minutes())
        new_time.addHours(self.hours() + other.hours())

        return new_time
    #end def

    def secondsOverflow(self) -> bool: # check if seconds overflow
        return self.__seconds >= Time.SECONDS_PER_MINUTE
    def minutesOverflow(self) -> bool: # check if minutes overflow
        return self.__minutes >= Time.MINUTES_PER_HOUR
    #end def

    def addHours(self, hours: int):
        self.__hours += int(hours)
    #end def

    def addMinutes(self, minutes: int):
        self.__minutes += int(minutes)
        if self.minutesOverflow():
            total_minutes = self.__minutes
            self.__minutes = self.__minutes % Time.MINUTES_PER_HOUR
            total_minutes -= self.__minutes
            self.addHours(total_minutes / Time.MINUTES_PER_HOUR)
        #end if
    #end def

    def addSeconds(self, seconds: int):
        self.__seconds += int(seconds)
        if self.secondsOverflow():
            total_secs = self.__seconds
            self.__seconds = self.__seconds % Time.SECONDS_PER_MINUTE
            total_secs -= self.__seconds
            self.addMinutes(total_secs / Time.SECONDS_PER_MINUTE)
        #end if
    #end def

    def addSecond(self):
        self.addSeconds(1)
    #end def

    def addMinute(self):
        self.addMinutes(1)
    #end def

    def addHour(self):
        self.addHours(1)
    #end def

    def seconds(self) -> int:
        return self.__seconds
    def minutes(self) -> int:
        return self.__minutes
    def hours(self) -> int:
        return self.__hours
    #end def

    def totalSeconds(self) -> int:
        return self.seconds() + (
            self.minutes() + 
            (self.hours() * Time.MINUTES_PER_HOUR)
        ) * self.SECONDS_PER_MINUTE
    #end def

    def toSeconds(self) -> int:
        return self.totalSeconds()
    def toMinutes(self) -> float:
        return (
            self.hours() * Time.MINUTES_PER_HOUR +
            self.minutes() +
            self.seconds() / Time.SECONDS_PER_MINUTE
        )
    def toHours(self) -> float:
        return (
            self.hours() +
            (
                self.minutes() +
                self.seconds() / Time.SECONDS_PER_MINUTE
            ) / Time.MINUTES_PER_HOUR
        )
    #end def

    def reset(self):
        self.__seconds = 0
        self.__minutes = 0
        self.__hours = 0
    #end def

    def isReset(self):
        if self.seconds() == 0 and self.minutes() == 0 and self.hours() == 0:
            return True
        return False
    #end def

    def fromStr(self, string: str):
        re_comp = re.compile(Time.REGEX)
        try:
            match_ = re_comp.findall(string)[0]
            self.__hours = int(match_[re_comp.groupindex['H']-1])
            self.__minutes = int(match_[re_comp.groupindex['M']-1])
            self.__seconds = int(match_[re_comp.groupindex['s']-1])

            return self
        except IndexError:
            raise Time.WrongFormatError
        #end try
    #end def

    # STATIC
    def from_str(string: str):
        return Time().fromStr(string)
    def from_seconds(seconds: int):
        t = Time()
        t.addSeconds(seconds)

        return t
    #end def 

    def __str__(self) -> str:
        return "%s:%s:%s" %(
            str(self.hours()).zfill(2),
            str(self.minutes()).zfill(2),
            str(self.seconds()).zfill(2)
        )
    #end def
#end class
