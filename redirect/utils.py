def encode_with_alphabet(number, alphabet):
    base = len(alphabet)
    res = ''
    if 0 <= number < base:
        return alphabet[number]
    while number != 0:
        number, i = divmod(number, len(alphabet))
        res = alphabet[i] + res
    return res

def encode_short_key(id):
    alphabet = '346789abcdefghjknpqrtuvwxy'
    return encode_with_alphabet(id, alphabet)

def encode_long_key(id):
    alphabet = [
        'den',
        'aar',
        'ver',
        'van',
        'gen',
        'een',
        'oor',
        'sch',
        'die',
        'der',
        'nde',
        'dat',
        'ing',
        'aan',
        'iet',
        'cht',
        'ten',
        'nie',
        'eer',
        'and',
        'ken',
        'het',
        'voo',
        'men',
        'ste',
        'ond',
        'ren',
        'lyk',
        'zyn',
        'ter',
        ]

    return encode_with_alphabet(id, alphabet)
