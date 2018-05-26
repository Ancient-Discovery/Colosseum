import os

INDEX_PATH = "oracle_classification.html"
file_dir="cnn_prediction.txt" 
INPUT_PATH=".\j2b\Oracle\\"

def generate_index_file(index_path):
	f=open(file_dir,"r",encoding='utf-8')
	count=0
	with open(index_path, "w") as fp:
		fp.write("<html><body><table><tr>")
		fp.write("<th>Oracle Images</th><th>Prediction</th><th>Target</th></tr>")
					
	while 1:
		content=f.readline()
		count=count+1	
		useful=content.split(" ")
		use=useful[0].split(".")
		if(len(use)==2):
			image_name=use[0]+".jpg"		
			prediction=use[1][3]
			with open(index_path, "a") as fp:
				fp.write("<tr>")
				# print(image_name)
				fp.write("<td><img src='"+INPUT_PATH+"%s'></td>" % image_name)
				fp.write("<td>%s</td>" % prediction)		
				fp.write("<td>%s</td>" % image_name[0])					
				fp.write("</tr>")
		else:
			break


if __name__ == "__main__":
	generate_index_file(INDEX_PATH)


