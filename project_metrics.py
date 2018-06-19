"""
Generates metrics for an given project.

TODO: project config should be supplied as input, not imported
"""

import os, config
import code_metrics

_all_file_paths = False

def is_source_file(filename):
	return filename.endswith(config.source_file_name_endings)

def find_files(root_path, file_test):
	result = []
	for root, dirs, files in os.walk(root_path):
		for file_name in files:
			if not file_test(file_name):
				continue
			path = os.path.join(root, file_name)
			result.append(path)
	return result

def get_all_file_paths(project_root):
	global _all_file_paths
	if not _all_file_paths:
		_all_file_paths = find_files(project_root, is_source_file)
	return _all_file_paths

def report(project_root):
	result = {}
	for path in get_all_file_paths(project_root):
		with open(path, "r") as input_file:
			try:
				result[path] = code_metrics.report(input_file.read())
			except IOError:
				continue
	return result

if __name__ == "__main__":
	print(report(config.project_root))
