def gen():
    for c in "ab":
        yield c

print(list(gen()))

def nw():
    yield from "bd"

print(list(nw()))