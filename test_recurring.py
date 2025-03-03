import subprocess

import recurring

# e2e

def test_e2e():
    process = subprocess.run(
        './recurring.py 1 3'.split(),
        capture_output=True,
        text=True,
    )
    assert process.returncode == 0
    assert process.stdout == '0.(3)\n'

def test_e2e_bad_arg_count():
    process = subprocess.run(
        'python3 recurring.py 1'.split(),
        capture_output=True,
        text=True,
    )
    assert process.returncode == 1
    assert process.stdout == ''
    assert process.stderr.startswith(
        'Usage: recurring.py NUMERATOR DENOMINATOR'
    )

def test_e2e_bad_args():
    process = subprocess.run(
        'python3 recurring.py one three'.split(),
        capture_output=True,
        text=True,
    )
    assert process.returncode == 1
    assert process.stdout == ''
    assert process.stderr == 'Need integer args\n'

# unit

def test_divide_integer():
    assert recurring.divide(0, 3) == '0'
    assert recurring.divide(4, 2) == '2'
    assert recurring.divide(12, 3) == '4'
    assert recurring.divide(100, 2) == '50'

def test_divide_non_recurring_fraction():
    assert recurring.divide(1, 4) == '0.25'

def test_divide_recurring_fraction():
    assert recurring.divide(1, 3) == '0.(3)'
    assert recurring.divide(10, 3) == '3.(3)'
    assert recurring.divide(1, 999) == '0.(001)'
    assert recurring.divide(999, 7) == '142.(714285)'
    assert recurring.divide(999, 23) == '43.(4347826086956521739130)'
