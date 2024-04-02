from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Opening the image
    img = Image.open(image_path)
    # Converting the image to grayscale
    img = img.convert("L")
    # Converting the image to a numpy array
    img_array = np.array(img)

    # Applying the encryption algorithm
    encrypted_array = img_array + key

    # Clamping values to 0-255 range
    encrypted_array = np.clip(encrypted_array, 0, 255)

    # Converting the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))

    return encrypted_img

def decrypt_image(encrypted_img, key):
    # Converting the encrypted image to a numpy array
    encrypted_array = np.array(encrypted_img)

    # Applying the decryption algorithm
    decrypted_array = encrypted_array - key

    # Clamping values to 0-255 range
    decrypted_array = np.clip(decrypted_array, 0, 255)

    # Converting the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))

    return decrypted_img

image_path ="C:/Pictures/download.png"
key = 50

# Encrypting the image
encrypted_img = encrypt_image(image_path, key)
encrypted_img.save("C:/Pictures/encrypted_image.jpg")

# Decrypting the image
decrypted_img = decrypt_image(encrypted_img, key)
decrypted_img.save("C:/Pictures/decrypted_image.jpg")
