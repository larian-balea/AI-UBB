class Brand:
    def __init__(self, name, net_worth, predicted_monthly_growth):
        self.__name = name
        self.__net_worth = net_worth
        self.__predicted_monthly_growth = predicted_monthly_growth

    def get_name(self):
        return self.__name

    def get_net_worth(self):
        return self.__net_worth

    def get_predicted_monthly_growth(self):
        return self.__predicted_monthly_growth

    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("name should be string!")
        self.__name = name

    def set_net_worth(self, net_worth):
        if not isinstance(net_worth, int):
            raise ValueError("net worth should be integer!")
        self.__net_worth = net_worth

    def set_predicted_monthly_growth(self, predicted_monthly_growth):
        if isinstance(predicted_monthly_growth, int):
            predicted_monthly_growth = float(predicted_monthly_growth)
        if not isinstance(predicted_monthly_growth, float):
            raise ValueError("predicted_monthly_growth should be float!")
        self.__predicted_monthly_growth = predicted_monthly_growth

    def __str__(self):
        return self.get_name() + " - " + str(self.get_net_worth()) + " - " + str(self.get_predicted_monthly_growth())

    def __repr__(self):
        return str(self)


def domain_tests():
    b1 = Brand("Microsoft", 1000, 1)
    try:
        b1.set_name(1)
        assert False
    except ValueError as ve:
        assert str(ve) == "name should be string!"
    b1.set_name("Google")
    b1.set_net_worth(1500)
    b1.set_predicted_monthly_growth(10)
    assert b1.get_name() == "Google"
    assert b1.get_net_worth() == 1500
    assert b1.get_predicted_monthly_growth() == 10.0
    assert str(b1) == "Google - 1500 - 10.0"
    print("Domain tests passed!")


domain_tests()
