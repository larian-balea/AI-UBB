from tests.vector_tests import run_tests
from ui.console import console


def main():
    run_tests()
    print("All tests passed!")
    console()


main()
