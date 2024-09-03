from itertools import combinations


def all_variants(text):
    for x in range(len(text) + 1):
        for combo in combinations(text, x):
            yield combo


a = all_variants("abc")
for i in a:
    print(i)
