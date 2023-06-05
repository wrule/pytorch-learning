#!python3
import torch
import pandas as pd

def csv_to_tensor(csv_path):
  df = pd.read_csv(csv_path, header = None)
  return torch.tensor(df.to_numpy())

def main():
  t = csv_to_tensor('./data/ethusdt-1683364860372.csv')
  print(t.__len__())

main()
