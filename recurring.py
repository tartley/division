#!/usr/bin/env python3
import sys

def divide(numerator: int, denominator:int) -> str:
    # Accumulate parts of our result here
    results = []
    # Remainders seen to date, mapped to their position in the result
    remainders = {}
    while True:
        int_part = str(numerator // denominator)
        remainder = numerator % denominator
        numerator = remainder * 10
        results.append(int_part)

        # If there is no remainder, we are done
        if remainder == 0:
            break

        # Add a decimal point after our first integer part
        if len(results) == 1:
            results.append(".")

        # We have found a cycle of decimal digits! Insert parens into results,
        # from the last position of this remainder, up to the current digit.
        if remainder in remainders:
            last_pos = remainders[remainder]
            results = (
                results[:last_pos] +
                ["("] +
                results[last_pos:] +
                [")"]
            )
            break
        # Remember the position at which we saw this remainder
        remainders[remainder] = len(results)

    return ''.join(results)

def parse_cmdline(args):
    assert \
        len(sys.argv) == 3, \
        "Usage: recurring.py NUMERATOR DENOMINATOR # (both ints)"
    try:
        numerator = int(args[0])
        denominator = int(args[1])
        return numerator, denominator
    except ValueError:
        assert 0, "Need integer args"

def main():
    try:
        numerator, denominator = parse_cmdline(sys.argv[1:])
        print(divide(numerator, denominator))
    except AssertionError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

