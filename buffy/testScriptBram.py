from buffy.buffer import Buffer
import matplotlib.pyplot as plt

b = Buffer()
pHvalues = list()
aMinvalues = list()
HAvalues = list()
for x in list(range(20)):
    pHvalues.append(b.read_ph())
    aMinvalues.append(b.Amin)
    HAvalues.append(b.HA)
    b.add_drip("base")
plt.plot(pHvalues)
plt.ylabel("pH")
plt.xlabel("Base added")
plt.show()

plt.plot(aMinvalues)
plt.plot(HAvalues)
plt.show()
