How to run the program.. Note that python must be pre-installed

Step 1: Create a local folder on your machine, lets take it as 'xyz'. Then download the main.py and move it to the 'xyz' folder.
Step 2: Create a virtual environment (venv) by writing this following commands in the terminal of the directory

# install virtual environment
python3 -m venv venv

# activate venv
source venv/bin/activate

# install required library 
pip install PyMuPDF numpy

# run the program
python main.py Document.pdf (Here Document.pdf is assumed to be in the same directory with the main.py), while there is another way which is to write the path location instead
