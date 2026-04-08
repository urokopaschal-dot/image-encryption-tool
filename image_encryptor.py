from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]

            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save("encrypted_image.png")
    print("Encrypted image saved!")


def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]

            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save("decrypted_image.png")
    print("Decrypted image saved!")


print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Choose: ")
image = input("Enter image name (e.g. photo.png): ")
key = int(input("Enter key: "))

if choice == "1":
    encrypt_image(image, key)
elif choice == "2":
    decrypt_image(image, key)
else:
    print("Invalid choice")