import math
import random

def generate_uhos():
    u_count = random.betavariate(2, 5) * 50
    u_count = int(u_count)

    us = ["ｳ"] * u_count
    uhos = [u + "ﾎ" * int(random.uniform(1, 5)) for u in us]
    gorilla_str = "".join(uhos)
    if (len(gorilla_str) > 140):
        gorilla_str = gorilla_str[0:140]
    return gorilla_str;

print(generate_uhos())