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
                if not list_of_pairs[random_index].last_shift > (i - 3):
                    new_genetic_code.append(list_of_pairs[random_index].pair_id)

                    if (
                        not is_6_escales_pause_created and i == 1
                    ):  #  generating 6 shift escales
                        list_of_pairs[random_index].last_shift = i + 5
                        is_6_escales_pause_created = True
                    elif (
                        random_index + 1 == 3
                        and i > 6
                        and is_6_escales_pause_created
                        and not is_5_escales_pause_created
                    ):  # generating 4 shift scale
                        list_of_pairs[random_index].last_shift = i + 4
                        is_5_escales_pause_created = True
                    else:
                        list_of_pairs[random_index].last_shift = i  #  normal cases

                    valid_pair = True

        self.genetic_code = new_genetic_code.copy()

    def print_scale(self):
        print("seg \t ter \t qua \t qui \t sex \t sab \t dom")
        initial = 0
        print(
            f"{self.genetic_code[initial]} \t\t {self.genetic_code[initial + 3]} \t\t {self.genetic_code[initial + 6]} \t\t {self.genetic_code[initial + 9]} \t\t {self.genetic_code[initial +12]} \t\t {self.genetic_code[initial + 15]} \t\t {self.genetic_code[initial+ 18] } \n "
        )
        initial = 1
        print(
            f"{self.genetic_code[initial]} \t\t {self.genetic_code[initial + 3]} \t\t {self.genetic_code[initial + 6]} \t\t {self.genetic_code[initial + 9]} \t\t {self.genetic_code[initial +12]} \t\t {self.genetic_code[initial+ 15] } \t\t {self.genetic_code[initial + 18]} \n "
        )
        initial = 2
        print(
            f"{self.genetic_code[initial]} \t\t {self.genetic_code[initial + 3]} \t\t {self.genetic_code[initial + 6]} \t\t {self.genetic_code[initial + 9]} \t\t {self.genetic_code[initial + 12]} \t\t {self.genetic_code[initial + 15] } \t\t {self.genetic_code[initial + 18]} \n "
        )

    def check_if_genetic_code_is_valid(self):
        is_escale_valid = True
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
            if list_os_teams_last_work_turn[shift - 1] + 2 > index:
                is_escale_valid = False

            if shift == 1:
                last_escale = list_os_teams_last_work_turn[shift - 1]
                if last_escale != -10 and index > last_escale + 5:
                    has_6_pause_escale = True

            if shift == 3:
                last_escale = list_os_teams_last_work_turn[shift - 1]
                if last_escale != -10 and index > last_escale + 4:
                    has_5_pause_escale = True

            list_os_teams_last_work_turn[shift - 1] = index

        #  Verify if escale is valid when the pair does not appear after 5 escales pause
        if not has_5_pause_escale:
            last_escale = list_os_teams_last_work_turn[2]
            if len(self.genetic_code) > last_escale + 4:
                has_5_pause_escale = True
        #  Verify if escale is valid when the pair does not appear after 5 escales pause
        if not has_6_pause_escale:
            last_escale = list_os_teams_last_work_turn[0]
            if len(self.genetic_code) > last_escale + 5:
                has_6_pause_escale = True

        if is_escale_valid and has_6_pause_escale and has_5_pause_escale:
            return {
                "valid": True,
                "2_turns": is_escale_valid,
                "6_pause": has_6_pause_escale,
                "5_pause": has_5_pause_escale,
            }
        else:
            return {
                "valid": False,
                "2_turns": is_escale_valid,
                "6_pause": has_6_pause_escale,
                "5_pause": has_5_pause_escale,
            }
