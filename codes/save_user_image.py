import random
import os
# My own codes import
import directory


def save_temp(img, address):
    img.save(address)


def save_predict(img, number, address):
    address += number + '/'
    files_in_folder = os.listdir(address)
    while True:
        name = f'/{random.randint(0,100_000)}.jpg'
        if name not in files_in_folder:
            img.save(address + name)
            break
