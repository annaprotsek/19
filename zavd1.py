import pickle

def arithmetic_progression(start, diff, n):
    return [start + i * diff for i in range(n)]

prog1 = arithmetic_progression(0.7, 2.7, 40)
prog2 = arithmetic_progression(4.3, 5.2, 38)

common_elements = list(set(prog1) & set(prog2))

with open("digits.bin", "wb") as file:
    pickle.dump(common_elements, file)

with open("digits.bin", "rb") as file:
    data = pickle.load(file)
    print("Спільні елементи прогресій:", data)
