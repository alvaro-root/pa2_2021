from collections import OrderedDict
import string

ordinary_dict = {}
ordered_dict = OrderedDict()

for k in string.ascii_lowercase[::-1] + string.digits[::-1] + string.ascii_uppercase[::-1]:
    ordinary_dict[k] = ord(k)
    ordered_dict[k] = ord(k)

for k,v in ordinary_dict.items():
    print(f"{k}: {v}")

for k,v in ordered_dict.items():
    print(f"ORDERED: {k}: {v}")


#################
## default dict
#################
from collections import defaultdict
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)
favourite_colours = defaultdict(list)
for name, colour in colours:
    favourite_colours[name].append(colour)
print(favourite_colours)


