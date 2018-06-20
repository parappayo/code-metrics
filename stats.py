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
