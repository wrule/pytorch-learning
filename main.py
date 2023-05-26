import torch

def main():
  x = torch.rand(5, 3)
  print(x)
  f = open('./data/btcusdt-1683364830172.json')
  print('read')
  lines = f.read()
  print(lines[0])
  print('ok')
  f.close()
  input("Press Enter to continue...")

main()
