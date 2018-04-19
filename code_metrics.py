"""
Generates metrics for given source code input.

Command Line:
> python code_metrics.py [file path]
"""

import sys

def line_count(code):
	return code.count('\n')

def line_length_histogram(code):
	result = {}
	for line in code.splitlines():
		line_len = len(line)
		if line_len in result:
			result[line_len] += 1
		else:
			result[line_len] = 1
	return result

def report(code):
	print("work in progress")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print(__doc__)
		#TODO: test() - import code_metrics_test.py
		exit()

	path = sys.argv[1]
	with open(path, "r") as input_file:
		code = input_file.read()
		print(report(code))
