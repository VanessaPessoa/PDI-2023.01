import cv2
from filters.HSB import HSB
from filters.RGB import RGB


def load_image(image_path):
    try:
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise FileNotFoundError
        return img
    except FileNotFoundError:
        print("Não foi possível encontrar a imagem.")
        return None


def save_image(output_path, image):
    image_converted = cv2.convertScaleAbs(image)
    cv2.imwrite(output_path, image_converted)


def main():
    # Carregar a imagem
    name_img = input("Informe o nome da imagem a ser tratada: ")
    image_format = input("Informe o formato da imagem: ")
    image_path = f"img/{name_img}.{image_format}"
    img_original = load_image(image_path)

    if img_original is None:
        return

    rgb = RGB()
    hsb = HSB()

    # 1. Conversão RGB-HSB-RGB
    img_hsb = rgb.toHSB(img_original)
    save_image(f"output/q1/{name_img}_RGB_HSB.{image_format}", img_hsb)

    img_RGB_HSB_RGB = hsb.toRGB(img_hsb)
    save_image(f"output/q1/{name_img}_RGB_HSB_RGB.{image_format}", img_RGB_HSB_RGB)

    # 2. Alteração de matiz e saturação no HSB
    color = float(input("Informe um valor de 0 a 360 para ser a cor da matiz:"))
    img_hue_change_value = hsb.set_hue(color, img_hsb)
    save_image(
        f"output/q2/{name_img}_hue_change_value.{image_format}", img_hue_change_value
    )
    save_image(
        f"output/q2/{name_img}_hue_change_valueRGB.{image_format}",
        hsb.toRGB(img_hue_change_value),
    )

    degree = float(input("Informe um valor de 0 a 360 para somar no grau da matiz:"))
    img_hue_change_degree = hsb.set_hue_degree(degree, img_hsb)
    save_image(
        f"output/q2/{name_img}_hue_change_degree.{image_format}", img_hue_change_degree
    )
    save_image(
        f"output/q2/{name_img}_hue_change_degreeRGB.{image_format}",
        hsb.toRGB(img_hue_change_degree),
    )

    saturation = float(input("Informe um valor de 0 a 1 para ser a saturação:"))
    img_saturation_change_value = hsb.set_saturation(saturation, img_hsb)
    save_image(
        f"output/q2/{name_img}_saturation_change_value.{image_format}",
        img_saturation_change_value,
    )
    save_image(
        f"output/q2/{name_img}_saturation_change_valueRGB.{image_format}",
        hsb.toRGB(img_saturation_change_value),
    )

    degree = float(input("Informe um valor de 0 a 1 para somar no grau da saturação:"))
    img_saturation_change_degree = hsb.set_saturation_degree(degree, img_hsb)
    save_image(
        f"output/q2/{name_img}_saturation_change_degree.{image_format}",
        img_saturation_change_degree,
    )
    save_image(
        f"output/q2/{name_img}_saturation_change_degreeRGB.{image_format}",
        hsb.toRGB(img_saturation_change_degree),
    )

    # 3. Negativo em RGB e na banda V do HSV
    img_negative_RGB = rgb.negative(img_original)
    save_image(f"output/q3/{name_img}_negative_rgb.{image_format}", img_negative_RGB)

    img_negative_HSB = hsb.negative(img_hsb)
    save_image(f"output/q3/{name_img}_negative_hsb.{image_format}", img_negative_HSB)
    save_image(
        f"output/q3/{name_img}_negative_hsb_rgb.{image_format}",
        hsb.toRGB(img_negative_HSB),
    )


if __name__ == "__main__":
    main()
