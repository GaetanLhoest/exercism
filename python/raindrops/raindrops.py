def convert(number: int = 0) -> str:
    rain_string = ''
    if number % 3 == 0:
        rain_string += 'Pling'
    if number % 5 == 0:
        rain_string += 'Plang'
    if number % 7 == 0:
        rain_string += 'Plong'
    if rain_string == '':
        return str(number)
    return rain_string


if __name__ == "__main__":
    print(convert(1))
