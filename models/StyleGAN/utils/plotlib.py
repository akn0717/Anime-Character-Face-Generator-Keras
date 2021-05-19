import matplotlib.pyplot as plt 
import cv2
import numpy as np

def plot_multiple_vectors(v, figsize = (15,5), title = None, xlabel = None, ylabel = None, legends = None, save_path = None, show = False):
    plt.figure(figsize = figsize)
    for vector in v:
        plt.plot(vector)
    if title!=None:
        plt.title(title)
    if xlabel != None:
        plt.xlabel(xlabel)
    if ylabel != None:
        plt.ylabel(ylabel)
    if legends!= None:
        plt.legend(legends)
    if save_path != None:
        plt.savefig(save_path)
    if show == True:
        plt.show()

def display_img(img_list, save_path = None ,show = False):
    n = len(img_list)
    for i in range(n):
        img_list[i] = cv2.cvtColor(img_list[i],cv2.COLOR_RGB2BGR)
    size = int(np.sqrt(n))
    cnt = 0
    vertical = None
    for i in range(size):
        temp = img_list[cnt]
        cnt += 1
        for _ in range(size):   
            temp = np.hstack((temp,img_list[cnt]))
            cnt += 1
        if i==0:
            vertical = temp.copy()
        else:
            vertical = np.vstack((vertical,temp.copy()))
    
    if show==True:
        cv2.imshow('Preview', vertical)
        cv2.waitKey()
    
    if save_path!=None:
        cv2.imwrite(save_path, vertical)