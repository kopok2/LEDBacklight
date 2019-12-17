# coding=utf-8
"""Led backlight change detection using machine learning techniques."""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression
from joblib import dump


if __name__ == '__main__':
    print('Led Backlight Machine Learning backend 2019 by Karol Oleszek')
    print('ON MODEL')
    print('Loading data...')
    data = pd.read_csv('outraw1.csv')

    print('Splitting data...')
    X = data.drop(['target'], axis=1)
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    print('Training model...')
    model = LogisticRegression()
    model.fit(X_train, y_train)

    print('Evaluating model...')
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))
    print('Test:')
    print(confusion_matrix(y_test, predictions))
    print('Training:')
    print(confusion_matrix(y_train, model.predict(X_train)))

    print('Saving model...')
    dump(model, 'model1.joblib')

    print('OFF MODEL')
    print('Loading data...')
    data = pd.read_csv('outraw2.csv')

    print('Splitting data...')
    X = data.drop(['target'], axis=1)
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    print('Training model...')
    model = LogisticRegression()
    model.fit(X_train, y_train)

    print('Evaluating model...')
    predictions = model.predict(X_test)
    print(classification_report(y_test, predictions))
    print('Test:')
    print(confusion_matrix(y_test, predictions))
    print('Training:')
    print(confusion_matrix(y_train, model.predict(X_train)))

    print('Saving model...')
    dump(model, 'model2.joblib')

    print('Ploting...')
    plt.plot(data)
    plt.show()