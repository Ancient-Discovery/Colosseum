'''
              _____                      _    __          __                         
     /\      / ____|                    | |   \ \        / /                         
    /  \    | (___  _ __ ___   __ _ _ __| |_   \ \  /\  / /__  _ __ ___   __ _ _ __  
   / /\ \    \___ \| '_ ` _ \ / _` | '__| __|   \ \/  \/ / _ \| '_ ` _ \ / _` | '_ \ 
  / ____ \   ____) | | | | | | (_| | |  | |_     \  /\  / (_) | | | | | | (_| | | | |
 /_/    \_\ |_____/|_| |_| |_|\__,_|_|   \__|     \/  \/ \___/|_| |_| |_|\__,_|_| |_|

 ___        ,__
  |_|`_'   _ |_|
  |_||_|  |_||_|
 _|_| ,,  |_|| |
    ||\_|   / `|   

This script can draw the trend for each ancient character, and the character order is based on their image numbers.
You can change the location of the images dataset to run the program.
The images in the program should not be divided into any sub-folders.                                                 
'''

# 绘制每一种文字图片数量柱状图的代码
import numpy as np    
import matplotlib.mlab as mlab    
import matplotlib.pyplot as plt 
import os
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib as mpl


file_name_of_all_words_with_pic="all_words.txt"
word_list=[]
pic_name_list=[]
pic_J_count={}
pic_B_count={}
pic_L_count={}
pic_S_count={}

file_dir="G:\Final_Project\Divided_Data_100X100\Ancient_Chinese_Character_Dataset"   
for root, dirs, pictures in os.walk(file_dir):  
	for picture in pictures:
		if picture[0] not in pic_name_list:
			pic_name_list.append(picture[0])
			pic_J_count[picture[0]]=0
			pic_B_count[picture[0]]=0
			pic_L_count[picture[0]]=0
			pic_S_count[picture[0]]=0

		if "j" in picture or "J" in picture:
			pic_J_count[picture[0]]=pic_J_count[picture[0]]+1
		elif "b" in picture or "B" in picture:
			pic_B_count[picture[0]]=pic_B_count[picture[0]]+1
		elif "L" in picture or "l" in picture:
			pic_L_count[picture[0]]=pic_L_count[picture[0]]+1
		elif "s" in picture or "S" in picture:
			pic_S_count[picture[0]]=pic_S_count[picture[0]]+1 

x=[]
y=[]
# with open(file_name_of_all_words_with_pic,"w",encoding='utf-8') as file:
# 	for index in range(0,len(pic_name_list)):
# 	# print()
# 		x.append(pic_name_list[index].encode('utf-8'))
# 		y.append(pic_J_count[pic_name_list[index]])
# 		file.write(pic_name_list[index]+" "+str(pic_J_count[pic_name_list[index]])+" "+str(pic_B_count[pic_name_list[index]])+" "+str(pic_S_count[pic_name_list[index]])+" "+str(pic_L_count[pic_name_list[index]]))
# 		file.write('\n')

# print(pic_name_list)
# print(len(pic_name_list)) 10782
c=0
oracle_count=sorted(pic_J_count.items(),key=lambda d: d[1],reverse=True)
print(len(pic_name_list))
for num in range(0,len(pic_name_list)):
	if oracle_count[num][1]<1:
		break;
	x.append(oracle_count[num][0])
	y.append(oracle_count[num][1])
	c=c+oracle_count[num][1]
	# if oracle_count[num][1]>20:
	# 	print(oracle_count[num][0]+str(oracle_count[num][1])+"\n")
print(x[0]+str(y[0]))
print("总字数"+str(c))
print("字数"+str(len(x)))

x10=[]
y10=[]
c=0
oracle_count=sorted(pic_J_count.items(),key=lambda d: d[1],reverse=True)
# print(len(pic_name_list))
for num in range(0,len(pic_name_list)):
	if oracle_count[num][1]<10:
		break;
	x10.append(oracle_count[num][0])
	y10.append(oracle_count[num][1])
	c=c+oracle_count[num][1]
	# if oracle_count[num][1]>20:
	# 	print(oracle_count[num][0]+str(oracle_count[num][1])+"\n")
print(10)
print(len(x10))

x20=[]
y20=[]
c=0
oracle_count=sorted(pic_J_count.items(),key=lambda d: d[1],reverse=True)
# print(len(pic_name_list))
for num in range(0,len(pic_name_list)):
	if oracle_count[num][1]<20:
		break;
	x20.append(oracle_count[num][0])
	y20.append(oracle_count[num][1])
	c=c+oracle_count[num][1]
	# if oracle_count[num][1]>20:
	# 	print(oracle_count[num][0]+str(oracle_count[num][1])+"\n")
print(20)
print(len(x20))



custom_font = mpl.font_manager.FontProperties(fname=r'E:\Programs\Python\Python36\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\Vera.ttf')

width = 0.4 
ind = np.linspace(1,50,len(x))  
# make a figure  
fig = plt.figure()  
ax  = fig.add_subplot(1,1,1)  
# Bar Plot  
ax.bar(ind,y,width,color='blue')  
# Set the ticks on x-axis  
ax.set_xticks(ind)  
ax.set_xticklabels(x,fontproperties=custom_font)  
# labels  
ax.set_xlabel('Character')  
ax.set_ylabel('Count')  
# title  
ax.set_title('Seal Character Count', bbox={'facecolor':'0.8', 'pad':5})  
# plt.grid(True)  
plt.show()  
# for value_x,value_y in zip(x,y):
# 	plt.text(value_x,value_y)
plt.savefig("bar.jpg")  
plt.close()

# 总字数 10782
# r:甲骨文 27143 1123字  最多 方：291
# 	金文   23364 2048字  最多 宝：273
# 说文篆字 10641 10184字 最多 难：5
# 六书通   34511 5531字  最多 寿：140
# w:24673甲骨文 964汉字 23035

# 总字数 10614 总图片 88166
# r:甲骨文 24056 954字  最多 方：291    >20 296  >10 429
# 	金文   21363 1933字  最多 宝：273   >20 289  >10 505
# 说文篆字 10475 10033字 最多 难：5         
# 六书通   32272 5531字  最多 寿：140  313		933

# Oracle	  24144	   971	方	291	 298	429
# Bronze	  26528	  1943	显	482	 299	516
# Seal	      29517	  10023	亦	1887  12	12
# Liushutong  32134	  5379	寿	140	 312	932
# Total	112323	10622				