def filter_words(st):
    return' '.join((st[0].upper()+st[1::].lower()).split())

print(filter_words('This    will    not    pass'))