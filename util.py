import numpy as np
import skimage.color as color
import scipy.ndimage.filters as ft
import skimage.io as io
import numpy as np
import os
from skimage.transform import resize
from scipy.fftpack import dct, idct

def dct2(arr):
    """
    @todo: 2D-dct, constructed from scipy's dct2
    @params { np.ndarray } arr
    @return { np.ndarray }
    """
    array = np.float64(arr)
    result = dct(dct(array, axis=0), axis=1)
    return result

def idct2(arr):
    """
    @params { np.ndarray } arr
    @return { np.ndarray }
    """
    array = np.float64(arr)
    result = idct(idct(array, axis=0), axis=1)
    return result

def normalize(image, subtractMin):
    """
    @params { array-like } image Skimage type acceptable
    @return { np.ndarray }
    """
    if subtractMin:
        return color.rgb2grey(image)
    else:
        return np.divide(a, np.max(a))

def gaussian(image, sigma):
    return ft.gaussian_filter(image, sigma)

def rgb2lab(img, colorType):
    cType = colorType.lower()
    if cType is 'rgb':
        return img
    if cType is 'lab':
        return color.rgb2lab(img)

def getChannel(img, channelNum):
    """
    get a single color channle of image
    @param {3d-array like} img
    @param {int} channelNum
    """
    if not img.ndim is 3:
        raise TypeError('wrong dimension')
    return img[:,:,channelNum]

def loadImg(inp):
    """
    return image array
    @param {str} inp  path to image
    @param {list} inp nested list of image
    """
    if isinstance(inp, str):
        #@todo : add url support
        path = os.path.join(os.getcwd(), str)
        if not os.path.isfile(path):
            raise IOError('no such file')
        return io.imread(inp)
    elif isinstance(inp, list):
       result = np.array(inp)
       if result.ndim == 3 or result.ndim ==4:
           return np.float64(result)
       else:
           raise Exception('invalid dimension')
    else:
        raise TypeError('Need Filename or list')

def resize(img, width):
    #image.shape : height, width, rgb
    height = float(img.shape[1]) / width * img.shape[0]
    height = int(height)
    return resize(img, (height, width))
