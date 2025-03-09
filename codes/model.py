from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dense, Dropout
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import directory

global a
# Create a custom callback for saving the model


class SaveModelCallback(tf.keras.callbacks.Callback):
    global a

    def __init__(self, filepath, val_loss, val_accuracy):
        super(SaveModelCallback, self).__init__()
        self.filepath = filepath
        self.best_val_loss = val_loss
        self.best_val_accuracy = val_accuracy

    def on_epoch_end(self, epoch, logs=None):
        current_val_loss = logs.get('val_loss')
        current_val_accuracy = logs.get('val_accuracy')

        if (current_val_loss < self.best_val_loss) and (current_val_accuracy > self.best_val_accuracy):

            self.best_val_loss = min(self.best_val_loss, current_val_loss)
            self.best_val_accuracy = max(self.best_val_accuracy, current_val_accuracy)

            a[0] = self.best_val_loss
            a[1] = self.best_val_accuracy

            with open(address + directory.temp_txt, 'a+') as f:
                f.write(f'val_accuracy: {self.best_val_accuracy:.4f}\nval_loss: {self.best_val_loss:.4f}\n---------------------------------\n')

            # Save the model
            self.model.save(self.filepath, overwrite=True)

            print(f'\nModel saved at {self.filepath}\n')


a = [100, -100]

address = directory.add()
train_data = pd.read_csv(address + directory.persian_alphabet_train_img_csv)

for j in range(5):
    train_data = train_data.sample(frac=1)  # shuffle train_data

x_train = train_data.iloc[:, :-1].values  # select all row and all columns except last one which is lable
y_train = train_data.iloc[:, -1].values   # select all row and only last column  which is lable

model = keras.Sequential([
    keras.Input(shape=(784,)),

    Dense(units=300, activation='relu'),
    Dropout(0.2),  # Add dropout layer with a rate of 0.2 (20%)

    Dense(units=200, activation='relu'),
    Dropout(0.2),  # Add dropout layer with a rate of 0.2 (20%)

    Dense(units=32, activation='softmax'),
])

early_stopping = EarlyStopping(
    monitor='val_loss',
    patience=4,          # Number of epochs with no improvement to wait before stopping
    restore_best_weights=True  # Restore model weights from the epoch with the best validation loss
)

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Create an instance of the custom callback
save_model_callback = SaveModelCallback(filepath=address + directory.hand_write_persian_alphabet, val_loss=a[0], val_accuracy=a[1])

model.fit(x_train, y_train, batch_size=5, epochs=50, validation_split=0.1, callbacks=[early_stopping, save_model_callback], shuffle=True)
