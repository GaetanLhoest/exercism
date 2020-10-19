class Garden:

    _plants = {
        "R": "Radishes", "C": "Clover", "G": "Grass", "V": "Violets"
    }

    def __init__(self, diagram: str = None, students=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Joseph', 'Ileana', 'Kincaid',  'Larry']):
        self.diagram = diagram
        self.students = students
        self.students.sort()
        self._pl = diagram.split('\n')
        self._st = dict(list([(s, index*2)
                              for index, s in enumerate(self.students)]))

    def plants(self, student):
        return [self._plants[plant] for plant in self._pl[0][self._st[student]: self._st[student] + 2]+self._pl[1][self._st[student]: self._st[student]+2]]
