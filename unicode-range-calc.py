import argparse


ignore_unicode_ranges = [
    (0, 0x20),  # C0 controls + space
]


def ranges_contains_value(ranges, value):
    for (a, b) in ranges:
        if value >= a and value <= b:
            return True
    return False


def to_ranges(ordered_ints):
    result = []

    range_start_value = None
    range_end_value = None
    range_next_expected_value = None

    for x in ordered_ints:
        if not range_start_value:
            range_start_value = x
            range_end_value = x
            range_next_expected_value = x + 1
        elif range_next_expected_value != x:
            result.append((range_start_value, range_end_value))
            range_start_value = x
            range_end_value = x
            range_next_expected_value = x + 1
        else:
            range_end_value = x
            range_next_expected_value = x + 1

    if range_start_value:
        result.append((range_start_value, range_end_value))

    return result


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--show-chars",
                        dest='show_chars',
                        action='store_true',
                        required=False)

    parser.add_argument("--ignore-chars",
                        dest='ignored_chars',
                        action='store',
                        default='',
                        required=False)

    parser.add_argument('file',
                        type=argparse.FileType('r', encoding='UTF-8'),
                        nargs='+')

    args = parser.parse_args()

    ignored_chars = args.ignored_chars
    charset = set()

    for f in args.file:
        for line in f:
            charset.update(line)

    ordered_codes = sorted([ord(x)
                            for x
                            in charset
                            if not (ranges_contains_value(ignore_unicode_ranges, ord(x)) or (x in ignored_chars))])
    code_ranges = to_ranges(ordered_codes)

    if args.show_chars:
        for (a, b) in code_ranges:
            if a == b:
                print("{:04x}({})".format(a, chr(a)))
            else:
                print("{:04x}({})-{:04x}({})".format(a, chr(a), b, chr(b)))
    else:
        for (a, b) in code_ranges:
            if a == b:
                print("{:04x}".format(a))
            else:
                print("{:04x}-{:04x}".format(a, b))


if __name__ == '__main__':
    main()