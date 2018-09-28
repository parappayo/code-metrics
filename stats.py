"""
Statistics helper methods.
"""

def distribution(values):
	result = {}
	for value in values:
		result[value] = result.get(value, 0) + 1
	return result

def sort_distribution(distr_dict):
	keys, values = [], []
	for key in sorted(distr_dict):
		keys.append(key)
		values.append(distr_dict[key])
	return keys, values

def merge_into_distribution(dest, src):
	for key, value in src.items():
		dest[key] = dest.get(key, 0) + value

class Metric:
	def __init__(self, id, name, type, method):
		self.id = id
		self.name = name
		self.type = type
		self.method = method

	def __str__(self):
		print('id={metric.id},name={metric.name},type={metric.type}',
			metric=self)

	def count(self, data):
		return sum(map(self.method, data))

	def distribution(self, data):
		return distribution(map(self.method, data))

	def value(self, data):
		if self.type == 'bool':
			return self.count(data)
		if self.type == 'int':
			return self.distribution(data)
