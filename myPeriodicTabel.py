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
            elif count == 30:
                element = Element_Gallium(moduel)
                element_list.append(element)
            elif count == 31:
                element = Element_Germanium(moduel)
                element_list.append(element)
            elif count == 32:
                element = Element_Arsenic(moduel)
                element_list.append(element)
            elif count == 33:
                element = Element_Selenium(moduel)
                element_list.append(element)
            elif count == 34:
                element = Element_Bromine(moduel)
                element_list.append(element)
            elif count == 35:
                element = Element_Krypton(moduel)
                element_list.append(element)
            elif count == 36:
                element = Element_Rubidium(moduel)
                element_list.append(element)
            elif count == 37:
                element = Element_Strontium(moduel)
                element_list.append(element)
            elif count == 38:
                element = Element_Yttrium(moduel)
                element_list.append(element)
            elif count == 39:
                element = Element_Zirconium(moduel)
                element_list.append(element)
            elif count == 40:
                element = Element_Niobium(moduel)
                element_list.append(element)
            elif count == 41:
                element = Element_Molybdeum(moduel)
                element_list.append(element)
            elif count == 42:
                element = Element_Technetium(moduel)
                element_list.append(element)
            elif count == 43:
                element = Element_Ruthenium(moduel)
                element_list.append(element)
            elif count == 44:
                element = Element_Rhodium(moduel)
                element_list.append(element)
            elif count == 45:
                element = Element_Palladium(moduel)
                element_list.append(element)
            elif count == 46:
                element = Element_Silver(moduel)
                element_list.append(element)
            elif count == 47:
                element = Element_Cadmium(moduel)
                element_list.append(element)
            elif count == 48:
                element = Element_Indium(moduel)
                element_list.append(element)
            elif count == 49:
                element = Element_Tin(moduel)
                element_list.append(element)
            elif count == 50:
                element = Element_Antimony(moduel)
                element_list.append(element)
            elif count == 51:
                element = Element_Tellurium(moduel)
                element_list.append(element)
            elif count == 52:
                element = Element_Iodine(moduel)
                element_list.append(element)
            elif count == 53:
                element = Element_Xenon(moduel)
                element_list.append(element)
            elif count == 54:
                element = Element_Cesium(moduel)
                element_list.append(element)
            elif count == 55:
                element = Element_Barium(moduel)
                element_list.append(element)
            elif count == 56:
                element = Element_Lanthanum(moduel)
                element_list.append(element)
            elif count == 57:
                element = Element_Cerium(moduel)
                element_list.append(element)
            elif count == 58:
                element = Element_Praseodymium(moduel)
                element_list.append(element)
            elif count == 59:
                element = Element_Neodymium(moduel)
                element_list.append(element)
        data = {"elements": element_list}
        with open("PeriodicTabel.json", 'w') as f:
            json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)


if __name__ == "__main__":
    element = get_en_periodic_table()
    print "add element successfully"
