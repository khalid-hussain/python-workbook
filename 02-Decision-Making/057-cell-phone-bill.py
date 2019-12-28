BASE_COST = 15.00
BASE_AIRTIME = 50
BASE_SMS = 50
XTRA_MIN = 0.25
XTRA_SMS = 0.15

BILL_911 = 0.44
SALES_TAX = 0.05

minutes = int(input('Input no. of minutes: '))
sms = int(input('Input no. of messages: '))

extra_minutes = minutes - BASE_AIRTIME
extra_sms = sms - BASE_SMS

addi_minutes_cost = (minutes - BASE_AIRTIME) * XTRA_MIN
addi_sms_cost = (sms - BASE_SMS) * XTRA_SMS

print(f'Base charge: ${BASE_COST:,.2f}')

if addi_minutes_cost > 0:
    print(f'Additional minutes charge: ${addi_minutes_cost:,.2f}')
if addi_sms_cost > 0:
    print(f'Additional messages charge: ${addi_sms_cost:,.2f}')

print(f'911 Fee: ${BILL_911:,.2f}')

sub_total = BASE_COST \
    + addi_minutes_cost \
    + addi_sms_cost \
    + BILL_911 \

tax = sub_total * SALES_TAX
total = sub_total + tax

print(f'Tax: ${tax:,.2f}')
print(f'Total: ${total:,.2f}')
