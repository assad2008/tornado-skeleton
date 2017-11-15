#/usr/bin/python
# coding=utf-8

from paycenter.common.functions import debug


def isnumeric(s):
    return all(c in "0123456789.+-" for c in s)


def checkAmount(amount):
    k = amount.rfind(".")
    h = amount.rfind(",")
    if k == -1 and h == -1:
        pass
    else:
        if k != -1 and h == -1:
            rightStr = amount[k + 1:]
            if len(rightStr) > 2:
                amount = amount.replace(".", "")
            else:
                leftStr = amount[0:k]
                amount = leftStr.replace(",", "") + "." + rightStr
        elif k == -1 and h != -1:
            rightStr = amount[h + 1:]
            if len(rightStr) > 2:
                amount = amount.replace(",", "")
            else:
                leftStr = amount[0:h]
                amount = leftStr.replace(",", "") + "." + rightStr
        elif k != -1 and h != -1:
            rightStr1 = amount[k + 1:]
            rightStr2 = amount[h + 1:]
            if len(rightStr1) <= 2:
                leftStr = amount[0:k]
                amount = leftStr.replace(".", "").replace(",", "") + "." + rightStr1
            elif len(rightStr2) <= 2:
                leftStr = amount[0:h]
                amount = leftStr.replace(".", "").replace(",", "") + "." + rightStr2
            else:
                amount = amount.replace(".", "").replace(",", "")
    return amount


def newCheckAmount(unit, amount):
    k = amount.rfind(".")
    h = amount.rfind(",")
    if k == -1 and h == -1:
        pass
    else:
        amount = checkAmount(amount)
    return amount


def pamount(tvalue, amountStr):
    if isnumeric(tvalue):
        for i in range(0, len(amountStr)):
            midStr = amountStr[i:i + 1]
            if(midStr != "," and midStr != "."):
                if not isnumeric(midStr):
                    sepPosition = i
                    break
        if sepPosition != -1:
            amount = amountStr[0:sepPosition].rstrip().lstrip()
            unit = amountStr[sepPosition:len(amountStr)].rstrip().lstrip()
    else:
        if len(tvalue) == 1:
            for i in range(len(amountStr) - 1, -1, -1):
                midStr = amountStr[i:i + 1]
                if midStr != "," and midStr != ".":
                    if midStr != "":
                        if not isnumeric(amountStr):
                            sepPosition = i
                            break
            if sepPosition != -1:
                unit = amountStr[0:sepPosition + 1].rstrip().lstrip()
                amount = amountStr[sepPosition + 1:len(amountStr)].rstrip().lstrip()
        elif len(tvalue) == 3:
            for i in range(2, len(amountStr)):
                midStr = amountStr[i:i + 1]
                if midStr != "," and midStr != ".":
                    if midStr != "":
                        if not isnumeric(amountStr):
                            sepPosition = i
                            break
            if sepPosition != -1:
                unit = amountStr[0:sepPosition + 1].rstrip().lstrip()
                amount = amountStr[sepPosition + 1:len(amountStr)].rstrip().lstrip()
    return unit, amount


def paseramount(amountStr):
    amountStr = amountStr.encode("utf-8")
    sepPosition = 1
    amountStr = amountStr.lstrip().rstrip().replace(" ", "")
    if amountStr != "":
        if isnumeric(amountStr):
            unit = ""
            amount = amountStr
        else:
            onebit = amountStr[0:1]
            threebit = amountStr[0:3]
            if onebit in ["$", "£"]:
                return amountStr[1:], onebit
            if isnumeric(onebit):
                unit, amount = pamount(onebit, amountStr)
            else:
                unit, amount = pamount(threebit, amountStr)
        unit = unit.upper()
        if amount != None and amount != "":
            if unit != "":
                amount = newCheckAmount(unit, amount)
    else:
        amount = ""
        unit = ""
    return amount, unit
