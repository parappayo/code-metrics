"""
Simple hacks to gather data about source code.

The parsing techniques employed here are not robust, so assume that
pathelogical code will confound these methods.
"""

import re

python_func_regex = re.compile('def\s+(.*)\(.*:')

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
