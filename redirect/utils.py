def encode_short_key(number):
    alphabet = '346789abcdefghjknpqrtuvwxy'
    base = len(alphabet)
    res = ''
    if 0 <= number < base:
        return alphabet[number]
    while number != 0:
        number, i = divmod(number, len(alphabet))
        res = alphabet[i] + res
    return res
