from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    # Convert the image to grayscale
    img = img.convert("L")
    # Convert the image to a numpy array
    img_array = np.array(img)

    # Apply the encryption algorithm
    encrypted_array = img_array + key

    # Clamp values to 0-255 range
    encrypted_array = np.clip(encrypted_array, 0, 255)

    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))

    return encrypted_img

def decrypt_image(encrypted_img, key):
    # Convert the encrypted image to a numpy array
    encrypted_array = np.array(encrypted_img)

    # Apply the decryption algorithm
    decrypted_array = encrypted_array - key

    # Clamp values to 0-255 range
    decrypted_array = np.clip(decrypted_array, 0, 255)

    # Convert the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))

    return decrypted_img

# Example usage
image_path ="C:/Pictures/download.png"
key = 50

# Encrypt the image
encrypted_img = encrypt_image(image_path, key)
encrypted_img.save("C:/Pictures/encrypted_image.jpg")

# Decrypt the image
decrypted_img = decrypt_image(encrypted_img, key)
decrypted_img.save("C:/Pictures/decrypted_image.jpg")
