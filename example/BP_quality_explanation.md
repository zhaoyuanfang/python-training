# 质量预测程序解释
## loadData方法
在目标文件中读取数据，返回特征矩阵和标签矩阵  
这里的[0:27]，是手动统计的特征维度数目，大家自己做例子的时候，尽量选择合适自己数据集的提取数据方法  
总之，这是一个将数据从文件读取到程序的方法  
相信大家已经了解什么是“方法”了

## comData方法
这里本来是想把数据输出一部分用来直接观察的  
在这段程序里，这个方法没有被调用，也就是说，这个方法没什么用

## class Chromosome
定义了染色体类，是为了后续研究中，应用遗传算法  
这段程序里没有应用遗传算法

## initGroup方法
遗传函数的初始化种群方法

## crossGroup方法
遗传函数的染色体交叉方法

## changeGroup方法
遗传函数的染色体变异方法

## generateNextGroup方法
遗传函数的选择方法

---
以上有关遗传算法的方法在本段程序中没有被调用

## main方法
重点是这句程序  
***mlp=MLPRegressor(i,activation='logistic',solver='sgd',learning_rate='constant',learning_rate_init=0.00000001*r*r)***  

选择sklearn机器学习库中，多层回归，也就是神经网络方法，激活函数选择***logistics***，优化器选择***随机梯度下降法（sgd）***，学习率取***固定值‘constant’***，初始化为***0.00000001\*r\*r***  
这段程序用来运算效果并不好，只是给大家举个例子，希望大家能够写出更好的程序以及说明文档