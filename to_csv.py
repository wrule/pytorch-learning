import sys

def main():
  argv_path = sys.argv[len(sys.argv) - 1]
  if (not argv_path.lower().endswith('.json')): return
  in_file_path = argv_path
  out_file_path = in_file_path.replace('.json', '.csv')
  in_file = open(in_file_path)
  out_file = open(out_file_path, 'w')
  for line in in_file.readlines():
    line = line.strip().strip(',').strip('[').strip(']')
    out_file.writelines([line, '\n'])
  out_file.close()
  in_file.close()

main()
