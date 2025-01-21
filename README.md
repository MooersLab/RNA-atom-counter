![Version](https://img.shields.io/static/v1?label=RNA-atom-counter&message=0.1&color=brightcolor)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
# Tally the number of atoms by element in a given RNA strand

Some *ab inito* structure determination programs require the number
of atoms by element expected in the asymmetric unit.
This program returns the number of atoms by element based on the
single-letter RNA base sequence given as a command line argument.
This program assumes that there is a 5'-phosphate.
Adjust the results accordingly if this is not the case.

```bash
Usage: python script.py SEQUENCE
Example: python script.py AGCU
```

The script only depends on Python3.
It imports only the `sys` module.

## Update history

|Version      | Changes                                                                                                                                                                         | Date                 |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| Version 0.1 |   Added badges, funding, and update table.  Initial commit.                                                                                                                | 2025 January 20  |

## Sources of funding

- NIH: R01 CA242845
- NIH: R01 AI088011
- NIH: P30 CA225520 (PI: R. Mannel)
- NIH: P20 GM103640 and P30 GM145423 (PI: A. West)
