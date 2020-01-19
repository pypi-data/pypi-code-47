#! /usr/bin/env python3

import configparser

class WandId:

    @staticmethod
    def __code_bit_diff(code_1, code_2):
        return sum(1 for a, b in zip(code_1, code_2) if a != b)

    def best_wand_match(self, found_wand):
        """
            Accepts a found wand binary code.

            Returns a string for the best wand match.
            If no match, returns None
        """
        wands = self.find_wand_names(found_wand)
        if wands:
            return max(wands, key=wands.get)
        else:
            return None

    def find_wand_names(self, found_wand):
        """
            Accepts a found wand binary code.

            Returns a dicitonary of all defined wands within the defined
            bit tolerance
        """

        # dictionary comprehension.
        # returns
        #   - wand_name:diff_from_found
        #   - for every wand defined in the config
        #   - allows for a bit difference defined by wand_bit_tolerance
        #  
        found_wand_codes = {
            self.wands.get(x):self.__code_bit_diff(found_wand, x) 
            for x in self.wands.keys() 
            if self.__code_bit_diff(found_wand, x) <= self.wand_bit_tolerance
        }
        return found_wand_codes

    def __init__(self, config_file_path="wand_config.ini"):
        
        config = configparser.ConfigParser()
        config.read(config_file_path)

        self.wand_bit_tolerance = config.getint('TUNING', 'wand_bit_tolerance', fallback=1)

        if config.has_section('WANDS'):
            self.wands = {wcode:wname for wname, wcode in config['WANDS'].items()}
