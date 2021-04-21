from django.db import models

# Create your models here.


class Ticker(models.Model):
    ticker_name = models.CharField(max_length=200, null=True, blank=True)
    ticker_logo = models.TextField(null=True,blank=True)
    def __str__(self):
        return '{0}'.format(self.ticker_name)

class comment(models.Model):
    site_name = models.CharField(max_length=200, null=True, blank=True)

    ticker_symbol = models.CharField(max_length=200, null=True, blank=True)

    original_comment = models.TextField(null=True, blank=True)

    pre_processed_comment = models.TextField(null=True, blank=True)

    comment_date = models.DateTimeField()

    comment_like_count = models.IntegerField(null=True,blank=True)

    pos = models.FloatField(null=True, blank=True)
    neu = models.FloatField(null=True, blank=True)
    neg = models.FloatField(null=True, blank=True)
    compound = models.FloatField(null=True, blank=True)

    label = models.CharField(max_length=200, null=True, blank=True)
    actual_label = models.CharField(max_length=200, null=True, blank=True)

    ticker = models.ForeignKey(Ticker,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return '{0}, {1}'.format(self.site_name, self.ticker_symbol)

class Exceptions(models.Model):
    exception = models.TextField(null=True, blank=True)
    extra_info = models.TextField(null=True, blank=True)
    time_happened = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{0},Time : {1}'.format(self.exception, self.time_happened)