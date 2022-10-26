import csv, json, matplotlib.pyplot as plt

with open('proj2/pop.json', encoding= 'ascii') as f:
    text = f.read()
    china_dict = json.loads(text)
    china_data = china_dict[1]

years =[]
pop=[]

for i in range(len(china_data)):
    years.append(china_data[i]['date'])
    pop.append(china_data[i]['value'])

years.reverse()
pop.reverse()

plt.plot(years, pop)
plt.xlabel('Year')
plt.xticks(years)
plt.ylim(min(pop), max(pop))
plt.xticks(rotation=60, fontsize = 8)
plt.ylabel('Population Size')
plt.title('China Population Size Over Time')
plt.show()