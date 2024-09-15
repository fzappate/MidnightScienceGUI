import tkinter as tk
from tkinter import filedialog, ttk
from collections import defaultdict
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
        self.LoadSettings()
        self.LoadResults()
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
        folder = filedialog.askdirectory()
        # Update the working folder entry with the selecter folder 
        self.UpdateEntry(self.view.pathSelector.pathEntry,folder)
        # Update model setting
        self.model.settings.workingFolder = folder
        # Set the workign folder of the setting object the same as the content of the entry 
        self.UpdateSettingFile("workingFolder", folder)
        
        
        
    def BrowseResultsFile(self) -> None:
        '''This function allows the selection of a file.'''
        # Open the dialog window
        filePath = filedialog.askopenfilename()
        # Update the entry text
        self.UpdateEntry(self.view.mainTabColl.plotter.signalSelector.inputsPanel.fileSelector.pathEntry,filePath)
        # Update model setting 
        self.model.settings.resultsFilePath = filePath
        # Update setting file
        self.UpdateSettingFile("resultsFilePath", filePath)
        
        
                
    def SetWorkingFolderManually(self,event=None)->None:
        """This function allows the user to select a working directory by copying 
        and pasting in the setting object. """
        workingFolder = self.view.pathSelector.pathEntry.get()
        # Set the workign folder of the setting object the same as the content of the entry 
        self.UpdateSettingWorkingFolder(workingFolder)

        
        
    def UpdateWorkingFolder(self,workingFolder)->None:
        """This function makes sure that when a working folder is chosen the path is properly 
        updated in the Settings object and settings file."""



        # Update settings file
        file = open(self.model.settings.settingsFilePath,'r')
        lines = file.readlines()
        file.close()
        
        counter = 0
        for line in lines:
            if line.startswith('-'):
                
                lineMod = line.replace(line[0],"")
                tokens = lineMod.split(',')
                keyword = tokens[0].strip()                
                setting = tokens[1].strip()
                if keyword == "workingFolder":
                    break
            counter +=1
        
        lines[counter] = "- workingFolder, " + workingFolder + "\n"
        file = open(self.model.settings.settingsFilePath,'w')
        file.writelines(lines)
        file.close()
       
        
        
    def UpdateSettingFile(self, targetSettingKey, targetSettingVal)->None:
        """This function makes sure that when a working folder is chosen the path is properly 
        updated in the Settings object and settings file.
        
        settingInModel:     structure of the setting in the UI.
                            Eg: self.model.settings.workingFolder
        targetSettingKey:   keyword of the setting in the settings file.
                            Eg: workingFolder
        setting:            data entered in the model setting structure and file."""

        # Update settings file
        file = open(self.model.settings.settingsFilePath,'r')
        lines = file.readlines()
        file.close()
        
        counter = 0
        for line in lines:
            if line.startswith('-'):
                
                lineMod = line.replace(line[0],"")
                tokens = lineMod.split(',')
                keyword = tokens[0].strip()                
                setting = tokens[1].strip()
                if keyword == targetSettingKey:
                    break
            counter +=1
        
        lines[counter] = "- " + targetSettingKey + ", "  + targetSettingVal + "\n"
        file = open(self.model.settings.settingsFilePath,'w')
        file.writelines(lines)
        file.close()



    # Load funcions
    
    def LoadData(self)->None:
        '''This function loads the inputs, outputs and so on.'''

        # Load the results of the simulation 
        # self.LoadResults()
        
        # Load GearGen data
        # self.LoadGearGenData()

        # Load GeometryCode data
        # self.LoadGeomCodeData()



    def LoadSettings(self) -> None:
        ''' This function loads the GUI settings.'''
        
        # Check that the settings file exists
        settingsFileExist = os.path.exists(self.model.settings.settingsFilePath)
        
        if (settingsFileExist):
            print('Settings file found at: ' + self.model.settings.settingsFilePath)
        else:
            print('Settings file not found at: ' + self.model.settings.settingsFilePath)
            
        # Read setting file
        file = open(self.model.settings.settingsFilePath,'r')
        lines = file.readlines()
        
        # Create setting dictionary
        settingDict = {}
        for line in lines:
            if line.startswith('-'):
                
                line = line.replace(line[0],"")
                tokens = line.split(',')
                keyword = tokens[0].strip()                
                setting = tokens[1].strip()
                
                settingDict[keyword] = setting
                    
        file.close()
        
        # load setting dictionary in setting structure
        self.model.settings.workingFolder = settingDict.get("workingFolder")
        self.model.settings.resultsFilePath = settingDict.get("resultsFilePath")
        
        # Update entries
        self.UpdateEntry(self.view.pathSelector.pathEntry,settingDict.get("workingFolder"))
        self.UpdateEntry(self.view.mainTabColl.plotter.plotManagerPane.plotManager.fileSelector.pathEntry,settingDict.get("resultsFilePath"))
          
        
        
    def LoadResults(self) -> None:
        '''Load results.'''
        # Read results file
        file = open(self.model.settings.resultsFilePath,'r')
        lines = file.readlines()
        file.close()
        
        # Update the model dictionary containing the results 
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
                    
        self.model.results = resDict
        
        # Update the combobox
        self.view.mainTabColl.plotter.plotManagerPane.plotManager.signalCollection['values'] = tuple(self.model.results.keys())
        
        
        
        
        

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