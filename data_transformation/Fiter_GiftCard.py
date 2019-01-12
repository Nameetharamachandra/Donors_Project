#To count the number of giftcards purchased by each unique buyer account
import pandas  as pd
import tqdm
giftcards_2015=giftcards[(giftcards['date_purchased'].apply(lambda x:x[0:4]) == '2015')]
unique_id=giftcards_2015['_buyer_acctid'].unique().tolist()
Data = pd.DataFrame(columns=['Account_Id','Giftcard_Count'])
#plot graph for donations made and gift cards purchased by unique donor Id
count=0
Flag=0
for item in tqdm(unique_id[0:100])
    for j,total in giftcards_2015.iterrows():
            if total['_buyer_acctid']==item:                   
                        count=count+1
    Data.loc[Flag]=[item,count]
    Flag=Flag+1
    Count=0
Data.to_csv(path)
