'''
INPUT :
4,3,4

4   # initialEnergy
3   # rate of energy increasing
4   # timesN term, we have to determine the energy for this time

OUTPUT:
16
    - 4 10 13 16 19 22
'''

[energyInitial, rate, timesN] = list(map(int, input().split(",")))

totalEnergy = energyInitial
for i in range(timesN):
    totalEnergy += rate

print(totalEnergy)
