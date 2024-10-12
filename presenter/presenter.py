import tkinter as tk
from tkinter import filedialog, ttk
from collections import defaultdict
import os
import threading
import subprocess
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

from ui.collapsiblepanes import TogglePaneDel
from ui.resfilemanager import ResFileManager
from ui.resfilepane import ResFilePane
from ui.signalpane import SignalPane
from model.PlotModel import PlotModel
from model.SubplotModel import SubplotModel
from model.ResultFileModel import ResultFileModel




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
        self.LoadResultsFromSavedSettings()
        self.view.protocol("WM_DELETE_WINDOW", self._on_closing)  # Force closing when 
        self.view.mainloop()

    def _on_closing(self):
        self.view.quit()  # stops mainloop
        self.view.destroy()  # this is necessary on Windows to prevent Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
    def UpdateEntry(self,entry:ttk.Entry,txt:str)->None:
        """This function takes whatever entry, deleted the text, and write the new 
        text given as input. """
        # Delete and rewrite the entry text 
        entry.delete(0,tk.END)
        entry.insert(0,txt)


    # GUI Initialization

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
        # self.UpdateEntry(self.view.pathSelector.pathEntry,settingDict.get("workingFolder"))
        # self.UpdateEntry(self.view.mainTabColl.plotter.plotManagerPane.plotManager.fileSelector.pathEntry,settingDict.get("resultsFilePath"))
    
    def LoadResultsFromSavedSettings(self) -> None:
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
        # self.view.mainTabColl.plotter.plotManagerPane.plotManager.signalCollection['values'] = tuple(self.model.results.keys())
    
    
    # Working Folder Selection
    
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
                    
    def SetWorkingFolderManually(self,event=None)->None:
        """This function allows the user to select a working directory by copying 
        and pasting in the setting object. """
        workingFolder = self.view.pathSelector.pathEntry.get()
        # Set the workign folder of the setting object the same as the content of the entry 
        # self.UpdateSettingWorkingFolder(workingFolder)
        
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

     
    # Subplot Handling
    
    def AddSubplot(self,plotManager)->None:
        '''Add subplot to PlotManager and Plot.
        Add a toggle frame to the plot manager pane.'''
        # Get useful information 
        noOfSubplot = self.model.plotModel.noOfSubplots
        
        # Create SubplotModel
        subplot = SubplotModel()
        subplot.name = str(noOfSubplot)
        subplot.indx = noOfSubplot
        
        # Update PlotModel adding a SubplotModel
        self.model.plotModel.AddSubplot(subplot)
        
        # Redraw PlotManager
        self.RedrawPlotManager()
        # Redraw PlotUI
         
    def DeleteSubplot(self,subplotPane)->None:
        '''Delete a toggle pane and connected subplot.'''        
        # Update PlotModel deleting the SubplotModel
        self.model.plotModel.DeleteSubplot(subplotPane)
        
        # Redraw PlotManager
        self.RedrawPlotManager()
           
    def SelectXAxis(self,event,resFileManager)->None:
        '''Function invoked when an item is selected from the subplot X axis selection.'''
        # Identify the subplot indx
        subplotIndx = resFileManager.master.master.indx
        
        # Find the index of the signal selected
        selectedSigNo = resFileManager.xAxisSelect.current
        
        # Update the subplotModel 
        self.model.plotModel.containedSubplots[subplotIndx].xAxisSelectedIndx = selectedSigNo
        signalsName = self.model.plotModel.containedSubplots[subplotIndx].xAxisSignalsName
        self.model.plotModel.containedSubplots[subplotIndx].xAxisSelectedName = signalsName[selectedSigNo]
        
        
            
    # ResultFile Handling
        
    def AddResultFile(self, resFileManager)->None:
        '''Add ResultFile to Subplot.'''
        # Get useful information 
        noOfResFile = resFileManager.noOfRows
        subplotIndx = resFileManager.master.master.indx
        
        # Create ResFileModel
        resultFileModel = ResultFileModel()
        resultFileModel.name = str(noOfResFile)
        resultFileModel.indx = noOfResFile
        
        # Update SubplotModel adding a ResultFile
        self.model.plotModel.containedSubplots[subplotIndx].AddResultFile(resultFileModel)
        
        # Redraw PlotManager
        self.RedrawPlotManager()
        
    def DeleteResultFile(self,resFilePane)->None:
        '''Delete ResultFile from the model and redraw the PlotManager.'''
        subplotIndx = resFilePane.master.master.master.indx
        
        # Update SubplotModel adding a ResultFile
        self.model.plotModel.containedSubplots[subplotIndx].DeleteResultFile(resFilePane)
        
        # Redraw PlotManager
        self.RedrawPlotManager()
        
    def BrowseResFile(self,fileSelector,resFilePane) -> None:
        '''This function allows the selection of a file.'''
        # Open the dialog window
        filePath = filedialog.askopenfilename()
        
        # Update the entry text
        fileSelector.UpdateEntry(filePath)
        
        self.FileSelectorReturn(None, fileSelector, resFilePane)
        
    def FileSelectorReturn(self, event, fileSelector, resFilePane)->None:
        '''Event called whenever a file is copied and return is hit. Or when the entry looses focus.'''

        # Retrieve file path from entry
        filePath = fileSelector.GetEntry()
        
        # Check if a path exists
        pathExists = os.path.exists(filePath)
        if not pathExists:
            return
                
        # Update model setting 
        self.model.settings.resultsFilePath = filePath
        # Update setting file
        self.UpdateSettingFile("resultsFilePath", filePath)
        
        # Retrieve useful info
        subplotIndx = resFilePane.master.master.master.indx
        resFileIndx = resFilePane.indx
        
        # Load the signals into ResultFileModel
        self.model.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].absPath = filePath
        self.model.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].LoadResults(filePath)
        
        # Extract signals and their names from the results file just loaded 
        signals = self.model.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].signals
        signalNames = self.model.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].signalNames
        
        # If the first result pane is added
        if resFilePane.indx == 0:
        # Add the signals to the x axis selection 
            for signal, signalName in zip(signals, signalNames):
                self.model.plotModel.containedSubplots[subplotIndx].xAxisSignals.append(signal)
                self.model.plotModel.containedSubplots[subplotIndx].xAxisSignalsName.append(signalName)
        
        self.RedrawPlotManager()
        print('Result file added.')

        
    # Signal Handling
    
    def AddSignal(self,event, resFilePane)->None:
        '''Moves one signal from the ResultModel to the PlottedSignal.'''
        
        # Get useful information
        subplotIndx = resFilePane.master.master.master.indx
        resFileIndx = resFilePane.indx
        
        # Find the index of the signal selected
        selectedSigNo = resFilePane.signalCollection.current()
        # Extract from the ResultFileModel the signal selected
        signalToPlot = self.model.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].signals[selectedSigNo]
        # Add it to the ResultFilePane selectedSignals list 
        self.model.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].selectedSignals.append(signalToPlot)
        # Add it to the SubplotModel plottedSignals list
        self.model.plotModel.containedSubplots[subplotIndx].plottedSignals.append(signalToPlot)
        
        self.RedrawPlotManager()
        
    def DeleteSignal(self, signalPane)->None:
        '''Delete signal.'''
        
        # Get the index of the result file and subplot
        subplotIndx = signalPane.master.master.master.master.indx
        resFileIndx = signalPane.master.indx
        signalIndx = signalPane.indx
        
        # Remove signal from ResultFileModel selectedSignals list
        self.model.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].selectedSignals.pop(signalIndx)
        # Remove the signal from the SubplotModel plottedSignals list
        self.model.plotModel.containedSubplots[subplotIndx].plottedSignals.pop(signalIndx)
        
        self.RedrawPlotManager()
        
        
    # Plot Manager
    
    def RedrawPlotManager(self)->None:
        '''
        Redraw the plot manager time.
        '''
        # Delete everything in the plot manager but the first row
        plotManagerChildren = self.view.mainTabColl.plotter.plotManager.winfo_children()
        for ii,child in enumerate(plotManagerChildren):
            if ii == 0:
                continue
            child.destroy()
            
        # Redraw everything in the plot manager
        areCollapsed = self.model.plotModel.areCollapsed
        # Iterate on the Subplots
        for ii,sp in enumerate(self.model.plotModel.containedSubplots):
            spRow = ii+1 # Skip the 'Add subplot' button
            toggleFrame = TogglePaneDel(self.view.mainTabColl.plotter.plotManager,
                                        self,
                                        label = sp.name,
                                        indx=ii,
                                        isCollapsed=areCollapsed[ii],
                                        bg = 'cyan')
            toggleFrame.grid(row = spRow, column = 0, sticky='EW')
            resFileManager = ResFileManager(toggleFrame.interior, 
                                            self, 
                                            current = sp.xAxisSelectedIndx,
                                            listOfSignals = sp.xAxisSignalsName,
                                            bg = 'blue')
            resFileManager.grid(row=0,column=0,sticky='EW')
            
            # Iterate on the ResultFile
            for jj,rf in enumerate(sp.resultFiles):
                rfRow=jj+3 # Skip the label, combobox, and 'Add result file' button
                resFile = ResFilePane(resFileManager,
                                      self,
                                      indx = jj,
                                      entryText=rf.absPath,
                                      comboboxList=rf.signalNames)
                resFile.grid(row=rfRow,column=0,sticky='EW')
                
                # Iterate on the Signalpane
                for kk, ss in enumerate(rf.selectedSignals):
                    ssRow = kk+2 # Skip the button and combobox row
                    sigName = ss.name
                    sigPane = SignalPane(   resFile,
                                            self,
                                            indx = kk,
                                            sigName = sigName,
                                            bg = 'red')
                    sigPane.grid(row=ssRow,column=0,sticky='EW')
            
    def RedrawPlotCanvas(self)->None:
        '''This function redraws the plot canvas.'''
        # Destroy toolbar and canvas
        plotManagerChildren = self.view.mainTabColl.plotter.plot.winfo_children()
        for ii,child in enumerate(plotManagerChildren):
            child.destroy()
            
        # Calculate the number of subplots that must be generated
        noOfSubplots = self.model.plotModel.noOfSubplots
        self.fig, axList = plt.subplots(noOfSubplots,1)
        
        if noOfSubplots == 1:
            plottedSignal = self.model.plotModel.containedSubplots[0].plottedSignals
            for sig in plottedSignal:
                axList.plot(0,0) 
        elif noOfSubplots > 1:
            for ii in range(0,noOfSubplots):
                s = 5
                
        else:
            f = 9
                # axList[ii].plot(x,y1) 
            
        # Draw the canvas and toolbar
        self.view.mainTabColl.plotter.plot.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.view.mainTabColl.plotter.plot.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.view.mainTabColl.plotter.plot.toolbar.update()
        self.view.mainTabColl.plotter.plot.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.view.mainTabColl.plotter.plot.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            
            
            
            
            
        
        
    def UpdatedCollapsiblePaneModel(self, collapsiblePane)->None:
        '''Update the PlotModel areCollapsed property.'''
        indx = collapsiblePane.indx
        isCollapsed = collapsiblePane.isCollapsed
        self.model.plotModel.areCollapsed[indx] = isCollapsed
    
    def DelResFilePane(self, fileSelector):
        fileSelector.master.destroy()

    def AddSignalToPlotData(self,key)->None:
        '''Add a signal to plot data.'''
        # Extract value from results dictionary
        value = self.model.results[key]
        # Create key-value pair in plotData dictionary
        self.model.plotData.results[key].append(value)
        
    def PlotPlotData(self)->None:
        '''Plot the signals contained in plotData.'''
        
    def AddPlotToggleFrame(self)->None:
        '''Add a toggle frame in the plot manager pane.'''
        self.view.mainTabColl.plotter.plotManagerPane.plotManager 
        
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