import PIL.Image as pilimg
import numpy as np
import matplotlib.pyplot as plt
import math
im = pilimg.open('I.png')
imsi= np.array(im)
hb=1558021
hb=(hb%100)*2
th =math.radians(hb)
sin=math.sin(th)
cos=math.cos(th)
c=np.array(([0]))
x=np.array(imsi[1,:,1].shape)
y=np.array(imsi[:,1,1].shape)
w=np.array(([cos,-sin],[sin,cos]))
ps=np.array(([0,x,0,x],[0,0,y,y]))
rot=np.dot(w,ps)
rot1=np.copy(rot)
rot1[0]=rot1[0]-np.min(rot1[0])
wx=int(np.max(rot[0])-np.min(rot[0]))
wy=int(np.max(rot[1]))
win=np.zeros((wy,wx))
yyy=np.arange(wy)
xxx=np.arange(wx)
[xxx,yyy]=np.meshgrid(xxx,yyy)
py=np.arange(y)
px=np.arange(x)
ws=np.array(([cos,-sin,-np.min(rot[0])],[sin,cos,0],[0,0,1]))
[px,py]=np.meshgrid(px,py)
jeh=np.array(np.where(win==0))
pxy=np.array((px,py,1))
pxy1=np.dot(ws,pxy)
pxy2=np.dot(ws,pxy)
pxy2[0]=pxy1[0].astype(np.int32)
pxy2[1]=pxy1[1].astype(np.int32)
win[pxy2[1]-1,pxy2[0]-1]=np.array(imsi[y-pxy[1]-1,pxy[0]-1,2])
pxx=np.copy(rot1[0])
pyy=np.copy(rot1[1])
w1=(((pyy[2]-pyy[0])/(pxx[2]-pxx[0]))*(xxx-pxx[0]))+pyy[0]
w2=((pyy[2]-pyy[3])/(pxx[2]-pxx[3]))*(xxx-pxx[3])+pyy[3]
w3=((pyy[1]-pyy[3])/(pxx[1]-pxx[3]))*(xxx-pxx[3])+pyy[3]
w4=((pyy[1]-pyy[0])/(pxx[1]-pxx[0]))*(xxx-pxx[1])+pyy[1]
jeh=np.array(np.where((yyy<w3)&(yyy>w4)&(yyy<w2)&(yyy>w1)&(win==0)))
jeh=np.delete(jeh,np.where(jeh[0]==np.max(jeh[0])),axis=1)
jeh=np.delete(jeh,np.where(jeh[0]==np.min(jeh[0])),axis=1)
jeh=np.delete(jeh,np.where(jeh[1]==np.max(jeh[1])),axis=1)
jeh=np.delete(jeh,np.where(jeh[1]==np.min(jeh[1])),axis=1)
I1=(win[jeh[0],jeh[1]+1]+win[jeh[0],jeh[1]-1])/2##x에 대한 1차함수
I2=(win[jeh[0]+1,jeh[1]]+win[jeh[0]-1,jeh[1]])/2##y에 대한 1차함수
IO=np.array(((I1+I2)/2))
c=np.concatenate((c,IO))
win[jeh[0],jeh[1]]=c[1:]
plt.imshow(win,'gray',origin='lower')
plt.show()

