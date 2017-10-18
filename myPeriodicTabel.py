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
            elif count == 60:
                element = Element_Promethium(moduel)
                element_list.append(element)
            elif count == 61:
                element = Element_Samarium(moduel)
                element_list.append(element)
            elif count == 62:
                element = Element_Europium(moduel)
                element_list.append(element)
            elif count == 63:
                element = Element_Gadolinium(moduel)
                element_list.append(element)
            elif count == 64:
                element = Element_Terbium(moduel)
                element_list.append(element)
            elif count == 65:
                element = Element_Dysprosium(moduel)
                element_list.append(element)
            elif count == 66:
                element = Element_Holmium(moduel)
                element_list.append(element)
            elif count == 67:
                element = Element_Erbium(moduel)
                element_list.append(element)
            elif count == 68:
                element = Element_Thulium(moduel)
                element_list.append(element)
            elif count == 69:
                element = Element_Ytterbium(moduel)
                element_list.append(element)
            elif count == 70:
                element = Element_Lutetium(moduel)
                element_list.append(element)
            elif count == 71:
                element = Element_Hafnium(moduel)
                element_list.append(element)
            elif count == 72:
                element = Element_Tantalum(moduel)
                element_list.append(element)
            elif count == 73:
                element = Element_Tungsten(moduel)
                element_list.append(element)
            elif count == 74:
                element = Element_Rhenium(moduel)
                element_list.append(element)
            elif count == 75:
                element = Element_Osmium(moduel)
                element_list.append(element)
            elif count == 76:
                element = Element_Iridium(moduel)
                element_list.append(element)
            elif count == 77:
                element = Element_Platinum(moduel)
                element_list.append(element)
            elif count == 78:
                element = Element_Gold(moduel)
                element_list.append(element)
            elif count == 79:
                element = Element_Mercury(moduel)
                element_list.append(element)
            elif count == 80:
                element = Element_Thallium(moduel)
                element_list.append(element)
            elif count == 81:
                element = Element_Lead(moduel)
                element_list.append(element)
            elif count == 82:
                element = Element_Bismuth(moduel)
                element_list.append(element)
            elif count == 83:
                element = Element_Polonium(moduel)
                element_list.append(element)
            elif count == 84:
                element = Element_Astatine(moduel)
                element_list.append(element)
            elif count == 85:
                element = Element_Radon(moduel)
                element_list.append(element)
            elif count == 86:
                element = Element_Francium(moduel)
                element_list.append(element)
            elif count == 87:
                element = Element_Radium(moduel)
                element_list.append(element)
            elif count == 88:
                element = Element_Actinium(moduel)
                element_list.append(element)
            elif count == 89:
                element = Element_Thorium(moduel)
                element_list.append(element)
            elif count == 90:
                element = Element_Protactinium(moduel)
                element_list.append(element)
            elif count == 91:
                element = Element_Uranium(moduel)
                element_list.append(element)
            elif count == 92:
                element = Element_Neptunium(moduel)
                element_list.append(element)
            elif count == 93:
                element = Element_Plutonium(moduel)
                element_list.append(element)
            elif count == 94:
                element = Element_Americium(moduel)
                element_list.append(element)
            elif count == 95:
                element = Element_Curium(moduel)
                element_list.append(element)
            elif count == 96:
                element = Element_Berkelium(moduel)
                element_list.append(element)
            elif count == 97:
                element = Element_Californium(moduel)
                element_list.append(element)
            elif count == 98:
                element = Element_Einsteinium(moduel)
                element_list.append(element)
            elif count == 99:
                element = Element_Fermium(moduel)
                element_list.append(element)
            elif count == 100:
                element = Element_Mendelevium(moduel)
                element_list.append(element)
            elif count == 101:
                element = Element_Nobelium(moduel)
                element_list.append(element)
            elif count == 102:
                element = Element_Lawrencium(moduel)
                element_list.append(element)
            elif count == 103:
                element = Element_Rutherfordium(moduel)
                element_list.append(element)
            elif count == 104:
                element = Element_Dubnium(moduel)
                element_list.append(element)
            elif count == 105:
                element = Element_Seaborgium(moduel)
                element_list.append(element)
            elif count == 106:
                element = Element_Bohrium(moduel)
                element_list.append(element)
            elif count == 107:
                element = Element_Hassium(moduel)
                element_list.append(element)
            elif count == 108:
                element = Element_Metinerium(moduel)
                element_list.append(element)
            elif count == 109:
                element = Element_Darmstadtium(moduel)
                element_list.append(element)
            elif count == 110:
                element = Element_Roentgenium(moduel)
                element_list.append(element)
            elif count == 111:
                element = Element_Copernicium(moduel)
                element_list.append(element)
            elif count == 112:
                element = Element_Nihonium(moduel)
                element_list.append(element)
            elif count == 113:
                element = Element_Flerovium(moduel)
                element_list.append(element)
            elif count == 114:
                element = Element_Moscovium(moduel)
                element_list.append(element)
            elif count == 115:
                element = Element_Livermorium(moduel)
                element_list.append(element)
            elif count == 116:
                element = Element_Tennessine(moduel)
                element_list.append(element)
            elif count == 117:
                element = Element_Oganesson(moduel)
                element_list.append(element)
        data = {"elements": element_list}
        with open("PeriodicTabel.json", 'w') as f:
            json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)


if __name__ == "__main__":
    element = get_en_periodic_table()
    print "add element successfully"
