# code-metrics

Python scripts for scraping code projects and gathering statistics. The goal is to create helpful reports on which files in a project are good candidates for code auditing and clean-up.

For example, code files with lots of dependencies are likely important and should be well maintained. Large code files may benefit from being decomposed into smaller units. Code files with minor typographical errors such as trailing whitespace may have been hastily authored and not carefully checked.

# Features Wishlist

* Line count per file stats
* Line length stats
* Count of lines with trailing whitespace (configurable)
* List of custom regex rules to generate line counts for
* Max nested scope depth (configurable for curlys, parens, brackets, keywords)
* Nested scope depth stats (number of instances of each depth)
* Line counts within a scope stats
* Member function, member variable stats (requires reflection?)
* Include / Using count stats, most number of dependencies
* Include depth stats (tree of includes), largest total compilation units
* Most frequently touched files (git, svn)
* Most number of users touched files (git, svn)

# Helpful Links

* [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
