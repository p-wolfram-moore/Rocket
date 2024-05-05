# Image Classification with Time Series Dimension Reduction Methods

Have you ever wondered if 2D images could be analyzed like time series arrays?  While images do not have explicit temporal associations between pixels, the layering of columns and rows does in fact provide time-like frequency and structure to the array and can be analyzed in a similar fashion.

This notebook performs a number of preprocessing steps to reorder pixels in the MNIST handwritten digits in order to exploit the pixel-adjacent associations and information contained therein.  The hypothesis is that images can be treated similar to time series arrays because it captures patterns that occur on a frequency-like basis.  

Consider how in a 60x60 pixel image that the first pixel in the first row, first column is next to both the first pixel in the second row and first pixel in the second column.  If you flatten a 2D image (either row-wise or column-wise), the result is every 60th pixel is in fact associated - a frequency that can be considered in a way similar to a time series with a pattern occuring every minute (60 seconds). 

### DOWNLOAD THE ORIGINAL MNIST DATASET

I used the following link to download a .csv represetnation of the original MNIST dataset, but feel free to use whatever source you find.

https://drive.google.com/file/d/1eEKzfmEu6WKdRlohBQiqi3PhW_uIVJVP/view

The most important element is that the first column in the numeric label {0,9} and the rest of the array is the flattened row-wise representation of the image.

In order to reproduce the results found in this repo, preserve the train/test split provided by the MNIST data set and simply point the jupyter notebook MNIST_MultiRocket.ipynb to your dataset.

