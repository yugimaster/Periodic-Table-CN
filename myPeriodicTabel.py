#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    Periodic Table with Chinese
'''
import json
from elements import *


def get_en_periodic_table():
    with open('PeriodicTableJSON.json') as f:
        json_data = json.load(f)
        element_list = []
        for (count, moduel) in enumerate(json_data['elements']):
            if count == 0:
                element = Element_Hydrogen(moduel)
                element_list.append(element)
            elif count == 1:
                element = Element_Helium(moduel)
                element_list.append(element)
            elif count == 2:
                element = Element_Lithium(moduel)
                element_list.append(element)
            elif count == 3:
                element = Element_Beryllium(moduel)
                element_list.append(element)
            elif count == 4:
                element = Element_Boron(moduel)
                element_list.append(element)
            elif count == 5:
                element = Element_Carbon(moduel)
                element_list.append(element)
            elif count == 6:
                element = Element_Nitrogen(moduel)
                element_list.append(element)
            elif count == 7:
                element = Element_Oxygen(moduel)
                element_list.append(element)
            elif count == 8:
                element = Element_Fluorine(moduel)
                element_list.append(element)
            elif count == 9:
                element = Element_Neon(moduel)
                element_list.append(element)
            elif count == 10:
                element = Element_Sodium(moduel)
                element_list.append(element)
            elif count == 11:
                element = Element_Magnesium(moduel)
                element_list.append(element)
            elif count == 12:
                element = Element_Aluminium(moduel)
                element_list.append(element)
            elif count == 13:
                element = Element_Silicon(moduel)
                element_list.append(element)
            elif count == 14:
                element = Element_Phosphorus(moduel)
                element_list.append(element)
            elif count == 15:
                element = Element_Sulfur(moduel)
                element_list.append(element)
            elif count == 16:
                element = Element_Chlorine(moduel)
                element_list.append(element)
            elif count == 17:
                element = Element_Argon(moduel)
                element_list.append(element)
            elif count == 18:
                element = Element_Potassium(moduel)
                element_list.append(element)
            elif count == 19:
                element = Element_Calcium(moduel)
                element_list.append(element)
            elif count == 20:
                element = Element_Scandium(moduel)
                element_list.append(element)
            elif count == 21:
                element = Element_Titanium(moduel)
                element_list.append(element)
            elif count == 22:
                element = Element_Vanadium(moduel)
                element_list.append(element)
            elif count == 23:
                element = Element_Chromium(moduel)
                element_list.append(element)
            elif count == 24:
                element = Element_Manganese(moduel)
                element_list.append(element)
            elif count == 25:
                element = Element_Iron(moduel)
                element_list.append(element)
            elif count == 26:
                element = Element_Cobalt(moduel)
                element_list.append(element)
            elif count == 27:
                element = Element_Nickel(moduel)
                element_list.append(element)
            elif count == 28:
                element = Element_Copper(moduel)
                element_list.append(element)
            elif count == 29:
                element = Element_Zinc(moduel)
                element_list.append(element)
        data = {"elements": element_list}
        with open("PeriodicTabel.json", 'w') as f:
            json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)


if __name__ == "__main__":
    element = get_en_periodic_table()
    print "add element successfully"
