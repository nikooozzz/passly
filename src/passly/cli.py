import argparse
from passly.checks import CHECKS


def parse_args():
    parser = argparse.ArgumentParser(
        description="Passly - A simple CLI toolkit for auditing password manager exports",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("input", help="Path to the input CSV file")

    available_checks = ", ".join(sorted(CHECKS.keys()))
    check_help = (
        "Comma-separated list of checks to run.\n"
        f"Available checks: {available_checks}"
    )
    parser.add_argument("--check", "-c", required=True, help=check_help)

    parser.add_argument("--output", "-o", help="Optional path to save the report")

    color_group = parser.add_mutually_exclusive_group()
    color_group.add_argument(
        "--color",
        choices=["true", "false"],
        default="true",
        help="Enable or disable color in output (default: true)",
    )
    parser.set_defaults(color=True)

    return parser.parse_args()
