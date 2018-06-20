"""
Methods to output code metrics in html or other formats.
"""

import stats

html_report_format = """
<!doctype html>
<html>

<head>
<title>Metrics: {report[source_path]}</title>
<script src="Chart.min.js"></script>
</head>

<body>

<h1>Metrics: {report[source_path]}</h1>

<table>
<tr><td>Line Count</td><td>{report[line_count]}</td></tr>
<tr><td>Trailing Whitespace Lines</td><td>{report[lines_ending_in_whitespace_count]}</td></tr>
<tr><td>Function Count</td><td>{function_count}</td></tr>
</table>

{charts}

</body>
</html>
"""

html_chart_format = """
<h3>{title}</h3>
<canvas id="{id}" width="200" height="100"></canvas>

<script>
var ctx = document.getElementById("{id}").getContext('2d');
var {id} = new Chart(ctx, {{
	type: 'bar',
	data: {{
		labels: {keys},
		datasets: [{{
			label: '{label}',
			data: {values}
		}}]
	}},
	options: {{
		scales: {{
			yAxes: [{{
				ticks: {{
					beginAtZero:true
				}}
			}}]
		}}
	}}
}});
</script>
"""

def function_length_distribution(functions_report):
	result = {}
	for function_name, report in functions_report.items():
		line_count = report['line_count']
		result[line_count] = result.get(line_count, 0) + 1
	return result

def charts_html(report):
	charts = []
	keys, values = stats.sort_distribution(report['line_length_distribution'])
	charts.append(html_chart_format.format(
		title='Line Lengths',
		label='line count',
		id='line_length_distribution',
		keys=keys,
		values=values))
	keys, values = stats.sort_distribution(report['line_indent_distribution'])
	charts.append(html_chart_format.format(
		title='Line Indents',
		label='line count',
		id='line_indent_distribution',
		keys=keys,
		values=values))
	keys, values = stats.sort_distribution(function_length_distribution(report['functions']))
	charts.append(html_chart_format.format(
		title='Function Lengths',
		label='function count',
		id='function_length_distribution',
		keys=keys,
		values=values))
	return ''.join(charts)

def print_report(report, format):
	if format == 'pydict':
		print(report)
	else:
		print(html_report_format.format(
			report=report,
			function_count=len(report['functions']),
			charts=charts_html(report)))