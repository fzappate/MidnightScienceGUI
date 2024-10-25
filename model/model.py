from model.settings import Settings
from model.signalcollection import SignalCollection
from model.ProjectModel import ProjectModel

class Model():
    '''Model class containing all the submodel of the software.'''

    def __init__(self)->None:
        '''Initialize the model class.'''

        self.settings = Settings()
        self.results = {}
        self.plotData = SignalCollection()
        self.projectModel = ProjectModel()
        
        



        