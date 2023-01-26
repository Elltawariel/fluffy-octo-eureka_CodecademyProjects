import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head(5))
print(cart.head(5))
print(checkout.head(5))
print(purchase.head(5))
visits_cart = pd.merge(visits, cart, how="left")
print(visits_cart.head(5))
lent = len(visits_cart)
print(lent)
notor = visits_cart[visits_cart.cart_time.isnull()]
print(notor)
perc = float(len(notor)) / float(lent) * 100
print(perc)

cart_checkout = pd.merge(cart, checkout, how="left")
print(cart_checkout.head(5))
lent2 = len(cart_checkout)
print(lent2)
notor2 = cart_checkout[cart_checkout.checkout_time.isnull()]
print(notor2)
perc2 = float(len(notor2)) / float(lent2) * 100
print(perc2)

all_data = visits_cart.merge(checkout, how="left").merge(purchase, how="left")
print(all_data.head(5))
allu = float(len(all_data))
notor3 = all_data[all_data.checkout_time.isnull()]
notor4 = all_data[all_data.purchase_time.isnull()]
perc3 = (float(len(notor4)) - float(len(notor3))) / float(allu - float(len(notor3))) * 100
print(perc3)
print(all_data[all_data.cart_time.isnull()])
print(all_data[all_data.checkout_time.isnull()])
print(all_data[all_data.purchase_time.isnull()])
all_data['time_to_purchase'] = all_data.purchase_time -    all_data.visit_time
print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
