class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix_string = matrix_string
        self.convert_matrix_string_to_matrix()

    def convert_matrix_string_to_matrix(self):
        self.rows = [[int(e) for e in r.split(' ')]
                     for r in self.matrix_string.split('\n')]
        self.columns = [list(c) for c in zip(*self.rows)]

    def row(self, index: int) -> [int]:
        return self.rows[index - 1]

    def column(self, index: int) -> [int]:
        return self.columns[index - 1]
