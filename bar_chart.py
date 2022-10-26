import csv, json, matplotlib.pyplot as plt, numpy as np

with open('proj2/exams.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)

    groupA = 0
    groupAwritingscores=[]
    groupAreadingscores=[]

    groupB = 0
    groupBwritingscores=[]
    groupBreadingscores=[]

    groupC = 0
    groupCwritingscores=[]
    groupCreadingscores=[]

    groupD = 0
    groupDwritingscores=[]
    groupDreadingscores=[]

    groupE = 0
    groupEwritingscores=[]
    groupEreadingscores=[]

    for row in reader:
        skip = next
        if(row[1] == 'group A'):
            groupA += 1
            groupAwritingscores.append(int(row[7]))
            groupAreadingscores.append(int(row[6]))
        elif(row[1] == 'group B'):
            groupB += 1
            groupBwritingscores.append(int(row[7]))
            groupBreadingscores.append(int(row[6]))
        elif(row[1] == 'group C'):
            groupC += 1
            groupCwritingscores.append(int(row[7]))
            groupCreadingscores.append(int(row[6]))
        elif(row[1] == 'group D'):
            groupD += 1
            groupDwritingscores.append(int(row[7]))
            groupDreadingscores.append(int(row[6]))
        else:
            groupE += 1
            groupEwritingscores.append(int(row[7]))
            groupEreadingscores.append(int(row[6]))
        
labels = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']

groupAwritingscoresmean = (sum(groupAwritingscores) / len(groupAwritingscores))
groupAreadingscoresmean = sum(groupAreadingscores) / len(groupAreadingscores)

groupBwritingscoresmean = sum(groupBwritingscores) / len(groupBwritingscores)
groupBreadingscoresmean = sum(groupBreadingscores) / len(groupBreadingscores)

groupCwritingscoresmean = sum(groupCwritingscores) / len(groupCwritingscores)
groupCreadingscoresmean = sum(groupCreadingscores) / len(groupCreadingscores)

groupDwritingscoresmean = sum(groupDwritingscores) / len(groupDwritingscores)
groupDreadingscoresmean = sum(groupDreadingscores) / len(groupDreadingscores)

groupEwritingscoresmean = sum(groupEwritingscores) / len(groupEwritingscores)
groupEreadingscoresmean = sum(groupEreadingscores) / len(groupEreadingscores)

writing_means = [groupAwritingscoresmean, groupBwritingscoresmean, groupCwritingscoresmean, groupDwritingscoresmean, groupEwritingscoresmean]
reading_means = [groupAreadingscoresmean, groupBreadingscoresmean, groupCreadingscoresmean, groupDreadingscoresmean, groupEreadingscoresmean]

b = np.arange(len(labels)) 
width = 0.4

plt.bar(b, writing_means, color = 'b', width = width, label='Writing')
plt.bar(b + width, reading_means, color = 'r', width = width, label='Reading')
  
plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Average Student Scores by Subject, per Group")
  
# plt.grid(linestyle='--')
plt.xticks(b + width/2, labels)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
  
plt.show()
