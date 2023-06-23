#!python3
import torch
import pandas as pd

def csv_to_tensor(csv_path):
  df = pd.read_csv(csv_path, header = None)
  return torch.tensor(df.to_numpy())

def main():
  t = csv_to_tensor('./data/btcusdt-1683364830172.csv')
  print(t.__len__())
  a = input('please input')
  print(a)

main()
