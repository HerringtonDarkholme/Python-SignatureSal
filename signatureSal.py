from util import *
import numpy as np
from skimage.viewer import viewers
import default
import matplotlib.pyplot as plt
ImageViwer = viewers.ImageViewer

class SignatureSal(object):
    """Docstring for SignatureSal """

    def __init__(self,src, params=None):
        """return saliency map

        :src: @todo

        """
        self._params = default.defaultParam()
        #override default
        if params:
            for k, v in params.items():
                self._params[k] = v
        self._map = self.makeMap(src)

    def makeMap(self, src):
        img = loadImg(src)
        orgSize = img.shape[1]
        img = rgb2lab(img, self._params['colorChannel'])
        img = resize(img, self._params['mapWidth'])

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
        plt.imshow(self._map)
        plt.show()

if __name__ == '__main__':
    import sys
    #test = SignatureSal(sys.argv[1], {'colorChannel': 'rgb'})
    test = SignatureSal(sys.argv[1])
    test.show()
