# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 10:13:45 2021

@author: Kurniawan
"""

import pandas as panda
import math

class classData:
    __data=[]
    __tempCluster=[]
    
    def __init__(self):
        self.__readExcel()
        # print ('dataset \n', self.__data)
        # jarak = self.getDist(14, 6)
        # print('jarak :', jarak)
        # dist=self.__calAllDist(15)
        # print("dist :",dist)
        # self.getNewCluster(7, 2)
        # print(self.__tempCluster)
        # print("core :",self.getIdxCoreNewCluster(7))
    
    def getSizeData(self):
        return len(self.__data)

    def __readExcel(self):
        file=panda.read_excel(open('dataset.xlsx','rb'))
        df=panda.DataFrame(file,columns=(['x','y']))
        dataset=df.values.tolist()
        self.__data=dataset
    
    def __distEuclidian(self,data1,data2):
        n=len(data1)
        m=len(data2)
        tot=0
        if n==m:
            for i in range(n):
                tot=tot+pow((data1[i]-data2[i]),2)
        return math.sqrt(tot)
    
    def getDist(self, idx1,idx2):
        data=self.__data
        dist=self.__distEuclidian(data[idx1], data[idx2])
        return dist
        
    def __calAllDist(self,idxCore):
        data=self.__data
        n=len(data)
        dist=[]
        for i in range(n):
            dist.append(self.__distEuclidian(
                data[i], data[idxCore-1]))
        return dist 
    
    def setPoints(self,idxPoints):
        n=len(idxPoints)
        points=[]
        for i in range(n):
            points.append(self.__data[i])
        return points
    
    def getNewCluster(self,idxCore,eps):
        dist=self.__calAllDist(idxCore)
        n=len(dist)
        idx=[]
        for i in range (n):
            if dist[i]<=eps:
                idx.append(i+1)
        return idx
    
    def getCore(self,idxCore,border):
        n=len(border)
        dist=[]
        for i in range(n):
            idx=border[i]-1
            dist.append(self.getDist(
                idxCore-1,idx))
        return dist
    
    def cekCore(self,idxCore,eps,MinPts):
        pts=self.__getPtsCore(idxCore, eps)
        if pts<MinPts:
            return False
        else:
            return True

# data = classData()
# data.cekCore(15, 2, 3)