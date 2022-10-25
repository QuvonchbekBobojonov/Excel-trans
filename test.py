from Uzbek_Trans.transliterate import to_latin, to_cyrillic


def test():
    print('1: latin, 2: cyrillic')
    variant = int(input('Turni kiriting:'))
    if variant == 1:
        text = input("matn kiriting:")
        print(to_latin(text))
    elif variant == 2:
        text = input("матн киритинг:")
        print(to_cyrillic(text))
    else:
        print('Xatolik')


if __name__ == '__main__':
    test()
