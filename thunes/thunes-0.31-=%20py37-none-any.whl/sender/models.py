from django.db import models


# Create your models here.
class Sender(models.Model):
    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    ID_TYPE = (
        ('PASSPORT', 'Passport'),
        ('NATIONAL_ID', 'National Identification Card'),
        ('DRIVING_LICENSE', 'Driving License'),
        ('SOCIAL_SECURITY', 'Social Security Card/Number'),
        ('TAX_ID', 'Tax Payer Identification Card/Number'),
        ('SENIOR_CITIZEN_ID', 'Senior Citizen Identification Card'),
        ('BIRTH_CERTIFICATE', 'Birth Certificate'),
        ('VILLAGE_ELDER_ID', 'Village Elder Identification Card'),
        ('RESIDENT_CARD', 'Permanent Residency Identification Card'),
        ('ALIEN_REGISTRATION', 'Alien Registration Certificate/Card'),
        ('PAN_CARD', 'PAN Card'),
        ('VOTERS_ID', 'Voter’s Identification Card'),
        ('HEALTH_CARD', 'Health Insurance Card/Number'),
        ('EMPLOYER_ID', 'Employer Identification Card'),
        ('OTHER', 'Others not listed')
    )
    BENEFICIARY_RELATIONSHIP = (
        ('AUNT', 'Aunt'),
        ('BROTHER', 'Brother'),
        ('BROTHER_IN_LAW', 'Brother-in-law'),
        ('COUSIN', 'Cousin'),
        ('DAUGHTER', 'Daughter'),
        ('FATHER', 'Father'),
        ('FATHER_IN_LAW', 'Father-in-law'),
        ('FRIEND', 'Friend'),
        ('GRAND_FATHER', 'Grandfather'),
        ('GRAND_MOTHER', 'Grandmother'),
        ('HUSBAND', 'Husband'),
        ('MOTHER', 'Mother'),
        ('MOTHER_IN_LAW', 'Mother-in-law'),
        ('NEPHEW', 'Nephew'),
        ('NIECE', 'Niece'),
        ('SELF', 'Self (i.e. the sender, himself)'),
        ('SISTER', 'Sister'),
        ('SISTER_IN_LAW', 'Sister-in-law'),
        ('SON', 'Son'),
        ('UNCLE', 'Uncle'),
        ('WIFE', 'Wife'),
        ('OTHER', 'Others not listed')
    )
    lastname = models.CharField(max_length=50, blank=False, verbose_name='Last Name')
    lastname2 = models.CharField(max_length=50, blank=True, verbose_name='Additional last name(s)')
    middlename = models.CharField(max_length=50, blank=True, verbose_name='Middle Name')
    firstname = models.CharField(max_length=50, blank=False, verbose_name='First Name')
    nativename = models.CharField(max_length=50, blank=True, verbose_name='Full name in native characters')
    nationality_country_iso_code = models.CharField(max_length=10, blank=False,
                                                    verbose_name='National Country ISO Code')
    code = models.CharField(max_length=10, blank=True, verbose_name='code')
    date_of_birth = models.DateField(blank=False, verbose_name='Date Of Birth')
    country_of_birth_iso_code = models.CharField(max_length=10, blank=False, verbose_name='Country Of Birth ISO Code')
    gender = models.CharField(default='MALE', max_length=10, choices=GENDER, verbose_name='gender')
    address = models.CharField(max_length=50, blank=False, verbose_name='Address')
    postal_code = models.CharField(max_length=50, blank=False, verbose_name='Postal Code', )
    city = models.CharField(max_length=50, blank=False, verbose_name='City')
    country_iso_code = models.CharField(max_length=50, blank=False, verbose_name='Country ISO Code')
    msisdn = models.CharField(max_length=50, blank=False, verbose_name='MSISDN in international format')
    email = models.EmailField(max_length=50, blank=False, verbose_name='Email Address')
    id_type = models.CharField(default='', choices=ID_TYPE, max_length=50, blank=False,
                               verbose_name='Presented identification type')
    id_country_iso_code = models.CharField(max_length=50, blank=False,
                                           verbose_name='ID country in ISO 3166-1 alpha-3 format')
    id_number = models.CharField(max_length=50, blank=False, verbose_name='Presented identification number')
    id_delivery_date = models.DateField(max_length=50, blank=False, verbose_name='ID delivery date in ISO 8601 format')
    id_expiration_date = models.DateField(max_length=50, blank=True, null=True,
                                          verbose_name='ID expiration date in ISO 8601 format')
    occupation = models.CharField(max_length=50, blank=False, verbose_name='Occupation')
    bank = models.CharField(max_length=50, blank=True, verbose_name='Name of bank')
    bank_account = models.CharField(max_length=50, blank=True, verbose_name='Bank account number')
    card = models.CharField(max_length=50, blank=True, verbose_name='Credit card number')
    province_state = models.CharField(max_length=50, blank=True, verbose_name='Address province/state')
    beneficiary_relationship = models.CharField(default='', choices=BENEFICIARY_RELATIONSHIP,
                                                max_length=50, verbose_name='Relationship to beneficiary')
    source_of_funds = models.CharField(max_length=50, blank=True, verbose_name='Source of funds')

    def __str__(self):
        return 'Sender {} {}'.format(self.lastname, self.firstname)

    class Meta:
        verbose_name = 'sender'
        db_table = 'sender'
