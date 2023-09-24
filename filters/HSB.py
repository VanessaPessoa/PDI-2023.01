import numpy as np
import math
from functools import reduce


class HSB:
    def fractionalColors(self, hue, saturation, brightness):
        sectorPos = hue / 60.0
        sectorNumber = int(math.floor(sectorPos))
        fractionalSector = sectorPos - sectorNumber

        p = brightness * (1.0 - saturation)
        q = brightness * (1.0 - (saturation * fractionalSector))
        t = brightness * (1.0 - (saturation * (1 - fractionalSector)))

        if sectorNumber == 0:
            return (brightness, t, q)
        if sectorNumber == 1:
            return (q, brightness, p)
        if sectorNumber == 2:
            return (p, brightness, t)
        if sectorNumber == 3:
            return (p, q, brightness)
        if sectorNumber == 4:
            return (t, p, brightness)
        if sectorNumber == 5:
            return (brightness, p, q)

    def toRGB(self, np_image):
        (row, col, _) = np_image.shape
        result = np.zeros((row, col, 3))
        for i in range(0, row):
            for j in range(0, col):
                (hue, saturation, brightness) = np_image[i, j]

                if saturation == 0:
                    result[i, j] = (brightness, brightness, brightness)
                    continue
                (r, g, b) = self.fractionalColors(hue, saturation, brightness)
                result[i, j] = (r * 255.0, g * 255.0, b * 255.0)

        return result

    def setHueDegree(self, degree, np_image):
        (row, col, _) = np_image.shape
        result = np.zeros((row, col, 3))
        for i in range(0, row):
            for j in range(0, col):
                (h, s, b) = np_image[i, j]
                result[i, j] = ((h + degree) % 360, s, b)
        return result

    def setHue(self, value, np_image):
        (row, col, _) = np_image.shape
        result = np.zeros((row, col, 3))
        for i in range(0, row):
            for j in range(0, col):
                (_, s, b) = np_image[i, j]
                h = 0.0
                if value > 360.0:
                    h = 360.0
                elif value > 0:
                    h = value
                result[i, j] = (h, s, b)
        return result

    def setSaturation(self, value, np_image):
        (row, col, _) = np_image.shape
        result = np.zeros((row, col, 3))
        for i in range(0, row):
            for j in range(0, col):
                (h, _, b) = np_image[i, j]
                s = 0.0
                if value > 1.0:
                    s = 1.0
                elif value > 0:
                    s = value
                result[i, j] = (h, s, b)
        return result

    def setSaturationDegree(self, degree, np_image):
        (row, col, _) = np_image.shape
        result = np.zeros((row, col, 3))
        for i in range(0, row):
            for j in range(0, col):
                (h, s, b) = np_image[i, j]
                result[i, j] = (h, (s + degree) % 1, b)
                result[i, j] = (h, s, b)
        return result

    def negative(self, np_image):
        result = np.zeros(np_image.shape)
        (row, col, _) = np_image.shape
        for i in range(0, row):
            for j in range(0, col):
                (h, s, b) = np_image[i, j]
                result[i, j] = (h, s, 1 - b)
        return result
