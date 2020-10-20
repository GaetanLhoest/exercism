class School:
    def __init__(self):
        self._roster = {}

    def add_student(self, name, grade):
        self._roster[grade] = self._roster.get(grade, []) + [name]
        self._roster[grade].sort()

    def roster(self):
        response = []
        for students in [self._roster[key] for key in sorted(self._roster.keys())]:
            response = response + students
        return response

    def grade(self, grade_number):
        return self._roster.get(grade_number, [])
