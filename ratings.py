"""Restaurant rating lister."""
d = {}

def sorted_list():
    with open("scores.txt") as f:
        for line in f:
            (key, val) = line.rstrip().split(":")
            d[(key)] = val

        for line in sorted(d.items()):
            print(line[0], 'is rated', line[1])


def add_restaurant():
    r_name = input(str('Add Restaurant and rating here, seperated by a "," \n'))
    (key, val) = r_name.rstrip().split(",")
    d[(key)] = val


def main():
    add_restaurant()
    sorted_list()
   
main()
