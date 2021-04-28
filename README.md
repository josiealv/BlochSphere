# pythonBlockSphere

Physics 495, Senior Project
Angel Flores, Josie Alvarez, Marisa Class

Project:
Data Visualisation of a Bloch Sphere

## Before Starting
**Installation:**
1. Make sure to have Python 2.7 (or higher) installed
    - Install at: (https://www.python.org/downloads/)
2. Install Tkinter 
-Run on command line: `python3 -m pip install pysimplegui`
3. Install the Bloch Sphere library from QuTip
-Installation instructions at: (https://pypi.org/project/bloch-sphere/)

## About external_animate_bloch()
- The first 4 parameters of the function represent the real and imaginary components of complex number, alpha and beta
    - `alpha_reals` & `beta_reals` represent the real parts of alpha & beta and **must** be passed in as an array in case more than 1 state vector is to be plotted
    - `alpha_imags` & `beta_imags` represent the imaginary parts of alpha & beta and also **must** be passed in as an array 
    - Example: `alpha = 1+0i` & `beta = 1+1i`
        - `alpha_reals = []`
        - `alpha_imags = []`
        - `beta_reals = []`
        - `beta_imags = []`
        - `alpha_reals.append(1)`
        - `alpha_imags.append(0)`
        - `beta_reals.appen(1)`
        - `beta_imags.append(1)`
- The filename parameter takes in a string and it can include the path including the filename or just the file name. **Do not include the file extension.**
    - if the path is not included in the filename, the file will save in the same directory as bloch.py
## Animating from Separate Python File
1. Import the bloch.py file into the python file you want to call the function from
     - `import bloch as *name here*`
    - If in different directory where the path is: 
        - `package2/subpackage1/bloch.py`, then:
            -  `import sys`
            - `sys.path.insert(1, package2/subpackage1)`
            - `import bloch as *name here*`
2. Call the function: `external_animate_bloch()`
with:
    - `b.external_animate_bloch(alpha_reals, alpha_imags, beta_reals, beta_imags, filename)`
        - where b is the name given when importing bloch.py
            