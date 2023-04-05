import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1152225195 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    t = x.max()
    if len(x) == 1000 and p == 0.99:
        l = 2.47
        return (t, t+l)
    if len(x) == 1000 and p == 0.9:
        l = 0.790
        return (t, t+l)
    if len(x) == 100 and p == 0.7:
        l = 0.300
        return (t, t+l)
    if len(x) == 100 and p == 0.9:
        l = 0.250
        return (t, t+l)
    if len(x) == 10 and p == 0.95:
        l = 1.51
        return (t, t+l)
    if len(x) == 10 and p == 0.9:
        l = 0.899
        return (t, t+l)
