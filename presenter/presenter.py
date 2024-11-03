import tkinter as tk
from tkinter import filedialog, ttk
import os
import json
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

from ui.PlotPane import PlotPane
from ui.CollapsiblePane import TogglePaneDelOpts
from ui.ResFileManager import ResFileManager
from ui.ResFilePane import ResFilePane
from ui.SignalPane import SignalPane
from ui.SubplotOptions import SubplotOptions
from ui.SignalOptions import SignalOptions
from ui.SubplotPane import SubplotPane

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
        self.view.initUI(self)
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
        self.model.settings.projectFolder = settingDict.get("ProjectFolder")

        # Update entries
        self.UpdateEntry(self.view.pathSelector.pathEntry,settingDict.get("ProjectFolder"))
    
    
    
    # JSON HANDLING
    
    def LoadProjectModel(self) -> None:
        '''Load project from JSON.'''
        # Check that a ProjectModel.json exists
        projectModelPath = self.model.settings.projectFolder + "/ProjectModel.json"
        projectModelFileExists = os.path.exists(projectModelPath)
        if (projectModelFileExists):
            print('Project file found at: ' + projectModelPath)
        else:
            print(' file not found at: ' + projectModelPath)
            
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
                # subplotModel.containedResultFiles = jsonSubplot["containedResultFiles"]
                # subplotModel.plottedSignals = jsonSubplot["plottedSignals"]
                
                subplotModel.xAxisSelectedIndx = jsonSubplot["xAxisSelectedIndx"]
                
                
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
                        selectedSignalModel.indx = jsonSelSign["indx"]
                        selectedSignalModel.width = jsonSelSign["width"]
                        selectedSignalModel.style = jsonSelSign["style"]
                        selectedSignalModel.marker = jsonSelSign["marker"]
                        selectedSignalModel.color = jsonSelSign["color"]
                        selectedSignalModel.label = jsonSelSign["label"]
                        selectedSignalModel.label = jsonSelSign["name"]
                        selectedSignalModel.units = jsonSelSign["units"]
                        selectedSignalModel.scalingFactor = jsonSelSign["scalingFactor"] 
                        selectedSignalModel.quantity = jsonSelSign["quantity"]
                        selectedSignalModel.indxInResFile = jsonSelSign["indxInResFile"]
                        
                        selectedSignalModel.rawData = resFileModel.signals[selectedSignalModel.indxInResFile].rawData
                        selectedSignalModel.scaledData = [dataPoint*selectedSignalModel.scalingFactor for dataPoint in selectedSignalModel.rawData]
                        
                        # Append PlottedSignal inside the ResultFileModel.selectedSignals
                        resFileModel.selectedSignals.append(selectedSignalModel)
                    
                    # Append ResultFileModel to SubplotModel.containedResultFiles
                    subplotModel.containedResultFiles.append(resFileModel)

                
                subplotModel.xAxisSignals = subplotModel.containedResultFiles[0].signals
                subplotModel.xAxisSignalsName = subplotModel.containedResultFiles[0].signalNames
                subplotModel.xAxisSelected = subplotModel.containedResultFiles[0].signals[subplotModel.xAxisSelectedIndx]
                subplotModel.xAxisSelectedName = subplotModel.containedResultFiles[0].signals[subplotModel.xAxisSelectedIndx].name
                
                
                # Load plotted signals data
                jsonPlottedSignals = jsonSubplot["plottedSignals"]
                for ll, jsonPlottedSignal in enumerate(jsonPlottedSignals):
                    plottedSignalModel = PlottedSignalModel()
                    plottedSignalModel.name = jsonPlottedSignal["name"]
                    plottedSignalModel.indx = jsonPlottedSignal["indx"]
                    plottedSignalModel.width = jsonPlottedSignal["width"]
                    plottedSignalModel.style = jsonPlottedSignal["style"]
                    plottedSignalModel.marker = jsonPlottedSignal["marker"]
                    plottedSignalModel.color = jsonPlottedSignal["color"]
                    plottedSignalModel.label = jsonPlottedSignal["label"]
                    plottedSignalModel.label = jsonPlottedSignal["name"]
                    plottedSignalModel.units = jsonPlottedSignal["units"]
                    plottedSignalModel.scalingFactor = jsonPlottedSignal["scalingFactor"] 
                    plottedSignalModel.quantity = jsonPlottedSignal["quantity"]
                    plottedSignalModel.indxInResFile = jsonSelSign["indxInResFile"]
                    
                    plottedSignalModel.rawData = resFileModel.signals[selectedSignalModel.indxInResFile].rawData
                    plottedSignalModel.scaledData = [dataPoint*plottedSignalModel.scalingFactor for dataPoint in plottedSignalModel.rawData]
                    
                    subplotModel.plottedSignals.append(plottedSignalModel)
                    
                # Append the SubplotModel inside the PlotModel.containedSubplots
                plotModel.containedSubplots.append(subplotModel)
                
            # Append the PlotModel inside the ProjectModel.containedPlots
            projModel.containedPlots.append(plotModel)      
            
        self.model.projectModel = projModel
         
        # Plot Manager
    
    def SaveProjectModel(self)->None:
        '''Save project model.'''
        
        f = open("ProjectModelSave.json", "w")
        
        self.SaveProjectToJson(self.model.projectModel,f)
        
    def SaveProjectToJson(self,projectModel,f)->None:
        f.write('{')
        f.write('"name": "'+ projectModel.name +'",\n')
        f.write('"tabSelected": '+ str(projectModel.tabSelected) +',\n')
        f.write('"containedPlots": [\n')
        
        noOfContainedPlots = len(self.model.projectModel.containedPlots)-1
        for ii,plot in enumerate(self.model.projectModel.containedPlots):
            self.SavePlotToJson(plot,f)
            
            if ii < noOfContainedPlots:
                f.write('}\n,\n') # Close PlotModel object
            else:
                f.write('}\n]\n') # Close containedPlots list
                    
            f.write('}') # Close the ProjectModel
                
    def SavePlotToJson(self,plotModel,f)->None:
        '''Save PlotModel object to Json.'''
        f.write('{')
        f.write('"name": "'+ plotModel.name +'",\n')
        f.write('"indx": '+ str(plotModel.indx) +',\n')
        f.write('"noOfSubplots": '+ str(plotModel.noOfSubplots) +',\n')
        f.write('"containedSubplots": [\n')
        
        # print subplots
        noOfContainedSubplots = len(plotModel.containedSubplots)-1
        for jj, subplot in enumerate(plotModel.containedSubplots):
            self.SaveSubplotToJson(subplot,f)
            
            if jj < noOfContainedSubplots:
                f.write('}\n,\n') # Close SubplotModel object
            else:
                f.write('}\n]\n') # Close containedSubplots list
               
    def SaveSubplotToJson(self,subplotModel,f)->None:
        '''Save SubplotModel to Json.'''
        f.write('{')
        f.write('"name": "'+ subplotModel.name +'",\n')
        f.write('"indx": '+ str(subplotModel.indx)+',\n')
        f.write('"isCollapsed": '+ str(subplotModel.isCollapsed) +',\n')
        f.write('"xLabel": "'+ subplotModel.xLabel +'",\n')
        f.write('"yLabel": "'+ subplotModel.yLabel +'",\n')
        f.write('"xLim": '+ str(subplotModel.xLim) + ',\n')
        f.write('"yLim": '+ str(subplotModel.yLim) + ',\n')
        f.write('"xLimUser": '+ str(subplotModel.xLimUser) + ',\n')
        f.write('"yLimUser": '+ str(subplotModel.yLimUser) + ',\n')
        f.write('"useUserLim": '+ str(subplotModel.useUserLim) + ',\n')
        f.write('"xTick": '+ str(subplotModel.xTick)+',\n')
        f.write('"yTick": '+ str(subplotModel.yTick)+',\n')
        f.write('"xTickUser": '+ str(subplotModel.xTickUser)+',\n')
        f.write('"yTickUser": '+ str(subplotModel.yTickUser)+',\n')
        f.write('"useUserTicks": '+ str(subplotModel.useUserTicks)+',\n')
        f.write('"setGrid": '+ str(subplotModel.setGrid)+',\n')
        f.write('"colorCounter": '+ str(subplotModel.colorCounter)+',\n')
        f.write('"noOfResFile": '+ str(subplotModel.noOfResFile)+',\n')
        f.write('"xAxisSelectedIndx": '+ str(subplotModel.xAxisSelectedIndx)+',\n')
        
        # Print Result files
        f.write('"containedResultFiles": [\n')
        noOfResltFile = len(subplotModel.containedResultFiles)-1
        for kk, resultFile in enumerate(subplotModel.containedResultFiles):
            self.SaveResultFileToJson(resultFile,f)

            if kk < noOfResltFile:
                f.write('}\n,\n') # Close ResultFile object
            else:
                f.write('}\n],\n') # Close containedResultFiles list
                
        # Print Plotted signals
        f.write('"plottedSignals": [\n')        
        noOfPlottedSignals = len(subplotModel.plottedSignals)-1
        for kk, plottedSignal in enumerate(subplotModel.plottedSignals):
            self.SavePlottedSignalToJson(plottedSignal,f)

            if kk < noOfPlottedSignals:
                f.write(',\n') # Close ResultFile object
            else:
                f.write(']\n') # Close containedResultFiles list
        
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
            else:
                f.write(']\n') # Close SelectedSignals list
        
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
        f.write('"indx": '+ str(plottedSignal.indx)+',\n')
        f.write('"indxInResFile": '+ str(plottedSignal.indxInResFile)+'\n')
        f.write('}'+'\n')
                              
                              
  
    # PROJECT FOLDER SELECTION
    
    def BrowseProjectFolder(self)->None:
        """This function allows the user to select a working directory by browsing 
        and store its path in the main control models. """
        # Open the dialog window
        folder = filedialog.askdirectory()
        # Update the working folder entry with the selecter folder 
        self.UpdateEntry(self.view.pathSelector.pathEntry,folder)
        # Update model setting
        self.model.settings.workingFolder = folder
        # Set the workign folder of the setting object the same as the content of the entry 
        self.UpdateSettingFile("ProjectFolder", folder)
                    
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

    def ReloadResults(self)->None: # Deprecated?
        '''Reload results.'''
        for ii,sp in enumerate(self.model.projectModel.plotModel.containedSubplots):
            for jj, rf in enumerate(sp.resultFiles):
                rf.RemoveDataFromResultSignals()
                rf.LoadResults(rf.absPath)
        
        # Redraw PlotManager
        self.RedrawPlotManager()
        # Redraw PlotUI
        self.RedrawPlotCanvas()        
        
        
        
    # PLOT (TAB) HANDLING
    
    def UpdateSelectedTabIndx(self,event)->None:
        '''Update the selected tab index in the project model.'''
        notebook = event.widget
        selTabName = notebook.select()
        selTabIndx = notebook.index(selTabName)
        self.model.projectModel.tabSelected = selTabIndx
        print("Selected tab:", selTabIndx)
        
    def AddPlotTab(self)->None:
        '''Add a Plot in the ProjectModel containedPlots list.'''
        # Build default plot model 
        plot = PlotModel()
        # Assign an index to the plot model
        plot.indx = len(self.model.projectModel.containedPlots) + 1
        # Append plot model to project model
        self.model.projectModel.containedPlots.append(plot)
        # Set the newly created plot as selected folder
        self.model.projectModel.tabSelected = plot.indx
        # Unbind to avoid calling UpdateSelectedTabIndx during notebook redrawing
        self.view.projectNotebook.unbind("<<NotebookTabChanged>>")
        # Redraw plot notebook 
        self.RedrawPlotNotebook()
        # Rebind
        self.view.projectNotebook.bind("<<NotebookTabChanged>>", self.UpdateSelectedTabIndx)
        # Move to the newly created tab
        self.view.projectNotebook.select(plot.indx-1)
                
    def DeletePlotTab(self)->None:
        '''Delete plot tab.'''
        # Find the selected tab
        tabSelected = self.model.projectModel.tabSelected
        # Find how many tabs are in the notebook
        noOfTabs = len(self.model.projectModel.containedPlots)        
        # Delete the selected tab
        del self.model.projectModel.containedPlots[tabSelected]
        # Unbind to avoid calling UpdateSelectedTabIndx during notebook redrawing
        self.view.projectNotebook.unbind("<<NotebookTabChanged>>")
        # Redraw plot notebook 
        self.RedrawPlotNotebook()
        # Rebind
        self.view.projectNotebook.bind("<<NotebookTabChanged>>", self.UpdateSelectedTabIndx)
        
        # If the last tab is selected, cancel it and select the adjacent left
        if noOfTabs>1:
            if tabSelected == noOfTabs-1:
                self.view.projectNotebook.select(tabSelected-1)
            else:
                self.view.projectNotebook.select(tabSelected)
        else:
            '''Don't select anything.'''
        
     
     
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
           
    def SelectXAxis(self,event,resFileManager)->None:
        '''Function invoked when an item is selected from the subplot X axis selection.'''
        # Identify the subplot indx
        subplotIndx = resFileManager.master.master.indx
        # Extract the list of signals tht can be selected as x axis
        xAxisSignals = self.model.projectModel.plotModel.containedSubplots[subplotIndx].xAxisSignals
        # Find the index of the signal selected
        selectedSigNo = resFileManager.xAxisSelect.current()        
        # Update the subplotModel 
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].xAxisSelected = xAxisSignals[selectedSigNo]
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].xAxisSelectedIndx = selectedSigNo
        
        # Redraw PlotUI
        self.RedrawPlotCanvas()
                
                
                
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
        subplotIndx = subplotPane.indx
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
        subplotIndx = subplotOptionsPane.indx
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].name = subplotOptionsPane.titleEntry.get()
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].xLabel = subplotOptionsPane.xAxisLabEntry.get()
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].yLabel = subplotOptionsPane.yAxisLabEntry.get()
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].xLimUser = [float(subplotOptionsPane.xAxisLowLimEntry.get()), float(subplotOptionsPane.xAxisUpLimEntry.get())]
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].yLimUser = [float(subplotOptionsPane.yAxisLowLimEntry.get()), float(subplotOptionsPane.yAxisUpLimEntry.get())]
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].useUserLim = subplotOptionsPane.userLimVar.get()
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].xTickUser = float(subplotOptionsPane.xAxisTicksEntry.get())
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].yTickUser = float(subplotOptionsPane.yAxisTicksEntry.get())
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].useUserTicks = subplotOptionsPane.userTicksVar.get()
        self.model.projectModel.containedPlots[plotIndx].containedSubplots[subplotIndx].grid = subplotOptionsPane.gridVar.get()
        
        self.RedrawPlotNotebook()
        
    def CloseSubplotOptions(self,subplotOptionsPane)->None:
        '''Close subplot options.'''
        subplotOptionsPane.parent.destroy()
        
    def OkSubplotOptions(self, subplotOptionsPane)->None:
        '''Ok Subplot Options'''
        self.ApplySubplotOptions(subplotOptionsPane)
        self.CloseSubplotOptions(subplotOptionsPane)
        
        
        
    # RESULT FILE HANDLING
        
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
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].AddResultFile(resultFileModel)
        
        # Redraw PlotUI
        self.RedrawPlotCanvas()
        # Redraw PlotManager
        self.RedrawPlotManager()
        
    def DeleteResultFile(self,resFilePane)->None:
        '''Delete ResultFile from the model and redraw the PlotManager.'''
        subplotIndx = resFilePane.master.master.master.indx
        
        # Update SubplotModel adding a ResultFile
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].DeleteResultFile(resFilePane)
        
        # Redraw PlotUI
        self.RedrawPlotCanvas()
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
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].absPath = filePath
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].LoadResults(filePath)
        
        # Extract signals and their names from the results file just loaded 
        signals = self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].signals
        signalNames = self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].signalNames
        
        # If the first result pane is added
        if resFilePane.indx == 0:
            # Load the first signal for the x axis
            self.model.projectModel.plotModel.containedSubplots[subplotIndx].xAxisSelected = signals[0]
            self.model.projectModel.plotModel.containedSubplots[subplotIndx].xAxisSelectedIndx = 0
            # Add the signals to the x axis selection 
            for signal, signalName in zip(signals, signalNames):
                self.model.projectModel.plotModel.containedSubplots[subplotIndx].xAxisSignals.append(signal)
                self.model.projectModel.plotModel.containedSubplots[subplotIndx].xAxisSignalsName.append(signalName)
        
        # Redraw PlotUI
        self.RedrawPlotCanvas()
        # Redraw PlotManager
        self.RedrawPlotManager()

        
        
    # SIGNAL HANDLING
    
    def AddSignal(self,event, resFilePane)->None:
        '''Moves one signal from the ResultModel to the PlottedSignal.'''
        
        # Get useful information
        subplotIndx = resFilePane.master.master.master.indx
        resFileIndx = resFilePane.indx
        
        # Find the index of the signal selected
        selectedSigNo = resFilePane.signalCollection.current()
        # Extract from the ResultFileModel the signal selected
        signalToPlot = self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].signals[selectedSigNo]
        
        # Create a PlottedSignal instance 
        plottedSignal = PlottedSignalModel()
        # Copy the signal properties into the PlottedSignal
        plottedSignal.CopySignalProperties(signalToPlot)
        # Extract color counter from subplot
        colorCounter = self.model.projectModel.plotModel.containedSubplots[subplotIndx].colorCounter
        # Assign the PlottedSignal a color
        rgbTuple = self.ChooseSignalColor(colorCounter)
        plottedSignal.color=rgbTuple
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].colorCounter=colorCounter+1
        
        # Add it to the ResultFilePane selectedSignals list (for the left pane with the plot controls)
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].selectedSignals.append(plottedSignal)
        # Add it to the SubplotModel plottedSignals list (for the plot canvas)
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].plottedSignals.append(plottedSignal)
        
        # Redraw PlotUI
        self.RedrawPlotCanvas()
        # Redraw PlotManager
        self.RedrawPlotManager()
        
    def DeleteSignal(self, signalPane)->None:
        '''Delete signal.'''
        
        # Get the index of the result file and subplot
        subplotIndx = signalPane.master.master.master.master.indx
        resFileIndx = signalPane.master.indx
        signalIndx = signalPane.indx
        
        # Remove signal from ResultFileModel selectedSignals list
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].selectedSignals.pop(signalIndx)
        # Remove the signal from the SubplotModel plottedSignals list
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].plottedSignals.pop(signalIndx)
        
        # Redraw PlotUI
        self.RedrawPlotCanvas()
        # Redraw PlotManager
        self.RedrawPlotManager()
        
    def ModifySignalScaling(self,event,signalPane, scalingList)->None:
        '''Change the scaling of the signal.'''
        # Get the index of the result file and subplot
        optSelected = signalPane.unitsCb.current()
        scalingFactor = scalingList[optSelected]
        
        subplotIndx = signalPane.master.master.master.master.indx
        resFileIndx = signalPane.master.indx
        signalIndx = signalPane.indx
        # Calculate the scaled data
        rawData = self.model.projectModel.plotModel.containedSubplots[subplotIndx].plottedSignals[signalIndx].rawData
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].plottedSignals[signalIndx].scalingFactor = scalingFactor
        scaledData = [scalingFactor*val for val in rawData] 
        # Save the scaled data in the PlottedSignal and SelectedSignals list
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].plottedSignals[signalIndx].scaledData = scaledData 
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resFileIndx].selectedSignals[signalIndx].scaledData = scaledData
        
        # Redraw PlotUI
        self.RedrawPlotCanvas()
        
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
        
        
        # Get the signal, result file, and subplot index
        sigIndx = signalPane.indx
        resIndx = signalPane.master.indx
        subplotIndx = signalPane.master.master.master.master.indx
        
        # Get the PlottedSignal object to retrieve its property
        signal = self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resIndx].selectedSignals[sigIndx]
        
        # Create a SignalOptions pane
        signalOpts = SignalOptions(optsWindow,
                                   self,
                                   signal,
                                   sigIndx= sigIndx,
                                   resIndx = resIndx,
                                   subplotIndx = subplotIndx,
                                   bg ='cyan')
        signalOpts.grid(row=0,column=0,sticky='NEWS')
    
    def ApplySignalOptions(self,signalOptions)->None:
        '''Apply signal options.'''    
        # Get the index of the subplot, result file, and signal
        
        sigIndx = signalOptions.sigIndx
        resIndx = signalOptions.resIndx
        subplotIndx = signalOptions.subplotIndx
        
        
        # Get the signal options values
        lineWidth = float(signalOptions.lineWidthCb.get())
        lineStyle = signalOptions.lineStyleCb.get()
        lineMarker = signalOptions.GetMarkerOpts()
        color= signalOptions.selectedColor
        
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resIndx].selectedSignals[sigIndx].color=color
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resIndx].selectedSignals[sigIndx].width=lineWidth
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resIndx].selectedSignals[sigIndx].style=lineStyle
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].resultFiles[resIndx].selectedSignals[sigIndx].marker=lineMarker
        
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].plottedSignals[sigIndx].color=color
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].plottedSignals[sigIndx].width=lineWidth
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].plottedSignals[sigIndx].style=lineStyle
        self.model.projectModel.plotModel.containedSubplots[subplotIndx].plottedSignals[sigIndx].marker=lineMarker
        # Redraw plot canvas
        self.RedrawPlotCanvas()
        # Redraw plot manager 
        self.RedrawPlotManager()
        
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
            sigTemp = SignalModel(name=name,units=units,quantity=sigQuantity,indx = i)
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
        # Delete existing tabs
        tabs = self.view.projectNotebook.tabs()
        for ii, tab in enumerate(self.view.projectNotebook.tabs()):
             self.view.projectNotebook.forget(tab)
        
        # Redraw tabs
        for ii,plot in enumerate(self.model.projectModel.containedPlots):
            plotPane = PlotPane(self.view.projectNotebook, self,ii)
            self.view.projectNotebook.add(plotPane)
            
            # Clear all the existing subplots, and create the axis for the new ones
            plt.close('all') 
            plotManagerChildren = plotPane.plotCanvas.winfo_children()
            for ii,child in enumerate(plotManagerChildren):
                child.destroy()
                
            noOfSubplots = len(plot.containedSubplots)
            if noOfSubplots>0:
                fig, axList = plt.subplots(noOfSubplots,1, squeeze=False)
            
            # REDRAW PLOT MANAGER ==========================
            # Redraw subplots
            for jj, subplot in enumerate(plot.containedSubplots):
                subplotPane = SubplotPane(plotPane.plotManager.interior,
                                          self, 
                                          jj,
                                          subplot,
                                          bg = 'blue')
                subplotPane.grid(row=jj,column=0,sticky='NEW')
                
                # Redraw result files 
                for kk, resultFile in enumerate(subplot.containedResultFiles):
                    resFile = ResFilePane(subplotPane.interior,
                                        self,
                                        indx = jj,
                                        entryText=resultFile.absPath,
                                        comboboxList=resultFile.signalNames)
                    resFile.grid(row=kk,column=0,sticky='NEW')
                    
                    # Redraw selected signals
                    for hh, selectedSignal in enumerate(resultFile.selectedSignals): 
                        sigPane = SignalPane(   resFile.interior,
                                                self,
                                                selectedSignal,
                                                indx = kk,
                                                bg = 'red')
                        sigPane.grid(row=hh,column=0,sticky='EW')
                        
                    
                if noOfSubplots>0:
                    # REDRAW PLOT CANVAS ==========================
                    # Extract x axis signal 
                    xAxisSelected = subplot.xAxisSelected
                            
                    # Do not plot anything if the x axis is not selected
                    if xAxisSelected == []:
                        continue
                    
                    # Extract plotted signals and plot them
                    plottedSignals = subplot.plottedSignals
                    for plottedSig in plottedSignals:
                        psCol=plottedSig.color
                        psWidth=plottedSig.width
                        psStyle=plottedSig.style
                        psMarker=plottedSig.marker
                        psLabel=plottedSig.label
                        axList[jj,0].plot(xAxisSelected.scaledData,plottedSig.scaledData,
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
                    
                    # Set subplot properties
                    # Title
                    axList[jj,0].title.set_text(subplot.name)
                    # Labels
                    axList[jj,0].set_xlabel(subplot.xLabel)
                    axList[jj,0].set_ylabel(subplot.yLabel)
                    # Grid
                    axList[jj,0].grid(subplot.setGrid)
                    # Axis Limits
                    if subplot.useUserLim & (subplot.xLimUser[0] != subplot.xLimUser[1]):
                        axList[jj,0].set_xlim(subplot.xLimUser)
                    if subplot.useUserLim & (subplot.yLimUser[0] != subplot.yLimUser[1]):
                        axList[jj,0].set_ylim(subplot.yLimUser)
                    # Ticks
                    if subplot.useUserTicks & (subplot.xTickUser!=0):
                        currTickX = list(axList[jj,0].get_xlim())
                        tickVectX = np.arange(currTickX[0],currTickX[1], subplot.xTickUser).tolist()
                        axList[jj,0].set_xticks(tickVectX)
                        
                    if subplot.useUserTicks & (subplot.yTickUser!=0):
                        currTickY = list(axList[jj,0].get_ylim())
                        tickVectY = np.arange(currTickY[0],currTickY[1],subplot.yTickUser).tolist()
                        axList[jj,0].set_yticks(tickVectY)
                            
                    
                    # Draw the canvas and toolbar inside the Plotter object
                    plotPane.plotCanvas.canvas = FigureCanvasTkAgg(fig, master=plotPane.plotCanvas)
                    plotPane.plotCanvas.toolbar = NavigationToolbar2Tk(plotPane.plotCanvas.canvas, plotPane.plotCanvas)
                    plotPane.plotCanvas.toolbar.update()
                    plotPane.plotCanvas.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
                    plotPane.plotCanvas.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
                
            # Add tab to notebook
            plotTitle = "Plot " + str(ii)
            self.view.projectNotebook.add(plotPane, text = plotTitle)

    def RedrawPlotCanvas(self)->None: # Deprecated  
        '''This function redraws the plot canvas.'''
        # Close all the figures, destroy toolbar and canvas
        plt.close('all') 
        plotManagerChildren = self.view.mainTabColl.plotter.plot.winfo_children()
        for ii,child in enumerate(plotManagerChildren):
            child.destroy()
            
        # Calculate the number of subplots that must be generated
        subplots = self.model.projectModel.plotModel.containedSubplots
        noOfSubplots = self.model.projectModel.plotModel.noOfSubplots
        fig, axList = plt.subplots(noOfSubplots,1, squeeze=False)
        # fig.subplots_adjust(left=0.05, bottom=0.05, right=0.95, top=0.95, wspace=0.1, hspace=0.2)
        
        for spNo, subplot in enumerate(subplots):
            # Extract x axis signal 
            xAxisSelected = self.model.projectModel.plotModel.containedSubplots[spNo].xAxisSelected
                       
            # Do not plot anything if the x axis is not selected
            if xAxisSelected == []:
                continue
            
            # Extract plotted signals and plot them
            plottedSignals = self.model.projectModel.plotModel.containedSubplots[spNo].plottedSignals
            for plottedSig in plottedSignals:
                psCol=plottedSig.color
                psWidth=plottedSig.width
                psStyle=plottedSig.style
                psMarker=plottedSig.marker
                psLabel=plottedSig.label
                axList[spNo,0].plot(xAxisSelected.scaledData,plottedSig.scaledData,
                                    color=psCol,
                                    linewidth=psWidth,
                                    linestyle=psStyle,
                                    marker=psMarker,
                                    label=psLabel)
                axList[spNo,0].legend()
           
            # Extract subplot default settings
            self.model.projectModel.plotModel.containedSubplots[spNo].xLim = list(axList[spNo,0].get_xlim())
            self.model.projectModel.plotModel.containedSubplots[spNo].yLim = list(axList[spNo,0].get_ylim())
            yTicksArray = axList[spNo,0].get_yticks()
            xTicksArray = axList[spNo,0].get_xticks()
            xTicks = float(xTicksArray[1]) - float(xTicksArray[0])
            yTicks = float(yTicksArray[1]) - float(yTicksArray[0])
            self.model.projectModel.plotModel.containedSubplots[spNo].xTick = xTicks
            self.model.projectModel.plotModel.containedSubplots[spNo].yTick = yTicks
            
            # Set subplot properties
            # Title
            axList[spNo,0].title.set_text(subplot.name)
            # Labels
            axList[spNo,0].set_xlabel(subplot.xLabel)
            axList[spNo,0].set_ylabel(subplot.yLabel)
            # Grid
            axList[spNo,0].grid(subplot.setGrid)
            # Axis Limits
            if subplot.useUserLim & (subplot.xLimUser[0] != subplot.xLimUser[1]):
                axList[spNo,0].set_xlim(subplot.xLimUser)
            if subplot.useUserLim & (subplot.yLimUser[0] != subplot.yLimUser[1]):
                axList[spNo,0].set_ylim(subplot.yLimUser)
            # Ticks
            if subplot.useUserTicks & (subplot.xTickUser!=0):
                currTickX = list(axList[spNo,0].get_xlim())
                tickVectX = np.arange(currTickX[0],currTickX[1], subplot.xTickUser).tolist()
                axList[spNo,0].set_xticks(tickVectX)
                
            if subplot.useUserTicks & (subplot.yTickUser!=0):
                currTickY = list(axList[spNo,0].get_ylim())
                tickVectY = np.arange(currTickY[0],currTickY[1],subplot.yTickUser).tolist()
                axList[spNo,0].set_yticks(tickVectY)
                 

            
        # Draw the canvas and toolbar
        self.view.mainTabColl.plotter.plot.canvas = FigureCanvasTkAgg(fig, master=self.view.mainTabColl.plotter.plot)
        self.view.mainTabColl.plotter.plot.toolbar = NavigationToolbar2Tk(self.view.mainTabColl.plotter.plot.canvas, self.view.mainTabColl.plotter.plot)
        self.view.mainTabColl.plotter.plot.toolbar.update()
        self.view.mainTabColl.plotter.plot.toolbar.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.view.mainTabColl.plotter.plot.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
    def RedrawPlotManager(self)->None: # Deprecated  
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
        areCollapsed = self.model.projectModel.plotModel.areCollapsed
        # Iterate on the Subplots
        for ii,sp in enumerate(self.model.projectModel.plotModel.containedSubplots):
            spRow = ii+1 # Skip the 'Add subplot' button
            toggleFrame = TogglePaneDelOpts(self.view.mainTabColl.plotter.plotManager,
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
                    sigPane = SignalPane(   resFile,
                                            self,
                                            ss,
                                            indx = kk,
                                            bg = 'red')
                    sigPane.grid(row=ssRow,column=0,sticky='EW')
                # Separator between result files 
                separatorRow = 2+len(rf.selectedSignals)+1
                separator = tk.Frame(resFile, bg = 'green', height=5)
                separator.grid(row=separatorRow,column = 0, sticky = 'EW')
                
            # Separator between subplots
            separatorRow = 3+len(sp.resultFiles)+1
            separator = tk.Frame(toggleFrame.interior, bg = 'red', height=10)
            separator.grid(row=separatorRow,column = 0, sticky = 'EW')