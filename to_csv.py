def main():
  in_file = open('./data/btcusdt-1683364830172.json')
  out_file = open('./data/btcusdt-1683364830172.csv', 'w')
  for line in in_file.readlines():
      line = line.strip().strip(',').strip('[').strip(']')
      out_file.writelines([line, '\n'])
  out_file.close()
  in_file.close()

main()
