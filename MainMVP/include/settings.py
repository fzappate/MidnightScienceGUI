class Settings():
    '''Class containing all the settings of the software instance.'''

    # Slots 
    # __slots__ = ('inputsFileName','exePath','profile1Name','profile2Name',
    #              'geomCodeGearParaDict','radialRecessDictionary',
    #              'workingFolder',
    #              'inputsFilePath','profile1Path','profile2Path')

    def __init__(self)->None:
        '''Initialize the application setting object.'''

        # Working folder path
        self.workingFolder = ''

        # Predefined Gear Generator files name
        self.gearGenInputsFileName = '/shapingPara_dim.txt'
        self.exePath = './MainMVP/gearOpti.exe'
        self.profile1Name = '/gear1.txt'
        self.profile2Name = '/gear2.txt'
        
        self.gearGenInputsFilePath = ''
        self.profile1Path = ''
        self.profile2Path = ''

        # Predefined Gear Generator files name
        self.geomCodeInputsFileName = '/inputs.txt'
        self.geomCodeGearParaDict = '/Inputs/gearParametersDictionary.txt'
        self.radialRecessDict = '/Inputs/radialRecessDictionary.txt'

        self.geomCodeInputsFilePath = ''
        self.geomCodeGearParaDictPath = ''
        self.radialRecessDictPath = ''