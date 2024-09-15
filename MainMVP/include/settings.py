class Settings():
    '''Class containing all the settings of the software instance.'''

    def __init__(self)->None:
        '''Initialize the application setting object.'''

        self.settingsFilePath = './MainMVP/utilities/settings.md'
        self.workingFolder = ''
        self.resultsFile = ''
        self.resultsFilePath = ''