import sys

with open(sys.argv[1], 'r') as inp_file:
	with open(sys.argv[2], 'w') as out_file:
		for line in inp_file:
			if ("TESTS.PAS" in line.upper()) or ("TESTSCONST.PAS" in line.upper()):
				print(line.upper())
				line = line.replace("'..\\", "'..\\UnitTests\\")
				print(line)
			out_file.write(line)
