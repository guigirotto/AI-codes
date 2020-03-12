class Chromosome:
    def __init__(self, genetic_code=[], generation=0):
        self.genetic_code = genetic_code
        self.fitness = 0
        self.generation = generation
        self.probability = 0

    def set_fitness(self, new_fitness):
        self.fitness = new_fitness

    def set_probability(self, new_probability):
        self.probability = new_probability

    def create_random_genetic_code(self):
        from project2.model.Pair import Pair
        import random

        new_genetic_code = []
        is_6_escales_pause_created = False
        is_5_escales_pause_created = False
        list_of_pairs = [
            Pair(pair_id=1, employee_1=1, employee_2=2),
            Pair(pair_id=2, employee_1=3, employee_2=4),
            Pair(pair_id=3, employee_1=5, employee_2=6),
            Pair(pair_id=4, employee_1=7, employee_2=8),
            Pair(pair_id=5, employee_1=9, employee_2=10),
        ]

        for i in range(1, 22):
            valid_pair = False
            while not valid_pair:
                random_index = random.randint(0, 4)
                if i == 1:
                    random_index = 0
                if not list_of_pairs[random_index].last_shift >= (i - 3):
                    new_genetic_code.append(list_of_pairs[random_index])

                    if (
                        not is_6_escales_pause_created and i == 1
                    ):  #  generating 6 shift escales
                        list_of_pairs[random_index].last_shift = i + 3
                        is_6_escales_pause_created = True
                    elif (
                        random_index + 1 == 3
                        and i > 6
                        and is_6_escales_pause_created
                        and not is_5_escales_pause_created
                    ):  # generating 4 shift scale
                        list_of_pairs[random_index].last_shift = i + 2
                        is_5_escales_pause_created = True
                    else:
                        list_of_pairs[random_index].last_shift = i  #  normal cases

                    valid_pair = True

        self.genetic_code = new_genetic_code.copy()

    def create_really_random_genetic_code(self):
        from project2.model.Pair import Pair
        import random

        new_genetic_code = []
        list_of_pairs = [
            Pair(pair_id=1, employee_1=1, employee_2=2),
            Pair(pair_id=2, employee_1=3, employee_2=4),
            Pair(pair_id=3, employee_1=5, employee_2=6),
            Pair(pair_id=4, employee_1=7, employee_2=8),
            Pair(pair_id=5, employee_1=9, employee_2=10),
        ]

        for i in range(1, 22):
            random_index = random.randint(0, 4)
            new_genetic_code.append(list_of_pairs[random_index])

        self.genetic_code = new_genetic_code

    def print_scale(self):
        print("seg \t ter \t qua \t qui \t sex \t sab \t dom")
        initial = 0
        print(
            f"{self.genetic_code[initial].pair_id} \t\t {self.genetic_code[initial + 3].pair_id} \t\t {self.genetic_code[initial + 6].pair_id} \t\t {self.genetic_code[initial + 9].pair_id} \t\t {self.genetic_code[initial +12].pair_id} \t\t {self.genetic_code[initial + 15].pair_id} \t\t {self.genetic_code[initial+ 18].pair_id } \n "
        )
        initial = 1
        print(
            f"{self.genetic_code[initial].pair_id} \t\t {self.genetic_code[initial + 3].pair_id} \t\t {self.genetic_code[initial + 6].pair_id} \t\t {self.genetic_code[initial + 9].pair_id} \t\t {self.genetic_code[initial +12].pair_id} \t\t {self.genetic_code[initial+ 15].pair_id } \t\t {self.genetic_code[initial + 18].pair_id} \n "
        )
        initial = 2
        print(
            f"{self.genetic_code[initial].pair_id} \t\t {self.genetic_code[initial + 3].pair_id} \t\t {self.genetic_code[initial + 6].pair_id} \t\t {self.genetic_code[initial + 9].pair_id} \t\t {self.genetic_code[initial + 12].pair_id} \t\t {self.genetic_code[initial + 15].pair_id } \t\t {self.genetic_code[initial + 18].pair_id} \n "
        )

    def check_if_genetic_code_is_valid(self):
        is_escale_valid = True
        quantity_of_invalid_3_turns_pause = 0
        has_6_pause_escale = False
        has_5_pause_escale = False
        list_os_teams_last_work_turn = [
            -10,
            -10,
            -10,
            -10,
            -10,
        ]  #  Starts with a invalid turn
        for index, shift in enumerate(self.genetic_code, start=0):
            if index <= list_os_teams_last_work_turn[shift.pair_id - 1] + 3:
                is_escale_valid = False
                quantity_of_invalid_3_turns_pause += 1
            if shift.pair_id == 1:
                last_escale = list_os_teams_last_work_turn[shift.pair_id - 1]
                if last_escale != -10 and index > last_escale + 6:
                    has_6_pause_escale = True

            if shift.pair_id == 3:
                last_escale = list_os_teams_last_work_turn[shift.pair_id - 1]
                if last_escale != -10 and index > last_escale + 5:
                    has_5_pause_escale = True

            list_os_teams_last_work_turn[shift.pair_id - 1] = index

        #  Verify if escale is valid when the pair does not appear after 5 escales pause
        if not has_5_pause_escale and list_os_teams_last_work_turn[2] != -10:
            last_escale = list_os_teams_last_work_turn[2]
            if len(self.genetic_code) > last_escale + 4:
                has_5_pause_escale = True
        #  Verify if escale is valid when the pair does not appear after 5 escales pause
        if not has_6_pause_escale and list_os_teams_last_work_turn[0] != -10:
            last_escale = list_os_teams_last_work_turn[0]
            if len(self.genetic_code) > last_escale + 5:
                has_6_pause_escale = True

        if is_escale_valid and has_6_pause_escale and has_5_pause_escale:
            return {
                "valid": True,
                "3_turns": is_escale_valid,
                "6_pause": has_6_pause_escale,
                "5_pause": has_5_pause_escale,
                "invalid_3_pauses": quantity_of_invalid_3_turns_pause,
            }
        else:
            return {
                "valid": False,
                "3_turns": is_escale_valid,
                "6_pause": has_6_pause_escale,
                "5_pause": has_5_pause_escale,
                "invalid_3_pauses": quantity_of_invalid_3_turns_pause,
            }

    def count_scales_by_pair(self):
        list_of_count_turns = [0, 0, 0, 0, 0]
        for item in self.genetic_code:
            list_of_count_turns[item.pair_id - 1] += 1

        return list_of_count_turns

    def count_interval_between_work_by_pair(self):
        list_of_worked_days = [[], [], [], [], []]
        list_of_interval_days = [[], [], [], [], []]

        for index, value in enumerate(self.genetic_code):
            last_worked_day = 0
            size_list_of_work_interval_of_pair = len(
                list_of_worked_days[value.pair_id - 1]
            )
            if size_list_of_work_interval_of_pair > 0:
                last_worked_day = list_of_worked_days[value.pair_id - 1][
                    size_list_of_work_interval_of_pair - 1
                ]
            list_of_worked_days[value.pair_id - 1].append(index)
            list_of_interval_days[value.pair_id - 1].append(index - last_worked_day)

        list_of_average_of_interval = []

        for item in list_of_interval_days:
            avarage = 0
            if len(item) > 0:
                avarage = sum(item) / len(item)
            list_of_average_of_interval.append(avarage)
        return list_of_average_of_interval

    def calculate_fitness(self):

        is_genetic_code_valid = self.check_if_genetic_code_is_valid()
        validation_operator = 1
        if not is_genetic_code_valid["3_turns"]:
            validation_operator = validation_operator * (
                0.85 ** is_genetic_code_valid["invalid_3_pauses"]
            )
        if not is_genetic_code_valid["5_pause"]:
            validation_operator = validation_operator * 0.75
        if not is_genetic_code_valid["6_pause"]:
            validation_operator = validation_operator * 0.75

        avg = 4
        number_of_scales = self.count_scales_by_pair()
        interval_between_scales = self.count_interval_between_work_by_pair()
        converted_scale = []
        for index, item in enumerate(number_of_scales):
            converted_scale.append(
                5 * ((item - 4) ** 2) + 0.5 * (interval_between_scales[index] - 4) ** 2
            )

        #  result = sum((x-media)²)
        result = (0.1 + 100 * (1 / sum(converted_scale))) * validation_operator
        return result
