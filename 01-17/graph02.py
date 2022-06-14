import numpy as np
import matplotlib.pyplot as plt
wert = np.array([1, 3, 5, 10, 12, 15])
ergebnis = np.array([4, 12, 18, 52, 44, 79])
plt.plot(wert, ergebnis, 'Dr')
m, b = np.polyfit(wert, ergebnis, 1)
plt.plot(wert, m*wert + b)
plt.show()
