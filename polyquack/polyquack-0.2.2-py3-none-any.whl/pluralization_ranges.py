"""
This module defines pluralization ranges for certain languages. For instance, Scottish Gaelic has one form
for numbers in the ranges (3..10, 13..19).
"""

rule_4_range_2 = list(range(3, 11)) + list(range(13, 20))

rule_5_range_1 = list(range(1, 20))

rule_6_range_1 = list(range(11, 20))

rule_11_range_2 = list(range(3, 7))
rule_11_range_3 = list(range(7, 11))

rule_12_range_2 = list(range(3, 11))

rule_13_range_1 = list(range(1, 11))
rule_13_range_2 = list(range(11, 20))

rule_16_exclude_range_2 = [13, 14, 19, 73, 74, 79, 93, 94, 99]
