#Контейнер расчета
from sympy import *
from typing import Tuple, List  # Для аннотации типов параметров функций
from matplotlib import pyplot as plt # Для визуализации
import os # Надо импортировать os библиотеку, ошибка


k, T, C, L = symbols('k T C L')
#1 способ
C_ost = 1_000_000
Am_lst = []
C_ost_lst = []
for i in range(15):
  Am = (C - L) / T
  C_ost -= Am.subs({C: 1000000, T: 15, L: 0})
  Am_lst.append(round(Am.subs({C: 1000000, T: 15, L: 0}), 2))
  C_ost_lst.append(round(C_ost, 2))
print(f'Am_lst={Am_lst}\nC_ost_lst={C_ost_lst}')

# #Контейнер табличного вывода

print('\n')
print_with_stars("Работа с pandas")

import pandas as pd

def build_frame(C_history, Am_history):
  colums=['Y', 'C_history', 'Am_history']
  y = range(1, len(C_history) + 1)
  table = list(zip(y, C_history, Am_history))
  return pd.DataFrame(table, columns=colums)

# tframe = build_frame(C_ost_lst, Am_lst)
# tframe2 = build_frame(C_ost_lst_2, Am_lst_2)

# print(tframe)
# print(tframe2)


# print('\n')
# print_with_stars("Визуализация")
# # #Контейнер визуализации

# plt.plot(tframe['Y'], tframe['C_history'], label = 'Am')
# plt.plot(tframe2['Y'], tframe2['C_history'], label = 'Am_2')
# plt.show()


def show_pie(Am_lst):
  vals = Am_lst
  labels = list(range(1, len(Am_lst) + 1))
  explode = [0.1] * len(Am_lst)
  fig, ax = plt.subplots()
  ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'--', 'edgecolor': "k"}, rotatelabels=True)
  ax.axis("equal")
  plt.show()


# show_pie(Am_lst) # Доли амортизации при линейной
# show_pie(Am_lst_2) # Доли амортизации при НЕлинейной

def show_bar(tframe):
  plt.bar(tframe['Y'], tframe['Am_history'])
  plt.show()

# show_bar(tframe) # Диаграмма амортизации при линейной
# show_bar(tframe2) # Диаграмма амортизации при НЕлинейной




# Рассчет с другими параметраами

print("\n")
print_with_stars("Вариант 5")
# Вариант 5

# Поменял 2 строчки кода - два парамтера для функций
#Good Work
С = 1_000_000
T = 15
Am_linear, C_history_linear = amortization1(C=С, T=T, L=0)
print(f"\nЛинейная амортизация\nAm={Am_linear}\nC_history = {C_history}")


Am_history_2, C_history_2 = amortization2(C=С, T=T, k=2)
print(f"\nНЕлинейная амортизация\nAm={Am_history_2}\nC_history = {C_history_2}")


print('\n')
print("Фреймы")
# Фреймы
tframe_var5 = build_frame(C_history_linear, [Am_linear]*len(C_history_linear))
tframe2_var5 = build_frame(C_history_2, Am_history_2)

print(tframe_var5)
print(tframe2_var5)

print('\n')
print("Визуализация")


plt.plot(tframe_var5['Y'], tframe_var5['C_history'], label = 'Am')
plt.plot(tframe2_var5['Y'], tframe2_var5['C_history'], label = 'Am_2')
plt.show()

show_pie([Am_linear] * len(C_history))
show_pie(Am_history_2)

show_bar(tframe_var5)
show_bar(tframe2_var5)
