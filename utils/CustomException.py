import datetime

class AdminError(Exception) : 
    def __init__(self, trigger_date, message) -> None:
        self.__trigger_date=trigger_date
        super().__init__(message)
    
    @property
    def trigger_date(self) : 
        return self.__trigger_date

class BasicExcetion(Exception) : 
    def __init__(self, msg):
        super().__init__(msg)