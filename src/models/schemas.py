# coding=utf-8

from peewee import *
from paycenter.models import BaseModel


class Orders(BaseModel):
    orderid = CharField(primary_key=True)
    cporderid = CharField(null=False)
    ordertype = IntegerField()
    orderchannel = CharField()
    uid = IntegerField(null=False)
    account_id = IntegerField()
    productid = CharField()
    companyid = CharField()
    channelid = CharField()
    appid = CharField(null=False)
    amount = CharField()
    amoutunit = CharField()
    cpprice = CharField()
    currency = CharField()
    currencycode = CharField()
    merpriv = CharField()
    realamout = CharField()
    denomination = CharField()
    gameversionname = CharField(null=False)
    gameroleid = CharField(null=False)
    gameserverid = CharField(null=False)
    platformid = CharField()
    osversion = CharField()
    countrycode = CharField()
    language = CharField()
    orderstatus = IntegerField(null=False)
    create_at = IntegerField()
    ip_addr = CharField()
    update_at = IntegerField()


class Molorders(BaseModel):
    oid = IntegerField(primary_key=True)
    orderid = CharField()
    uid = IntegerField()
    amount = CharField()
    channeid = CharField()
    transid = CharField()
    applicationCode = CharField()
    currency = CharField()
    paystatus = CharField()
    paydate = CharField()
    create_at = IntegerField()
    calbcktxt = CharField()


class Googleorders(BaseModel):
    oid = IntegerField(primary_key=True)
    order_id = CharField()
    uid = IntegerField()
    transid = CharField()
    receipt = CharField()
    bid = CharField()
    product_id = CharField()
    create_at = IntegerField()


class Appleorders(BaseModel):
    oid = IntegerField(primary_key=True)
    order_id = CharField()
    uid = IntegerField()
    transid = CharField()
    receipt = CharField()
    bid = CharField()
    product_id = CharField()
    create_at = IntegerField()


class Onestoreorders(BaseModel):
    oid = IntegerField(primary_key=True)
    order_id = CharField()
    uid = IntegerField()
    transid = CharField()
    receipt = CharField()
    bid = CharField()
    product_id = CharField()
    create_at = IntegerField()


class Naverorders(BaseModel):
    oid = IntegerField(primary_key=True)
    order_id = CharField()
    uid = IntegerField()
    transid = CharField()
    receipt = CharField()
    bid = CharField()
    product_id = CharField()
    create_at = IntegerField()


class Cultureorders(BaseModel):
    oid = IntegerField(primary_key=True)
    order_id = CharField()
    uid = IntegerField()
    transid = CharField()
    receipt = CharField()
    bid = CharField()
    product_id = CharField()
    create_at = IntegerField()


class Mycardorders(BaseModel):
    oid = IntegerField(primary_key=True)
    order_id = CharField()
    uid = IntegerField()
    receipt = CharField()
    bid = CharField()
    product_id = CharField()
    create_at = IntegerField()
    verify = TextField()
    TradeSeq = CharField()


class blupayorders(BaseModel):
    id = IntegerField(primary_key=True)
    order_id = CharField()
    cmd = CharField()
    bt_id = CharField()
    msisdn = CharField()
    paytype = CharField()
    price = CharField()
    productid = CharField()
    status = IntegerField()
    t_id = CharField()
    currency = CharField()
    interfacetype = CharField()
    text = TextField()
    create_at = IntegerField()


class Paynotice(BaseModel):
    callid = IntegerField(primary_key=True)
    orderid = CharField()
    cporderid = CharField()
    orderchannel = CharField()
    productid = CharField()
    cardno = CharField()
    transid = CharField()
    companyid = CharField()
    channelid = CharField()
    appid = CharField()
    amount = CharField()
    realamout = CharField()
    amountunit = CharField()
    paystatus = CharField()
    cardstatus = CharField()
    merpriv = CharField()
    platformid = CharField()
    isinqueue = IntegerField()
    iscallback = IntegerField()
    callbacktext = CharField()
    callbackparams = CharField()
    create_at = IntegerField()
    update_at = IntegerField()
