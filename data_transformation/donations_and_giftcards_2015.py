# Purpose: To count the number of giftcards and donations
# by individuals every year

import pandas  as pd
from tqdm import tqdm
import socket
import sys
if socket.gethostname()=='isds-research':
    path='/home/test/donorschoose/raw_files/'
else:
    path=''
print("Reading data file ....")

# Read the json file
donations = pd.read_csv(Donorspath,escapechar='\\', names=['_donationid', '_projectid', '_donor_acctid', '_cartid', 'donor_city', 'donor_state', 'donor_zip', 'is_teacher_acct', 'donation_timestamp', 'donation_to_project', 'donation_optional_support', 'donation_total', 'donation_included_optional_support', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched','is_teacher_referred', 'giving_page_id', 'giving_page_type', 'for_honoree', 'thank_you_packet_mailed'])
# Filter the data for respective year from donations data
Total_donations=donations[(donations['donation_timestamp'].apply(lambda x:x[0:4]) == '2015')]

giftcards = pd.read_csv(path+'opendata_giftcards000.gz', escapechar='\\', names=['_giftcardid', 'dollar_tier', '_buyer_acctid', 'buyer_city', 'buyer_state', 'buyer_zip', 'date_purchased', '_buyer_cartid', '_recipient_acctid', 'recipient_city', 'recipient_state', 'recipient_zip', 'redeemed', 'date_redeemed', '_redeemed_cartid', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched'])
print("Filtering data for 2015...")
giftcards_2015=giftcards[(giftcards['date_purchased'].apply(lambda x:x[0:4]) == '2015')]

giftcards_2015.payment_included_acct_credit.replace(['t', 'f'], [1, 0], inplace=True)
giftcards_2015.payment_included_campaign_gift_card.replace(['t', 'f'], [1, 0], inplace=True)
giftcards_2015.payment_included_web_purchased_gift_card.replace(['t', 'f'], [1, 0], inplace=True)
giftcards_2015.payment_was_promo_matched.replace(['t', 'f'], [1, 0], inplace=True)
giftcards_2015_Test=giftcards_2015.groupby(['_buyer_acctid'])[['payment_included_acct_credit','payment_included_campaign_gift_card','payment_included_web_purchased_gift_card','payment_was_promo_matched']].sum()
Total_donations_2015_test=Total_donations.groupby('_donor_acctid')[['_donor_acctid']].count()
Total_donations_2015_test=Total_donations_2015_test.rename(columns={'_donor_acctid':'count_Donations'})
Gift_Merge_with_Donation=pd.merge(giftcards_2015_Test,Total_donations_2015_test, how='left',left_on=['_buyer_acctid'],right_on=['_donor_acctid'])
Gift_Merge_with_Donation["Year"]=2015
Gift_Merge_with_Donation['count_Donations'].fillna(0, inplace=True)
Gift_Merge_with_Donation.to_csv("C://Users/Nameetha/Desktop/Stata/GiftCard_Type.csv")


# TODO: We need to run this for other years. Lets create 
# a function where we pass the year and filename of final
# output file and the file is saved in a given location


