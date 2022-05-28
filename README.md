# foodkg-search-tool
A tool to search recipes in foodkg and display its data by specific search

# How to use:
Note: The following steps assume you already have python and pip installed.

## 1. Clone this repository

## 2. Download the dataset
- Go to this google drive(https://drive.google.com/drive/folders/1Kro-oICwmctn_Cg6I6KoBPPfFQC-kFsX) and download the file called <pre><code>MAIN_h02dsaqlo1jd9w9u.seg</code></pre>
- Move this file into your local cloned repository, under the path <pre><code>path_to_cloned_repository/src/indexdir</code></pre>

## 3. Download the required Python libraries, Whoosh and PyQt5

Mac/Linux Users:
- (optional but suggested) create and activate a python virtual environment by running <pre><code>python3 -m venv venv</code></pre> then <pre><code>source venv/bin/activate</code></pre> in the command line. make sure to run <pre><code>source venv/bin/activate</code></pre> in the same directory every time you want to run the program.
- install Whoosh by running <pre><code>pip install Whoosh</code></pre>
- install PyQt5 by running <pre><code>pip install PyQt5</code></pre>

Windows Users:
- (optional but suggested) create a python virtual environment by running <pre><code>python -m venv venv</code></pre> then <pre><code>venv\Scripts\Activate.ps1</code></pre> in the command line. if you created the virtual environment make sure to run <pre><code>venv\Scripts\Activate.ps1</code></pre> in the same directory every time you want to run the program. 
- install Whoosh by running <pre><code>pip install Whoosh</code></pre>
- install PyQt5 by running <pre><code>pip install PyQt5</code></pre>

## 4. Run the program
- run <pre><code>python path_to_cloned_repository/src/main.py</code></pre> in the command line or run <pre><code>main.py</code></pre> in your code editor.


