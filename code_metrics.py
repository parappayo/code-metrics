"""
Generates metrics for given source code input.

Command Line:
> python code_metrics.py [file path]
"""

import sys

def ends_with_whitespace(line):
	if len(line) < 1: return False
	return line[len(line)-1].isspace()

def line_count(code):
	return code.count('\n')

def lines_ending_in_whitespace_count(lines):
	return sum(map(ends_with_whitespace, lines))

def length_per_line(lines):
	result = {}
	for line in lines:
		line_len = len(line)
		if line_len in result:
			result[line_len] += 1
		else:
			result[line_len] = 1
	return result

def report(code):
	lines = code.splitlines()
	return {
		'line_count': line_count(code),
		'lines_ending_in_whitespace_count': lines_ending_in_whitespace_count(lines),
		'length_per_line': length_per_line(lines)
	}

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print(__doc__)
		#TODO: test() - import code_metrics_test.py
		exit()

	path = sys.argv[1]
	with open(path, "r") as input_file:
		code = input_file.read()
		print(report(code))
