import sys
from passly.cli import parse_args
from passly.output import OutputManager
from passly.checks import CHECKS
from passly.parsers import get_parser


def main():
    args = parse_args()
    selected_checks = [c.strip() for c in args.check.split(",")]

    for c in selected_checks:
        if c not in CHECKS:
            print(f"Unknown check: {c}")
            sys.exit(1)

    format_parser = get_parser(args.vendor, args.input)
    entries = format_parser.parse(args.input)
    output = OutputManager(output_path=args.output, color=args.color)

    for check_name in selected_checks:
        check_cls = CHECKS[check_name]
        check = check_cls(entries, output=output)
        check.run()


if __name__ == "__main__":
    main()
