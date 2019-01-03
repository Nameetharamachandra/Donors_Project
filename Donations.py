import pandas  as pd
import numpy as np
from matplotlib import pyplot as plt
import io
import pandas as pd
import path
 # Read the json file
donations = pd.read_csv('/home/test/donorschoose/raw_files/opendata_donations000.gz',escapechar='\\', names=['_donationid', '_projectid', '_donor_acctid', '_cartid', 'donor_city', 'donor_state', 'donor_zip', 'is_teacher_acct', 'donation_timestamp', 'donation_to_project', 'donation_optional_support', 'donation_total', 'donation_included_optional_support', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched','is_teacher_referred', 'giving_page_id', 'giving_page_type', 'for_honoree', 'thank_you_packet_mailed'])
 # Filter the data for respective year from donations data
Total_donations=donations[(donations['donation_timestamp'] > '2016-00-0 0:00:00.00')]
#Select unique donor Id's
Unique_donations=Total_donations.drop_duplicates('_donor_acctid')
#read giftcard csv
giftcards= pd.read_csv("giftcards.csv")
giftcards['date_purchased'] = pd.to_datetime(giftcards['date_purchased'])
giftcards_2016=giftcards[(giftcards['date_purchased']> '2016')]
Data = pd.DataFrame(columns=['Date', 'Role'])
count=0
#plot graph for donations made and gift cards purchased by unique donor Id
for i, unique in Unique_donations.iterrows():
    for j,total in Total_donations.iterrows():
        if unique['_donor_acctid']==total['_donor_acctid']:
        #for every donation made by a donor add value '1' to perform groupby
            Data.loc[count] = [total['donation_timestamp'],1]
            count=count+1
    for k, gift in giftcards_2016.iterrows():
        if unique['_donor_acctid']==gift['_buyer_acctid']:
        #for every giftcard bought by a donor add value '0' to perform groupby
            Data.loc[count] = [gift['date_purchased'],0]
            count=count+1
    Data['Date']=pd.DatetimeIndex(Data['Date']).normalize()
    Plot = (Data.reset_index()
          .groupby(['Date','Role'], as_index=False)
          .count()
          
          .rename(columns={'index':'count'})
       )
    Plot['Log_count']=np.log(Plot['count'])
    fig, ax = plt.subplots()
    Title=account
    linestyles = ['-', '--', '-.', ':']
    line_type=0
    # key gives the group name (i.e. RepName), data gives the actual values
    for key, data in Plot.groupby('Role'):
        plt.title('accountId ='+item)
        if(key== 1):
            label_name='Donation'
        else:
            label_name='Giftcard'

        data.plot(x='Date', y='Log_count', ax=ax, linestyle=linestyles[line_type],label=label_name, sharex=False)
        line_type=line_type+1
    plt.savefig(total['_donor_acctid']+'.pdf')
    plt.show
