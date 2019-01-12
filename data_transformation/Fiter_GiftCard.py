#To count the number of giftcards purchased by each unique buyer account
import pandas  as pd
import tqdm
import socket
if socket.gethostname()=='isds-research':
    path='/home/test/donorschoose/raw_files/'
else:
    path=''
giftcards = pandas.read_csv(path+'opendata_giftcards000.gz', escapechar='\\', names=['_giftcardid', 'dollar_tier', '_buyer_acctid', 'buyer_city', 'buyer_state', 'buyer_zip', 'date_purchased', '_buyer_cartid', '_recipient_acctid', 'recipient_city', 'recipient_state', 'recipient_zip', 'redeemed', 'date_redeemed', '_redeemed_cartid', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched'])
giftcards_2015=giftcards[(giftcards['date_purchased'].apply(lambda x:x[0:4]) == '2015')]
unique_id=giftcards_2015['_buyer_acctid'].unique().tolist()
Data = pd.DataFrame(columns=['Account_Id','Giftcard_Count'])
#plot graph for donations made and gift cards purchased by unique donor Id
count=0
Flag=0
for item in tqdm(unique_id)
    for j,total in giftcards_2015.iterrows():
            if total['_buyer_acctid']==item:                   
                        count=count+1
    Data.loc[Flag]=[item,count]
    Flag=Flag+1
    Count=0
Data.to_csv(path)
