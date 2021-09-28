def computepay(hours, rate) :
    if hours > 40:
        regpay = 40 * rate
        otpay = (hours - 40) * (rate * 1.5)
        totalpay = regpay + otpay
    else:
        totalpay = hours * rate
    return totalpay

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)
totalpay = computepay(h,r)

print("Pay:",totalpay)
