#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Description: Generate a simple .html file for demenstration 
# 			   of transformation from bronze to oracle, along with target oracle
#			  Tested under Python 3.6 on Win10.
# Author: Lin Lyu
# Credits: Yongzhen Ren & Lulu Wang
# Date created: 2018-05-20

import os

INDEX_PATH = "b2j.html"
INPUT_PATH = ".\j2b\\bronze_input\\"
OUTPUT_PATH=".\j2b\\bronze2oracle\\"
TARGET_PATH= ".\j2b\\Oracle\\"
# LIST_PATH = "list.txt"

def generate_index_file(index_path):
	if os.path.exists(index_path):
		index = open(index_path, "a")
	else:
		with open(index_path, "w") as fp:
			fp.write("<html><body><table><tr>")
			fp.write("<th>	name	</th><th>	input	</th><th>	output   </th><th>   target 1	</th><th>	target 2	</th><th>	target 3	</th><th>	target 4	</th><th>	target 5	</th></tr>")
			for img_name in os.listdir(INPUT_PATH):
				character_split=img_name.split('.')
				character=character_split[0]
				fake_img_name=character+"_fake.gif"
				target_list=[]

				for img_target in os.listdir(TARGET_PATH):
					if img_name[0] in img_target and len(target_list)<5:
						target_list.append(img_target)

				if len(target_list) >0:
					fp.write("<tr>")
					fp.write("<td>%s</td>" % character)
					fp.write("<td><img src='"+INPUT_PATH+"%s'></td>" % img_name)
					fp.write("<td><img src='"+OUTPUT_PATH+"%s'></td>" % fake_img_name)
					for i in range(len(target_list)):
						fp.write("<td><img src='"+TARGET_PATH+"%s'></td>" % target_list[i])
					fp.write("</tr>")

if __name__ == "__main__":
	generate_index_file(INDEX_PATH)
