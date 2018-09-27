"""
Generates a metrics report for given source code input.

Loosely speaking, the following dependencies are employed:
- code_parse.py is used to gather raw metrics about the input
- stats.py is used to gather statistics from the raw metrics
- metrics_formatter.py is used to generate output from the metrics
"""

import os, argparse
import stats, line_metrics, code_parse, metrics_formatter

lang_file_ext = {
	'.py': 'python',
	'.js': 'javascript',
	'.cs': 'csharp',
	'.c': 'c',
	'.cpp': 'cplusplus',
}

def file_ext_lang(path):
	filename, file_ext = os.path.splitext(path)
	return lang_file_ext.get(file_ext, 'generic')

def lines_ending_in_whitespace_count(lines):
	return sum(map(line_metrics.ends_with_whitespace, lines))

def line_length_distribution(lines):
	return stats.distribution(map(len, lines))

def line_indent_distribution(lines):
	return stats.distribution(map(line_metrics.indent_level, lines))

def report_function(lines):
	return {
		'line_count': len(lines)
	}

def report_functions(lines):
	result = {}
	functions = code_parse.split_functions_python(lines) #TODO: if lang == Python
	for name, lines in functions.items():
		result[name] = report_function(lines)
	return result

def report(path, code, target_lang):
	if target_lang != 'python':
		print('input lang not supported yet:', target_lang)
		return {}
	lines = code.splitlines()
	# TODO: need to gather stats about classes also
	return {
		'source_path': path,
		'line_count': len(lines),
		'lines_ending_in_whitespace_count': lines_ending_in_whitespace_count(lines),
		'line_length_distribution': line_length_distribution(lines),
		'line_indent_distribution': line_indent_distribution(lines),
		'functions': report_functions(lines)
	}

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('input_file_path', metavar='file')
	parser.add_argument('--lang', nargs='?',
		help='override input language',
		choices=['c', 'cplusplus', 'generic', 'javascript', 'python'])
	parser.add_argument('--format', nargs='?',
		help='override output format',
		choices=['html', 'pydict'])
	args = parser.parse_args()

	path = args.input_file_path

	target_lang = args.lang
	if not target_lang:
		target_lang = file_ext_lang(path)

	output_format = args.format
	if not output_format:
		output_format = 'html'

	with open(path, "r") as input_file:
		code = input_file.read()
		metrics_formatter.write_report(report(path, code, target_lang), args.format, sys.stdout)
