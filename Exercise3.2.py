hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input")
quit()

if h > 40:
    regpay = 40 * r
    otpay = (h - 40) * (r * 1.5)
    totalpay = regpay + otpay
else:
    totalpay = h * r
print("Pay:",totalpay)
