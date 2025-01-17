REM Description: This script is used to run PyInstaller to create a standalone executable of the Midnight Science Plotter.
REM Run this script from a terminal in the root directory of the project.
REM
REM Inputs
REM pyinstaller     : Call pyinstaller to create the executable
REM --name          : Name the executable "Midnight Science Plotter"
REM --clean         : Clean the cashed files
REM --onefile       : Create a single executable file that unzip itself when run
REM --specpath      : Define where to save the exe and the build files
REM --windowed      : Run the executable in a window
REM --icon          : Set the path of icon of the executable
REM --add-data      : Set the path to additional data required by the executable
REM --add-data      : Set the path to additional data required by the executable
REM ../main.py      : Set the path to the main python file
REM
REM Typical usage:
REM pyinstaller ^
REM --name "Midnight Science Plotter" ^
REM --clean ^
REM --onefile 
REM --specpath "../bin" ^
REM --windowed ^
REM --icon="..\assets\MSPlotterIcon.png" ^
REM --add-data "../assets:assets" ^
REM --add-data "../utilities:utilities" ../main.py
REM
REM Suggestions: 
REM To ease debuggin process, remove the --onefile flag and run the executable from the terminal.

pyinstaller ^
--name "Midnight Science Plotter" ^
--clean ^
--onefile ^
--specpath "../bin" ^
--windowed ^
--icon="..\assets\MSPlotterIcon.png" ^
--add-data "../assets:assets" ^
--add-data "../utilities:utilities" ../main.py