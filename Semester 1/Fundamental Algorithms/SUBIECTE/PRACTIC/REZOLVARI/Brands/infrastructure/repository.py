from domain.brand import Brand


class BrandRepo:
    def __init__(self, brands):
        self.__brands = brands

    def get_all(self):
        return self.__brands

    def print_all(self):
        for brand in self.get_all():
            print(str(brand))

    def delete_brand_by_name(self, name):
        """
        It delets all brands that have the given name
        In: name - str
        Out: -
        Error: ValueError - if there are no elements in list
        """
        brands = self.get_all()
        lenght = len(brands)
        for brand in brands[:]:
            if brand.get_name() == name:
                brands.remove(brand)
        if len(brands) == lenght:
            raise ValueError("no brand with given name!")

    def get_brands_with_net_worth_higher_than_value(self, value):
        """
        It returns the brands whose net worth are higher than given value
        In: value - int
        Out: list of brands
        Error: Value error - if there are no elements in list or if there are no elements with the given property
        """
        brands = self.get_all()
        if len(brands) == 0:
            raise ValueError("There are no brands!")
        filtered = list(filter(lambda x: x.get_net_worth() > value, brands))
        if len(filtered) == 0:
            raise ValueError("There are no brands with net worth higher than given value!")
        return filtered

    def get_net_worth_of_companies_after_number_of_months(self, number):
        """
        It prints the brands name and their net worth after given number of months
        In: number - int
        Out:
        :param number:
        :return:
        """
        brands = self.get_all()
        if len(brands) == 0:
            raise ValueError("There are no brands!")
        print("After " + str(number) + " months: \n")
        for brand in brands:
            new = brand.get_net_worth()
            for i in range(0, number):
                new += new * brand.get_predicted_monthly_growth() / 100
            print(brand.get_name() + " - " + str(new))


def repo_tests():
    brands = []
    repo = BrandRepo(brands)
    try:
        repo.get_brands_with_net_worth_higher_than_value(1)
        assert False
    except ValueError as ve:
        assert str(ve) == "There are no brands!"
    b1 = Brand("Microsoft", 1000, 1)
    brands.append(b1)
    repo = BrandRepo(brands)
    try:
        repo.get_brands_with_net_worth_higher_than_value(1001)
        assert False
    except ValueError as ve:
        assert str(ve) == "There are no brands with net worth higher than given value!"
    assert repo.get_brands_with_net_worth_higher_than_value(999) == [b1]
    print("Repo tests passed!\n")


repo_tests()
