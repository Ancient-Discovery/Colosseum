#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Description: Generate a simple .html file for demenstration 
# 			   of transformation from oracle to simplified, along with target oracle
#			  Tested under Python 3.6 on Win10.
# Author: Lin Lyu
# Credits: Yongzhen Ren & Lulu Wang
# Date created: 2018-05-20

import os

INDEX_PATH = "j2s.html"
INPUT_PATH = ".\j2s\TestA\\"
OUTPUT_PATH = ".\j2s\\ApredictionB_dis\\"
TARGET_PATH= ".\j2s\Character_Dataset\\"
# LIST_PATH = "list.txt"

def generate_index_file(index_path):
	if os.path.exists(index_path):
		index = open(index_path, "a")
	else:
		with open(index_path, "w") as fp:
			# fp.write("<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"utf-8\">")
			# Header.
			fp.write("<html><body><table><tr>")
			fp.write("<th>	name	</th><th>	input	</th><th>	output   </th><th>   target 1	</th><th>	target 2	</th><th>	target 3	</th><th>	target 4	</th><th>	target 5	</th></tr>")
			for img_name in os.listdir(OUTPUT_PATH):
				#img_name out put
				character_split=img_name.split('.')
				character=character_split[0]
				split=img_name.split('_')
				input_img_name=split[0]+"_"+split[1]+".jpg"
				target_img_name=split[0]+".jpg"

				# if len(target_list) >0:
				fp.write("<tr>")
				fp.write("<td>%s</td>" % character[0])
				fp.write("<td><img src='"+INPUT_PATH+"%s'></td>" % input_img_name)
				fp.write("<td><img src='"+OUTPUT_PATH+"%s'></td>" % img_name)
				# for i in range(len(target_list)):
				fp.write("<td><img src='"+TARGET_PATH+"%s'></td>" % target_img_name)
				fp.write("</tr>")

if __name__ == "__main__":
	generate_index_file(INDEX_PATH)
