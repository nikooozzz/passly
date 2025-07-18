import sys
import csv
from passly.cli import parse_args
from passly.output import OutputManager
from passly.checks import CHECKS


def load_entries(input_path):
    entries = []
    with open(input_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            entries.append(row)
    return entries


def main():
    args = parse_args()
    selected_checks = [c.strip() for c in args.check.split(",")]

    for c in selected_checks:
        if c not in CHECKS:
            print(f"Unknown check: {c}")
            sys.exit(1)

    entries = load_entries(args.input)
    output = OutputManager(output_path=args.output, color=args.color)

    for check_name in selected_checks:
        check_cls = CHECKS[check_name]
        check = check_cls(entries, output=output)
        check.run()


if __name__ == "__main__":
    main()
