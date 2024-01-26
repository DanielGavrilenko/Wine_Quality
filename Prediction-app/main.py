import tensorflow as tf
import downloading_data as dw
from tensorflow.python.keras import initializers


def loss_fu(y_pred, y_real_res, n):
    res = 0
    for i in range(n):
        res += (y_pred[i] - y_real_res[i])**2
    return res


def main():
    x, y, n, n_features = dw.read_data()

    x_train_ds = []
    y_train_ds = []
    x_final_ds = []
    y_final_ds = []
    # 70% training set
    for i in range(int(0.7 * n)):
        x_train_ds.append([0.0] * n_features)
        y_train_ds.append([0])
    # 30% practise set
    for i in range(n - int(0.7 * n)):
        x_final_ds.append([0.0] * n_features)
        y_final_ds.append([0])

    '''
    dividing data set in two parts, for training and checking
    '''
    for i in range(int(0.7 * n)):
        for j in range(n_features):
            x_train_ds[i][j] = x[i][j]
        y_train_ds[i] = y[i]
    for i in range(int(0.7 * n), n):
        for j in range(n_features):
            x_final_ds[i - int(0.7 * n)][j] = x[i][j]
        y_final_ds[i - int(0.7 * n)] = y[i]

    # compiling model

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(n, activation='swish', bias_initializer=initializers.Zeros(), kernel_initializer=initializers.Zeros()),
        tf.keras.layers.Dense(10, activation='swish',),
        tf.keras.layers.Dense(1)
    ])

    model.compile(optimizer="Adam", loss=tf.keras.losses.MeanSquaredError())

    model.fit(x_train_ds, y_train_ds)
    y_predicts = model.predict(x_final_ds)

    print(loss_fu(y_predicts, y_final_ds, n - int(0.7 * n)))
    model.save('../Api-service/model-document')


if __name__ == "__main__":
    main()
