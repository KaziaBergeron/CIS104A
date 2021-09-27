hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
if h > 40:
    regpay = 40 * r
    otpay = (h - 40) * (r * 1.5)
    totalpay = regpay + otpay
else:
    totalpay = h * r
print("Pay:",totalpay)
