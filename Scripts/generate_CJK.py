#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	Description: Create a text file in the same directory containing all CJK
                 unified characters (87870) except 12 ones in the block named
                 CJK Compatibility Ideographs according to Unicode 10.0.
    Author: Yongzhen Ren
	Credits: Lin Lyu & Lulu Wang
    Date created: 2018-03-06
'''

output_file = "CJK_Unified_Characters.txt"

CJK_UI = (0x4E00, 0x9FEA)
CJK_UI_EX_A = (0x3400, 0x4DB5)
CJK_UI_EX_B = (0x20000, 0x2A6D6)
CJK_UI_EX_C = (0x2A700, 0x2B734)
CJK_UI_EX_D = (0x2B740, 0x2B81D)
CJK_UI_EX_E = (0x2B820, 0x2CEA1)
CJK_UI_EX_F = (0x2CEB0, 0x2EBE0)
blocks = [CJK_UI, CJK_UI_EX_A, CJK_UI_EX_B, CJK_UI_EX_C, CJK_UI_EX_D, CJK_UI_EX_E, CJK_UI_EX_F]

if __name__ == "__main__":
	with open(output_file, 'w') as fp:
		for block in blocks:
			for code_point in range(block[0], block[1] + 1):
			# Inclusive.
				fp.write(chr(code_point) + '\n')
