"""
Розглянемо квадрат зі стороною 2, центр якого співпадає з центром вписаного в
нього кола радіусом 1. Якщо випадково кидати точки на площині, то відношення кількості точок,
що потрапили в коло, до загальної кількості точок буде приблизно дорівнювати
відношенню площі кола до площі квадрата, тобто π/4.
"""

import random
import matplotlib.pyplot as plt

def monte_carlo_pi(num_samples):
    # 1. Визначення моделі або системи.
    inside_circle = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []
    # 2. Генерація випадкових вхідних даних
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # 3. Виконання обчислень
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    # 4. Агрегування та аналіз результатів
    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate, x_inside, y_inside, x_outside, y_outside

# Задаємо кількість випадкових точок
num_samples = 10

# Запускаємо метод Монте-Карло для обчислення π
pi_estimate, x_inside, y_inside, x_outside, y_outside = monte_carlo_pi(num_samples)

# Виводимо результат
print(f"Оцінка значення π за методом Монте-Карло з {num_samples} випадкових точок: {pi_estimate}")

# Візуалізація результатів
plt.figure(figsize=(8, 8))
plt.scatter(x_inside, y_inside, color='blue', s=1, label='Точки всередині кола')
plt.scatter(x_outside, y_outside, color='red', s=1, label='Точки поза колом')
circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
plt.gca().add_patch(circle)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f"Метод Монте-Карло для оцінки π\nЧисло точок: {num_samples}\nОцінка π: {pi_estimate}")
plt.legend()
plt.show()


"""
- У фінансовій сфері метод застосовується для оцінки ризиків, 
ціноутворення опціонів та інших фінансових інструментів.

Припустимо, у нас є європейський опціон типу "call" на акцію, поточна ціна якої S0.
Страйк ціна опціону K, опціон закінчується через T років, безризикова процентна ставка r,
а волатильність акції σ.
Ціль: оцінити вартість опціону за допомогою методу Монте-Карло.
"""

# import numpy as np
# import matplotlib.pyplot as plt
#
# # Параметри опціону
# S0 = 100  # Поточна ціна акції
# K = 110  # Страйк ціна
# T = 1  # Час до закінчення опціону в роках
# r = 0.05  # Безризикова процентна ставка
# sigma = 0.2  # Волатильність
#
# # Параметри симуляції
# num_simulations = 10000  # Кількість симуляцій
# num_steps = 252  # Кількість кроків на рік (щоденні кроки)
#
# # Функція для обчислення ціни опціону методом Монте-Карло
# def monte_carlo_option_pricing(S0, K, T, r, sigma, num_simulations, num_steps):
#     dt = T / num_steps  # Часовий крок
#     prices = np.zeros((num_simulations, num_steps + 1))
#     prices[:, 0] = S0
#
#     for t in range(1, num_steps + 1):
#         z = np.random.standard_normal(num_simulations)
#         prices[:, t] = prices[:, t - 1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
#
#     payoffs = np.maximum(prices[:, -1] - K, 0)  # Payoff для опціону call
#     option_price = np.exp(-r * T) * np.mean(payoffs)  # Дисконтована середня вартість
#
#     return option_price, prices
#
# # Обчислення ціни опціону
# option_price, prices = monte_carlo_option_pricing(S0, K, T, r, sigma, num_simulations, num_steps)
#
# # Вивід результату
# print(f"Оцінена вартість опціону (call) методом Монте-Карло: {option_price:.2f} $")
#
# # Візуалізація кількох симуляцій
# plt.figure(figsize=(10, 6))
# for i in range(min(num_simulations, 10)):  # Відобразимо тільки 10 симуляцій
#     plt.plot(prices[i, :])
# plt.title('Симуляції цін акцій за методом Монте-Карло')
# plt.xlabel('Часові кроки')
# plt.ylabel('Ціна акції')
# plt.show()


"""
Використовуючи велику кількість випадкових вибірок, можна оцінити ймовірності 
подій та різні статистичні характеристики, такі як середнє значення, дисперсія, медіана тощо.


Припустимо, що ми хочемо оцінити майбутню вартість портфеля акцій через рік. 
Ми знаємо початкову вартість портфеля, середню річну дохідність та волатильність 
(стандартне відхилення річної дохідності). За допомогою методу Монте-Карло ми 
зможемо оцінити розподіл майбутніх вартостей портфеля, а також обчислити такі 
статистичні характеристики, як середнє значення, дисперсія та медіана.
"""

# import numpy as np
# import matplotlib.pyplot as plt
#
# # Параметри портфеля
# initial_portfolio_value = 100000  # Початкова вартість портфеля
# expected_return = 0.07  # Середня річна дохідність
# volatility = 0.15  # Річна волатильність (стандартне відхилення)
#
# # Параметри симуляції
# num_simulations = 10000  # Кількість симуляцій
# num_years = 1  # Період симуляції у роках
#
# # Функція для симуляції майбутньої вартості портфеля методом Монте-Карло
# def monte_carlo_portfolio_value(initial_value, expected_return, volatility, num_simulations, num_years):
#     dt = 1 / 252  # Часовий крок (252 торгових дні в році)
#     num_steps = int(num_years / dt)  # Кількість кроків
#     portfolio_values = np.zeros((num_simulations, num_steps + 1))
#     portfolio_values[:, 0] = initial_value
#
#     for t in range(1, num_steps + 1):
#         z = np.random.standard_normal(num_simulations)
#         portfolio_values[:, t] = portfolio_values[:, t - 1] * np.exp((expected_return - 0.5 * volatility**2) * dt + volatility * np.sqrt(dt) * z)
#
#     final_values = portfolio_values[:, -1]
#     return final_values
#
# # Симуляція майбутньої вартості портфеля
# final_portfolio_values = monte_carlo_portfolio_value(initial_portfolio_value, expected_return, volatility, num_simulations, num_years)
#
# # Обчислення статистичних характеристик
# mean_value = np.mean(final_portfolio_values)
# variance_value = np.var(final_portfolio_values)
# median_value = np.median(final_portfolio_values)
#
# # Вивід результатів
# print(f"Середнє значення майбутньої вартості портфеля: {mean_value:.2f} $")
# print(f"Дисперсія майбутньої вартості портфеля: {variance_value:.2f}")
# print(f"Медіана майбутньої вартості портфеля: {median_value:.2f} $")
#
# # Візуалізація розподілу майбутньої вартості портфеля
# plt.figure(figsize=(10, 6))
# plt.hist(final_portfolio_values, bins=50, edgecolor='k', alpha=0.7)
# plt.axvline(mean_value, color='r', linestyle='dashed', linewidth=2, label=f'Середнє значення: {mean_value:.2f} $')
# plt.axvline(median_value, color='g', linestyle='dashed', linewidth=2, label=f'Медіана: {median_value:.2f} $')
# plt.title('Розподіл майбутньої вартості портфеля за методом Монте-Карло')
# plt.xlabel('Майбутня вартість портфеля ($)')
# plt.ylabel('Частота')
# plt.legend()
# plt.show()
