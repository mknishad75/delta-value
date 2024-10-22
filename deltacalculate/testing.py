import deltacalculate.kiteapp as kt
import pandas as pd
import deltacalculate.option as tt
from time import sleep
with open('enctoken.txt', 'r') as rd:
	token = rd.read()
kite = kt.KiteApp("kite", "mu", token)
kws = kite.kws()  # For Websocket


'''
# Place Order
oid = kite.place_order(variety="amo", exchange='NSE',
		tradingsymbol='SBIN', transaction_type='BUY',
		quantity=5, product='MIS', order_type="LIMIT",
		price=820, validity="DAY")


print(oid)
order = kite.orders()


print(order)
'''


S0 = 25790.95
X = 25800.00
σ = 12.79
t = 3
call_theta,put_theta,call_premium,put_premium,call_delta,put_delta,gamma,vega,call_rho,put_rho=tt.black_scholes_dexter(S0,X,t,σ,r=10,q=0.0,td=365)
print(call_theta)
print(put_theta)
print(call_premium)
print(put_premium)
print(call_delta)
print(put_delta)
print(gamma)
print(vega)
print(call_rho)
print(put_rho)

#holding = kite.holdings()
#print(holding)
