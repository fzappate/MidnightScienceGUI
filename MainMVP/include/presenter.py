import tkinter as tk
from tkinter import filedialog, ttk
import os
import threading
import subprocess
import numpy as np
# from  include.ui import UI -> Not working because of circular import


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
        pass


class Presenter():
    '''Class of the presenter.'''
    
    def __init__(self, model, view) -> None:
        '''Initialize the presenter object.'''
        # Save model and view into the presenter
        self.model = model
        self.view = view


    def RunUI(self):
        '''Run the UI.'''
        # Initialize UI and start the loop 
        self.view.initUI(self)
        self.view.mainloop()


    def UpdateEntry(self,entry:ttk.Entry,txt:str)->None:
        """This function takes whatever entry, deleted the text, and write the new 
        text given as input. """
        # Delete and rewrite the entry text 
        entry.delete(0,tk.END)
        entry.insert(0,txt)


    # Path selector 
    def BrowseWorkingFolder(self)->None:
        """This function allows the user to select a working directory by browsing 
        and store its path in the main control models. """
        # Open the dialog window
        workingFolder = filedialog.askdirectory()
        # Update the working folder entry with the selecter folder 
        self.UpdateEntry(self.view.pathSelector.pathEntry,workingFolder)
        # Set the workign folder of the setting object the same as the content of the entry 
        self.UpdateSettingWorkingFolder(workingFolder)
        
        
    def SetWorkingFolderManually(self,event=None)->None:
        """This function allows the user to select a working directory by copying 
        and pasting in the setting object. """
        workingFolder = self.view.pathSelector.pathEntry.get()
        # Set the workign folder of the setting object the same as the content of the entry 
        self.UpdateSettingWorkingFolder(workingFolder)

        
    def UpdateSettingWorkingFolder(self,workingFolder)->None:
        """This function makes sure that when a working folder is chosen the path is properly 
        updated in the Setting object."""

        # Update the setting object
        self.model.settings.workingFolder = workingFolder

        # Gear Generator
        self.model.settings.gearGenInputsFilePath = workingFolder + self.model.settings.gearGenInputsFileName
        self.model.settings.profile1Path = workingFolder + self.model.settings.profile1Name
        self.model.settings.profile2Path = workingFolder + self.model.settings.profile2Name

        # Geometry Code
        self.model.settings.geomCodeInputsFilePath = workingFolder + self.model.settings.geomCodeInputsFileName
        self.model.settings.geomCodeGearParaDict = workingFolder + self.model.settings.geomCodeGearParaDict
        self.model.settings.radialRecessDictPath = workingFolder + self.model.settings.radialRecessDict

        # # Reload inputs and gear set
        # self.LoadGearGenData()


    # Load funcions
    def LoadData(self)->None:
        '''This function loads all the inputs.'''

        # Load GearGen data
        self.LoadGearGenData()

        # Load GeometryCode data
        self.LoadGeomCodeData()

    
    def LoadGearGenData(self) -> None:
        '''This function starts the routine that loads all the data.
        First the inputs are stored in the dictionaries, then the gear profiles 
        and the inputs are stored in the gear set object, and finally the gear set is plotted '''

        # Check that the inputs file exists
        inputsFilePath = self.model.settings.gearGenInputsFilePath
        inputsFileExist = os.path.exists(inputsFilePath)

        if (inputsFileExist):
            self.model.gearGenInputs.inputFileFound = True
            print('GearGen inputs file found.')
        else:
            self.model.gearGenInputs.inputFileFound = False
            print('GearGen inputs file not found at: ' + inputsFilePath)

        # Check that the gears profile exists 
        profile1Path = self.model.settings.profile1Path
        profile2Path = self.model.settings.profile2Path
        profile1Exist = os.path.exists(profile1Path)
        profile2Exist = os.path.exists(profile2Path)

        if (profile1Exist & profile2Exist):
            self.model.gearGenPlot.gearSetFound = True
            print('Gear profile files found.')
        elif (profile1Exist & ~profile2Exist):
            self.model.gearGenPlot.gearSetFound = False
            print('Gear 2 profile file not found at')
            print(profile2Path)
        elif (~profile1Exist & profile2Exist):
            self.model.gearGenPlot.gearSetFound = False
            print('Gear 1 profile file not found at')
            print(profile1Path)
        elif (~profile1Exist & ~profile2Exist):
            self.model.gearGenPlot.gearSetFound = False
            print('Gear 1 and 2 profile files not found at: ')
            print(profile1Path)
            print(profile2Path)

        # Load the GearGen data
        self.LoadGearGenInputs()
        self.LoadGearSetProfiles()
        self.LoadGearSetData()
        self.PlotGearSet()
        

    def LoadGearGenInputs(self)->None:
        """Function that looks for the txt input file, reads the inputs, and store the values in the dictionary."""
        gearGenInputsFilePath = self.model.settings.gearGenInputsFilePath
        gearGenDictCollection = self.model.gearGenInputs.dictCollection
        labelHelpEntryList = self.view.mainTabColl.geomPreproc.geomPreprocTabs.gearGenInputs.inputsPanel.LabelHelpEntryList
        if (self.model.gearGenInputs.inputFileFound):
            # Open the file and read the content
            inputFile = open(gearGenInputsFilePath,"r")
            inputLines = inputFile.readlines()
            # Iterate on the dictionaries list to fill them one by one
            for ii, dictElem in enumerate(gearGenDictCollection):
                fileEntryTemp = dictElem['inputHeader']
                # Iterate line by line to find the mathching file entry     
                for jj, line in enumerate(inputLines):  
                    # Remove the new line from the end of the line 
                    line = line.strip('\n')
                    if (line == fileEntryTemp):
                        
                        # Extract value
                        valueTemp = inputLines[jj+1].rstrip('\n')
                        # Update dictionary
                        dictElem['value'] = float(valueTemp)
                        # Update entry 
                        self.UpdateEntry(labelHelpEntryList[ii],valueTemp)
        else:
            # Delete input panel entries
            for ii, labelHelpEntry in enumerate(labelHelpEntryList):
                labelHelpEntry.delete(0,tk.END)
            # Set all the values of the input dict to 0
            for ii, dictElem in enumerate(gearGenDictCollection):
                dictElem['value'] = None


    def LoadGearSetProfiles(self)->None:
        """Function that look for the txt gear profiles and load them in a gearset object."""

        # Get the working folder path and create the shapingPara file path
        profile1Path = self.model.settings.profile1Path
        profile2Path = self.model.settings.profile2Path

        if (self.model.gearGenPlot.gearSetFound):
            fileG1 = open(profile1Path,"r")
            coordG1 = fileG1.readlines()
            fileG1.close()

            fileG2 = open(profile2Path,"r")
            coordG2 = fileG2.readlines()
            fileG2.close()
            
            g1x = []
            g1y = []
            g2x = []
            g2y = []

            for idx, coord in enumerate(coordG1):
                words = coord.split('\t')
                g1x.append(float(words[0]))
                g1y.append(float(words[1]))

            for idx, coord in enumerate(coordG2):
                words = coord.split('\t')
                g2x.append(float(words[0]))
                g2y.append(float(words[1]))

            self.model.gearSet.SetGearsProfile(g1x,g1y,g2x,g2y)


        else:
            g1x = []
            g1y = []
            g2x = []
            g2y = []
            self.model.gearSet.SetGearsProfile(g1x,g1y,g2x,g2y)


    def LoadGearSetData(self)->None:
        """This function takes the value of interaxis and gear ratio 
        from the input dictionary and store them in the gear set object."""

        gearGenInputsFilePath = self.model.settings.gearGenInputsFilePath

        if (self.model.gearGenInputs.inputFileFound):
            N1 = self.model.gearGenInputs.GetValueFromDictionary("N1")
            N2 = self.model.gearGenInputs.GetValueFromDictionary("N2")
            self.model.gearSet.interaxis = self.model.gearGenInputs.GetValueFromDictionary("E")
            self.model.gearSet.gearRatio = N1/N2
        else:
            self.model.gearSet.interaxis = None
            self.model.gearSet.gearRatio = None


    def LoadGeomCodeData(self)->None:
        '''This function starts the routine that loads all the Geometry Code data.'''
        
        # Check that the inputs file exists
        geomCodeInputsFilePath = self.model.settings.geomCodeInputsFilePath
        inputsFileExist = os.path.exists(geomCodeInputsFilePath)

        if (inputsFileExist):
            self.model.geomCodeInputs.inputFileFound = True
            print('GeomCode inputs file found.')
        else:
            self.model.geomCodeInputs.inputFileFound = False
            print('GeomCode inputs file not found at: ' + geomCodeInputsFilePath)

        # Check that the gear parameters dictionary exists 
        geomCodeGearParaDictPath = self.model.settings.geomCodeGearParaDictPath
        geomCodeGearParaDictPathExist = os.path.exists(geomCodeGearParaDictPath)

        if (geomCodeGearParaDictPathExist):
            self.model.geomCodeInputs.gearParaDictFound = True
            print('GeomCode gear parameters dictionary found.')
        else:
            self.model.geomCodeInputs.gearParaDictFound = False
            print('GeomCode gear parameters dictionary not found at: ' + geomCodeGearParaDictPath)

        # Check that the radial recess dictionary exists 
        radialRecessDictPath = self.model.settings.radialRecessDictPath
        radialRecessDictPathExist = os.path.exists(radialRecessDictPath)

        if (radialRecessDictPathExist):
            self.model.geomCodeInputs.radialRecessFound = True
            print('GeomCode radial recess dictionary found.')
        else:
            self.model.geomCodeInputs.radialRecessFound = False
            print('GeomCode radial recess dictionary not found at: ' + radialRecessDictPath)

        self.LoadGeomCodeInputs()


    def LoadGeomCodeInputs(self)->None:
        print('here')
        # Load the Geometry Code inputs data
        geomCodeInputsFilePath = self.model.settings.geomCodeInputsFilePath
        geomCodeDictCollection = self.model.geomCodeInputs.dictCollection
        labelHelpEntryList = self.view.mainTabColl.geomPreproc.geomPreprocTabs.geomCodeInputs.inputsPanel.LabelHelpEntryList

        if (self.model.geomCodeInputs.inputFileFound):
            # Open the file and read the content
            inputFile = open(geomCodeInputsFilePath,"r")
            inputLines = inputFile.readlines()
            # Iterate on the dictionaries list to fill them one by one
            for ii, dictElem in enumerate(geomCodeDictCollection):
                fileEntryTemp = dictElem['inputHeader']
                # Iterate line by line to find the mathching file entry     
                for jj, line in enumerate(inputLines):  
                    # Remove the new line from the end of the line 
                    line = line.strip('\n')
                    if (line == fileEntryTemp):
                        # Extract value
                        valueTemp = inputLines[jj+1].rstrip('\n')
                        # Update dictionary
                        dictElem['value'] = valueTemp
                        # dictElem['value'] = float(valueTemp)
                        # Update entry 
                        self.UpdateEntry(labelHelpEntryList[ii],valueTemp)
        else:
            # Delete input panel entries
            for ii, labelHelpEntry in enumerate(labelHelpEntryList):
                labelHelpEntry.delete(0,tk.END)
            # Set all the values of the input dict to 0
            for ii, dictElem in enumerate(geomCodeDictCollection):
                dictElem['value'] = None



    # Save functions
    def SaveGearGenData(self)->None:
        '''Initiate the routing that saves all the data of the GearGen model.'''
        print('Save data')
        self.SaveGearGenInputs()
        self.SaveGearGenProfiles()


    def SaveGearGenInputs(self)->None:
        '''Save the GearGen inputs file in the working folder.'''
        # Update the dictionary based on what is in the entries
        self.UpdateDictionariesFromEntries() 
        inputsFilePath = self.model.settings.inputsFilePath
        # Delete the previous input dictionary
        if os.path.exists(inputsFilePath):
                os.remove(inputsFilePath)
        # Write the input dictionary file 
        inputFile = open(inputsFilePath,"w")
        for ii, dict in enumerate(self.model.gearGenInputs.dictCollection):
            inputFile.write(dict['inputHeader'])
            inputFile.write('\n')
            val = dict['value']
            inputFile.write(val)
            inputFile.write('\n')
            inputFile.write('\n')
        inputFile.close()


    def SaveGearGenProfiles(self)->None:
        '''Save the GearGen gear profile in the working folder.'''
        profile1Path = self.model.settings.profile1Path
        profile2Path = self.model.settings.profile2Path
        # Delete the previous profiles
        if os.path.exists(profile1Path):
                os.remove(profile1Path)
        if os.path.exists(profile2Path):
                os.remove(profile2Path)
        # Write the profile 1  file 
        profile1File = open(profile1Path,"w")
        for ii, point in enumerate(self.model.gearSet.profile1.x):
            valx = str(point)
            valy = str(self.model.gearSet.profile1.y[ii])
            profile1File.write(valx)
            profile1File.write('\t')
            profile1File.write(valy)
            profile1File.write('\n')
        profile1File.close()
        # Write the profile 2 file 
        profile2File = open(profile2Path,"w")
        for ii, point in enumerate(self.model.gearSet.profile2.x):
            valx = str(point)
            valy = str(self.model.gearSet.profile2.y[ii])
            profile2File.write(valx)
            profile2File.write('\t')
            profile2File.write(valy)
            profile2File.write('\n')
        profile2File.close()
        

    def UpdateDictionariesFromEntries(self)->None:
        '''Take the content of the input entries and store them in the GearGen dictionaries collection.'''
        # Iterate on the entries in the input panel
        for idx, dict in enumerate(self.model.gearGenInputs.dictCollection):
            correspondingLabelHelpEntry = self.view.mainTabColl.geomPreproc.geomPreprocTabs.gearGenInputs.inputsPanel.LabelHelpEntryList[idx]
            # Update the dictionariy
            dict["value"] = correspondingLabelHelpEntry.get()


    # Plot functions 
    def PlotGearSet(self)->None:
        '''Plot the ger set into the gear set plot.'''
        # Clear the axes 
        self.view.mainTabColl.geomPreproc.plot.ax.cla()
        # Add curve
        self.AddCurveToGearSetPlot(self.model.gearSet.profile1)
        self.AddCurveToGearSetPlot(self.model.gearSet.profile2)
        # Set cosmetic
        self.SetAxisOfGearSetPlot()
        self.SetLabelOfGearSetPlot()
        self.SetGearGenPlotGrid()
        # Redraw the canvas
        self.view.mainTabColl.geomPreproc.plot.canv.draw()
        # Update the canvas
        self.view.mainTabColl.geomPreproc.plot.canv.draw()


    def AddCurveToGearSetPlot(self,curve)->None:
        '''Add a curve to the gear set plot.'''
        self.view.mainTabColl.geomPreproc.plot.ax.plot(curve.xMod, curve.yMod)


    def SetAxisOfGearSetPlot(self)->None:
        '''Set the limits of the axes of the GerGenPlot.'''
        self.view.mainTabColl.geomPreproc.plot.ax.set_xlim(self.model.gearSet.xMin,self.model.gearSet.xMax)
        self.view.mainTabColl.geomPreproc.plot.ax.set_ylim(self.model.gearSet.yMin,self.model.gearSet.yMax)


    def SetLabelOfGearSetPlot(self)->None:
        '''Set the labels of the gear gen plot.'''
        self.view.mainTabColl.geomPreproc.plot.ax.set_xlabel('Length [mm]')
        self.view.mainTabColl.geomPreproc.plot.ax.set_ylabel('Length [mm]')


    def SetGearGenPlotGrid(self)->None:
        '''Take set the grid on the plot according to the property isGridOn.'''
        isGridOn = self.model.gearGenPlot.isGridOn
        self.view.mainTabColl.geomPreproc.plot.ax.grid(isGridOn)


    # Run model
    def CreateGearGenThread(self)->None:
        '''Create a thread to run the gear generator in parallel with the UI.'''
        threading.Thread(target=self.RunGearGen, daemon=True).start()


    def RunGearGen(self):
        '''Run the GearGenerator.'''
        # Make sure that the data in the entries are saved
        self.SaveGearGenInputs()

        # Create the exe file path 
        exePath = self.model.settings.exePath

        print('Looking for the exe at:' + exePath)
        
        if (os.path.exists(exePath)):
            print('exe found.')
        else:
            print('exe not found.')

        # Run the exe 
        p = subprocess.Popen([exePath, '-p'], stdout=subprocess.PIPE, bufsize=1, text=True,cwd = self.model.settings.workingFolder)
        
        while p.poll() is None: # check whether process is still running
            msg = p.stdout.readline().strip() # read a line from the process output
            if msg:
                print(msg)

        self.LoadGearSetProfiles()
        self.LoadGearSetData()
        self.PlotGearSet()

        # When the exe is done, load the gear profiles
        # self.plot.InitializeGearSet(self.workingFolderPath)

        # # Clear the axes 
        # self.plot.ax.cla()

        # # Update the axis content
        # self.plot.DrawGearSet()

        # # Update the canvas
        # self.plot.canv.draw()
        
        # self.plot.DrawGearSet()


    # Plot controls
    def RotateGearSet(self,rotValue=0)->None:
        '''Rotate the gearset profile coordinates by a value and update the GearGen plot.'''
        # Take the entry value and sum +1
        currentRotValue = self.view.mainTabColl.gearGen.plotControls.rotationGearSet.entry.get()
        nextRotValueDeg = float(currentRotValue)+rotValue
        nextRotValueRad = np.deg2rad(nextRotValueDeg)
        
        # Update the gear set rotation angle
        self.model.gearSet.rotationAngleDeg = nextRotValueDeg
        self.model.gearSet.rotationAngleRad = nextRotValueRad
        # Update profile 
        self.RotateGearSetProfile(self.model.gearSet,nextRotValueRad)
        # Update plot
        self.PlotGearSet()
        # Update control entry 
        self.UpdateEntry(self.view.mainTabColl.gearGen.plotControls.rotationGearSet.entry,nextRotValueDeg)

        
    def RotateGearSetProfile(self,gearSet,rotValue)->None:
        '''This function is intermediary between RotateGearSet and RotateProfile. 
        It extracts all the data necessary for the proper rotation, like interaxis, and gear ratio.'''
        gearRatio = gearSet.gearRatio
        interaxis = gearSet.interaxis
        profile1 = gearSet.profile1
        profile2 = gearSet.profile2

        # Rotate pinion 
        self.RotateProfile(profile1,rotValue)
        # Rotate gear
        self.RotateProfile(profile2,rotValue*gearRatio,0,-interaxis)


    def RotateProfile(self,profile,ang, dx = 0, dy = 0)->None:
        '''This function rotates the curve profile. The use can specify the rotatoin angle, and the center of rotation of the profile'''
        # dx and dy are the components of the vector that connects the origin 
        # of the RS and the center of the curve
        x = profile.x
        y = profile.y
        xFirst = np.subtract(x,dx)
        yFirst = np.subtract(y,dy)
        xSecond = xFirst*np.cos(ang) - yFirst*np.sin(ang)
        ySecond = xFirst*np.sin(ang) + yFirst*np.cos(ang)
        profile.xMod = xSecond+dx
        profile.yMod = ySecond+dy

    
    def ChangeGridState(self)->None:
        '''Add or remove the grid of the plot.'''
        self.targetPlotModel = self.model.gearGenPlot
        self.targetPlotView = self.view.mainTabColl.gearGen.plot
        self.checkbox = self.view.mainTabColl.gearGen.plotControls.gridControl
        if self.targetPlotModel.isGridOn:                # If the grid is on
            self.targetPlotModel.isGridOn = False             # Set it to false 
            self.targetPlotView.ax.grid(self.targetPlotModel.isGridOn) # Remove the grid from the plot 
            self.targetPlotView.canv.draw()                  # Redraw the plot
            self.checkbox.state(['!selected'])      # Uncheck the checkbutton

        else:                                       # If the grid is off   
            self.targetPlotModel.isGridOn = True              # Set isGridOn to false
            self.targetPlotView.ax.grid(self.targetPlotModel.isGridOn) # Add the grid to the target plot
            self.targetPlotView.canv.draw()                  # Redraw the plot
            self.checkbox.state(['selected'])       # Check the checkbutton   