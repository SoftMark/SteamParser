#!/usr/bin/env python3
import unittest
import steam_market as sm

class TestTF2Items(unittest.TestCase):
    def runTest(self):
        tf2_items = [
            'Strange Professional Killstreak Minigun',
            'Vintage Gunboats',
            'Name Tag',
            'Mann Co. Supply Crate Key'
        ]

        csgo_items = [
            'Gamma Case',
            '\u2605 Karambit | Bright Water (Factory New)',
            'AK-47 | Frontside Misty (Field-Tested)'
        ]

        print('Testing TF2 Items:\n')
        for item in tf2_items:
            print(item)
            market_item = sm.get_tf2_item(item)
            print([i.price for i in market_item.listings])

        print('\nTesting CS:GO Items:\n')
        for item in csgo_items:
            print(item)
            market_item = sm.get_csgo_item(item)
            print([i.price for i in market_item.listings])


print(sm.get_item(730, "Gamma Case"))