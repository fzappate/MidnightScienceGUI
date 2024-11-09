"""
Module: Model.py
=============

This module contains the `Model` class, which serves as the central data container 
for the application. It includes submodels such as the `Settings` and `ProjectModel` 
that manage the application's configuration and project-related data, respectively. 
The `Model` class acts as storage object for the application.

Author: Federico Zappaterra
Version: 1.0.0
Date: 11/05/24

Classes:
--------
Model:
    The main class representing the model in the MVC architecture. It holds references
    to submodels like `Settings` and `ProjectModel`, initializing them as needed.

"""

from model.Settings import Settings
from model.ProjectModel import ProjectModel

class Model:
    """
    Model class that encapsulates the application's data.
    
    This class is part of the Model-View-Presenter (MVP) design pattern and stores 
    various submodels, including application settings and project-related data.
    
    Attributes:
    -----------
    settings : Settings
        An instance of the `Settings` class, managing application settings.
    projectModel : ProjectModel
        An instance of the `ProjectModel` class, managing project data.

    Methods:
    --------
    __init__():
        Initializes the `Model` class, creating instances of `Settings` and `ProjectModel`.
    """

    def __init__(self) -> None:
        """
        Initializes the `Model` class by creating instances of its submodels.

        The constructor sets up the necessary components for managing settings and 
        project data by instantiating `Settings` and `ProjectModel`.

        Args:
            None

        Returns:
            None
        """
        
        # Instantiate the Settings submodel for app configuration
        self.settings = Settings()  
        
        # Instantiate the ProjectModel submodel to manage project data
        self.projectModel = ProjectModel()  
