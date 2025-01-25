```
# File Organizer

This is a simple file organizer application with a graphical user interface (GUI) created using Tkinter. The application allows users to select a folder and organize files into subfolders based on their file types.

## Features

- Organize files into categories such as Images, Documents, Videos, Music, Applications, Compressed Files, and Torrent Files.
- User-friendly interface with Tkinter.
- Allows users to select the folder to organize.

YOU CAN DOWNLOAD THE file_organizer_gui.exe FROM RELEASES AND RUN THE PROGRAM DIRECTLY
OR YOU CAN FOLLOW THE STEPS BELLOW:

## Requirements

- Python 3.x
- Tkinter (included with Python standard library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd file-organizer
   ```

3. (Optional) Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python file_organizer_gui.py
   ```

2. Select the folder you want to organize and click the "Organize Files" button.

## Building the Executable

To create an executable file (.exe) using PyInstaller, follow these steps:

1. Ensure PyInstaller is installed:
   ```bash
   pip install pyinstaller
   ```

2. Generate the executable:
   ```bash
   pyinstaller --onefile --windowed file_organizer_gui.py
   ```

3. Find the .exe file in the `dist` directory and share it with your friends.

## Contributions

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss any changes or improvements.
