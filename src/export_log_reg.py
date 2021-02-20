# coding=utf-8
"""Export double model to C."""

from joblib import load

if __name__ == '__main__':
    model1 = load('model1.joblib')
    model2 = load('model2.joblib')
    print(model1.intercept_, model1.coef_)
    print(model2.intercept_, list(model2.coef_[0]))
    print(len(model2.coef_[0]))