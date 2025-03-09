import os


def add():
    # Get the directory of the current script and go to mnist images directory
    ADDRESS = os.path.dirname(os.path.abspath(__file__))
    ADDRESS = list(ADDRESS)
    ADDRESS[2] = "/"
    ADDRESS[len(ADDRESS) - 6:len(ADDRESS)] = "/"
    ADDRESS = ''.join(ADDRESS)

    return ADDRESS


temp_txt = 'files/neural network/temp.txt'


English_alphabet_temp_img = './alphabet canvas image.jpg'
# MNIST train
English_alphabet_train_img_csv = 'files/English alphabet/Train image/train_image_data_csv.csv'
English_alphabet_train_img_excel = 'files/English alphabet/Train image/train_image_data_excel.xlsx'
English_alphabet_train_dataset = 'database/English alphabet/Train/'
# MNIST my jpg
my_English_alphabet_dataset = 'database/English alphabet/Mine/'
hand_write_English_alphabet = 'files/neural network/English alphabet.h5'


persian_number_temp_img = './alphabet canvas image.jpg'
# MNIST train
persian_number_train_img_csv = 'files/persian number/Train image/train_image_data_csv.csv'
persian_number_train_img_excel = 'files/persian number/Train image/train_image_data_excel.xlsx'
persian_number_train_dataset = 'database/persian number/Train/'
# MNIST my jpg
my_persian_number_dataset = 'database/persian number/Mine/'
hand_write_persian_number = 'files/neural network/persian_number.h5'


persian_alphabet_temp_img = './alphabet canvas image.jpg'
# MNIST train
persian_alphabet_train_img_csv = 'files/persian alphabet/Train image/train_image_data_csv.csv'
persian_alphabet_train_img_excel = 'files/persian alphabet/Train image/train_image_data_excel.xlsx'
persian_alphabet_train_dataset = 'database/persian alphabet/Train/'
# MNIST my jpg
my_persian_alphabet_dataset = 'database/persian alphabet/Mine/'
hand_write_persian_alphabet = 'files/neural network/persian_alphabet.h5'
