from collections import defaultdict

class ResultFileModel():
    def __init__(self)->None:
        '''
        Class that generates the model of a ResultFile object.
        The purpose of this class is to store all the signals
        and related information contained in a result file.
        '''
        # Dictionary with signal names and values
        self.name = ''
        self.indx = 0
        self.absPath = ''
        self.signals = {}
        
    def LoadResults(self,filePath)->None:
        '''Load results.'''

        
        # Read results file
        file = open(filePath,'r')
        lines = file.readlines()
        file.close()
        
        # Create a dictionary with the results 
        resDict = defaultdict(list)
        counter = 0
        for line in lines:
            lineTokens = line.split(',')
            lineTokens = [lineToken.strip() for lineToken in lineTokens ]
            lineTokens = lineTokens[:-1]
            
            if counter == 0:
                headerTokens = lineTokens
            else:
                valueTokens = lineTokens
                values = [float(x) for x in valueTokens]
                for i, key in enumerate(headerTokens):
                    resDict[key].append(values[i])
                
            counter +=1
            
        # Save the dictionary in the object
        self.signals = resDict
        
        # Update the combobox
        # self.view.mainTabColl.plotter.plotManagerPane.plotManager.signalCollection['values'] = tuple(self.model.results.keys())