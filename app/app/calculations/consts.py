#!/usr/bin/env python
# encoding: utf-8

import collections

mm = 1.0e-3         # 0.001
cm = 1.0e-2
m = 1.0
mm2 = 1.0e-6        # 0.000001
cm2 = 1.0e-4
kN = kNm = 1.0e3    # rowniez jako kN/m
MPa = 1.0e6         # 1000000
GPa = 1.0e9

# -----------------------------------------
# MATERIAL
c_tab = collections.OrderedDict([
    ('C12/15', 12), ('C16/20', 16), ('C20/25', 20), ('C25/30', 25),
    ('C30/37', 30), ('C35/45', 35), ('C40/50', 40), ('C45/55', 45),
    ('C50/60', 50), ('C55/67', 55), ('C60/75', 60), ('C70/85', 70),
    ('C80/95', 80), ('C90/105', 90)
])

s_tab = collections.OrderedDict([
    ('35G2Y', 410), ('34GS', 410), ('RB400', 400), ('RB400W', 400),
    ('20G2VY-b', 490), ('RB500', 500), ('RB500W', 500), ('B500SP', 500),
    ('BSt420', 420), ('BSt500', 500)
])

# GEOMETRY
diameter_sw = (6, 8, 10, 12)    # LZ: dla odmiany uzylem tuple, listy niezmienne
supports = ('słup wewnętrzny', 'słup krawędziowy X', 'słup krawędziowy Y',
            'słup narożny', 'ściana-naroże', 'ściana-koniec')

sections = ('prostokątny', 'kołowy')


design_situations = ('trwała', 'przejściowa', 'wyjątkowa')

# TODO(LZ): dodac przekroje, typy podpor itp.
