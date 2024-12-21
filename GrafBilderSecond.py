import matplotlib.pyplot as plt
# Функция для расчета нового уровня воды
def calculate_water_level(previous_level, delta_t, Q_dot, d):
return previous_level - (4 * delta_t * Q_dot) / (3.14 * (d ** 2))
# Исходные данные
D = 102
d = 0.15 * D
h0 = 4 * D
g = 9.81
delta_t = 0.1
# Рассчитываем расход воды
S = (3.14 / 4) * (d ** 2) v = (2 * g * h0) ** 0.5 Q_dot = S * v
# Начальные условия
current_water_level = h0
threshold_level = 300 # Пороговое значение
# Списки для сохранения данных
time_steps = [0]
water_levels = [current_water_level]
# Цикл по временным шагам
for i in range(1, 51):  # 50 шагов
current_water_level = calculate_water_level(current_water_level, delta_t, Q_dot, d)
time_steps.append(i * delta_t) water_levels.append(current_water_level)
    # Регулирование расхода воды
if current_water_level < threshold_level: Q_dot *= 0.9 # Уменьшение расхода
elif current_water_level > threshold_level: Q_dot *= 1.1 # Увеличение расхода
# Построение графика
plt.plot(time_steps, water_levels, marker='o', linestyle='-', color='b') plt.title('Управление расходом воды')
plt.xlabel('Время, с')
plt.ylabel('Уровень воды, мм')
plt.axhline(y=threshold_level, color='r', linestyle='--', label='Пороговый уровень')
plt.legend()
plt.grid(True)
plt.show()
