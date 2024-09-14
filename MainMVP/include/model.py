from include.settings import Settings
from include.gearset import GearSet
from include.geargeninputs import GearGenInputs
from include.geargenplot import GearGenPlot
from include.geomcodeinputs import GeomCodeInputs


class Model():
    '''Model class containing all the submodel of the software.'''

    def __init__(self)->None:
        '''Initialize the model class.'''

        self.settings = Settings()

        self.gearSet = GearSet()

        self.gearGenInputs = GearGenInputs()
        self.gearGenPlot = GearGenPlot()

        self.geomCodeInputs = GeomCodeInputs()

        