# Purpose: To create point plots of number of donations and number of giftcards 
# received by individuals over time

import pandas  as pd
import numpy as np
from matplotlib import pyplot as plt
import io
import datetime
import matplotlib.dates as mdates

 # Read the json file
donations = pd.read_csv(Donorspath,escapechar='\\', names=['_donationid', '_projectid', '_donor_acctid', '_cartid', 'donor_city', 'donor_state', 'donor_zip', 'is_teacher_acct', 'donation_timestamp', 'donation_to_project', 'donation_optional_support', 'donation_total', 'donation_included_optional_support', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched','is_teacher_referred', 'giving_page_id', 'giving_page_type', 'for_honoree', 'thank_you_packet_mailed'])

# Filter the data for respective year from donations data
Total_donations=donations[(donations['donation_timestamp'].apply(lambda x:x[0:4]) == '2015')]

#Select unique donor Id's
Unique_donations=Total_donations.drop_duplicates('_donor_acctid')

account=Unique_donations._donor_acctid.tolist()

#read giftcard csv
giftcards= pd.read_csv("C://Users/Nameetha/Desktop/Stata/giftcards.csv")

#filter giftcard data for 2015
giftcards_2015=giftcards[(giftcards['date_purchased'].apply(lambda x:x[5:]) == '2015')]

# create blank dataframe
Data = pd.DataFrame(columns=['Date','Role','acctid'])
#plot graph for donations made and gift cards purchased by unique donor Id
count=0

for item in account:
    for j,total in Total_donations.iterrows():
            if total['_donor_acctid']==item:
                        Data.loc[count] = [total['donation_timestamp'],1,total['_donor_acctid']]                   
                        count=count+1

    for k, gift in giftcards_2015.iterrows():
            if gift['_buyer_acctid']==item:
                    Data.loc[count] = [gift['date_purchased'],0,gift['_buyer_acctid']]
                    count=count+1
Data['Date']=pd.DatetimeIndex(Data['Date']).normalize()
for item in account: 
    Plot1=Data[(Data['acctid']== item)]
    Plot = (Plot1.reset_index()
              .groupby(['Date','Role','acctid'], as_index=False)
              .count()

              .rename(columns={'index':'count'})
           )
Plot['Log_count']=np.log(Plot['count'])
fig, ax = plt.subplots()
Title=account
marker_counter=0
for key, data in Plot.groupby('Role'):
        xfmt = mdates.DateFormatter('%Y-%m')
        ax.xaxis.set_major_formatter(xfmt)
        plt.title('accountId ='+item)
        if(key== 1):
            label_name='Donation'  
            data.plot(x='Date', y='Log_count', ax=ax, marker='o',label=label_name, sharex=False)
        else:   
            label_name='Giftcard'
            data.plot(x='Date', y='Log_count', ax=ax, marker='*',label=label_name, sharex=False)
        plt.legend()
        plt.savefig(item+'.pdf')
        
