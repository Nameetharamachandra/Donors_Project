# Author: Vivek Singh
# Read gift card data and convert to csv 
# with header information

import pandas as pandas

path='C:\\Users\\vivek4\\Downloads\\donorschoose\\'
giftcards = pandas.read_csv(path+'opendata_giftcards000.gz', escapechar='\\', names=['_giftcardid', 'dollar_tier', '_buyer_acctid', 'buyer_city', 'buyer_state', 'buyer_zip', 'date_purchased', '_buyer_cartid', '_recipient_acctid', 'recipient_city', 'recipient_state', 'recipient_zip', 'redeemed', 'date_redeemed', '_redeemed_cartid', 'payment_method', 'payment_included_acct_credit', 'payment_included_campaign_gift_card', 'payment_included_web_purchased_gift_card', 'payment_was_promo_matched'])
giftcards.to_csv(path+'giftcards.csv', index=False)