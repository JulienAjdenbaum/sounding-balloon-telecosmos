import pandas as pd
import matplotlib.pyplot as plt
# from scipy.interpolate import spline

df = pd.read_csv("F_2.log", sep=";")
print(df["Up-Time"])
for c in df:
    print(c)
nb = df.shape[0]
df["Seconds"] = [0]*nb
for t in range(nb):
    a, b, c = df["Up-Time"][t].split(":")
    # print(a, b, c)
    secs = 3600*int(a)+60*int(b)+int(c)
    df["Seconds"][t] = secs

df = df[df['Seconds'] > 3180]
df["speed"] = df['Altitude NN [m]'].diff()/df["Seconds"].diff()
print(df.head())
print(df["Seconds"])
# df = df[df["seconds"] < 13000]
sum = 0
for t in df["speed"][1:]:
    sum += int(t)
print(sum)
df['Seconds'] = df['Seconds'] - 3180
df.plot(x="Seconds", y="speed")
plt.title("Rate of climb")
plt.ylabel("m/s")
plt.show()
