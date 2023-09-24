#!/usr/bin/python3

from catboost.datasets import titanic

train, test = titanic()

train.to_csv("../../data/RAW/train.csv", index=False)

test.to_csv("../../data/RAW/test.csv", index=False)
