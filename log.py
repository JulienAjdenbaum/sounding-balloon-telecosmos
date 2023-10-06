import pandas as pd
import matplotlib.pyplot as plt
# from scipy.interpolate import spline

df = pd.read_csv("F_2.log", sep=";")
print(df["Up-Time"])
for c in df:
    print(c)
nb = df.shape[0]
df["seconds"] = [0]*nb
for t in range(nb):
    a, b, c = df["Up-Time"][t].split(":")
    # print(a, b, c)
    secs = 3600*int(a)+60*int(b)+int(c)
    df["seconds"][t] = secs

df = df[df['seconds'] > 3180]
df["vitesse"] = df['Altitude NN [m]'].diff()/df["seconds"].diff()
print(df.head())
print(df["seconds"])
# df = df[df["seconds"] < 13000]
sum = 0
for t in df["vitesse"][1:]:
    sum += int(t)
print(sum)
df['seconds'] = df['seconds'] - 3180
df.plot(x="seconds", y="vitesse")
plt.title("Vitesse ascensionnelle")
plt.show()
