import calendar
import datetime


def calculateMoney(bm, ir, dur, receiveDate, payDate):
  output = 'Table for money payment:\
    \n-----------------------------------------------------------------------------------------------------\
    \nBorrow Money: {bm}\
    \nInterest Rate: {ir}\
    \nDuration(Month): {dur}\
    \nReceive: {rd}\
    \nPayment: {pay}\
    \n-----------------------------------------------------------------------------------------------------\
    \n#\tDate\t\tMoney\t\tInterest pay\t\tMoney to pay\t\tTotal pay\
    \n-----------------------------------------------------------------------------------------------------\
    '.format(
      bm = bm,
      ir = ir,
      dur = dur,
      rd = receiveDate,
      pay = payDate
    )
  datePay = datetime.datetime.strptime(payDate, "%d/%m/%Y").date()
  moneyToPay = interest = totalPay = 0
  daysInMonth = ''
  for i in range(0, 12):
    if i == 0:
      moneyToPay = bm / dur
      interest = (bm * ir) / 100
      totalPay = moneyToPay + interest
    elif i > 0:
      bm -= moneyToPay
      interest = (bm * ir) / 100
      totalPay = moneyToPay + interest
      daysInMonth = calendar.monthrange(datePay.year, datePay.month)[1]
      datePay += datetime.timedelta(days=daysInMonth)
    output += '\n{id}\t{date}\t{money}\t\t{interest}\t\t\t\t{mtp}\t\t\t\t{tp}\
      '.format(
        id = i + 1,
        date = '{0}/{1}/{2:02}'.format(datePay.day, datePay.month, datePay.year),
        money = round(bm, 2),
        interest = round(interest, 2),
        mtp = round(moneyToPay, 2),
        tp = round(totalPay, 2)
      )
  return output

print(calculateMoney(8000, 1.5, 12, '15/11/2018', '02/12/2018'))
