class Time:
    def __init__(self, hours:int=0, minutes:int=0, seconds:int=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
    #end def

    def addSecond(self):
        self.__seconds += 1
        if self.__seconds >= 60:
            self.__seconds = 0
            self.addMinute()
        #end if
    #end def

    def addMinute(self):
        self.__minutes += 1
        if self.__minutes >= 60:
            self.__minutes = 0
            self.addHour()
        #end if
    #end def

    def addHour(self):
        self.__hours += 1
    #end def

    def seconds(self) -> int:
        return self.__seconds
    def minutes(self) -> int:
        return self.__minutes
    def hours(self) -> int:
        return self.__hours
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

    def __str__(self) -> str:
        return "%s:%s:%s" %(
            str(self.hours()).zfill(2),
            str(self.minutes()).zfill(2),
            str(self.seconds()).zfill(2)
        )
    #end def
#end class