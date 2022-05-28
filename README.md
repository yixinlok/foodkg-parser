# foodkg-search-tool
A tool to search recipes in foodkg and display its data by specific search

# How to use:
Note: The following steps assume you already have python and pip installed.

## 1. Clone this repository

## 2. Download the dataset
- Go to this google drive(https://drive.google.com/drive/folders/1Kro-oICwmctn_Cg6I6KoBPPfFQC-kFsX) and download the file called '''MAIN_h02dsaqlo1jd9w9u.seg'''
- Move this file into your local cloned repository, under the path ''path_to_cloned_repository/src/indexdir''

## 3. Download the required Python libraries, Whoosh and PyQt5

Mac/Linux Users:
- (optional but suggested) create and activate a python virtual environment by running '''python3 -m venv venv''' then '''source venv/bin/activate''' in the command line. make sure to run '''source venv/bin/activate''' in the same directory every time you want to run the program.
- install Whoosh by running '''pip install Whoosh'''
- install PyQt5 by running '''pip install PyQt5'''

Windows Users:
- (optional but suggested) create a python virtual environment by running '''python -m venv venv''' then '''venv\Scripts\Activate.ps1''' in the command line. if you created the virtual environment make sure to run '''venv\Scripts\Activate.ps1''' in the same directory every time you want to run the program. 
- install Whoosh by running '''pip install Whoosh'''
- install PyQt5 by running '''pip install PyQt5'''

## 4. Run the program
- run '''python path_to_cloned_repository/src/main.py''' in the command line or run '''main.py''' in your code editor.

if you just want to experiment with the tool with a smaller dataset (it's faster) instead
- run '''python path_to_cloned_repository/src/partial_main.py'''. This will run it with only 50 recipes from foodkg instead of over 10000.

