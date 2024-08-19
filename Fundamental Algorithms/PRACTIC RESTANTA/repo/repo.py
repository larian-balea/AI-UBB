from domain.recipe import Recipe


class Repo:
    def __init__(self, lst):
        self.__lst = lst

    def get_all(self):
        return self.__lst

    def add(self, id, name, type, difficulty, time):
        """
        It adds an element to the list
        In: id - int
            name - str
            type - str
            difficulty - int
            time - int
        Out: -
        Error: if in variables ar invalid
        """
        if not id:
            print("invalid id!")
            return
        if not name:
            print("invalid name!")
            return
        if type not in ["italian", "mexican", "indian"]:
            print("invalid type!")
            return
        if not difficulty or difficulty > 10:
            print("invalid difficulty!")
            return
        if time < 1:
            print("invalid time!")
            return
        lst = self.get_all()
        ok = 1
        for r in lst:
            if r.get_id() == id:
                print("already in list!")
                return
        if ok == 1:
            lst.append(Recipe(id, name, type, difficulty, time))

    def sortt(self):
        """
        It sorts the list alphabeticaly
        In: -
        Out: sorted list of Recipes
        """
        lst = self.get_all()
        return list(sorted(lst, key=lambda x: x.get_name()))

    def update(self, id, time):
        """
        It updates the Recipe with given id with given time
        In: id - int
            time - int
        Out: -
        Error: if time < 1 or no recipe with id
        """
        if time < 1:
            print("invalid time!")
            return
        lst = self.get_all()
        for i in lst:
            if i.get_id() == id:
                i.set_time(time)
                return
        print("no recipe with id")

    @staticmethod
    def tests():
        lst = [Recipe(1, "Tiramisu", "italian", 5, 60)]

        r = Repo(lst)

        r.add(2, "Coffee", "italian", 1, 3)

        assert len(r.get_all()) == 2
        assert str(r.get_all()[-1]) == "2 - Coffee - italian - 1 - 3"

        l = r.sortt()
        assert l[0].get_name() == "Coffee"
        assert l[1].get_name() == "Tiramisu"

        r.update(2, 2)
        assert l[0].get_time() == 2

        print("All tests passed!\n")
