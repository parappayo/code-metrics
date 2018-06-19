# code-metrics

Python scripts for scraping code projects and gathering statistics. The goal is to create helpful reports on which files in a project are good candidates for code auditing and clean-up.

For example, code files with lots of dependencies are likely important and should be well maintained. Large code files may benefit from being decomposed into smaller units. Code files with minor typographical errors such as trailing whitespace may have been hastily authored and not carefully checked.

Target language support is intended to be broad and focus on commonly applicable stats.

# Usages

There are two major entry points into the code-metrics project.

## code_metrics.py

This program generates code metrics for a single target file. It expects to be configured via command-line arguments. It can also be imported and used as a library.

## project_metrics.py

This program generates code metrics for a project comprised of code files. It expects to be configured via a settings file. The code files in the target project may consist of different programming languages.

# Features Wishlist

## Lang Support

* By default use filename to determine language type
* Can manually set language
* Python
* Generic curly-langs (C, C++, C#, Java, JavaScript)

## Output

* HTML format output with nice charts (Chart.js)
* human-readable output by default

## Stats

* Custom regex rules to generate line counts / distributions for
* Max nested scope depth (configurable for curlys, parens, brackets, keywords)
* Nested scope depth stats (number of instances of each depth)
* Line counts within a scope stats
* Member function, member variable stats (requires reflection?)
* Include / Using count stats, most number of dependencies
* Include depth stats (tree of includes), largest total compilation units

## Revision Control Integration

* git support
* Subversion support
* Most frequently touched files, count / distribution
* Count / distribution (per week) of unique users who touched files

# Helpful Links

* [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
