import pandas as pd


def read_data():
    df = pd.read_csv('Wine_quality\winequality-white.csv')
    # conversion data in array format
    arr_buf = df.to_numpy()
    # lenght of data set
    nw = 4890   # 3425
    #nw = 1000   # 702
    n = 11
    x = []
    y = []
    '''
    creating array of data set
    '''
    for i in range(nw):
        x.append([0.0] * n)
        y.append([0.0])
    for i in range(nw):
        first_space = 0
        for j in range(n):
            second_space = arr_buf[i][0].find(';', first_space)
            x[i][j] = float(arr_buf[i][0][first_space:second_space])
            first_space = second_space+1
        y[i] = float(arr_buf[i][0][first_space:])

    return x, y, nw, n
