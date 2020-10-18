def two_fer(name:str='you'):
    if name is None or name == '':
        name='you'
    return f'One for {name}, one for me.'


if __name__ == "__main__":
    print(two_fer('Gaetan'))