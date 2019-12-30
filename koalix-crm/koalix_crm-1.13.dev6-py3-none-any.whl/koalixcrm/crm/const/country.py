# -*- coding: utf-8 -*

from django.utils.translation import ugettext as _

COUNTRIES = (
    ('AF', 'AFG', '004', _('Afghanistan')),
    ('AX', 'ALA', '248', _('Aland Islands')),
    ('AL', 'ALB', '008', _('Albania')),
    ('DZ', 'DZA', '012', _('Algeria')),
    ('AS', 'ASM', '016', _('American Samoa')),
    ('AD', 'AND', '020', _('Andorra')),
    ('AO', 'AGO', '024', _('Angola')),
    ('AI', 'AIA', '660', _('Anguilla')),
    ('AQ', 'ATA', '010', _('Antarctica')),
    ('AG', 'ATG', '028', _('Antigua and Barbuda')),
    ('AR', 'ARG', '032', _('Argentina')),
    ('AM', 'ARM', '051', _('Armenia')),
    ('AW', 'ABW', '533', _('Aruba')),
    ('AU', 'AUS', '036', _('Australia')),
    ('AT', 'AUT', '040', _('Austria')),
    ('AZ', 'AZE', '031', _('Azerbaijan')),
    ('BS', 'BHS', '044', _('the Bahamas')),
    ('BH', 'BHR', '048', _('Bahrain')),
    ('BD', 'BGD', '050', _('Bangladesh')),
    ('BB', 'BRB', '052', _('Barbados')),
    ('BY', 'BLR', '112', _('Belarus')),
    ('BE', 'BEL', '056', _('Belgium')),
    ('BZ', 'BLZ', '084', _('Belize')),
    ('BJ', 'BEN', '204', _('Benin')),
    ('BM', 'BMU', '060', _('Bermuda')),
    ('BT', 'BTN', '064', _('Bhutan')),
    ('BO', 'BOL', '068', _('Bolivia')),
    ('BA', 'BIH', '070', _('Bosnia and Herzegovina')),
    ('BW', 'BWA', '072', _('Botswana')),
    ('BV', 'BVT', '074', _('Bouvet Island')),
    ('BR', 'BRA', '076', _('Brazil')),
    ('IO', 'IOT', '086', _('British Indian Ocean Territory')),
    ('BN', 'BRN', '096', _('Brunei Darussalam')),
    ('BG', 'BGR', '100', _('Bulgaria')),
    ('BF', 'BFA', '854', _('Burkina Faso')),
    ('BI', 'BDI', '108', _('Burundi')),
    ('KH', 'KHM', '116', _('Cambodia')),
    ('CM', 'CMR', '120', _('Cameroon')),
    ('CA', 'CAN', '124', _('Canada')),
    ('CV', 'CPV', '132', _('Cape Verde')),
    ('KY', 'CYM', '136', _('Cayman Islands')),
    ('CF', 'CAF', '140', _('Central African Republic')),
    ('TD', 'TCD', '148', _('Chad')),
    ('CL', 'CHL', '152', _('Chile')),
    ('CN', 'CHN', '156', _('China')),
    ('CX', 'CXR', '162', _('Christmas Island')),
    ('CC', 'CCK', '166', _('Cocos (Keeling) Islands')),
    ('CO', 'COL', '170', _('Colombia')),
    ('KM', 'COM', '174', _('Comoros')),
    ('CG', 'COG', '178', _('Congo')),
    ('CD', 'COD', '180', _('Democratic Republic of the Congo')),
    ('CK', 'COK', '184', _('Cook Islands')),
    ('CR', 'CRI', '188', _('Costa Rica')),
    ('CI', 'CIV', '384', _('Cote d\'Ivoire')),
    ('HR', 'HRV', '191', _('Croatia')),
    ('CU', 'CUB', '192', _('Cuba')),
    ('CY', 'CYP', '196', _('Cyprus')),
    ('CZ', 'CZE', '203', _('Czech Republic')),
    ('DK', 'DNK', '208', _('Denmark')),
    ('DJ', 'DJI', '262', _('Djibouti')),
    ('DM', 'DMA', '212', _('Dominica')),
    ('DO', 'DOM', '214', _('Dominican Republic')),
    ('EC', 'ECU', '218', _('Ecuador')),
    ('EG', 'EGY', '818', _('Egypt')),
    ('SV', 'SLV', '222', _('El Salvador')),
    ('GQ', 'GNQ', '226', _('Equatorial Guinea')),
    ('ER', 'ERI', '232', _('Eritrea')),
    ('EE', 'EST', '233', _('Estonia')),
    ('ET', 'ETH', '231', _('Ethiopia')),
    ('FK', 'FLK', '238', _('Falkland Islands (Malvinas)')),
    ('FO', 'FRO', '234', _('Faroe Islands')),
    ('FJ', 'FJI', '242', _('Fiji')),
    ('FI', 'FIN', '246', _('Finland')),
    ('FR', 'FRA', '250', _('France')),
    ('GF', 'GUF', '254', _('French Guiana')),
    ('PF', 'PYF', '258', _('French Polynesia')),
    ('TF', 'ATF', '260', _('French Southern and Antarctic Lands')),
    ('GA', 'GAB', '266', _('Gabon')),
    ('GM', 'GMB', '270', _('Gambia')),
    ('GE', 'GEO', '268', _('Georgia')),
    ('DE', 'DEU', '276', _('Germany')),
    ('GH', 'GHA', '288', _('Ghana')),
    ('GI', 'GIB', '292', _('Gibraltar')),
    ('GR', 'GRC', '300', _('Greece')),
    ('GL', 'GRL', '304', _('Greenland')),
    ('GD', 'GRD', '308', _('Grenada')),
    ('GP', 'GLP', '312', _('Guadeloupe')),
    ('GU', 'GUM', '316', _('Guam')),
    ('GT', 'GTM', '320', _('Guatemala')),
    ('GG', 'GGY', '831', _('Guernsey')),
    ('GN', 'GIN', '324', _('Guinea')),
    ('GW', 'GNB', '624', _('Guinea-Bissau')),
    ('GY', 'GUY', '328', _('Guyana')),
    ('HT', 'HTI', '332', _('Haiti')),
    ('HM', 'HMD', '334', _('Heard Island and McDonald Islands')),
    ('VA', 'VAT', '336', _('Vatican City Holy See')),
    ('HN', 'HND', '340', _('Honduras')),
    ('HK', 'HKG', '344', _('Hong Kong')),
    ('HU', 'HUN', '348', _('Hungary')),
    ('IS', 'ISL', '352', _('Iceland')),
    ('IN', 'IND', '356', _('India')),
    ('ID', 'IDN', '360', _('Indonesia')),
    ('IR', 'IRN', '364', _('Iran')),
    ('IQ', 'IRQ', '368', _('Iraq')),
    ('IE', 'IRL', '372', _('Ireland')),
    ('IM', 'IMN', '833', _('Isle of Man')),
    ('IL', 'ISR', '376', _('Israel')),
    ('IT', 'ITA', '380', _('Italy')),
    ('JM', 'JAM', '388', _('Jamaica')),
    ('JP', 'JPN', '392', _('Japan')),
    ('JE', 'JEY', '832', _('Jersey')),
    ('JO', 'JOR', '400', _('Jordan')),
    ('KZ', 'KAZ', '398', _('Kazakhstan')),
    ('KE', 'KEN', '404', _('Kenya')),
    ('KI', 'KIR', '296', _('Kiribati')),
    ('KP', 'PRK', '408', _('North Korea')),
    ('KR', 'KOR', '410', _('South Korea')),
    ('KW', 'KWT', '414', _('Kuwait')),
    ('KG', 'KGZ', '417', _('Kyrgyzstan')),
    ('LA', 'LAO', '418', _('Laos Lao')),
    ('LV', 'LVA', '428', _('Latvia')),
    ('LB', 'LBN', '422', _('Lebanon')),
    ('LS', 'LSO', '426', _('Lesotho')),
    ('LR', 'LBR', '430', _('Liberia')),
    ('LY', 'LBY', '434', _('Libya Libyan Arab Jamahiriya')),
    ('LI', 'LIE', '438', _('Liechtenstein')),
    ('LT', 'LTU', '440', _('Lithuania')),
    ('LU', 'LUX', '442', _('Luxembourg')),
    ('MO', 'MAC', '446', _('Macau Macao')),
    ('MK', 'MKD', '807', _('Macedonia')),
    ('MG', 'MDG', '450', _('Madagascar')),
    ('MW', 'MWI', '454', _('Malawi')),
    ('MY', 'MYS', '458', _('Malaysia')),
    ('MV', 'MDV', '462', _('Maldives')),
    ('ML', 'MLI', '466', _('Mali')),
    ('MT', 'MLT', '470', _('Malta')),
    ('MH', 'MHL', '584', _('Marshall Islands')),
    ('MQ', 'MTQ', '474', _('Martinique')),
    ('MR', 'MRT', '478', _('Mauritania')),
    ('MU', 'MUS', '480', _('Mauritius')),
    ('YT', 'MYT', '175', _('Mayotte')),
    ('MX', 'MEX', '484', _('Mexico')),
    ('FM', 'FSM', '583', _('Micronesia')),
    ('MD', 'MDA', '498', _('Moldova')),
    ('MC', 'MCO', '492', _('Monaco')),
    ('MN', 'MNG', '496', _('Mongolia')),
    ('ME', 'MNE', '499', _('Montenegro')),
    ('MS', 'MSR', '500', _('Montserrat')),
    ('MA', 'MAR', '504', _('Morocco')),
    ('MZ', 'MOZ', '508', _('Mozambique')),
    ('MM', 'MMR', '104', _('Myanmar')),
    ('NA', 'NAM', '516', _('Namibia')),
    ('NR', 'NRU', '520', _('Nauru')),
    ('NP', 'NPL', '524', _('Nepal')),
    ('NL', 'NLD', '528', _('Netherlands')),
    ('AN', 'ANT', '530', _('Netherlands Antilles')),
    ('NC', 'NCL', '540', _('New Caledonia')),
    ('NZ', 'NZL', '554', _('New Zealand')),
    ('NI', 'NIC', '558', _('Nicaragua')),
    ('NE', 'NER', '562', _('Niger')),
    ('NG', 'NGA', '566', _('Nigeria')),
    ('NU', 'NIU', '570', _('Niue')),
    ('NF', 'NFK', '574', _('Norfolk Island Norfolk Island')),
    ('MP', 'MNP', '580', _('Northern Mariana Islands')),
    ('NO', 'NOR', '578', _('Norway')),
    ('OM', 'OMN', '512', _('Oman')),
    ('PK', 'PAK', '586', _('Pakistan')),
    ('PW', 'PLW', '585', _('Palau')),
    ('PS', 'PSE', '275', _('Palestinian Territory')),
    ('PA', 'PAN', '591', _('Panama')),
    ('PG', 'PNG', '598', _('Papua New Guinea')),
    ('PY', 'PRY', '600', _('Paraguay')),
    ('PE', 'PER', '604', _('Peru')),
    ('PH', 'PHL', '608', _('Philippines')),
    ('PN', 'PCN', '612', _('Pitcairn Islands')),
    ('PL', 'POL', '616', _('Poland')),
    ('PT', 'PRT', '620', _('Portugal')),
    ('PR', 'PRI', '630', _('Puerto Rico')),
    ('QA', 'QAT', '634', _('Qatar')),
    ('RE', 'REU', '638', _('Reunion')),
    ('RO', 'ROU', '642', _('Romania')),
    ('RU', 'RUS', '643', _('Russia')),
    ('RW', 'RWA', '646', _('Rwanda')),
    ('SH', 'SHN', '654', _('Saint Helena')),
    ('KN', 'KNA', '659', _('Saint Kitts and Nevis')),
    ('LC', 'LCA', '662', _('Saint Lucia')),
    ('PM', 'SPM', '666', _('Saint Pierre and Miquelon')),
    ('VC', 'VCT', '670', _('Saint Vincent and the Grenadines')),
    ('WS', 'WSM', '882', _('Samoa')),
    ('SM', 'SMR', '674', _('San Marino')),
    ('ST', 'STP', '678', _('Sao Tome and Principe')),
    ('SA', 'SAU', '682', _('Saudi Arabia')),
    ('SN', 'SEN', '686', _('Senegal')),
    ('RS', 'SRB', '688', _('Serbia')),
    ('SC', 'SYC', '690', _('Seychelles')),
    ('SL', 'SLE', '694', _('Sierra Leone')),
    ('SG', 'SGP', '702', _('Singapore')),
    ('SK', 'SVK', '703', _('Slovakia')),
    ('SI', 'SVN', '705', _('Slovenia')),
    ('SB', 'SLB', '090', _('Solomon Islands')),
    ('SO', 'SOM', '706', _('Somalia')),
    ('ZA', 'ZAF', '710', _('South Africa')),
    ('GS', 'SGS', '239', _('South Georgia and the South Sandwich Islands')),
    ('ES', 'ESP', '724', _('Spain')),
    ('LK', 'LKA', '144', _('Sri Lanka')),
    ('SD', 'SDN', '736', _('Sudan')),
    ('SR', 'SUR', '740', _('Suriname')),
    ('SJ', 'SJM', '744', _('Svalbard and Jan Mayen')),
    ('SZ', 'SWZ', '748', _('Swaziland')),
    ('SE', 'SWE', '752', _('Sweden')),
    ('CH', 'CHE', '756', _('Switzerland')),
    ('SY', 'SYR', '760', _('Syria')),
    ('TW', 'TWN', '158', _('Taiwan')),
    ('TJ', 'TJK', '762', _('Tajikistan')),
    ('TZ', 'TZA', '834', _('Tanzania')),
    ('TH', 'THA', '764', _('Thailand')),
    ('TL', 'TLS', '626', _('East Timor')),
    ('TG', 'TGO', '768', _('Togo')),
    ('TK', 'TKL', '772', _('Tokelau')),
    ('TO', 'TON', '776', _('Tonga')),
    ('TT', 'TTO', '780', _('Trinidad and Tobago')),
    ('TN', 'TUN', '788', _('Tunisia')),
    ('TR', 'TUR', '792', _('Turkey')),
    ('TM', 'TKM', '795', _('Turkmenistan')),
    ('TC', 'TCA', '796', _('Turks and Caicos Islands')),
    ('TV', 'TUV', '798', _('Tuvalu')),
    ('UG', 'UGA', '800', _('Uganda')),
    ('UA', 'UKR', '804', _('Ukraine')),
    ('AE', 'ARE', '784', _('United Arab Emirates')),
    ('GB', 'GBR', '826', _('United Kingdom')),
    ('US', 'USA', '840', _('United States')),
    ('UM', 'UMI', '581', _('United States Minor Outlying Islands')),
    ('UY', 'URY', '858', _('Uruguay')),
    ('UZ', 'UZB', '860', _('Uzbekistan')),
    ('VU', 'VUT', '548', _('Vanuatu')),
    ('VE', 'VEN', '862', _('Venezuela')),
    ('VN', 'VNM', '704', _('Vietnam Viet Nam')),
    ('VG', 'VGB', '092', _('British Virgin Islands')),
    ('VI', 'VIR', '850', _('United States Virgin Islands')),
    ('WF', 'WLF', '876', _('Wallis and Futuna')),
    ('EH', 'ESH', '732', _('Western Sahara')),
    ('YE', 'YEM', '887', _('Yemen')),
    ('ZM', 'ZMB', '894', _('Zambia')),
    ('ZW', 'ZWE', '716', _('Zimbabwe')),
)
