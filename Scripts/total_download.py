# -*- coding: UTF-8 -*-
import requests
import re

# 编码转换
import sys
import importlib
importlib.reload(sys)

import urllib
import os


def download_pic(textUTF, filePath, string, type_pic):

	url = 'http://hanziyuan.net/etymology'

	header = {
		'Host': "hanziyuan.net",
		'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
		'Accept': "text/html, */*; q=0.01",
		'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
		'Accept-Encoding': "gzip, deflate",
		'Referer': "http://hanziyuan.net/?chinese=%E8%BD%A6",
		'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
		'Seal': "CfDJ8Mzn9iLt2QFKnxf77lKUUCAjvJ5oaqDUdtwgPcQEeHZX73io7TN5ckKttTvjQC0mcqhRTOi6mMTX-UvEdVxizg00qqzsmAThD-OXd4xcg1aEB9KmgV6rI94q5K-bW1ZkQXKnOCVlwQ2udjqvC1VMcec",
		'X-Requested-With': "XMLHttpRequest",
		'Content-Length': "180",
		'Cookie': "Hm_lvt_44bf35035989ecd905587eb98a45525e=1520252611,1520334486,1520339472,1520398892; _ga=GA1.2.1041153465.1520252043; _gid=GA1.2.693634523.1520252043; Oracle=CfDJ8Mzn9iLt2QFKnxf77lKUUCC9fXHu76g6bbXHSg5Lvfw3uc1UmzE3MA9-xlm2hKDxHPLAXxSohe_AeU-3c2DZxG1q3UQFDsMDb_OF0zbOuLD2dn6ET-QHPl8cVgI7UfNATDBmYT-jLzge7pf1szaUSNI; Bronze=CfDJ8Mzn9iLt2QFKnxf77lKUUCAjvJ5oaqDUdtwgPcQEeHZX73io7TN5ckKttTvjQC0mcqhRTOi6mMTX-UvEdVxizg00qqzsmAThD-OXd4xcg1aEB9KmgV6rI94q5K-bW1ZkQXKnOCVlwQ2udjqvC1VMcec; ARRAffinity=a3d1506eba3de0cebafee0ce75940bafa7ccabdaed8217d0f54b27b46990a5c1; Hm_lpvt_44bf35035989ecd905587eb98a45525e=1520399050",
		'Connection': "keep-alive"
	}

	d = "chinese="+textUTF+"&Bronze=CfDJ8Mzn9iLt2QFKnxf77lKUUCAjvJ5oaqDUdtwgPcQEeHZX73io7TN5ckKttTvjQC0mcqhRTOi6mMTX-UvEdVxizg00qqzsmAThD-OXd4xcg1aEB9KmgV6rI94q5K-bW1ZkQXKnOCVlwQ2udjqvC1VMcec"
	html = requests.post(url, data = d, headers = header)

	#仅有当前页面存放URL的部分
#	part_html = re.findall('<style type="text/css">(.*?)</style>', html.text)
	#part_html = re.findall('(.*?)', html)

#	print(part_html)

	# 包含甲骨文代码和URL
	#title = re.findall('.etymology-(.*?) }', part_html[0])
	title = re.findall('.etymology-(.*?) }', html.text)
	#print(title)

	#循环读取得到甲骨文编码和URL
	#保存图片到本地
	for Value in title:
		imageNUM = Value.split("{")[0]
		imageURL = re.sub("['()]", "", Value.split("{ background-image: url")[1])
		#print(imageNUM)
		#print(imageURL)

		#实现保存到本地
		file_path = filePath+string
		if not os.path.exists(file_path):
			print('文件夹'+file_path+'不存在')
			os.makedirs(file_path)
		file_suffix = os.path.splitext(imageURL)[1]
		imageName = imageNUM+type_pic
		filename = '{}{}{}{}'.format(file_path, os.sep, imageName, file_suffix)
		urllib.request.urlretrieve(imageURL, filename = filename)


filePath = "D:/a_total/" #硬盘地址
type_pic = ".gif"


url = 'http://hanziyuan.net/etymology'
available_word_file="D:\python_64\characters_with_oracle_new.txt"


header = {
	'Host': "hanziyuan.net",
	'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0",
	'Accept': "text/html, */*; q=0.01",
	'Accept-Language': "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
	'Accept-Encoding': "gzip, deflate",
	'Referer': "http://hanziyuan.net/?chinese=%E8%BD%A6",
	'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8",
	'Seal': "CfDJ8Mzn9iLt2QFKnxf77lKUUCAjvJ5oaqDUdtwgPcQEeHZX73io7TN5ckKttTvjQC0mcqhRTOi6mMTX-UvEdVxizg00qqzsmAThD-OXd4xcg1aEB9KmgV6rI94q5K-bW1ZkQXKnOCVlwQ2udjqvC1VMcec",
	'X-Requested-With': "XMLHttpRequest",
	'Content-Length': "180",
	'Cookie': "Hm_lvt_44bf35035989ecd905587eb98a45525e=1520252611,1520334486,1520339472,1520398892; _ga=GA1.2.1041153465.1520252043; _gid=GA1.2.693634523.1520252043; Oracle=CfDJ8Mzn9iLt2QFKnxf77lKUUCC9fXHu76g6bbXHSg5Lvfw3uc1UmzE3MA9-xlm2hKDxHPLAXxSohe_AeU-3c2DZxG1q3UQFDsMDb_OF0zbOuLD2dn6ET-QHPl8cVgI7UfNATDBmYT-jLzge7pf1szaUSNI; Bronze=CfDJ8Mzn9iLt2QFKnxf77lKUUCAjvJ5oaqDUdtwgPcQEeHZX73io7TN5ckKttTvjQC0mcqhRTOi6mMTX-UvEdVxizg00qqzsmAThD-OXd4xcg1aEB9KmgV6rI94q5K-bW1ZkQXKnOCVlwQ2udjqvC1VMcec; ARRAffinity=a3d1506eba3de0cebafee0ce75940bafa7ccabdaed8217d0f54b27b46990a5c1; Hm_lpvt_44bf35035989ecd905587eb98a45525e=1520399050",
	'Connection': "keep-alive"
}

f=open('CJK_Unified_Characters.txt','r', encoding='UTF-8')
text=f.read()
text=re.sub('[0123456789 ]','',text)
list=text.split()

num=0
for i in range(1,len(list)):
	temp=list[i].encode('utf-8')
	textUTF=""
	# print(temp)
	for n in range(0,len(temp)):
		transString=str(hex(temp[n]))
		transString=re.sub('[0][x]','',transString)
		textUTF=textUTF+"%"+transString
		#print(textUTF)
	# print(textUTF)
	d = "chinese="+textUTF+"&Bronze=CfDJ8Mzn9iLt2QFKnxf77lKUUCAjvJ5oaqDUdtwgPcQEeHZX73io7TN5ckKttTvjQC0mcqhRTOi6mMTX-UvEdVxizg00qqzsmAThD-OXd4xcg1aEB9KmgV6rI94q5K-bW1ZkQXKnOCVlwQ2udjqvC1VMcec"
	html = requests.post(url, data = d, headers = header)
	#print(html.text)
	html.encoding='utf-8'
	print(num)
	string = bytes.decode(temp)
	print(string)

	if ".etymology-J" in html.text:
		with open(available_word_file,"a") as f:
			f.write(list[i])
			f.write('\n')
		download_pic(textUTF, filePath, string, type_pic)

	num = num+1