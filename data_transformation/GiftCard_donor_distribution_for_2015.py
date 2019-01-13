#To count the number of giftcards purchased by each unique buyer account
import pandas  as pd
from tqdm import tqdm
import socket
import sys
if socket.gethostname()=='isds-research':
    path='/home/test/donorschoose/raw_files/'
else:
    path=''
giftcards = pd.read_csv(path+'opendata_giftcards000.gz', escapechar='\\', names=['_giftcardid', 'dollar_tier', '_buyer_acctid', 'buyer_city', 'buyer_state', 'buyer_zip', 'date_purchased', '_buyer_cartid', '_recipient_acctid', 'recipient_city', 'recipient_state', 'recipient_zip', 'redeemed', 'date_redeemed', '_redeemed_cartid', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched'])
giftcards_2015=giftcards[(giftcards['date_purchased'].apply(lambda x:x[0:4]) == '2015')]
tmp=giftcards_2015.head(15)
Data=tmp.groupby(['_buyer_acctid'])[['_buyer_acctid']].count()
#rename column
Data=Data.rename(columns={'_buyer_acctid':'count'})
# In above dataframe, the index is the relevant column, so 
# I created a new column 'buyer_acctid' with values same as 
# index
Data['buyer_acctid']=Data.index
# Lets create the result csv with the same name as the python 
# script since it will be easy to track it.
Data.to_csv(sys.argv[0]+'.csv')
