"""
Module: ProjectModel
====================

This module defines the ProjectModel class, which is responsible for managing the
overall structure of the project. It contains attributes and methods that represent
a project, including the project's name, the index, and the selected tab. It also holds
the list of contained plots within the project.

Author: Federico Zappaterra
Version: 1.0.0
Date: 2024-11-05

Classes
-------
ProjectModel
    Represents a project model containing plots and other project details.
    
Methods
-------
__init__()
    Initializes the ProjectModel instance, setting up default values and creating
    empty containers for plots.
"""

class ProjectModel():
    '''
    Create a project model instance.
    
    The ProjectModel class is responsible for holding the project-related data,
    including project name, index, tab selection, and the list of contained plots.
    '''
    
    def __init__(self)->None:
        '''
        Initialize the ProjectModel instance.
        
        This method sets up the default values for the project, including its name,
        index, object name, selected tab, and initializes an empty list to hold plots.
        '''
        # Initialize project name
        self.name = 'ProjectModel'
        
        # Initialize index for internal tracking
        self.indx = 0
        
        # Initialize object name for reference
        self.objectName = 'ProjectModel'
        
        # Initialize the index of the selected tab
        self.tabSelected = 0
        
        # Initialize an empty list for holding contained plots
        self.containedPlots = []
