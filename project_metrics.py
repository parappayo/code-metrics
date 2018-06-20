"""
Generates code metrics for a given project. Whereas code_metrics.py operates
on a single stream of source code input, this program walks a project tree and
generates reports based on all of the source code found.

TODO: project config should be supplied as input, not imported
"""

import os, config
from shutil import copyfile
import code_metrics, format_metrics

def is_code_file(path):
	filename, file_ext = os.path.splitext(path)
	return file_ext in config.code_filename_extensions

def find_files(root_path, filter):
	result = []
	for root, dirs, files in os.walk(root_path):
		for file_name in files:
			if not filter(file_name):
				continue
			path = os.path.join(root, file_name)
			result.append(path)
	return result

def report(project_root):
	result = {}
	for path in find_files(project_root, is_code_file):
		target_lang = code_metrics.file_ext_lang(path)
		with open(path, 'r') as input_file:
			try:
				result[path] = code_metrics.report(path, input_file.read(), target_lang)
			except IOError:
				continue
	return result

def write_report_file(report, filepath, target_dir):
	if report == {}:
		return

	filename = os.path.basename(filepath)
	filename = filename.replace('.', '_')
	filename += '.html'
	out_file_path = target_dir + '/' + filename

	attempts = 1
	while os.path.exists(out_file_path):
		out_file_path += str(attempts)
		attempts += 1

	with open(out_file_path, 'w') as output_file:
		format_metrics.write_report(report, 'html', output_file)

def write_report(project_report, target_dir):
	if os.path.exists(target_dir):
		print('error: cannot create output dir', target_dir)
		exit()
	os.mkdir(target_dir)

	for filepath, report in project_report.items():
		write_report_file(report, filepath, target_dir)

if __name__ == '__main__':
	# TODO: make output dir configurable
	write_report(report(config.project_root), 'project_report')
	copyfile('Chart.min.js', './project_report/')
