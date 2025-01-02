This repository demonstrates a common error in Python:  handling empty lists and type errors in calculations. The `bug.py` file contains code that calculates the average of a list of numbers. This code is designed to fail in two ways:

1. **Empty List:** If an empty list is passed as input, the code handles it gracefully and returns 0 to avoid a `ZeroDivisionError`.
2. **Type Error:** If the input list contains non-numeric elements (e.g. strings), a `TypeError` will occur because the `sum()` function can not be applied to mixed types.

The `bugSolution.py` file provides a corrected version of the code that addresses these potential issues. This solution utilizes error handling (try-except blocks) to gracefully deal with these edge cases and return appropriate results.