#!python3
import torch
import pandas as pd

def main():
  print('你好，世界')
  df = pd.read_csv('./data/ethusdt-1683364860372.csv', header = None)
  print(df.head(10))

main()
