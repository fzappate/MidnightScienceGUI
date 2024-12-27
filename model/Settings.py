"""
Module: Setting.py
===========

This module defines the `Settings` class, which contains all the settings for the software instance.
It initializes the settings from a specified file path and provides attributes related to the project folder
and other software settings.

Author: Federico Zappaterra
Version: 1.0.0
Date: 2024-11-05

Classes
-------
Settings
    Class that manages the software's settings, including file paths and project folder configuration.

"""

class Settings():
    '''Class containing all the settings of the software instance.'''

    def __init__(self)->None:
        '''
        Initialize the application setting object.

        This method sets default values for the settings, including the file path for the settings
        file and an empty project folder.
        '''
        
        self.settingsFilePath = './utilities/settings.md'
        self.projectFolder = ''
        self.projectFileName = ''
        self.projectFileNameTemp = ''