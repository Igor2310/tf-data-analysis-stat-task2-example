
import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1152225195 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    a = 0.14
    n = len(x)
    x_max = x.max()
    alpha = (1 - p)**(1./n)
    left = x_max
    right= (x_max - a) / alpha + a
    return (left, right)
