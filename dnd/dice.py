import random

def daditos():
    rolls = []
    result = None

    def roll_dice():
        nonlocal rolls, result
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.sort(reverse=True)
        rolls = rolls[:3]
        result = sum(rolls)

    roll_dice()
    return f"Los dados fueron {rolls}. El total es {result}."

print(daditos())