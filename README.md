# pythonBlockSphere

Physics 495, Senior Project
Angel Flores, Josie Alvarez, Marisa Class

Project:
Data Visualisation of a Bloch Sphere

## Before Starting
**Installation:**
1. Make sure to have Python 3 installed
    - Install at: https://www.python.org/downloads/
2. Install Tkinter 
    - Run on command line: `pip3 install pysimplegui`
        - More info: https://pysimplegui.readthedocs.io/en/latest/
3. Install the Bloch Sphere library from QuTip
    - Installation instructions at: http://qutip.org/docs/4.1/installation.html#windows-and-python-2-7
4. Install OpenCV
    - Run on command line: `pip3 install opencv-python`
        - More info: https://pypi.org/project/opencv-python/
5. Install imageio-ffmpeg
    - Run on command line: `pip3 install imageio-ffmpeg`
        - More info: https://github.com/imageio/imageio-ffmpeg

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
- The `filename` parameter takes in a string and it can include the path including the filename or just the file name. **Do not include the file extension.**
    - if the path is not included in the filename, the file will save in the same directory as bloch.py
- The `file_type` parameter takes in a string where you **must** specify what file type you want the animation to be: gif or mp4. The file size of the mp4 is much smaller than the gif, so it is recommended that you use mp4 
    - **Note**: You do not need to add '.' to the `file_type` string, just 'gif' or 'mp4'
## About external_animate_bloch_multiple()
- The function parameters are similar to external_animate_bloch(), only difference is that there is one extra parameter: `numV`. This parameter represents the number of animations you want and they play simultaneously
- Changes to alpha and beta arrays:
    - the only change to these arrays is that they **must** now be a **2D array** where each index in the first dimension represents a different animation
    - Example: `numV = 2` where `alpha1 = 1+0i` & `beta1 = 1+1i` and `alpha2 = 0+1i` & `beta2 = 1+0i`
        - `alpha_reals = []`
        - `alpha_imags = []`
        - `beta_reals = []`
        - `beta_imags = []`
            - these are the 2D arrays that we will be passing into the `external_animate_bloch_multiple()` function
        - `alpha_r1 = []`
        - `alpha_i1 = []`
        - `beta_r1 = []`
        - `beta_i1 = []`
            - the arrays needed for the first animation
        - `alpha_r1.append(1)`
        - `alpha_i1.append(0)`
        - `beta_r1.appen(1)`
        - `beta_i1.append(1)`
            - adding in the real and imaginary parts of alpha1 and beta1 to their respective arrays
        - `alphas_reals.append(alpha_r1)`
        - `alphas_imags.append(alpha_i1)`
        - `betas_reals.append(beta_r1)`
        - `betas_imags.append(beta_i1)`
            - adding the arrays for the first animation to our 2D arrays
        - `alpha_r2 = []`
        - `alpha_i2 = []`
        - `beta_r2 = []`
        - `beta_i2 = []`
            - the arrays needed for the second animation
        - `alpha_r2.append(0)`
        - `alpha_i2.append(1)`
        - `beta_r2.appen(1)`
        - `beta_i2.append(0)`
         - adding in the real and imaginary parts of alpha2 and beta2 to their respective arrays 
        - `alphas_reals.append(alpha_r2)`
        - `alphas_imags.append(alpha_i2)`
        - `betas_reals.append(beta_r2)`
        - `betas_imags.append(beta_i2)`
            - adding the arrays for the second animation to our 2D arrays
        - So if you were to access `alphasR[0]` you would get the `alpha_r1` array, representing the first half of `alpha1` which is also part of the first animation. (This isn't the only way to create the 2D arrays in python, this is just most straightfoward method without using a for loop)
## Animating from Separate Python File
1. Import the bloch.py file into the python file you want to call the function from
     - `import bloch as *name here*`
    - If in different directory where the path is: 
        - `package2/subpackage1/bloch.py`, then:
            -  `import sys`
            - `sys.path.insert(1, package2/subpackage1)`
            - `import bloch as *name here*`
2. To call the function: `external_animate_bloch()`
use:
    - `b.external_animate_bloch(alpha_reals, alpha_imags, beta_reals, beta_imags, filename, file_type)`
        - where b is the name given when importing bloch.py
3. To call the function: `external_animate_bloch_multiple()`
use:
    - `b.external_animate_bloch_multiple(numV, alpha_reals, alpha_imags, beta_reals, beta_imags, filename, file_type)`
        - where b is the name given when importing bloch.py
            