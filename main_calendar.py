#!/usr/bin/env python3

# Arquivo para estudos da função de calendário do Python
# Eduardo Hernacki - 02/01/2017 e.v. - 21:15h
# Sol	12 CAP 49
# Lua	07 PIS 47
# Mercurio	01 CAP 11
# Venus	29 AQU 40
# Marte	11 PIS 03
# Jupiter	21 LIB 22
# Saturno	21 SAG 35	01 N 17
# Ascendente	23 LEO 05

import datetime

major_arcana = dict({
    0: "The Fool",
    1: "The Magus",
    2: "The High Priestess",
    3: "The Empress",
    4: "The Emperor",
    5: "The Hierophant",
    6: "The Lovers",
    7: "The Chariot",
    8: "Adjustment",
    9: "The Hermit",
    10: "Fortune",
    11: "Lust",
    12: "The Hanged Man",
    13: "Death",
    14: "Art",
    15: "The Devil",
    16: "The Tower",
    17: "The Star",
    18: "The Moon",
    19: "The Sun",
    20: "The Aeon",
    21: "The Universe"
})

# print(major_arcana)

# cycle 0, year 0, day 0 Vernal Equinox Time, assuming 12h as default
cycle_zero = datetime.datetime(1904, 3, 20, 12)


def get_current_cycle():
    d = datetime.datetime.now()
    # TODO: identificar em qual parte do ano esta
    years_since_al = (d.year - cycle_zero.year)

    # decreases year if we are before March 20
    if d.day < 20 and d.month < 3 and d.hour > 12:
        years_since_al -= 1

    # get how many times an cycle was counted
    cycle_count = years_since_al
    while cycle_count >= len(major_arcana):
        cycle_count = cycle_count / len(major_arcana)
    cycle_count = int(cycle_count)

    # get years from the current cycle
    year_count = years_since_al % len(major_arcana)

    # print(len(major_arcana))
    # print(years_since_al)
    # print(cycle_count)
    # print(year_count)

    return "Today is '%s' year from '%s' cycle" % (major_arcana[year_count], major_arcana[cycle_count])

print(get_current_cycle())
