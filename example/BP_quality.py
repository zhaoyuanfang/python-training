# -*- coding: UTF-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from numpy import *
from xlrd import *
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.learning_curve import learning_curve
from sklearn.cross_validation import cross_val_score
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neural_network import MLPRegressor
from mpl_toolkits.mplot3d import Axes3D
from random import *
import warnings
warnings.filterwarnings("ignore")
def loadData(fileName):
    fr=open_workbook(fileName)
    sheet=fr.sheets()[0]
    dataMat=[];lableMat=[]
    nrows=sheet.nrows
    ncols=sheet.ncols
    for i in range(nrows):
        dataMat.append(sheet.row_values(i)[0:27])
        lableMat.append(sheet.row_values(i)[27:-1])
    return mat(dataMat),mat(lableMat)

def comData(dataMat):
    numFeat =shape(dataMat)[1]
    print(dataMat[470, 2260], '\n')
    print(dataMat[471, 2260], '\n')
    print(dataMat[472, 2260], '\n')
    for i in range(numFeat):
        meanVal = mean(dataMat[nonzero(~isnan(dataMat[:,i].A))[0],i])
        dataMat[nonzero(isnan(dataMat[:,i].A))[0],i] = meanVal
    print(dataMat[470,2260],'\n')
    print(dataMat[471, 2260], '\n')
    print(dataMat[472, 2260], '\n')

class Chromosome:
    '''
    Ⱦɫ����
    ���԰������ڵ�����ѧϰ�ʡ���Ӧ��ֵ-����ʧ��������
    �����ڲ���Ⱦɫ���ʼ�������ݽڵ�����ѧϰ�ʼ�����Ӧ��ֵ
    ������������ʼ��Ⱦɫ�壬����Ⱦɫ�������Ӧ��
    '''

    def __init__(self,nodeNumber,learningRate):
        self.nodeNumber=nodeNumber
        self.learningRate=learningRate
    def getFitness(self,X,Y):
        mlp = MLPRegressor(self.nodeNumber, activation='logistic', solver='sgd', learning_rate='constant',
                           learning_rate_init=0.0001 * self.learningRate)
        mlp.fit(X, Y)
        loss = -cross_val_score(mlp, X, Y, cv=10, scoring='mean_squared_error')
        self.fitness=mean(loss)

def initGroup(groupNumber):
    '''
    �������Ϊ��Ⱥ��ģ
    �ڵ�����Χ[1,10000]
    ѧϰ��[1-5000]
    :param groupNumber:
    :return:
    ����ͨ��
    '''
    chroGroup=[]
    for i in range(groupNumber):
        n = randint(1, 10000)
        r = randint(1, 3000)
        chroGroup.append(Chromosome(n,r))
    print("init success")
    return chroGroup

def crossGroup(chroGroup,groupNumber):
    '''
    �������Ϊ����Ⱥ����Ⱥ��ģ
    ��֤�ڵ��ѧϰ�ʶ�Ϊ��
    :param chroGroup:
    :param groupNumber:
    :return:
    ���Գɹ�
    '''
    childGroup=[]
    for i in range(int(groupNumber/2)):
        alpha=randint(-25,125)/100
        n1=int(chroGroup[i].nodeNumber+alpha*chroGroup[i+1].nodeNumber)
        if n1<0:
            n1=-n1
        n2=int(chroGroup[i+1].nodeNumber+alpha*chroGroup[i].nodeNumber)
        if n2<0:
            n2=-n2
        r1 =int( chroGroup[i].learningRate + alpha * chroGroup[i + 1].learningRate)
        if r1<0:
            r1=-r1
        r2 = int(chroGroup[i + 1].learningRate + alpha * chroGroup[i].learningRate)
        if r2<0:
            r2=-r2
        child1=Chromosome(n1,r1)
        childGroup.append(child1)
        child2=Chromosome(n2,r2)
        childGroup.append(child2)
    print("cross success")
    return childGroup

def changeGroup(chroGroup,groupNumber):
    '''
    ��Ⱥ���溯��
    :param chroGroup:
    :param groupNumber:
    :return:
    ���Գɹ�
    '''
    childGroup=[]
    for i in range(groupNumber):
        alpha=randint(-5,5)/100
        n=int(chroGroup[i].nodeNumber*(1+alpha))
        if n<0:
            n=-n
        r=int(chroGroup[i].learningRate*(1+alpha))
        if r<0:
            r=-r
        child=Chromosome(n,r)
        childGroup.append(child)
    print("change success")
    return  childGroup

