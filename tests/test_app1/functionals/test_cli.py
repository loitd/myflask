import pytest
from pytest import ExitCode

# Possible exit codes
# Running pytest can result in six different exit codes:

# Exit code 0 All tests were collected and passed successfully
# Exit code 1 Tests were collected and run but some of the tests failed
# Exit code 2 Test execution was interrupted by the user
# Exit code 3 Internal error happened while executing tests
# Exit code 4 pytest command line usage error
# Exit code 5 No tests were collected

def test_mig_upgrade_dadb312e05e9(app, cli):
    rslt = cli.invoke(args=['db', 'upgrade', 'dadb312e05e9'])
    assert rslt is not None