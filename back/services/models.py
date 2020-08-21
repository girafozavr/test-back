from django.db import models


class Services(models.Model):
    START = "ST"
    STOP = "SP"
    RESTART = "RT"
    NONE = ''
    LAUNCH_ACTIONS = [
        (NONE, ''),
        (START, 'start'),
        (STOP, 'stop'),
        (RESTART, 'restart'),
    ]

    ENABLE = "EE"
    DISABLE = "DE"
    ENABLE_ACTIONS = [
        (NONE, ''),
        (ENABLE, 'enable'),
        (DISABLE, 'disable'),
    ]

    name = models.TextField()
    is_enabled = models.BooleanField()
    is_started = models.BooleanField()
    enable_action = models.CharField(max_length=2, blank=True, choices=ENABLE_ACTIONS, default=NONE)
    launch_action = models.CharField(max_length=2, blank=True, choices=LAUNCH_ACTIONS, default=NONE)


class Params(models.Model):
    EXIST = 'ET'

    limiter = models.CharField(max_length=2, unique=True, default=EXIST)
    cpu = models.IntegerField(default=0)
    ram = models.IntegerField(default=0)
