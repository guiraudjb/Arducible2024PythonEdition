import PIL.Image

def main():
    # Ouvrir l'image
    image = PIL.Image.open("image.jpg")

    # Convertir l'image en nuances de gris
    image = image.convert("L")

    # Réduire la résolution de l'image
    image = image.resize((100, 100))

    # Enregistrer l'image
    image.save("image_dessinee.jpg")


if __name__ == "__main__":
    main()
