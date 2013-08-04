from util import *
import numpy as np
from skimage.viewer.viewers import ImageViwer
import default

class SignatureSal(object):
    """Docstring for SignatureSal """

    def __init__(self,src, params):
        """return saliency map

        :src: @todo

        """
        self._params = default.defaultParam()
        #override default
        for k, v in params:
            self._params[k] = v
        self._map = self.makeMap(src)

    def makeMap(self, src):
        img = loadImg(src)
        orgSize = img.shape[1]
        img = resize(img, self._params['width'])
        img = rgb2lab(img, self._params['colorChannel'])

        outmap = np.zeros((img.shape[0], img.shape[1]))
        for i in range(img.shape[2]): #height, width, color
            channel = getChannel(img, i)
            channel = dct2(channel)
            channel = np.sign(channel)
            channel = idct2(channel)
            channel = np.square(channel)
            outmap = np.add(outmap, channel)
        outmap = np.divide(outmap, img.shape[2])
        outmap = gaussian(outmap, self._params['blurSigma'])

        if self._params['resizeToInput']:
          resize(outmap, orgSize)

        return outmap

    def show(self):
        """Todo"""
