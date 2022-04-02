#coding:utf-8

#add your parameters｜添加参数
fx=0
fy=0
cx=0
cy=0

#the intrinsics of the fisheye camera|鱼眼摄像头内参
# xi=1.9926618269451453
# gamma1=669.8940458885896
# gamma2=669.1450614220616
# u0=377.9459252967363
# v0=279.63655686698144
# cx=u0
# cy=v0
# fx=gamma1*xi
# fy=gamma2*xi

#the 3x3 intrinsics matrix k｜3x3内参矩阵k
k=[[fx, 0.0, cx], [0.0,fy, cy], [0.0, 0.0, 1.0]]


#output to the calib.txt files｜输出到calib.txt文件
with open('intrinsics.txt','a') as file:
	for line in k:
		for l in line:
			file.write(str("{:e}".format(l)))
			file.write(" ")
		file.write("0.000000000000e+00 ")


