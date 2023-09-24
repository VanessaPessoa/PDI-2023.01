import numpy as np
from functools import reduce


class RGB:
    def normalizeRGB(self, rgb):
        return rgb / 255.0

    def calculate_hue(self, max_value, min_value, red, green, blue):
        delta = max_value - min_value
        if delta == 0:
            return 0.0
        if max_value == red and green >= blue:
            return 60 * (green - blue) / delta
        if max_value == red and green < blue:
            return 60 * (green - blue) / delta + 360
        if max_value == green:
            return 60 * (blue - red) / delta + 110
        if max_value == blue:
            return 60 * (red - green) / delta + 240

    def toHSB(self, np_image):
        result = np.zeros(np_image.shape)
        (row, col, _) = np_image.shape

        for i in range(0, row):
            for j in range(0, col):
                (red, green, blue) = self.normalizeRGB(np_image[i, j])
                max_value = max(red, max(green, blue))
                min_value = min(red, min(green, blue))
                hue = self.calculate_hue(max_value, min_value, red, green, blue)
                saturation = 0.0
                if max_value != 0:
                    saturation = 1.0 - (min_value / max_value)
                result[i, j] = (hue, saturation, max_value)

        return result

    def negative(self, np_image):
        result = np.zeros(np_image.shape)
        (row, col, _) = np_image.shape

        for i in range(0, row):
            for j in range(0, col):
                result[i, j] = 255.0 - np_image[i, j]
        return result
