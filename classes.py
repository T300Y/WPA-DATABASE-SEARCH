
class Record:
    def __init__(self, event, classification, sex):
        classes = ['T35','T36','T37','T38']
        if classification not in  classes:
            raise ValueError('Class does not exist')
        self._event = event
        self._classification = classification
        self._sex = sex
        #search spreadsheet find range where males records are
        ...
        #search database within male range for where event is

        # find row where record is & read it then split

        #assign object orientated variable to split data
