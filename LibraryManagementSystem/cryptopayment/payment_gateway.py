"""
This is the script that checks for Payment models in the database
and if the payment is received in the given bitcoin address
it sets the Payment model's success to True
then calls the create order function, and creates an order for the cart
"""



import logging
import time

import bit
import bit.exceptions
from commercebackend.models import CartModel, OrderModel

from cryptopayment.models import Invoice, Payment

# set up the logger

log = logging.getLogger("payment_gateway")

def create_order(payment):
    order = OrderModel.objects.create(
        user=payment.user, cart=payment.cart, shipping=payment.shipping
    )
    log.info(f"{order} has been created")
    invoice = Invoice.objects.create(payment=payment, order=order)
    log.info(f"{invoice} has been created")

def check_payment_success():
    while True:
        log.info("Running checking for payment...\n")
        # get all payments in the payment table with success 0
        for payment in Payment.objects.all().filter(success=0):
            btc_cost = payment.total_price_btc
            # get the bitcoin address for the payment
            wallet = bit.PrivateKeyTestnet(payment.btc_address_wif)
            if wallet.get_balance("btc") == str(btc_cost):
                log.info(f"Payment received for {payment}\n")
                # if it is successfull, set the success flag to 1
                payment.success = 1
                # get the cart and set it bought
                cart = CartModel.all_objects.get(pk=payment.cart.id)
                # user might delete the cart, so get it from all_objects rather than objects
                cart.bought = 1
                cart.save()
                payment.save()
                create_order(payment)
        log.info("Payment checker ran successfully.\n")
        time.sleep(60)  # wait a minute, continue checking payments


# this function moves all the successfull payments from payment wallets to a specificed wallet
# move_payments('bitcoin_wallet_address')
def move_payments(to_wallet):
    # get all the payments with success 1
    payments = Payment.objects.all().filter(success=1)
    for payment in payments:
        # get the wallet
        wallet = bit.PrivateKeyTestnet(payment.btc_address_wif)
        # create transactions
        try:
            tx_id = wallet.send([], leftover=to_wallet)
            log.info(f"Payment from {wallet} to {to_wallet} is successfull.\nTxid:\n{tx_id}")
        except bit.exceptions.InsufficientFunds as e:
            log.error(f"Payment wallet {wallet} has insufficent funds for a transaction, \n{e}")
            continue
