import base64
import os
from Crypto.Cipher import AES


def pad(byte_array):
    BLOCK_SIZE = 16
    pad_len = BLOCK_SIZE - len(byte_array) % BLOCK_SIZE
    return byte_array + (bytes([pad_len]) * pad_len)


def encrypt(key, message):
    byte_array = message.encode("UTF-8")
    padded = pad(byte_array)
    iv = os.urandom(AES.block_size)
    cipher = AES.new(key.encode("UTF-8"), AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    return base64.b64encode(iv + encrypted).decode("UTF-8")


def unpad(byte_array):
    last_byte = byte_array[-1]
    return byte_array[0:-last_byte]


def decrypt(key, message):
    byte_array = base64.b64decode(message)
    iv = byte_array[0:16]
    messagebytes = byte_array[16:]
    cipher = AES.new(key.encode("UTF-8"), AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(messagebytes)
    decrypted = unpad(decrypted_padded)
    return decrypted.decode("UTF-8")