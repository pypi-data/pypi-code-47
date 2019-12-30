# -*- coding: UTF-8 -*-
logger.info("Loading 34 objects to table b2c_account...")
# fields: id, iban, bic, account_name, owner_name, last_transaction
loader.save(create_b2c_account(1,u'AL73552891583236787384690218',u'',u'',u'Garage Mergelsberg',date(2015,9,7)))
loader.save(create_b2c_account(2,u'AL66383778998922195726400092',u'',u'',u'Reinhards Baumschule',date(2015,9,7)))
loader.save(create_b2c_account(3,u'AD5257784281812851432256',u'',u'',u'Auto \xc9cole Verte',date(2015,9,7)))
loader.save(create_b2c_account(4,u'AT233377816198914246',u'',u'',u'Evers Eberhart',date(2015,9,7)))
loader.save(create_b2c_account(5,u'AZ72AOZV21841200481951294949',u'',u'',u'Kaivers Karl',date(2015,9,7)))
loader.save(create_b2c_account(6,u'BH50GDHO00603036234521',u'',u'',u'Lazarus Line',date(2015,9,7)))
loader.save(create_b2c_account(7,u'BH29GWOZ41746150114337',u'',u'',u'Malmendier Marc',date(2015,9,7)))
loader.save(create_b2c_account(8,u'BE83540256917919',u'',u'',u'Emonts-Gast Erna',date(2015,9,7)))
loader.save(create_b2c_account(9,u'BE62315236188996',u'',u'',u'Radermacher Berta',date(2015,9,7)))
loader.save(create_b2c_account(10,u'BE94532216847099',u'',u'',u'Radermacher Fritz',date(2015,9,7)))
loader.save(create_b2c_account(11,u'BE96553733406075',u'',u'',u'Radermacher Hans',date(2015,9,7)))
loader.save(create_b2c_account(12,u'BA086304331850728340',u'',u'',u'di Rupo Didier',date(2015,9,7)))
loader.save(create_b2c_account(13,u'BR2701798507625253316527482W6',u'',u'',u'Radermecker Rik',date(2015,9,7)))
loader.save(create_b2c_account(14,u'BR8916505915221714901465542D6',u'',u'',u'Denon Denis',date(2015,9,7)))
loader.save(create_b2c_account(15,u'BG33WODO90876019575940',u'',u'',u'AS Express Post',date(2015,9,7)))
loader.save(create_b2c_account(16,u'BG89NKTJ64315412156435',u'',u'',u'IIZI kindlustusmaakler AS',date(2015,9,7)))
loader.save(create_b2c_account(17,u'BG45LMDF68752666847493',u'',u'',u'Leffin Electronics',date(2015,9,7)))
loader.save(create_b2c_account(18,u'MK42869572001783450',u'',u'',u'R-Cycle Sperrgutsortierzentrum',date(2015,9,7)))
loader.save(create_b2c_account(19,u'CY94595189933551887423183914',u'',u'',u'Brocal Catherine',date(2015,9,7)))
loader.save(create_b2c_account(20,u'CY67178463066674360903454329',u'',u'',u'Baguette St\xe9phanie',date(2015,9,7)))
loader.save(create_b2c_account(21,u'CZ9233597294072726325676',u'',u'',u'Gerkens Gerd',date(2015,9,7)))
loader.save(create_b2c_account(22,u'CZ6595671096439786778328',u'',u'',u'Oikos',date(2015,9,7)))
loader.save(create_b2c_account(23,u'DK4827862790127019',u'',u'',u'Gerkens-Kasennova',date(2015,9,7)))
loader.save(create_b2c_account(24,u'DK1358026849419971',u'',u'',u'Jean\xe9mart-Thelen',date(2015,9,7)))
loader.save(create_b2c_account(25,u'DK0905734385914385',u'',u'',u'Frisch Ludwig',date(2015,9,7)))
loader.save(create_b2c_account(26,u'DO64127641001569019111921598',u'',u'',u'Frisch Bernd',date(2015,9,7)))
loader.save(create_b2c_account(27,u'DO40144771611278919843152876',u'',u'',u'Frisch Peter',date(2015,9,8)))
loader.save(create_b2c_account(28,u'DO34894434296388176648298583',u'',u'',u'Frisch Clara',date(2015,9,7)))
loader.save(create_b2c_account(29,u'DO87947053138589917553903987',u'',u'',u'Frisch Dennis',date(2015,9,7)))
loader.save(create_b2c_account(30,u'EE436294797788261706',u'',u'',u'Frisch Melba',date(2015,9,7)))
loader.save(create_b2c_account(31,u'EE386024163501444960',u'',u'',u'Frisch-Frogemuth',date(2015,9,7)))
loader.save(create_b2c_account(32,u'KW17RZFN7035889356330572874320',u'',u'',u'Zweith Petra',date(2015,9,7)))
loader.save(create_b2c_account(33,u'MT48FZJE39412800316166455316545',u'',u'',u'Jousten Jan',date(2015,9,7)))
loader.save(create_b2c_account(34,u'MC8574374915374698884193509',u'',u'',u'Lahm Lisa',date(2015,9,8)))

loader.flush_deferred_objects()
