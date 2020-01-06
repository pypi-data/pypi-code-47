# -*- coding: UTF-8 -*-
# Copyright 2017-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""The choicelists for this plugin.

"""

from lino.api import dd, rt, _


class ProfessionalStates(dd.ChoiceList):
    # 11 Selbstständig/Freiberufler
    # 31 Arbeiter/Angestellter
    # 51 in Ausbildung
    # 54 Hausfrau/Hausmann
    # 61 arbeitslos
    # 63 berufsunfähig
    # 65 Sozialhilfeempfänger
    # 80 im Ruhestand
    # 90 andere Situation            
    # 00 unbekannt                   
    # 10 Freiberufler (alt -> 11)    
    # 20 Selbstständiger (alt -> 11) 
    # 30 Angestellter (alt -> 31)    
    # 40 Arbeiter (alt -> 31)        
    # 62 Laufbahnunterbrechung (alt)
    verbose_name = _("Professional situation")

add = ProfessionalStates.add_item
add('11', _("Independent"))
add('31', _("Employed"))
add('51', _("Student"))
add('54', _("Homemaker"))
add('61', _("Workless"))
add('63', _("Invalid"))
add('65', _("Social aid recipient"))
add('80', _("Retired"))
add('90', _("Other"))
add('00', _("Unknown"))
add('62', _("Career interruption"))




# 01 dauert an
# 03 abgeschlossen
# 05 automatisch abgeschlossen
# 06 Abbruch der Beratung
# 09 Weitervermittlung
# 12 nur Erstkontakt


# from lino_xl.lib.clients.choicelists import ClientStates
# ClientStates.default_value = 'active'
# add = ClientStates.add_item
# add('01', _("Active"), 'active')
# add('03', _("Closed"), 'closed')
# add('05', _("Sleeping"), 'sleeping')
# add('06', _("Abandoned"), 'abandoned')
# add('09', _("Delegated"), 'delegated')  # Weitervermittlung
# add('12', _("First contact"), 'newcomer')  # Erstkontakt

from lino_xl.lib.clients.choicelists import ClientStates
ClientStates.default_value = None
ClientStates.clear()
add = ClientStates.add_item
# add('01', pgettext("client state", "Active"), 'active')
add('01', _("Active"), 'active')
add('03', _("Closed"), 'closed')
add('05', _("Cancelled"), 'cancelled')  # auto_closed')
add('06', _("Abandoned"), 'abandoned')
add('09', _("Forwarded"), 'forwarded')
add('12', _("Newcomer"), 'newcomer')
# obsolete values still used on old data
# add('00', _("00"))
# add('02', _("02"))
# add('04', _("04"))
# add('08', _("08"))
# add('10', _("10"))
# add('11', _("11"))
# add('99', _("99"))

CT = ClientStates.active.add_transition(required_states="cancelled abandoned newcomer")
CT = ClientStates.closed.add_transition(required_states="cancelled active abandoned forwarded newcomer")
CT = ClientStates.forwarded.add_transition(required_states="active newcomer")


