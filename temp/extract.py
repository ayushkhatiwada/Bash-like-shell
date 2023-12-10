# open tests.py

f = open("tests.py", "r")
result_file = open("result.txt", "w")

for line in f:
  if "cmdline = " in line:
    if "#" not in line:
      result_file.write(line.lstrip('\t'))


f.close()
result_file.close()