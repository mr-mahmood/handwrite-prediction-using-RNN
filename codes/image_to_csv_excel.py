import csv
from PIL import Image
import random
import os
# My own codes import
import normalize_image as ni
import directory
persian_alphabet = {
    26: 'آ', 27: 'ب', 28: 'پ', 29: 'ت', 30: 'ث', 31: 'ج', 32: 'چ', 33: 'ح', 34: 'خ',
    35: 'د', 36: 'ذ', 37: 'ر', 38: 'ز', 39: 'ژ', 40: 'س', 41: 'ش', 42: 'ص', 43: 'ض',
    44: 'ط', 45: 'ظ', 46: 'ع', 47: 'غ', 48: 'ف', 49: 'ق', 50: 'ک', 51: 'گ', 52: 'ل',
    53: 'م', 54: 'ن', 55: 'و', 56: 'ه', 57: 'ی'
}


def to_csv_excel(address):

    name1 = address + directory.persian_alphabet_train_img_csv
    address += directory.persian_alphabet_train_dataset

    results = []
    temp = address
    for i in range(32):
        with open(name1, 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # go to folder of image for 0, 1, 2, 3 and, ...
            temp += f'{persian_alphabet[26+i]}'

            # Get a list of files in the folder
            files_in_folder = os.listdir(temp)
            for image_file in files_in_folder:
                # find path to every single image
                image_path = temp + '/' + image_file
                image = Image.open(image_path)
                image = ni.main(image)
                results.append([image, i])

            temp = address
            for j in range(5):
                random.shuffle(results)
            # Write each image (784 colums for every pixel and last colum for the number that is)
            for result in results:
                row = result[0] + [result[1]]  # Append the label to the end of the flattened image
                writer.writerow(row)
            results = []


if __name__ == '__main__':

    address = directory.add()
    to_csv_excel(address)
