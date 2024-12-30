REM Description: This script is used to run PyInstaller to create a standalone executable of the Midnight Science Plotter.
REM Run this script from a terminal in the root directory of the project.
pyinstaller --name "Midnight Science Plotter" --clean --onefile --specpath dist --windowed --icon=..\assets\MSPlotterIcon.png --add-data "../assets:assets" --add-data "../utilities:utilities" main.py