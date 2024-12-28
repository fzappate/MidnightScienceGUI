import tkinter as tk
from tkinter import filedialog, ttk
import os
import sys

import json
import numpy as np
from shutil import copy2
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

from ui.PlotPane import PlotPane
from ui.PlotOptions import PlotOptions
from ui.ResFilePane import ResFilePane
from ui.SignalPane import SignalPane
from ui.SubplotOptions import SubplotOptions
from ui.SignalOptions import SignalOptions
from ui.SubplotPane import SubplotPane
from ui.SignalPaneX import SignalPaneX

from model.ProjectModel import ProjectModel
from model.PlotModel import PlotModel
from model.SubplotModel import SubplotModel
from model.ResultFileModel import ResultFileModel
from model.SignalModel import SignalModel
from model.PlottedSignalModel import PlottedSignalModel



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
        self.view.initView(self)
        self.LoadSettings()
        self.LoadProjectModel()
        self.RedrawPlotNotebook()
        
        # Force closing when using matplotlib
        self.view.protocol("WM_DELETE_WINDOW", self._on_closing)   
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
        settingFilePath = self.ResourcePath(self.model.settings.settingsFilePath)
        settingsFileExist = os.path.exists(settingFilePath)
        
        if (settingsFileExist):
            self.PrintMessage('Settings file found at: ' + settingFilePath)
        else:
            self.PrintError('Settings file found at: ' + settingFilePath)
            
        # Read setting file
        file = open(settingFilePath,'r')
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
        
        # Load settings
        self.model.settings.projectFolder = settingDict.get("ProjectFolder")
        self.model.settings.projectFileName = settingDict.get("ProjectFileName")
        self.model.settings.projectFileNameTemp = settingDict.get("ProjectFileNameTemp")
        
        # Update entries
        self.UpdateEntry(self.view.pathSelector.pathEntry,settingDict.get("ProjectFolder"))
    
            
        
    # JSON HANDLING
    
    def LoadProject(self)->None:
        self.LoadProjectModel()
        self.RedrawPlotNotebook()
             
    def LoadProjectModel(self) -> None:
        '''Load project from JSON.'''
        # Check that a ProjectModel.json exists
        projectModelPath = self.model.settings.projectFolder + "/ProjectModel.json"
        projectModelFileExists = os.path.exists(projectModelPath)
        if not projectModelFileExists:
            self.PrintMessage('No project file found at: ' + projectModelPath)
            self.PrintMessage('Creating empty project.')
            self.CreateEmptyProject()

        else:
            self.PrintMessage('Project file found at: ' + projectModelPath)
            
            # Load ProjectModel.json
            f = open(projectModelPath,'r')
            jsonProjMod = json.load(f)
            
            # Load project data
            projModel = ProjectModel()
            projModel.tabSelected = jsonProjMod["tabSelected"]
            
            # Load plot data        
            jsonContainedPlots = jsonProjMod["containedPlots"]
            for ii, jsonPlot in enumerate(jsonContainedPlots):
                plotModel = PlotModel()
                plotModel.name = jsonPlot["name"]
                plotModel.indx = jsonPlot["indx"]
                plotModel.leftMargin = jsonPlot["leftMargin"]
                plotModel.rightMargin = jsonPlot["rightMargin"]
                plotModel.bottomMargin = jsonPlot["bottomMargin"]
                plotModel.topMargin = jsonPlot["topMargin"]
            
                plotModel.noOfSubplots = jsonPlot["noOfSubplots"]
                
                # Load subplot data
                jsonContainedSubplots = jsonPlot["containedSubplots"]
                for jj, jsonSubplot in enumerate(jsonContainedSubplots):
                    subplotModel = SubplotModel()
                    subplotModel.name = jsonSubplot["name"]
                    subplotModel.indx = jsonSubplot["indx"]
                    subplotModel.isCollapsed = jsonSubplot["isCollapsed"]
                    
                    subplotModel.xLabel = jsonSubplot["xLabel"]
                    subplotModel.yLabel = jsonSubplot["yLabel"]
                    subplotModel.xLim = jsonSubplot["xLim"]
                    subplotModel.yLim = jsonSubplot["yLim"]
                    subplotModel.xLimUser = jsonSubplot["xLimUser"]
                    subplotModel.yLimUser = jsonSubplot["yLimUser"]
                    subplotModel.useUserLim = jsonSubplot["useUserLim"]
                    subplotModel.xTick = jsonSubplot["xTick"]
                    subplotModel.yTick = jsonSubplot["yTick"]
                    subplotModel.xTickUser = jsonSubplot["xTickUser"]
                    subplotModel.yTickUser = jsonSubplot["yTickUser"]
                    subplotModel.useUserTicks = jsonSubplot["useUserTicks"]
                    subplotModel.setGrid = jsonSubplot["setGrid"]
                    subplotModel.colorCounter = jsonSubplot["colorCounter"]
                    subplotModel.noOfResFile = jsonSubplot["noOfResFile"]
                    
                    
                    
                    # Load result files data
                    jsonContainedResFile = jsonSubplot["containedResultFiles"]
                    for kk, jsonResFile in enumerate(jsonContainedResFile):
                        resFileModel = ResultFileModel()
                        resFileModel.name = jsonResFile["name"]
                        resFileModel.indx = jsonResFile["indx"]
                        resFileModel.absPath = jsonResFile["absPath"]
                                            
                        resFileModel.signals, resFileModel.signalNames = self.LoadSignalsFromResFile(resFileModel.absPath)
                        
                        # Load selected signal data
                        jsonSelectedSignals = jsonResFile["selectedSignals"]
                        for hh, jsonSelSign in enumerate(jsonSelectedSignals):
                            selectedSignalModel = PlottedSignalModel()
                            selectedSignalModel.name = jsonSelSign["name"]
                            selectedSignalModel.width = jsonSelSign["width"]
                            selectedSignalModel.style = jsonSelSign["style"]
                            selectedSignalModel.marker = jsonSelSign["marker"]
                            selectedSignalModel.color = jsonSelSign["color"]
                            selectedSignalModel.label = jsonSelSign["label"]
                            selectedSignalModel.label = jsonSelSign["name"]
                            selectedSignalModel.units = jsonSelSign["units"]
                            selectedSignalModel.scalingFactor = jsonSelSign["scalingFactor"] 
                            selectedSignalModel.quantity = jsonSelSign["quantity"]
                            selectedSignalModel.indexInResFile = jsonSelSign["indexInResFile"]
                            
                            selectedSignalModel.rawData = resFileModel.signals[selectedSignalModel.indexInResFile].rawData
                            selectedSignalModel.scaledData = [dataPoint*selectedSignalModel.scalingFactor for dataPoint in selectedSignalModel.rawData]
                            
                            # Append PlottedSignal inside the ResultFileModel.selectedSignals
                            resFileModel.selectedSignals.append(selectedSignalModel)
                        
                        jsonXAxisSignals = jsonResFile["xAxisSignal"]
                        for jsonXAxisSignal in jsonXAxisSignals:
                            xAxisSignal = PlottedSignalModel()
                            xAxisSignal.name = jsonXAxisSignal["name"]
                            xAxisSignal.width = jsonXAxisSignal["width"]
                            xAxisSignal.style = jsonXAxisSignal["style"]
                            xAxisSignal.marker = jsonXAxisSignal["marker"]
                            xAxisSignal.color = jsonXAxisSignal["color"]
                            xAxisSignal.label = jsonXAxisSignal["label"]
                            xAxisSignal.label = jsonXAxisSignal["name"]
                            xAxisSignal.units = jsonXAxisSignal["units"]
                            xAxisSignal.scalingFactor = jsonXAxisSignal["scalingFactor"] 
                            xAxisSignal.quantity = jsonXAxisSignal["quantity"]
                            xAxisSignal.indexInResFile = jsonXAxisSignal["indexInResFile"]
                            
                            xAxisSignal.rawData = resFileModel.signals[xAxisSignal.indexInResFile].rawData
                            xAxisSignal.scaledData = [dataPoint*xAxisSignal.scalingFactor for dataPoint in xAxisSignal.rawData]
                            
                        # Use PlottedSignal as xAxisSignal
                        resFileModel.xAxisSignal = xAxisSignal
                        
                        # Append ResultFileModel to SubplotModel.containedResultFiles
                        subplotModel.containedResultFiles.append(resFileModel)
                    
                    # Append the SubplotModel inside the PlotModel.containedSubplots
                    plotModel.containedSubplots.append(subplotModel)
                    
                # Append the PlotModel inside the ProjectModel.containedPlots
                projModel.containedPlots.append(plotModel)      
                
            self.model.projectModel = projModel
         
    def CreateEmptyProject(self):
        '''Create an empty project.'''
        # Create empty project
        projModel = ProjectModel()
        plotModel = PlotModel()
        subplotModel = SubplotModel()
        
        # Append the SubplotModel inside the PlotModel.containedSubplots
        plotModel.containedSubplots.append(subplotModel)
        # Append the PlotModel inside the ProjectModel.containedPlots
        projModel.containedPlots.append(plotModel)      
        # Add the project model into 
        self.model.projectModel = projModel
        
    def SaveProjectModel(self)->None:
        '''Save project model.'''
        
        # Save temporary project file
        tempProjModelLocation = self.model.settings.projectFolder + self.model.settings.projectFileNameTemp
        f = open(tempProjModelLocation, "w")        
        self.SaveProjectToJson(self.model.projectModel,f)
        f.close()
        
        # Verify that the file was properly written
        f = open(tempProjModelLocation,'r')
        saveSuccessful = 1
        try:
            jsonProjMod = json.load(f)
        except:
            saveSuccessful = 0
        f.close()
        
        # If properly written overwrite official .json file
        projModelLocation = self.model.settings.projectFolder + self.model.settings.projectFileName
        if saveSuccessful: 
            copy2(tempProjModelLocation, projModelLocation)            
            self.PrintMessage('Project model saved in ' + projModelLocation)
        else:
            self.PrintMessage("Something went wrong while saving the project in " + projModelLocation)
        
    def SaveProjectToJson(self,projectModel,f)->None:
        f.write('{')
        f.write('"name": "'+ projectModel.name +'",\n')
        f.write('"tabSelected": '+ str(projectModel.tabSelected) +',\n')
        
        f.write('"containedPlots": [\n')
        noOfContainedPlots = len(self.model.projectModel.containedPlots)-1
        for ii,plot in enumerate(self.model.projectModel.containedPlots):
            self.SavePlotToJson(plot,f)
            if ii < noOfContainedPlots:
                f.write(',\n') # Close PlotModel object
        f.write(']\n') # Close containedPlots list
        
        f.write('}\n') # Close the ProjectModel
                
    def SavePlotToJson(self,plotModel,f)->None:
        '''Save PlotModel object to Json.'''
        f.write('{')
        f.write('"name": "'+ plotModel.name +'",\n')
        f.write('"indx": '+ str(plotModel.indx) +',\n')
        f.write('"noOfSubplots": '+ str(plotModel.noOfSubplots) +',\n')
        f.write('"leftMargin": '+ str(plotModel.leftMargin) +',\n')
        f.write('"rightMargin": '+ str(plotModel.rightMargin) +',\n')
        f.write('"bottomMargin": '+ str(plotModel.bottomMargin) +',\n')
        f.write('"topMargin": '+ str(plotModel.topMargin) +',\n')
        
        f.write('"containedSubplots": [\n')
        noOfContainedSubplots = len(plotModel.containedSubplots)-1
        for jj, subplot in enumerate(plotModel.containedSubplots):
            self.SaveSubplotToJson(subplot,f)
            if jj < noOfContainedSubplots:
                f.write(',\n') # Close SubplotModel object
        f.write(']\n') # Close containedSubplots list        
        
        f.write('}\n') # Close PlotModel object
        
    def SaveSubplotToJson(self,subplotModel,f)->None:
        '''Save SubplotModel to Json.'''
        f.write('{')
        f.write('"name": "'+ subplotModel.name +'",\n')
        f.write('"indx": '+ str(subplotModel.indx)+',\n')
        f.write('"isCollapsed": '+ str(subplotModel.isCollapsed) +',\n')
        f.write('"xLabel": "'+ subplotModel.xLabel +'",\n')
        f.write('"yLabel": "'+ subplotModel.yLabel +'",\n')
        f.write('"xLim": ['+ str(float(subplotModel.xLim[0])) + ',' + str(float(subplotModel.xLim[1])) + '],\n')
        f.write('"yLim": ['+ str(float(subplotModel.yLim[0])) + ',' + str(float(subplotModel.yLim[1])) + '],\n')
        f.write('"xLimUser": '+ str(subplotModel.xLimUser) + ',\n')
        f.write('"yLimUser": '+ str(subplotModel.yLimUser) + ',\n')
        f.write('"useUserLim": '+ str(float(subplotModel.useUserLim)) + ',\n')
        f.write('"xTick": '+ str(subplotModel.xTick)+',\n')
        f.write('"yTick": '+ str(subplotModel.yTick)+',\n')
        f.write('"xTickUser": '+ str(subplotModel.xTickUser)+',\n')
        f.write('"yTickUser": '+ str(subplotModel.yTickUser)+',\n')
        f.write('"useUserTicks": '+ str(float(subplotModel.useUserTicks)) +',\n')
        f.write('"setGrid": '+ str(float(subplotModel.setGrid)) +',\n')
        f.write('"colorCounter": '+ str(subplotModel.colorCounter)+',\n')
        f.write('"noOfResFile": '+ str(subplotModel.noOfResFile)+',\n')
        
        # Print Result files
        f.write('"containedResultFiles": [\n')
        noOfResltFile = len(subplotModel.containedResultFiles)-1
        for kk, resultFile in enumerate(subplotModel.containedResultFiles):
            self.SaveResultFileToJson(resultFile,f)
            if kk < noOfResltFile:
                f.write(',\n') # Add a comma in between ResultFile objects
        f.write(']\n') # Close containedResultFiles list
                
        f.write('}\n')
        
    def SaveResultFileToJson(self,resultFile,f)->None:
        '''Save ResultFile object to Json.'''
        f.write('{')
        f.write('"name": "'+ resultFile.name +'",\n')
        f.write('"indx": '+ str(resultFile.indx) +',\n')
        f.write('"absPath": "'+ resultFile.absPath +'",\n')
        
        f.write('"selectedSignals": [\n')
        # Print selected signals
        noOfSelSignals = len(resultFile.selectedSignals)-1
        for hh, selectedSignal in enumerate(resultFile.selectedSignals): 
            self.SavePlottedSignalToJson(selectedSignal,f)
            if hh < noOfSelSignals:
                f.write(',\n') # Close SelectedSignal object
        f.write('],\n') # Close SelectedSignals list
        
        f.write('"xAxisSignal": [')
        self.SavePlottedSignalToJson(resultFile.xAxisSignal,f)
        f.write(']\n')
        
        f.write('}\n')
        
    def SavePlottedSignalToJson(self, plottedSignal, f)->None:
        '''Save PlottedSignal object to Json.'''
        f.write('{')
        f.write('"name": "'+ plottedSignal.name +'",\n')
        f.write('"width": '+ str(plottedSignal.width) +',\n')
        f.write('"style": "'+ plottedSignal.style +'",\n')
        f.write('"marker": "'+ plottedSignal.marker +'",\n')
        f.write('"color": "'+ plottedSignal.color +'",\n')
        f.write('"label": "'+ plottedSignal.label +'",\n')
        f.write('"units": "'+ plottedSignal.units +'",\n')
        f.write('"scalingFactor": '+ str(plottedSignal.scalingFactor)+',\n')
        f.write('"quantity": "'+ plottedSignal.quantity +'"'+',\n')
        f.write('"indexInResFile": '+ str(plottedSignal.indexInResFile)+'\n')
        f.write('}\n')
                              
                              
  
    # PROJECT FOLDER SELECTION

    def BrowseProjectFolder(self)->None:
        """This function allows the user to select a working directory by browsing 
        and store its path in the main control models. """
        # Open the dialog window
        folder = filedialog.askdirectory()
        
        # Update the working folder entry with the selecter folder 
        self.UpdateEntry(self.view.pathSelector.pathEntry,folder)
        # Update model setting
        self.model.settings.projectFolder = folder
        # Set the workign folder of the setting object the same as the content of the entry 
        self.UpdateSettingFile("ProjectFolder", folder)
        
        # Redraw notebook
        self.LoadProject()
                    
    def SetWorkingFolderManually(self,event=None)->None:
        """This function allows the user to select a working directory by copying 
        and pasting in the setting object. """
        workingFolder = self.view.pathSelector.pathEntry.get()
        # Set the workign folder of the setting object the same as the content of the entry 
        # self.UpdateSettingWorkingFolder(workingFolder)
        
    def UpdateWorkingFolder(self,workingFolder)->None: # Deprecated?
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
        
        
        
    # PLOT (TAB) HANDLING
    
    def UpdateSelectedTabIndx(self,event)->None:
        '''Update the selected tab index in the project model.'''
        notebook = event.widget
        selTabName = notebook.select()
        if not selTabName == '':
            selTabIndx = notebook.index(selTabName)
            self.model.projectModel.tabSelected = selTabIndx
        else:
            self.model.projectModel.tabSelected = -1
            
    def AddPlotTab(self)->None:
        '''Add a Plot in the ProjectModel containedPlots list.'''
        # Build default plot model 
        plot = PlotModel()
        # Assign an index to the plot model
        plot.indx = len(self.model.projectModel.containedPlots)
        # Assign name to the plot name
        plot.name = 'Plot ' + str(plot.indx)
        # Append plot model to project model
        self.model.projectModel.containedPlots.append(plot)
        # Set the newly created plot as selected folder
        self.model.projectModel.tabSelected = plot.indx
        # Redraw plot notebook 
        self.RedrawPlotNotebook()
        
    def DeletePlotTab(self)->None:
        '''Delete plot tab.'''
        noOfPlots = len(self.model.projectModel.containedPlots)
        tabSelected = self.model.projectModel.tabSelected
        
        # If the last tab is cancelled
        if tabSelected == noOfPlots-1:
            self.model.projectModel.tabSelected = tabSelected-1
            
        # Find how many tabs are in the notebook
        noOfTabs = len(self.model.projectModel.containedPlots)        
        # Delete the selected tab
        del self.model.projectModel.containedPlots[tabSelected]
        # Redraw plot notebook 
        self.RedrawPlotNotebook()

    def OpenPlotOptions(self,optsButton)->None:
        '''Open plot options'''
        # Create new window
        optsWindowX = optsButton.winfo_rootx()
        optsWindowY = optsButton.winfo_rooty()
        optsWindow = tk.Toplevel(self.view)
        optsWindow.geometry(f"+{optsWindowX}+{optsWindowY}")
        optsWindow.columnconfigure(0,weight=1)
        optsWindow.rowconfigure(0,weight=1)
        optsWindow.resizable(False, False)
        optsWindow.grab_set()        
        
        # Extract subplot options
        plotIndx = self.model.projectModel.tabSelected
        # subplotIndx = plotPane.index
        plotModel = self.model.projectModel.containedPlots[plotIndx]
        
        # Populate the subplotOptions 
        plotOption = PlotOptions(optsWindow,
                                    self,
                                    plotModel)
        plotOption.grid(row=0,column=0,sticky = 'NEWS')
        
    def ApplyPlotOptions(self,plotOptionsPane)->None:
        '''Apply plot options.'''
        # Retrieve the plot index from the tab selection 
        plotIndx = self.model.projectModel.tabSelected

        # Extract subplot options
        self.model.projectModel.containedPlots[plotIndx].name = plotOptionsPane.titleEntry.get()
        self.model.projectModel.containedPlots[plotIndx].leftMargin = float(plotOptionsPane.plotMarginLeft.get())
        self.model.projectModel.containedPlots[plotIndx].rightMargin = float(plotOptionsPane.plotMarginRight.get())
        self.model.projectModel.containedPlots[plotIndx].bottomMargin = float(plotOptionsPane.plotMarginBottom.get())
        self.model.projectModel.containedPlots[plotIndx].topMargin = float(plotOptionsPane.plotMarginTop.get())
        
        # Redraw notebook
        self.RedrawPlotNotebook()
        
    def ClosePlotOptions(self,plotOptionsPane)->None:
        '''Apply plot options.'''
        # Destroy the window containing the plotOptionsPane
        plotOptionsPane.parent.destroy()
        
    def OkPlotOptions(self,plotOptionsPane)->None:
        '''Apply plot options.'''
        # Apply the plot options
        self.ApplyPlotOptions(plotOptionsPane)
        # Close the plot options
        self.ClosePlotOptions(plotOptionsPane)
     
     
     
    # SUBPLOT HANDLING
    
    def AddSubplot(self,plotManager)->None:
        '''Add subplot to PlotManager and Plot.
        Add a toggle frame to the plot manager pane.'''
        # Get useful information 
        notebook = self.view.projectNotebook
        plotIndx = self.model.projectModel.tabSelected

        noOfSubplot = self.model.projectModel.containedPlots[plotIndx].noOfSubplots
        
        # Create SubplotModel
        subplot = SubplotModel()
        subplot.name = str(noOfSubplot)
        subplot.indx = noOfSubplot
        
        # Update PlotModel adding a SubplotModel
        self.model.projectModel.containedPlots[plotIndx].AddSubplot(subplot)
        
        self.RedrawPlotNotebook()
         
    def DeleteSubplot(self,subplotPane)->None:
        '''Delete a toggle pane and connected subplot.'''        
        # Update PlotModel deleting the SubplotModel
        plotIndx = self.model.projectModel.tabSelected
        del self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotPane.index]
        
        self.RedrawPlotNotebook()
           
    def SelectXAxis(self,event,subplotPane)->None:
        '''Function invoked when an item is selected from the subplot X axis selection.'''
        # Identify the widget indexes
        plotIndx = self.model.projectModel.tabSelected
        subplotIndx = subplotPane.index
        # Extract the list of signals tht can be selected as x axis
        xAxisSignals = self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].xAxisSignals
        # Find the index of the signal selected
        selectedSigNo = subplotPane.xAxisSelect.current()        
        # Update the subplotModel 
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].xAxisSelected = xAxisSignals[selectedSigNo]
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].xAxisSelectedIndx = selectedSigNo
        
        # Redraw PlotUI
        self.RedrawPlotNotebook()
                
    def SaveSubplotStateIntoModel(self,subplotPane)->None:
        '''Save state into model'''
        plotIndx = self.model.projectModel.tabSelected
        subplotIndx = subplotPane.index
        
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].isCollapsed = subplotPane.isCollapsed
                
                
                
    # SUBPLOT OPTIONS
    
    def OpenSubplotOptions(self,subplotPane, subplotOptsBtn)->None:
        '''Open subplot options.'''   
        # Create new window
        optsWindowX = subplotOptsBtn.winfo_rootx()
        optsWindowY = subplotOptsBtn.winfo_rooty()
        optsWindow = tk.Toplevel(self.view)
        optsWindow.geometry(f"+{optsWindowX}+{optsWindowY}")
        optsWindow.columnconfigure(0,weight=1)
        optsWindow.rowconfigure(0,weight=1)
        optsWindow.resizable(False, False)
        optsWindow.grab_set()        
        
        # Extract subplot options
        plotIndx = self.model.projectModel.tabSelected
        subplotIndx = subplotPane.index
        subplot=self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx]
        
        # Populate the subplotOptions 
        subplotOption = SubplotOptions(optsWindow,
                                       self,
                                       subplotIndx,
                                       title = subplot.name,
                                       xLabel = subplot.xLabel,
                                       yLabel = subplot.yLabel,
                                       xLim = subplot.xLimUser,
                                       yLim = subplot.yLimUser,
                                       useUserLim = subplot.useUserLim,
                                       xTick = subplot.xTickUser,
                                       yTick = subplot.yTickUser,
                                       useUserTicks=subplot.useUserTicks,
                                       setGrid = subplot.setGrid)
        subplotOption.grid(row=0,column=0,sticky = 'NEWS')
    
    def ApplySubplotOptions(self,subplotOptionsPane)->None:
        '''Apply the subplot options to the subplot model.'''
        # Store options in the subplot model
        plotIndx = self.model.projectModel.tabSelected
        subplotIndx = subplotOptionsPane.index
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].name = subplotOptionsPane.titleEntry.get()
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].xLabel = subplotOptionsPane.xAxisLabEntry.get()
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].yLabel = subplotOptionsPane.yAxisLabEntry.get()
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].xLimUser = [float(subplotOptionsPane.xAxisLowLimEntry.get()), float(subplotOptionsPane.xAxisUpLimEntry.get())]
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].yLimUser = [float(subplotOptionsPane.yAxisLowLimEntry.get()), float(subplotOptionsPane.yAxisUpLimEntry.get())]
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].useUserLim = float(subplotOptionsPane.userLimVar.get())
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].xTickUser = float(subplotOptionsPane.xAxisTicksEntry.get())
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].yTickUser = float(subplotOptionsPane.yAxisTicksEntry.get())
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].useUserTicks = float(subplotOptionsPane.userTicksVar.get())
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].setGrid = float(subplotOptionsPane.gridVar.get())
        
        self.RedrawPlotNotebook()
        
    def CloseSubplotOptions(self,subplotOptionsPane)->None:
        '''Close subplot options.'''
        subplotOptionsPane.parent.destroy()
        
    def OkSubplotOptions(self, subplotOptionsPane)->None:
        '''Ok Subplot Options'''
        self.ApplySubplotOptions(subplotOptionsPane)
        self.CloseSubplotOptions(subplotOptionsPane)
        

        
    # RESULT FILE HANDLING
        
    def AddResultFile(self, subplotPane)->None:
        '''Add ResultFile to Subplot.'''
        # Get useful information 
        noOfResFile = subplotPane.noOfRows
        plotIndx = self.model.projectModel.tabSelected
        subplotIndx = subplotPane.index
        # Create ResFileModel
        resultFileModel = ResultFileModel()
        resultFileModel.name = str(noOfResFile)
        resultFileModel.indx = noOfResFile
        
        # Update SubplotModel adding a ResultFile
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles.append(resultFileModel)
        
        
        self.RedrawPlotNotebook()
        
    def DeleteResultFile(self,resFilePane)->None:
        '''Delete ResultFile from the model and redraw the PlotManager.'''
        subplotIndx = resFilePane.master.master.master.index
        plotIndx = self.model.projectModel.tabSelected
        
        # Update SubplotModel adding a ResultFile
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].DeleteResultFile(resFilePane)
        
        self.RedrawPlotNotebook()
        
    def BrowseResFile(self,fileSelector,resFilePane) -> None:
        '''This function allows the selection of a file.'''
        # Open the dialog window
        filePath = filedialog.askopenfilename()
        
        # Update the entry text
        if not filePath:
            '''Don't do anything.'''
        else: 
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
                
        # Retrieve useful info
        plotIndx = self.model.projectModel.tabSelected
        subplotIndx = resFilePane.master.master.master.index
        resFileIndx = resFilePane.index
        
        # Store the filepath
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].absPath = filePath
        
        # Load the signals into signal names
        signals, signalNames = self.LoadSignalsFromResFile(filePath)
        
        # Store the signals and signal names in the model
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].signals = signals
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].signalNames = signalNames
        
        # Set the first signal of the file as X axis by default
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].xAxisSignal = signals[0]
        
        self.RedrawPlotNotebook()

        
        
    # SIGNAL HANDLING
    
    def AddXAxisSignal(self, event,resFilePane)->None:
        '''Set the X Axis signal used in the result file model.'''
        # Get useful information
        plotIndx = self.model.projectModel.tabSelected
        subplotIndx = resFilePane.master.master.master.index
        resFileIndx = resFilePane.index
        
        # Find the index of the signal selected
        selectedSigIndex = event.widget.current()
        # selectedSigIndex = resFilePane.signalList.index(selectedSigName)
        # Extract from the ResultFileModel the signal selected
        signalToPlot = self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].signals[selectedSigIndex]
        
        # Create a PlottedSignal instance 
        plottedSignal = PlottedSignalModel()
        # Copy the signal properties into the PlottedSignal
        plottedSignal.CopySignalProperties(signalToPlot)
        # Assign the PlottedSignal a dummy color
        plottedSignal.color='#000000'
        
        # Add it to the ResultFilePane selectedSignals list (for the left pane with the plot controls)
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].xAxisSignal = plottedSignal
        
        # self.model.projectModel.tabSelected = self.view.projectNotebook.get()
        self.RedrawPlotNotebook()
    
    def AddSignal(self,event, resFilePane)->None:
        '''Moves one signal from the ResultModel to the PlottedSignal.'''
        # Get useful information
        plotIndx = self.model.projectModel.tabSelected
        subplotIndx = resFilePane.master.master.master.index
        resFileIndx = resFilePane.index
        
        # Find the index of the signal selected
        selectedSigIndex = event.widget.current()
        # Extract from the ResultFileModel the signal selected
        signalToPlot = self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].signals[selectedSigIndex]
        
        # Create a PlottedSignal instance 
        plottedSignal = PlottedSignalModel()
        # Copy the signal properties into the PlottedSignal
        plottedSignal.CopySignalProperties(signalToPlot)
        # Extract color counter from subplot
        colorCounter = self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].colorCounter
        # Assign the PlottedSignal a color
        rgbTuple = self.ChooseSignalColor(colorCounter)
        plottedSignal.color=rgbTuple
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].colorCounter=colorCounter+1
        
        # Add it to the ResultFilePane selectedSignals list (for the left pane with the plot controls)
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].selectedSignals.append(plottedSignal)
        
        self.RedrawPlotNotebook()
        
    def DeleteSignal(self, signalPane)->None:
        '''Delete signal.'''
        # Extract indexes
        signalIndx = signalPane.index
        resFilePaneIntern = signalPane.master
        resFilePane = signalPane.master.master
        resFileIndx = resFilePane.index
        collapsPaneIntern = signalPane.master.master.master
        collapsPane = signalPane.master.master.master.master
        subplotPane = signalPane.master.master.master.master.master
        subplotIndx = subplotPane.index
        plotIndx = self.model.projectModel.tabSelected
        
        # Remove signal from ResultFileModel selectedSignals list
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].selectedSignals.pop(signalIndx)
        
        self.RedrawPlotNotebook()
    
    def ModifyXSignalScaling(self,event,signalPane, scalingList)->None:
        '''Change the scaling of the signal.'''
        # Get the combobox index, string, and scaling factor
        optNoSelected = signalPane.unitsCb.current()
        optStrSelected = event.widget.get()
        scalingFactor = scalingList[optNoSelected]
        
        # Extract indexes
        signalIndx = signalPane.index
        resFilePaneIntern = signalPane.master
        resFilePane = signalPane.master.master
        resFileIndx = resFilePane.index
        collapsPaneIntern = signalPane.master.master.master
        collapsPane = signalPane.master.master.master.master
        subplotPane = signalPane.master.master.master.master.master
        subplotIndx = subplotPane.index
        plotIndx = self.model.projectModel.tabSelected
        
        # Extract row data and calculate scaled data
        rawData = self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].xAxisSignal.rawData
        scaledData = [scalingFactor*val for val in rawData] 
        # Save new units, scaling factor, and scaled data
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].xAxisSignal.units = optStrSelected
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].xAxisSignal.scalingFactor = scalingFactor
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].xAxisSignal.scaledData = scaledData
        
        # Redraw PlotUI
        self.RedrawPlotNotebook()
            
    def ModifySignalScaling(self,event,signalPane, scalingList)->None:
        '''Change the scaling of the signal.'''
        # Get the combobox index, string, and scaling factor
        optNoSelected = signalPane.unitsCb.current()
        optStrSelected = event.widget.get()
        scalingFactor = scalingList[optNoSelected]
        
        # Extract indexes
        signalIndx = signalPane.index
        resFilePaneIntern = signalPane.master
        resFilePane = signalPane.master.master
        resFileIndx = resFilePane.index
        collapsPaneIntern = signalPane.master.master.master
        collapsPane = signalPane.master.master.master.master
        subplotPane = signalPane.master.master.master.master.master
        subplotIndx = subplotPane.index
        plotIndx = self.model.projectModel.tabSelected
        
        # Extract row data and calculate scaled data
        rawData = self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].selectedSignals[signalIndx].rawData
        scaledData = [scalingFactor*val for val in rawData] 
        # Save new units, scaling factor, and scaled data
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].selectedSignals[signalIndx].units = optStrSelected
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].selectedSignals[signalIndx].scalingFactor = scalingFactor
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].selectedSignals[signalIndx].scaledData = scaledData
        
        # Redraw PlotUI
        self.RedrawPlotNotebook()
        
    def GetUnitsList(self,signal):
        '''Depending on the signal units, create the list of the possible units that
        the signal can be converted to. '''
        
        # First unit is always the default units
        if signal.quantity == 'Time':
            unitList = ['s','m','h']
            scalingList = [1, 0.01666666666, 0.00027777777]
            
        elif signal.quantity == 'Length':
            unitList = ['m','cm','mm','um']
            scalingList = [1, 1e-2, 1e-3, 1e-6]
            
        elif signal.quantity == 'Area':
            unitList = ['m^2','cm^2','mm^2','um^2']
            scalingList = [1, 1e-4, 1e-6, 1e-12]
            
        elif signal.quantity == 'Volume':
            unitList = ['m^3','cm^3','mm^3','um^3']
            scalingList = [1, 1e-6, 1e-9, 1e-18]
            
        elif signal.quantity == 'Flow':
            unitList = ['m^3/s','cm^3/s','mm^3/s','L/s','L/min','gal/min']
            scalingList = [1, 1e6, 1e9, 1e3, 1e3/60,  264.172052/60]
            
        elif signal.quantity == 'Pressure':
            unitList = ['Pa','MPa','bar']
            scalingList = [1, 1e-6, 1e-5]
        else:
            unitList = [signal.units]
            scalingList = [1]            

        return unitList, scalingList
        
     # Signal Options
    
    def ChooseSignalColor(self,colorCounter):
        '''Choose the color of a PlottedSignal based on how many signals have been
        plotted in that specific plot. Colors taken from the color-blind friendly palette Okabe-Ito.
        https://siegal.bio.nyu.edu/color-palette/'''
        
        colorList = ['#000000',     # Black
                     '#E69F00',     # Orange    
                     '#56B4E9',     # Light blue
                     '#009E73',     # Green
                     '#F0E442',     # Yellow    
                     '#0072B2',     # Blue
                     '#D55E00',     # Red
                     '#CC79A7']     # Pink
        
        noOfColors = len(colorList)
        colorCounterRem = colorCounter%noOfColors
        
        return colorList[colorCounterRem]
        
        
        
    # SIGNAL OPTIONS
    
    def OpenSignalOptions(self,signalPane, signalOptsBtn)->None:
        '''Open subplot options.'''   
        # Create new window
        optsWindowX = signalOptsBtn.winfo_rootx()
        optsWindowY = signalOptsBtn.winfo_rooty()
        optsWindow = tk.Toplevel(self.view)
        optsWindow.title("Signal Options")
        optsWindow.geometry("260x150")
        optsWindow.geometry(f"+{optsWindowX}+{optsWindowY}")
        optsWindow.columnconfigure(0,weight=1)
        optsWindow.rowconfigure(0,weight=1)
        optsWindow.resizable(False, False)
        optsWindow.grab_set()  
        
        # Extract indexes
        signalIndx = signalPane.index
        resFilePaneIntern = signalPane.master
        resFilePane = signalPane.master.master
        resFileIndx = resFilePane.index
        collapsPaneIntern = signalPane.master.master.master
        collapsPane = signalPane.master.master.master.master
        subplotPane = signalPane.master.master.master.master.master
        subplotIndx = subplotPane.index
        plotIndx = self.model.projectModel.tabSelected
        
        # Get the PlottedSignal object to retrieve its property
        signal = self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resFileIndx].selectedSignals[signalIndx]
        
        # Create a SignalOptions pane
        signalOpts = SignalOptions(optsWindow,
                                   self,
                                   signal,
                                   sigIndx= signalIndx,
                                   resIndx = resFileIndx,
                                   subplotIndx = subplotIndx)
        signalOpts.grid(row=0,column=0,sticky='NEWS')
    
    def ApplySignalOptions(self,signalOptions)->None:
        '''Apply signal options.'''    
        # Get the index of the subplot, result file, and signal
        
        sigIndx = signalOptions.sigIndx
        resIndx = signalOptions.resIndx
        subplotIndx = signalOptions.subplotIndx
        plotIndx = self.model.projectModel.tabSelected
        
        
        # Get the signal options values
        lineWidth = float(signalOptions.lineWidthCb.get())
        lineStyle = signalOptions.lineStyleCb.get()
        lineMarker = signalOptions.GetMarkerOpts()
        color= signalOptions.selectedColor
        
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resIndx].selectedSignals[sigIndx].color=color
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resIndx].selectedSignals[sigIndx].width=lineWidth
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resIndx].selectedSignals[sigIndx].style=lineStyle
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].containedResultFiles[resIndx].selectedSignals[sigIndx].marker=lineMarker
               
        self.RedrawPlotNotebook()
        
    def CloseSignalOptions(self,signalOptionsPane)->None:
        '''Close signal options.'''
        signalOptionsPane.parent.destroy()
        
    def OkSignalOptions(self,signalOptionsPane)->None:
        '''Apply the changes and close the window.'''
        self.ApplySignalOptions(signalOptionsPane)
        self.CloseSignalOptions(signalOptionsPane)
        


  # LOAD SIGNALS
             
    def LoadSignalsFromResFile(self,filePath):
        '''Load results.'''       
        # Read results file
        file = open(filePath,'r')
        lines = file.readlines()
        file.close()
        
        # Initialize lists 
        signals = []
        signalNames = []
        
        # Create the list of signals
        headerTokens = lines[0].split(',')
        headerTokens = headerTokens[:-1]
        for i, headerToken in enumerate(headerTokens):
            headerToken = headerToken.strip() 
            signalTokens = headerToken.split(':')
            name = signalTokens[:-1]
            name = ":".join(name)
            units = signalTokens[-1]
            sigQuantity = self.DetermineSignalQuantity(name,units)
            sigTemp = SignalModel(name=name,units=units,quantity=sigQuantity,indexInResFile=i)
            signals.append(sigTemp)
            signalNames.append(name)
        
        # Iterate on the lines - skip the first one
        for line in lines[1:]:
            valueTokens = line.split(',')
            valueTokens = valueTokens[:-1]
            for i, valueStr in enumerate(valueTokens):
                if valueStr == "":
                    continue
                
                value = float(valueStr) 
                signals[i].AppendData(value)
                
        return signals, signalNames
             
    def DetermineSignalQuantity(self,name,units)->str:
        '''Take the unit of the signal, and determine its quantity.'''
        if units == 's':
            return 'Time'
        
        elif units == 'm':
            return 'Length'
        
        elif units == 'm^2':
            return 'Area'
        
        elif units == 'm^3':
            return 'Volume'
        
        elif units == 'm^3/s':
            return 'Flow'
        
        elif units == 'Pa':
            return 'Pressure'
        
        elif units == 'Pa*s':
            return 'BulkModulus'
        
        elif units == '-':
            return 'Ratio'        
        
        else:
            print('Units of signal ' + name + ' not found.')



    # REDRAW GUI
    
    def RedrawPlotNotebook(self)->None:
        '''Redraw plot tab.'''
        
        self.view.projectNotebook.unbind("<<NotebookTabChanged>>")
        
        # Delete existing tabs
        tabs = self.view.projectNotebook.tabs()
        for ii, tab in enumerate(self.view.projectNotebook.tabs()):
             self.view.projectNotebook.forget(tab)
        # Redraw tabs
        for ii,plot in enumerate(self.model.projectModel.containedPlots):
            plotPane = PlotPane(self.view.projectNotebook,self,ii)
            if plot.name == '':
                self.view.projectNotebook.add(plotPane, text = "Plot " + str(ii))
            else:
                self.view.projectNotebook.add(plotPane, text = plot.name)
                
            # Clear all the existing subplots, and create the axis for the new ones
            plotCanvasChildren = plotPane.plotCanvas.winfo_children()
            for ii,child in enumerate(plotCanvasChildren):
                plt.close()
                child.destroy()
                
            noOfSubplots = len(plot.containedSubplots)
            if noOfSubplots>0:
                
                fig, axList = plt.subplots(noOfSubplots,1, squeeze=False)
                plt.subplots_adjust(left=plot.leftMargin, right=plot.rightMargin, top=plot.topMargin, bottom=plot.bottomMargin)
                
                # REDRAW PLOT MANAGER ==========================
                # Redraw subplots
                for jj, subplot in enumerate(plot.containedSubplots):
                    axList[jj,0].grid(subplot.setGrid)
                    subplotPane = SubplotPane(plotPane.plotManager.interior,
                                            self, 
                                            jj,
                                            subplot)
                    subplotPane.grid(row=jj,column=0,padx = [6,0],pady = [3,0],sticky='NEW')
                    
                    # PLOT CANVAS ==========================
                    # Title
                    axList[jj,0].title.set_text(subplot.name)
                    # Labels
                    axList[jj,0].set_xlabel(subplot.xLabel)
                    axList[jj,0].set_ylabel(subplot.yLabel)
                    # Grid
                    axList[jj,0].grid(subplot.setGrid)
                    # Axis Limits                        
                    if subplot.useUserLim:
                        axList[jj,0].set_xlim(subplot.xLimUser)
                        
                    if subplot.useUserLim:
                        axList[jj,0].set_ylim(subplot.yLimUser)
                                               
                    # Ticks
                    if bool(subplot.useUserTicks) & (subplot.xTickUser!=0):
                        currTickX = list(axList[jj,0].get_xlim())
                        tickVectX = np.arange(currTickX[0],currTickX[1], subplot.xTickUser).tolist()
                        axList[jj,0].set_xticks(tickVectX)
                        
                    if bool(subplot.useUserTicks) & (subplot.yTickUser!=0):
                        currTickY = list(axList[jj,0].get_ylim())
                        tickVectY = np.arange(currTickY[0],currTickY[1],subplot.yTickUser).tolist()
                        axList[jj,0].set_yticks(tickVectY)

        
                    # Draw result files 
                    for kk, resultFile in enumerate(subplot.containedResultFiles):
                        # PLOT MANAGER ==========================
                        resFile = ResFilePane(subplotPane.interior,
                                            self,
                                            index = kk,
                                            entryText=resultFile.absPath,
                                            comboboxList=resultFile.signalNames)
                        resFile.grid(row=kk,column=0,padx = [6,0],sticky='NEW')

                        
                                
                        # PLOT MANAGER ==========================
                        # If there is an X and Y signals selected plot
                        if not resultFile.xAxisSignal.name == '':
                            xAxisSignal = resultFile.xAxisSignal                        
                            xSigPane = SignalPaneX(   resFile.xAxisInterior,
                                                        self,
                                                        xAxisSignal)
                            xSigPane.grid(row=0,column=0,sticky='EW')
                        
                        # Redraw selected signals
                        for hh, selectedSignal in enumerate(resultFile.selectedSignals): 
                            sigPane = SignalPane(   resFile.yAxisInterior,
                                                    self,
                                                    selectedSignal,
                                                    index = hh)
                            sigPane.grid(row=hh,column=0,sticky='EW')
                            
                        
                            if not resultFile.xAxisSignal.name == '':
                                # PLOT CANVAS ==========================
                                # Extract plotted signals and plot them
                                plottedSig = selectedSignal
                                
                                psCol=plottedSig.color
                                psWidth=plottedSig.width
                                psStyle=plottedSig.style
                                psMarker=plottedSig.marker
                                psLabel=plottedSig.label
                                axList[jj,0].plot(xAxisSignal.scaledData,selectedSignal.scaledData,
                                                    color=psCol,
                                                    linewidth=psWidth,
                                                    linestyle=psStyle,
                                                    marker=psMarker,
                                                    label=psLabel)
                                axList[jj,0].legend()
                            
                                # Extract subplot default settings
                                subplot.xLim = list(axList[jj,0].get_xlim())
                                subplot.yLim = list(axList[jj,0].get_ylim())
                                yTicksArray = axList[jj,0].get_yticks()
                                xTicksArray = axList[jj,0].get_xticks()
                                xTicks = float(xTicksArray[1]) - float(xTicksArray[0])
                                yTicks = float(yTicksArray[1]) - float(yTicksArray[0])
                                subplot.xTick = xTicks
                                subplot.yTick = yTicks
                            
                            
                                    
                            
                # Draw the canvas and toolbar inside the Plotter object
                plotPane.plotCanvas.canvas = FigureCanvasTkAgg(fig, master=plotPane.plotCanvas)
                plotPane.plotCanvas.toolbar = NavigationToolbar2Tk(plotPane.plotCanvas.canvas, plotPane.plotCanvas)
      
                plotPane.plotCanvas.toolbar.update()
                plotPane.plotCanvas.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
                plotPane.plotCanvas.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            
        # Move to the newly created tab
        self.view.projectNotebook.select(self.model.projectModel.tabSelected)
        
        self.view.projectNotebook.bind("<<NotebookTabChanged>>", self.UpdateSelectedTabIndx)
        
    def UpdateEmpty(self, event)->None:
        '''Empty function'''
        
        
        
    # TEXT
    
    def PrintMessage(self, message)->None:
        '''Print message.'''
        message = message +'\n'
        self.view.textPane.text.config(state='normal')
        self.view.textPane.text.insert(tk.END,message)
        self.view.textPane.text.config(state='disabled')
        
    def PrintError(self, message)->None:
        '''Print error'''
        message = message +'\n'
        self.view.textPane.text.config(state='normal')
        self.view.textPane.text.tag_configure("red_text",foreground='red')
        self.view.textPane.text.insert(tk.END,message,"red_text")
        self.view.textPane.text.config(state='normal')
        

    # PYINSTALLER UTILITIES
    
    def ResourcePath(self,relative_path):
        """
        https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
        Get absolute path to resource, works for dev and for PyInstaller.
        Wherever there is a path to an asset, wrap the path to that asset in this function.
        For example:
        
        Logo = ResourcePath("Logo.png")
        """
        
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)