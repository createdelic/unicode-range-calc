import argparse


ignore_unicode_ranges = [
    (0, 0x1f),  # C0 controls (don't ignore space character which is 0x20)
]

FORMAT_ID_RANGE='range'
FORMAT_ID_RANGE_WITH_CHARACTERS='range_with_characters'
FORMAT_ID_CHARACTERS= 'characters'


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

    parser.add_argument('--format', help='the format to use', required=True, choices=[
        FORMAT_ID_RANGE,
        FORMAT_ID_RANGE_WITH_CHARACTERS,
        FORMAT_ID_CHARACTERS,
    ])

    parser.add_argument("--ignore-chars",
                        dest='ignored_chars',
                        action='append')

    parser.add_argument('--require-chars',
                        dest="required_chars",
                        action='append')

    parser.add_argument('file',
                        type=argparse.FileType('r', encoding='UTF-8'),
                        nargs='*')

    args = parser.parse_args()

    ignored_chars = ''
    if args.ignored_chars:
        ignored_chars = ''.join(args.ignored_chars)

    charset = set()

    if args.required_chars:
        for entry in args.required_chars:
            charset.update(entry)

    for f in args.file:
        for line in f:
            charset.update(line)

    ordered_codes = sorted([ord(x)
                            for x
                            in charset
                            if not (ranges_contains_value(ignore_unicode_ranges, ord(x)) or (x in ignored_chars))])
    code_ranges = to_ranges(ordered_codes)

    format = args.format
    if format == FORMAT_ID_RANGE_WITH_CHARACTERS:
        for (a, b) in code_ranges:
            if a == b:
                print("{:04x}({})".format(a, chr(a)))
            else:
                print("{:04x}({})-{:04x}({})".format(a, chr(a), b, chr(b)))
    elif format == FORMAT_ID_RANGE:
        for (a, b) in code_ranges:
            if a == b:
                print("{:04x}".format(a))
            else:
                print("{:04x}-{:04x}".format(a, b))
    else:
        result = []
        for (a, b) in code_ranges:
            if a == b:
                result.append(chr(a))
            else:
                for x in range(a, b+1):
                    result.append(chr(x))
        print("[" + "".join(result) + "]")


if __name__ == '__main__':
    main()