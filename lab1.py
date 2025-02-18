import random
import matplotlib.pyplot as plt


def simulate_dice_throws(sides, num_throws):
    # Генеруємо випадкові значення
    results = [random.randint(1, sides) for _ in range(num_throws)]

    # Підрахунок частоти випадання кожного числа
    frequencies = {i: 0 for i in range(1, sides + 1)}
    for result in results:
        frequencies[result] += 1

    # Обчислюємо відносні частоти
    relative_frequencies = {k: v / num_throws for k, v in frequencies.items()}

    # Побудова гістограми
    plt.bar(frequencies.keys(), relative_frequencies.values(), color='skyblue')
    plt.xlabel('Номер грані')
    plt.ylabel('Частота випадання')
    plt.title(f'Гістограма частот для {sides}-гранника при N={num_throws}')
    plt.xticks(range(1, sides + 1))
    plt.show()


# Моделюємо підкидання для 4, 6, 8 і 12-гранників при різних N
for sides in [4, 6, 8, 12]:
    for num_throws in [10, 100, 1000, 10000]:
        simulate_dice_throws(sides, num_throws)
