class Luhn:
    def __init__(self, card_num):
        card_num_string = card_num.replace(' ', '')
        self.valid_input = len(
            card_num_string) > 1 and card_num_string.isnumeric()
        if self.valid_input:
            self.num_array = [int(digit)
                              for digit in list(card_num_string)][::-1]

    def valid(self):
        if not self.valid_input:
            return self.valid_input
        check_array = [(digit * 2) % 9 if index % 2 != 0 and digit < 9 else digit for index,
                       digit in enumerate(self.num_array)]
        return bool(not sum(check_array) % 10)
