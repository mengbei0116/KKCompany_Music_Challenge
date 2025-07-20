import pandas as pd
import random
import collections as c

data=pd.read_parquet("meta_song.parquet")
test=pd.read_parquet("label_test_source.parquet")


ID=[]
top=[[],[],[],[],[]]
top1=[]
top2=[]
top3=[]
top4=[]
top5=[]
times=0

test=test.sort_values(by=['session_id', 'listening_order'])

print(test.session_id[0])

current=test.session_id[0]

randnum=random.sample(range(0, 1030712), 715320)

index=0
Set=set()

result=test.groupby('session_id')['song_id'].agg(list).reset_index()
for i in result.session_id:
    ID.append(i)
for i in result.song_id:
    for j in i:
        Set.add(j)
    if len(Set) <=5:
        count=0
        for j in Set:
            top[count].append(j)
            count+=1
        for j in range(count, 5):
            top[count].append(data.song_id[randnum[index]])
            index+=1
            count+=1
    else:
        count=c.Counter(i)
        if len(Set)<=19:
            top[0].append(count.most_common()[0][0])
            top[1].append(count.most_common()[1][0])
            top[2].append(count.most_common()[2][0])
            top[3].append(count.most_common()[3][0])
            top[4].append(count.most_common()[4][0])
        else:
            top[0].append(data.song_id[randnum[index]])
            top[1].append(data.song_id[randnum[index+1]])
            top[2].append(data.song_id[randnum[index+2]])
            top[3].append(data.song_id[randnum[index+3]])
            top[4].append(data.song_id[randnum[index+4]])
            index+=5
    Set=set()


        
col1="session_id"
col2="top1"
col3="top2"
col4="top3"
col5="top4"
col6="top5"

ans=pd.DataFrame({col1: ID, col2: top[0], col3: top[1], col4: top[2], col5: top[3], col6: top[4]})
ans.to_excel("ans.xlsx", index=False)

