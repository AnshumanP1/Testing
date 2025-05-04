# Simple Tkinter GUI Application

## Description

This is a very basic graphical user interface (GUI) application built using Python's Tkinter library. It displays a window with a single button labeled "Click Me". When the button is clicked, a message box appears with the text "Hello, Windows User!".

## Creating the Executable (`.exe`)

To package this application into a standalone Windows executable (`.exe`), we use the `pyinstaller` tool.

### Steps:

1.  **Install Dependencies:**
    Make sure you have Python installed. Then, install the required package (`pyinstaller`) using pip and the provided `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run PyInstaller:**
    Navigate to the project directory in your terminal or command prompt. Run the following `pyinstaller` command:
    ```bash
    pyinstaller --onefile --windowed main.py
    ```
    *   `--onefile`: Bundles everything into a single executable file.
    *   `--windowed`: Prevents a console window from opening when the GUI application runs.
    *   `main.py`: Specifies the main script of the application.

3.  **Locate the Executable:**
    PyInstaller will create a `dist` directory in your project folder. Inside the `dist` directory, you will find the generated `main.exe` file. This file can be run on Windows systems without needing Python or Tkinter installed separately.

## Important Note

The final `main.exe` file is **not** included in this repository. Due to limitations in the development/build environment, the executable could not be generated automatically as part of the repository setup.

You **must** perform the build steps described above yourself:
1. Install the necessary dependencies: `pip install -r requirements.txt`
2. Run the PyInstaller command: `pyinstaller --onefile --windowed main.py`

This will generate the `main.exe` file in the `dist` folder within your local copy of the project.
