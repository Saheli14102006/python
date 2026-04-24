team=dict()
for _ in range(3):
    k=input("Enter player id")
    v=list(input("Enter Player Name,Score").split(','))
    team[k]=v
print(team)
score=[]
for key in team.keys():
    num=team[key]
    print(num)
    score.append(num[1])

print("score",score)
for i in range(0,2):
    for j in range(0,2-i-1):
        if(score[j]>score[j+1]):
           score[j+1],score[j]=score[j],score[j+1]
print("score",score)
    
    
