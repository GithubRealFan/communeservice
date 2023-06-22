from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    ip = models.CharField(max_length=31)
    port = models.IntegerField()
    password = models.CharField(max_length=255)
    power = models.BooleanField(default=False)
    mining = models.BooleanField(default=False)
    miner_bash = models.CharField(max_length=2047, default='')
    miner_output = models.CharField(max_length=2047, default='')

class ColdKey(models.Model):
    walletname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    ss58 = models.CharField(max_length=48)

class HotKey(models.Model):
    walletname = models.CharField(max_length=255)
    hotkey = models.CharField(max_length=255)
    mnemonic = models.CharField(max_length=2047)
