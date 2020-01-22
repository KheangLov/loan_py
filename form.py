from tkinter import *

root = Tk()
root.title('Loan')


def submit():
    borrow = txtBorrow.get()
    type = txtDate.get()
    interest = txtInterest.get()
    dur = txtDur.get()
    renderTable(borrow, type, interest, dur)


def renderTable(br, ty, ir, dr):
    br = int(br)
    tableMaster = Tk()
    tableMaster.title('Table Loan')
    tblHeader = Frame(tableMaster, bg='#fff')
    lblHeader = Label(tblHeader, text='Table loan', font=("Courier", 32))

    tblSndHead = Frame(tableMaster, bg='#fff')
    lblBorrowHeader = Label(tblSndHead, text='Borrow money:', width=15, font=("Courier", 20), borderwidth=1, relief="solid")
    lblMoneyHeader = Label(tblSndHead, text=br, width=5, font=("Courier", 20), borderwidth=1, relief="solid")
    lblIRate = Label(tblSndHead, text='Interest rate:', width=15, font=("Courier", 20), borderwidth=1, relief="solid")
    lblIMoney = Label(tblSndHead, text=ir, width=5, font=("Courier", 20), borderwidth=1, relief="solid")
    lblDuratation = Label(tblSndHead, text='Duration:', width=15, font=("Courier", 20), borderwidth=1, relief="solid")
    lblMonth = Label(tblSndHead, text=dr, width=5, font=("Courier", 20), borderwidth=1, relief="solid")

    tblHeader.grid(row=0, column=0, columnspan=6)
    lblHeader.grid(row=0, column=0)
    tblSndHead.grid(row=1, column=0, sticky=W)
    lblBorrowHeader.grid(row=1, column=0, columnspan=2)
    lblMoneyHeader.grid(row=1, column=2)
    lblIRate.grid(row=1, column=3)
    lblIMoney.grid(row=1, column=4)
    lblDuratation.grid(row=1, column=5)
    lblMonth.grid(row=1, column=6)

    moreHeader = Frame(tableMaster, bg='#fff')
    lblTypeHeader = Label(moreHeader, text='Loan Type:', font=("Courier", 20), borderwidth=1, relief="solid")
    lblDecreaseHeader = Label(moreHeader, text=ty, font=("Courier", 20), borderwidth=1, relief="solid")

    moreHeader.grid(row=2, column=0, sticky=W)
    lblTypeHeader.grid(row=2, column=0)
    lblDecreaseHeader.grid(row=2, column=1)

    headers = Frame(tableMaster, bg='#fff')
    lblMm = Label(headers, text='mm', width=10, font=("Courier", 20), borderwidth=1, relief="solid")
    lblOBal = Label(headers, text='Obal', width=10, font=("Courier", 20), borderwidth=1, relief="solid")
    lblIR = Label(headers, text='IR', width=10, font=("Courier", 20), borderwidth=1, relief="solid")
    lblDbal = Label(headers, text='Dbal', width=10, font=("Courier", 20), borderwidth=1, relief="solid")
    lblPay = Label(headers, text='Pay', width=10, font=("Courier", 20), borderwidth=1, relief="solid")
    lblEbal = Label(headers, text='Ebal', width=10, font=("Courier", 20), borderwidth=1, relief="solid")

    headers.grid(row=3, column=0)
    lblMm.grid(row=4, column=0)
    lblOBal.grid(row=4, column=1)
    lblIR.grid(row=4, column=2)
    lblDbal.grid(row=4, column=3)
    lblPay.grid(row=4, column=4)
    lblEbal.grid(row=4, column=5)

    dbalMoney = int(br) / int(dr)

    for i in range(1, int(dr) + 1):
        Label(headers, text=i, width=12, font=("Courier", 16), borderwidth=1, relief="solid", bg='#fff').grid(row=i + 4, column=0)
        Label(headers, text=str(round(br, 2)), width=12, font=("Courier", 16), borderwidth=1, relief="solid", bg='#fff').grid(row=i + 4, column=1)

        inrt = round((float(br) * float(ir)) / 100, 2)

        Label(headers, text=str(inrt), width=12, font=("Courier", 16), borderwidth=1, relief="solid", bg='#fff').grid(row=i + 4, column=2)
        Label(headers, text=str(round(dbalMoney, 2)), width=12, font=("Courier", 16), borderwidth=1, relief="solid", bg='#fff').grid(row=i + 4, column=3)

        thisMPay = round(dbalMoney + inrt, 2)

        Label(headers, text=str(thisMPay), width=12, font=("Courier", 16), borderwidth=1, relief="solid", bg='#fff').grid(row=i + 4, column=4)

        br -= dbalMoney

        if round(br, 2) > 0:
            Label(headers, text=str(round(br, 2)), width=12, font=("Courier", 16), borderwidth=1, relief="solid", bg='#fff').grid(row=i + 4, column=5)
        else:
            Label(headers, text='0', width=12, font=("Courier", 16), borderwidth=1, relief="solid", bg='#fff').grid(row=i + 4, column=5)

    tableMaster.mainloop()


form = Frame(root, bg='#fff')
lblBorrow = Label(form, text='Borrow Money:', bg='#fff')
txtBorrow = Entry(form, width=30)
lblDate = Label(form, text='Type:', bg='#fff')
txtDate = Entry(form, width=30)
lblInterest = Label(form, text='Interest:', bg='#fff')
txtInterest = Entry(form, width=30)
lblDur = Label(form, text='Duration:', bg='#fff')
txtDur = Entry(form, width=30)
btnSubmit = Button(form, text='Submit', width=40, command=submit)

form.grid(row=0, column=0)
lblBorrow.grid(row=0, column=0, padx=10, pady=10, sticky=W)
txtBorrow.grid(row=0, column=1, padx=10, pady=10)
lblDate.grid(row=1, column=0, padx=10, pady=10, sticky=W)
txtDate.grid(row=1, column=1, padx=10, pady=10)
lblInterest.grid(row=2, column=0, padx=10, pady=10, sticky=W)
txtInterest.grid(row=2, column=1, padx=10, pady=10)
lblDur.grid(row=3, column=0, padx=10, pady=10, sticky=W)
txtDur.grid(row=3, column=1, padx=10, pady=10)
btnSubmit.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky=E)

root.mainloop()
