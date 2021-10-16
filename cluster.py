# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 10:38:06 2021

@author: Kurniawan
"""
from data import classData
import random
import numpy as np

class classCluster:
    __ObjData=classData()
    __cluster=[]
    __clusterLeft=[]
    __core=[]
    __coreLeft=[]
    __border=[]
    
    def __init__(self):
        self.__coreLeft.append(15)
        self.initClustLeft()
        print(self.__clusterLeft)
        self.getBorder(7,2)
        print(self.__border)
        print(self.__cekCoreLeft(7))
        print(self.nextCore(7))
        # idxCore=self.__getCoreRandom()
        # print(idxCore+1)
        # self.findCore(2, 3)
    
    def initClustLeft(self):
        n=self.__ObjData.getSizeData()
        cluster=[]
        for i in range(n):
            cluster.append(i+1)
        self.__clusterLeft=cluster

    def setCorePoints(self,idxCorePoint):
        self.__coreIdx.append(idxCorePoint)
    
    def joinCluster(self,idxPoints):
        self.__cluster.append(idxPoints)
    
    def initClusIndex(self,data):
        bar=len(data)
        for i in range(bar):
            cluster=[]
            cluster.append(i+1)
            self.__clusterLeft.append(cluster)
    
    def __getCoreRandom(self):
        return random.choice(self.__clusterLeft)-1
    
    def findCore(self,eps,MinPts):
        idxCore=self.__getCoreRandom()
        cek=self.__cekCore(idxCore,eps,MinPts)
        print(cek)
        if cek==True:
            self.__clusterCore.append(idxCore)
        else:
            self.findCore(eps, MinPts)
        
    def __cekCore(self,idxCore,eps,MinPts):
        cek=self.__ObjData.cekCore(idxCore,eps,MinPts)
        return cek
    
    def getBorder(self,idxCore,eps):
        self.__border=self.__ObjData.getNewCluster(idxCore,eps)
    
    def __sortCoreBorder(self,idx):
        distBorder=self.__ObjData.getCore(idx,self.__border)
        temp=np.array(distBorder)
        sort_idx=np.argsort(temp)
        sort=sort_idx[::-1]
        return sort.tolist()
    
    def __cekCoreLeft(self,core):
        n=len(self.__coreLeft)
        if n==0:
            return True
        else:
            for i in range (n):
                if core==self.__coreLeft[i]:
                    return False
                else:
                    return True
    
    def nextCore(self,idx):
        sort=self.__sortCoreBorder(idx)
        print(sort)
        n=len(sort)
        for i in range(n):
            core=self.__border[sort[i]]
            cek=self.__cekCoreLeft(core)
            if cek==True:
                return core
        return 0
    
clus=classCluster()
    