# code-metrics

This project contains Python scripts for scraping code projects and gathering statistics. The goal is to generate helpful reports to inform code auditing and refactoring efforts.

For example, knowing which code files contain many or few dependencies can give an idea as to what interfaces are higher level or lower level in the project, thus informing reorganization efforts. Large code files may benefit from being decomposed into smaller units. Code files with minor typographical errors such as trailing whitespace may have been hastily authored and may need to be audited.

The intent of these tools is to provide broad support for many programming languages by focusing on commonly applicable stats. For instance, most languages do not use trailing whitespace as a useful syntax, so we assume it to be unwanted. Most programmers will helpfully indent their code to indicate scope, so indent level is tracked in the hope of providing some measure of complexity. This project will endeavour to make these features configurable.

# Usage

There are multiple entry points into the code-metrics project. The starting points that are most useful for users are summarized below.

## code_metrics.py

This program gathers code metrics for a single target file and generates a report. It expects to be configured via command-line arguments. It can also be imported and used as a library.

TODO: provide examples here

## project_metrics.py

TODO: make this program work

This program gathers code metrics for a project comprised of code files and generates a report. It expects to be configured via a settings file. The code files in the target project may consist of different programming languages.

TODO: provide examples here

## repo_metrics.py

TODO: create this program

This program gathers code metrics for revision control repository (such as git or Subversion) and generates a report. It expects to be configured via a settings file. The created report shows the progression of the project over time.

TODO: provide examples here

# Caveats

* Python 3 required
* This project is not mature. There is a long road ahead toward making it properly useful.
* Robust parsing of code is not a priority for this project. Expect pathelogical code to generate unpredictable results.

# Features Wishlist

## General

* Test suite using doctest
* Generate some sample output by running this against other GitHub repos
* Modularize language support so that language specific parser rules live in their own plug-ins

## Lang Support

* Default to "generic" if the target lang not explicitly supported
* Lisp
* JavaScript
* C#
* C
* C++
* PHP (nothing is too gross)

## Output

* can navigate around project html output, drill into reports on each file
* Per-file stats should automatically include each per-line stat mean, 20th, 50th, 80th percentile values
* Per-project stats should automatically include each per-file stat mean, 20th, 50th, 80th percentile values
* source code for functions also included in file output, can drill to see code
* syntax highlighting for source code in output

## Stats

* Source Lines of Code (SLOC)
* Assignments, Branches, Conditions (ABC)
* Per-line bool stat could be defined in settings as a regex
* Max nested scope depth (configurable for curlys, parens, brackets, keywords)
* Nested scope depth stats (number of instances of each depth)
* Member function, member variable stats (requires reflection?)
* Include / Using count stats, most number of dependencies
* Include depth stats (tree of includes), largest total compilation units
* Cyclomatic complexity - estimate the number of unique execution paths

## Revision Control Integration

* git support
* Subversion support
* Most frequently touched files, count / distribution
* Count / distribution (per week) of unique users who touched files
* Generate reports for history over time by syncing to past revisions

# Helpful Links

* [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [Pythex](https://pythex.org/)
