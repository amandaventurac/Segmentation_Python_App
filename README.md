I built this app to construct a simple and correct geometry of microstructure Finite-element models.
The Finite-element model that I use is supposed to read a file with EBSD microscopy information and construct a 2D microstructure model. 
This information should be the initial and endpoints of segmentations (grain boundaries).
This small app begins with a microscopy image and asks the user to click the initial and endpoints of grain boundaries. 
These points are recorded, and the lines are constructed using the previously recorded point. 
The real size of the microscopy map is an input and is used to set the correct model size. 
After clicking these points, the result is a clean text file with simple geometry, that is rapidly read by the FEM software and allows producing the entire model.

This repository contains:

-Input microscopy image

-Python script (please press ESC to exit)

-Example image of clicking process

-Out text file with segmentation information

-Power point presentation with all the instructions


![Fig1](https://github.com/amandaventurac/Segmentation_Python_App/blob/main/real_and_model.png?raw=true)

Figure 1 : The initial microscopy image and final model.

![Fig2](https://github.com/amandaventurac/Segmentation_Python_App/blob/main/clicking_process.png?raw=true)

Figure 2 : Example image of clicking process.

