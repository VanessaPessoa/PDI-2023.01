import cv2
import numpy as np
from filters.correlation import Correlation


def load_image(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError
        return img
    except FileNotFoundError:
        print("Não foi possível encontrar a imagem.")
        return None


def apply_filter_and_save(correlation, img, mask_filename, output_filename):
    correlation.open_mask(mask_filename)
    filtered_image = correlation.apply(img)
    cv2.imwrite(output_filename, filtered_image)
    return filtered_image


def main():
    name_img = input("Informe o nome da imagem a ser tratada: ")
    image_format = input("Informe o formato da imagem: ")
    image_path = f"img/{name_img}.{image_format}"
    img_original = load_image(image_path)

    if img_original is None:
        return

    correlation = Correlation()

    apply_filter_and_save(
        correlation,
        img_original,
        "kernel/FiltroBox.txt",
        f"output/q4/{name_img}_Box.{image_format}",
    )

    sobelHotizontal = apply_filter_and_save(
        correlation,
        img_original,
        "kernel/SobelHorizontal.txt",
        f"output/q4/{name_img}_SobelHorizontal.{image_format}",
    )
    sobelVertical = apply_filter_and_save(
        correlation,
        img_original,
        "kernel/SobelVertical.txt",
        f"output/q4/{name_img}_SobelVertical.{image_format}",
    )
    gradient_magnitude = np.sqrt(sobelHotizontal**2 + sobelVertical**2)
    cv2.imwrite(f"output/q4/{name_img}_Sobel.{image_format}", gradient_magnitude)


if __name__ == "__main__":
    main()
