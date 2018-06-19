"""
Generates metrics for given source code input.
"""

import sys, os, re, argparse

python_func_regex = re.compile('def\s+(.*)\(.*:')

lang_file_ext = {
	'.py': 'python',
	'.js': 'javascript',
	'.cs': 'csharp',
	'.c': 'c',
	'.cpp': 'cplusplus',
}

def distribution(values):
	result = {}
	for value in values:
		result[value] = result.get(value, 0) + 1
	return result

def file_ext_lang(path):
	filename, file_ext = os.path.splitext(path)
	return lang_file_ext.get(file_ext, 'python')

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

def report(code, target_lang):
	if target_lang != 'python':
		print('input lang not supported yet:', target_lang)
		exit()
	lines = code.splitlines()
	return {
		'line_count': len(lines),
		'lines_ending_in_whitespace_count': lines_ending_in_whitespace_count(lines),
		'line_length_distribution': line_length_distribution(lines),
		'line_indent_distribution': line_indent_distribution(lines),
		'functions': report_functions(lines)
	}

def print_report(report, format):
	if format == 'pydict':
		print(report)
	else:
		print('html output not supported yet')

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('input_file_path', metavar='file')
	parser.add_argument('--lang', nargs='?',
		help='override input language',
		choices=['c', 'cplusplus', 'javascript', 'python'])
	parser.add_argument('--format', nargs='?',
		help='override output format',
		choices=['html', 'pydict'])
	args = parser.parse_args()

	path = args.input_file_path

	target_lang = args.lang
	if not target_lang:
		ext_lang = file_ext_lang(path)
		if ext_lang:
			target_lang = ext_lang
		else:
			target_lang = 'python'

	output_format = args.format
	if not output_format:
		output_format = 'html'

	with open(path, "r") as input_file:
		code = input_file.read()
		print_report(report(code, target_lang), args.format)
