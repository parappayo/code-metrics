"""
Generates metrics for given source code input.

Command Line:
> python code_metrics.py [file path]
"""

import sys, re

python_func_regex = re.compile('def\s+(.*)\(.*:')

def distribution(values):
	result = {}
	for value in values:
		result[value] = result.get(value, 0) + 1
	return result

def ends_with_whitespace(line):
	if len(line) < 1: return False
	return line[len(line)-1].isspace()

def lines_ending_in_whitespace_count(lines):
	return sum(map(ends_with_whitespace, lines))

def line_length_distribution(lines):
	return distribution(map(len, lines))

def line_indent_len(line):
	result = 0
	for c in line:
		if c.isspace():
			result += 1
		else:
			break
	return result

def line_indent_distribution(lines):
	return distribution(map(line_indent_len, lines))

def split_functions_python(lines):
	result = {}
	function_name = False
	function_body = False
	for line in lines:
		if function_name:
			if len(line.strip()) == 0:
				result[function_name] = function_body
				function_name = False
			else:
				function_body.append(line)
		else:
			match = re.match(python_func_regex, line)
			if match:
				function_name = match[1]
				function_body = []
	return result

def report_function(lines):
	return {
		'line_count': len(lines),
		'line_length_distribution': line_length_distribution(lines),
		'line_indent_distribution': line_indent_distribution(lines)
	}

def report_functions(lines):
	result = {}
	functions = split_functions_python(lines) #TODO: if lang == Python
	for name, lines in functions.items():
		result[name] = report_function(lines)
	return result

def report(code):
	lines = code.splitlines()
	return {
		'line_count': len(lines),
		'lines_ending_in_whitespace_count': lines_ending_in_whitespace_count(lines),
		'line_length_distribution': line_length_distribution(lines),
		'line_indent_distribution': line_indent_distribution(lines),
		'functions': report_functions(lines)
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
