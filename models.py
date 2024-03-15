from sqlitemodel import Database, Model
import datetime
import time
from storetime import Time

Database.DB_FILE = 'working_hours.db'

class SqLiteConvertions:
    class Booleans: #(Enum):
        TRUE = 1
        FALSE = 0
    #end class

    class WrongDateFormatError(Exception):
        def __init__(self, format):
            self.message = "Incorret format %s for date" %format
            super().__init__(self.message)
    #end class 

    def dateToUnix(date: datetime.datetime) -> int:
        unixtime = time.mktime(date.timetuple())

        return int(unixtime)
    #end def

    def strDateToUnix(date_string, format):
        try:
            date = datetime.datetime.strptime(date_string, format)

            return SqLiteConvertions.dateToUnix(date)
        except ValueError as e:
            raise SqLiteConvertions.WrongDateFormatError()
        #end try
    #end def

    def unixToDate(unixtime) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(unixtime)
    #end def
#end class

class Record(Model):
    def __init__(self, id=None, dbfile=None, foreign_keys=False, parse_decltypes=False):
        super().__init__(id, dbfile, foreign_keys, parse_decltypes)

        self.unix_date = 0
        self.seconds_worked = 0 

        self.getModel()
    #end def

    def is_none(self):
        if self.id is None:
            return True
        #end if
        return False
    #end if

    def tablename(self):
        return 'records'
    #end def

    def columns(self):
        return [
            {   'name':  'id',
                'type': 'INTEGER NOT NULL PRIMARY KEY'
            },
            {   'name': 'unix_date',
                'type': 'INTEGER'
            },
            {   'name': 'seconds_worked',
                'type': 'INTEGER'
            },
        ]
    #end def
#end class