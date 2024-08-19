class Console:
    def __init__(self, service):
        self.__service = service

    @staticmethod
    def print_sort_and_filter_menu():
        print("\n   ▶ 0. Exit\n"
              "   ▶ 3. Sort passengers by last name\n"
              "   ▶ 4. Sort planes by number of seats\n"
              "   ▶ 5. Sort planes by number of passengers with given prefix for first name\n"
              "   ▶ 6. Sort planes by concatenation of number of passengers and destination\n"
              "   ▶ 7. Filter planes with passengers with passport number with same 3 letters\n"
              "   ▶ 8. Filter passengers with string in name\n"
              "   ▶ 9. Filter planes with given passenger name\n"
              "   ▶ 10. Groups of k passengers with different last names\n"
              "   ▶ 11. Groups of k planes with the same destination but belonging to different airline companies\n")

    def run(self):
        commands = {3: [self.__service.sort_passengers_by_last_name, 'plane_name'],
                    4: [self.__service.sort_planes_by_number_of_seats],
                    5: [self.__service.sort_planes_by_number_of_passengers_with_given_prefix_for_first_name, 'prefix'],
                    6: [self.__service.sort_planes_by_concatenation_of_number_of_passengers_and_destination],
                    7: [self.__service.filter_planes_with_passengers_with_passport_number_with_same_3_letters],
                    8: [self.__service.filter_passengers_with_string_in_name, 'plane_name', 'string'],
                    9: [self.__service.filter_planes_with_given_passenger_name, 'passenger_name'],
                    10: [self.__service.groups_of_k_passengers_with_different_last_names, 'plane_name', 'k'],
                    11: [self.__service.groups_of_k_planes_with_the_same_destination_but_belonging_to_different_airline_companies, 'k']}
        while True:
            self.print_sort_and_filter_menu()
            command = int(input("Enter command: "))
            if command == 0:
                return
            elif command in commands.keys():
                if len(commands[command]) == 1:
                    print(commands[command][0]())
                elif len(commands[command]) == 2:
                    string = input("Enter " + commands[command][1] + ": ")
                    if command == 11:
                        string = int(string)
                    print(commands[command][0](string))
                elif len(commands[command]) == 3:
                    plane_name = input("Enter " + commands[command][1] + ": ")
                    string = input("Enter " + commands[command][2] + ": ")
                    if command == 10:
                        string = int(string)
                    print(commands[command][0](plane_name, string))
            else:
                print("Invalid command!\n")
