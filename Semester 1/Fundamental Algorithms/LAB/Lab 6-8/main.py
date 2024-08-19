from tests.point_tests import run_tests
from ui.console import console

if __name__ == "__main__":
    run_tests()  # running the tests
    print("All tests passed!\n")
    console()  # running the interface menu
