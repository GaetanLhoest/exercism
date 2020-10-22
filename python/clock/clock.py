class Clock:
    def __init__(self, hour, minute):
        self.hour = hour % 24
        self.minute = 0
        self = self + minute

    def __repr__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other):
        return other.hour == self.hour and other.minute == self.minute

    def __add__(self, minutes):
        if self.minute + minutes < 0:
            self.hour = (
                self.hour + int((self.minute + minutes + 1) / 60) - 1) % 24
        else:
            self.hour = (self.hour + int((self.minute + minutes) / 60)) % 24
        self.minute = (self.minute + minutes) % 60
        return self

    def __sub__(self, minutes):
        if self.minute - minutes < 0:
            self.hour = (
                self.hour + int((self.minute - minutes + 1) / 60) - 1) % 24
        self.minute = (self.minute - minutes) % 60
        return self


if __name__ == "__main__":
    clock = Clock(hour=9, minute=33)
    print(str(Clock(10, 3) - 5))
