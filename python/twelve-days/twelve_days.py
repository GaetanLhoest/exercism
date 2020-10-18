def recite(start_verse, end_verse):
    nth = {
        0: 'first',
        1: 'first',
        2: 'second',
        3: 'third',
        4: 'fourth',
        5: 'fifth',
        6: 'sixth',
        7: 'seventh',
        8: 'eighth',
        9: 'ninth',
        10: 'tenth',
        11: 'eleventh',
        12: 'twelfth'
    }

    numbers_elements = {
        1: 'a Partridge in a Pear Tree.',
        2: 'two Turtle Doves, and ',
        3: 'three French Hens, ',
        4: 'four Calling Birds, ',
        5: 'five Gold Rings, ',
        6: 'six Geese-a-Laying, ',
        7: 'seven Swans-a-Swimming, ',
        8: 'eight Maids-a-Milking, ',
        9: 'nine Ladies Dancing, ',
        10: 'ten Lords-a-Leaping, ',
        11: 'eleven Pipers Piping, ',
        12: 'twelve Drummers Drumming, '
    }

    return [f'On the {nth[i]} day of Christmas my true love gave to me: {"".join([numbers_elements[j] for j in range(i, 0, -1)])}' for i in range(start_verse, end_verse+1)]