def generateNextGroup(chroGroup,groupNumber,X,Y):
    '''
    :param chroGroup:����Ⱥ
    :param groupNumber: ��Ⱥ��ģ
    :param X: ����������
    :param Y: ���������
    :return: ��һ����Ⱥ
    '''
    tempGroup=crossGroup(changeGroup(chroGroup,groupNumber),groupNumber)
    chroFit=[]
    tempFit=[]
    for i in range(groupNumber):
        chroGroup[i].getFitness(X,Y)
        chroFit.append(chroGroup[i].fitness)
        tempGroup[i].getFitness(X, Y)
        tempFit.append(chroGroup[i].fitness)
        print("yes, 1 more again")
    print("tempGroup success")
    childGroup=[]
    childFit=[]
    temp_Fit=[]
    temp_Group=[]
    childGroup.append(chroGroup[chroFit.index(min(chroFit))])
    childFit.append(chroGroup[chroFit.index(min(chroFit))].fitness)
    childGroup.append(chroGroup[tempFit.index(min(tempFit))])
    childFit.append(chroGroup[tempFit.index(min(tempFit))].fitness)
    for i in range(groupNumber - 2):
        a=int(randint(0,groupNumber/2 - 1))
        b=int(a+groupNumber/2)
        temp_Fit.append(chroGroup[a].fitness)
        temp_Group.append(chroGroup[a])
        temp_Fit.append(chroGroup[b].fitness)
        temp_Group.append(chroGroup[b])
        temp_Fit.append(tempGroup[a].fitness)
        temp_Group.append(tempGroup[a])
        temp_Fit.append(tempGroup[b].fitness)
        temp_Group.append(tempGroup[b])
        index=temp_Fit.index(min(temp_Fit))
        childGroup.append(temp_Group[index])
        childFit.append(temp_Group[index].fitness)
    print("generate success")
    return childGroup,childFit

def main():
    dataMat,labelMat=loadData('xjbs.xlsx')
    X_scaled=preprocessing.scale(dataMat)
    Y_scaled=preprocessing.scale(labelMat)

    fig = plt.figure()
    #plt.scatter(X,Y)
    #plt.show()


    group=initGroup(50)
    scoreGA=[]
    x=[]
    ax0=fig.add_subplot(211)
    temp=0
    #for i in range(50):
    #    x.append(i)
    #    group,fit=generateNextGroup(group,50,dataMat,labelMat)
    #    scoreGA.append(min(fit))
    #    index=fit.index(min(fit))
    #    print(scoreGA[i],group[index].nodeNumber,group[index].learningRate)
    #    if abs(temp-scoreGA[i])/scoreGA[i]<0.001:
    #        break
    #    temp=scoreGA[i]
    #ax0.plot(x,scoreGA)
    #ax1 = fig.add_subplot(212, projection='3d')
    loss_list=[]
    xx=[]
    yy=[]
    for i in range(600,800):
        for r in range(1,100):
            xx.append(i)
            yy.append(r)
            mlp = MLPRegressor(i, activation='logistic', solver='sgd', learning_rate='constant',
                           learning_rate_init=0.0000001*r*r)
            mlp.fit(dataMat, labelMat)
            loss = -cross_val_score(mlp, dataMat, labelMat, cv=10, scoring='mean_squared_error')
            print(mean(loss),i,0.0000001*r*r)
            loss_list.append(mean(loss))
    print (min(loss_list))
    #ax1.scatter(xx,yy,loss_list,c='r',marker='o')
    #ax1.set_xlabel('number of neuron')
    #ax1.set_ylabel('learning rate')
    #ax1.set_zlabel('loss')
    plt.show()
    #Y_predict=mlp.predict(X_scaled)
    #print(Y_predict)

    model = linear_model.Ridge()
    model.fit(X_scaled,labelMat)
    #loss = -cross_val_score(model,X_scaled,labelMat,cv=10,scoring='mean_squared_error')
    #print(mean(loss))
    #lo=list(loss)
    #maxP=lo.index(max(lo))
    #print(maxP)
    pca=PCA(n_components=3)
    pca.fit(X_scaled)
    X_new=pca.transform(X_scaled)
    #print(pca.explained_variance_ratio_)
    #print(pca.components_)
    X=list(X_new[:,0])
    Y=[]
    for i in range(shape(labelMat)[0]):
        Y.append(labelMat[i,0])
main()
