from passly.checks.duplicates import DuplicatesCheck
from passly.checks.multi_accounts import MultiAccountsCheck

CHECKS = {
    "duplicates": DuplicatesCheck,
    "multi_accounts": MultiAccountsCheck,
}
