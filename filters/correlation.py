import numpy as np
import re


class Correlation:
    def __init__(self) -> None:
        self.kernel = []
        self.stride = None

    def open_mask(self, filename):
        self.kernel = []
        self.stride = None

        with open(filename, "r") as file:
            lines = file.readlines()
            for line in range(len(lines)):
                stride = re.findall("stride\s*=\s*(\d+)", lines[line])
                if stride:
                    self.stride = int(stride[0])
                else:
                    values = re.findall("([-+]?\d*\.?\d+)", lines[line])

                    if values:
                        row = np.array(list(map(float, values)))
                        if not self.kernel:
                            # Se self.kernel estiver vazio, adicione a primeira linha como uma única matriz
                            self.kernel.append(row)
                        else:
                            self.kernel.append(row)
            self.kernel = np.array(self.kernel)

    def apply(self, np_image):
        (m_kernel, n_kernel) = self.kernel.shape
        (m_image, n_image, _) = np_image.shape
        new_m = int((m_image - m_kernel) / self.stride) + 1
        new_n = int((n_image - n_kernel) / self.stride) + 1

        result = np.zeros((new_m, new_n, 3))

        for i in range(0, new_m):
            for j in range(0, new_n):
                # define a vizinhaça
                v = np_image[
                    i * self.stride : i * self.stride + m_kernel,
                    j * self.stride : j * self.stride + n_kernel,
                ]

                sum = 0

                # Realiza a correlação multiplicando a vizinhança pelo kernel
                for ii in range(0, m_kernel):
                    for jj in range(0, n_kernel):
                        sum += v[ii, jj] * self.kernel[ii, jj]

                result[i, j] = sum

        return result
