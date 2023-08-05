def file_gen(fnames):
    for fname in fnames:
        if fname.endswith('.txt'):
            yield fname
            
print()
def enum(items):
    idx = 0
    for item in items:
        yield (idx, item)
        idx += 1
print(enum('antu'))
def dayname(index):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    yield days[index - 1]
    yield days[index]
    yield days[(index + 1) % 7]
    print(dayname('mon'))