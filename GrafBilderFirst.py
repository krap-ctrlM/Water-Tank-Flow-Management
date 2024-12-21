import matplotlib.pyplot as plt # Исходные данные
 
D = 102
d = 0.15 * D
h0 = 4 * D
g = 9.81
delta_t = 0.1
# Рассчитываем расход воды
S = (3.14 / 4) * (d ** 2) v = (2 * g * h0) ** 0.5 Q_dot = S * v
# Начальные условия
h = h0
time_steps = [0]
water_levels = [h]
# Рассчитываем изменение уровня воды для нескольких шагов for i in range(1, 51): # 50 шагов
h = h - (4 * delta_t * Q_dot) / (3.14 * (d ** 2)) time_steps.append(i * delta_t) water_levels.append(h)
# Построение графика
plt.plot(time_steps, water_levels, marker='o', linestyle='-', color='b') plt.title('Изменение уровня воды в баке')
plt.xlabel('Время, с')
plt.ylabel('Уровень воды, мм')
plt.grid(True)
plt.show()
