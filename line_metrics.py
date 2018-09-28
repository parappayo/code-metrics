"""
Defines metrics that operate per line.
"""

import stats

class Metric:
	def __init__(self, id, name, type, method):
		self.id = id
		self.name = name
		self.type = type
		self.method = method

	def __str__(self):
		print('id={metric.id},name={metric.name},type={metric.type}',
			metric=self)

class LineMetric(Metric):
	def count(self, lines):
		return sum(map(self.method, lines))

	def distribution(self, lines):
		return stats.distribution(map(self.method, lines))

	def value(self, lines):
		if self.type == 'bool':
			return self.count(lines)
		if self.type == 'int':
			return self.distribution(lines)

def indent_level(line):
	result = 0
	for c in line:
		if c.isspace():
			result += 1
		else:
			break
	return result

def ends_with_whitespace(line):
	if len(line) < 1: return False
	return line[len(line)-1].isspace()

default = [
	LineMetric(
		'line_length',
		'Line Length',
		'int',
		len ),
	LineMetric(
		'line_indent_level',
		'Line Indent Level',
		'int',
		indent_level ),
	LineMetric(
		'line_exists',
		'Line Count',
		'bool',
		lambda x: True ),
	LineMetric(
		'line_ends_with_whitespace',
		'Lines Ending in Whitespace',
		'bool',
		ends_with_whitespace ),
]
