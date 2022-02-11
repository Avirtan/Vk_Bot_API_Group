from datetime import datetime, timedelta
import time


class HandlerTime:

    @staticmethod
    def TimeDelayToUnix(hour:int=0, min:int=0):
        timeDelayed = datetime.now()+timedelta(hours=hour ,minutes=min)
        unixTime = time.mktime(timeDelayed.timetuple())
        return unixTime
