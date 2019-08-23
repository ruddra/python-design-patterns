def count_to(count):
    numbers = ['ichi', 'nii', 'sun', 'shi', 'go', 'roku', 'nana', 'hachi']
    iterator = zip(range(count), numbers)

    for position, number in iterator:
        yield number


for x in count_to(5):
    print(x)
