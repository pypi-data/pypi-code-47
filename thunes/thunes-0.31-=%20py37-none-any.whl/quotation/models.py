from django.db import models

# Create your models here.


class Quotation(models.Model):
    QUOTATION_MODE = (
        ('SOURCE_AMOUNT', 'Quotation created by specifying desired source'),
        ('DESTINATION_AMOUNT', 'Quotation created by specifying desired destination'),
    )
    quotation_id = models.CharField(max_length=50, blank=False, verbose_name='Quotation reference ID')
    external_id = models.CharField(max_length=50, blank=False, verbose_name='External reference ID')
    payer_id = models.CharField(max_length=50, blank=False, verbose_name='Payer ID')
    mode = models.CharField(max_length=50, default='SOURCE_AMOUNT', choices=QUOTATION_MODE,
                            blank=False, verbose_name='Quotation mode')
    source = models.OneToOneField('Source', related_name='sourceEntity', on_delete=models.CASCADE,
                                  blank=False, verbose_name='Source information')
    destination = models.OneToOneField('Destination', related_name='destinationEntity', blank=False,
                                       on_delete=models.CASCADE, verbose_name='Destination information')

    class Meta:
        db_table = 'quotation'
        verbose_name = 'quotation'


class Source(models.Model):
    country_iso_code = models.CharField(max_length=10, blank=False,
                                        verbose_name='Country code in ISO 3166-1 alpha-3 format')
    currency = models.CharField(max_length=10, blank=False, verbose_name='Source currency in ISO 4217 format')
    amount = models.IntegerField(blank=True, verbose_name='Source amount')

    def __str__(self):
        return 'Source {}|{}|{}'.format(self.country_iso_code, self.currency, self.amount)


class Destination(models.Model):
    currency = models.CharField(max_length=10, blank=False, verbose_name='Source currency in ISO 4217 format')
    amount = models.IntegerField(blank=True, null=True, verbose_name='Source amount')

    def __str__(self):
        return 'Destination {}|{}'.format(self.currency, self.amount)

