"""
Application Module
==================

This module serves as the entry point for initializing and running the application.
It imports and creates instances of the Model, View, and Presenter classes and sets up 
a high-DPI awareness setting for improved display scaling on Windows.

Author: Federico Zappaterra
Version: 1.0
Date: 2024-11-05

Classes
-------
None

Functions
---------
main() -> None
    Initializes the application components (Model, View, and Presenter) and starts the UI.

Usage
-----
This module is intended to be run as the main entry point of the application.

    $ python main.py

    - Initializes Model, View, and Presenter objects.
    - Configures DPI settings on Windows.
    - Launches the application UI.

Notes
-----
- The `ctypes` library is used to enable high-DPI awareness on Windows. If `windll` 
  is not available, the setting is skipped without raising an error.
- This module follows the Model-View-Presenter (MVP) design pattern, which separates 
  the application logic (Model), user interface (View), and UI logic (Presenter).

"""
from model import Model
from ui.View import View
from presenter.presenter import Presenter

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except (ImportError, AttributeError):
    pass

def main() -> None:
    '''Initializes and runs the application.'''
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    presenter.RunUI()

if __name__ == "__main__":
    main()
