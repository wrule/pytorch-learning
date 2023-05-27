def main():
  in_file_path = './data/btcusdt-1683364830172.json'
  out_file_path = in_file_path.replace('.json', '.csv')
  in_file = open(in_file_path)
  out_file = open(out_file_path, 'w')
  for line in in_file.readlines():
      line = line.strip().strip(',').strip('[').strip(']')
      out_file.writelines([line, '\n'])
  out_file.close()
  in_file.close()

main()
# print('9999old1234'.replace('old', 'new'))
