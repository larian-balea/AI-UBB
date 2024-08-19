from domain.brand import Brand
from infrastructure.repository import BrandRepo

brands = [Brand("Microsoft", 1000, 1),
          Brand("Google", 1500, 10),
          Brand("Twitter", 1200, -10),
          Brand("MiniMarket", 12, 0.1),
          Brand("SpecialistIT", 100, -1.1)]


def print_menu():
    print("\n"
          "0. Exit \n"
          "1. Delete brand by name\n"
          "2. Get brands with net worth higher than value\n"
          "3. Get net worth of companies after number of months\n")


def main():
    repo = BrandRepo(brands)
    while True:
        repo.print_all()
        print_menu()
        x = int(input("Enter command: "))
        if x == 0:
            return
        elif x == 1:
            name = input("Enter name: ")
            try:
                repo.delete_brand_by_name(name)
            except ValueError as ve:
                print(str(ve))
        elif x == 2:
            value = input("Enter value: ")
            try:
                value = int(value)
                repo.get_brands_with_net_worth_higher_than_value(value)
            except ValueError as ve:
                print(str(ve))
        elif x == 3:
            number = input("Enter number of months: ")
            try:
                number = int(number)
                repo.get_net_worth_of_companies_after_number_of_months(number)
            except ValueError as ve:
                print(str(ve))
        else:
            print("Invalid command!")
        print("\n")


main()
