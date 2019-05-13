# 由质量预测引出的许多话题  
## 质量预测  
- 这是我做的主要的课题，基于循环神经网络对产品质量参数进行预测  
- 本质来说属于回归预测任务  
- 关于这部分之前汇报了很多，这里不展开了  



## 数据挖掘
  
-  **[数据挖掘](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98/216477?fr=aladdin)** 可以直观的从名字理解，就是从数据中挖掘出有价值的信息  

- 这里的数据通常是 **[结构化数据](https://baike.baidu.com/item/%E7%BB%93%E6%9E%84%E5%8C%96%E6%95%B0%E6%8D%AE)** 可以简单理解为二维数据表  
- 通常数据挖掘的任务可以有一下几种：
	1. **分类**：根据给定数据确定样本属于特定类别
	2. **回归**：根据给定数据计算样本某一属性具体数值
	3. **聚类**：把若干相似数据按某种方式分为若干子集，每一子集具有相似性，不同子集具有互斥性
	4. **降维**：降低数据维度，排除相关度较弱的数据属性  

- 前两种称为[**有监督学习**](https://baike.baidu.com/item/%E6%9C%89%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0/19185816?fr=aladdin) ，后两种称为[**无监督学习**](https://baike.baidu.com/item/%E6%97%A0%E7%9B%91%E7%9D%A3%E5%AD%A6%E4%B9%A0)
- 有无监督的区别主要在于已知数据是否有**确定标签**



### 举个栗子
![example](https://github.com/zhaoyuanfang/python-training/blob/master/pictures/index.jpg)

***分类***
---
![classify](https://github.com/zhaoyuanfang/python-training/blob/master/pictures/decessiontree.png)



***回归***
---
![regression](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/regression.png)

***聚类***
---
![cluster](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/agg.jpg)

***降维***
---
![dimenssion reduction](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/reduce.jpg)

## **十大算法**
---  
### [决策树(decission tree)](https://baike.baidu.com/item/%E5%86%B3%E7%AD%96%E6%A0%91/10377049?fr=aladdin)
- 关键概念：[**信息熵**](https://baike.baidu.com/item/%E4%BF%A1%E6%81%AF%E7%86%B5)
- 每次分割使得系统整体的信息熵减少最多
### [随机森林](https://baike.baidu.com/item/%E9%9A%8F%E6%9C%BA%E6%A3%AE%E6%9E%97)  
- 一堆决策树  
![forest](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/forest.png)
### [逻辑回归(logistic regression)](https://baike.baidu.com/item/logistic%E5%9B%9E%E5%BD%92/2981575?fromtitle=%E9%80%BB%E8%BE%91%E5%9B%9E%E5%BD%92&fromid=17202449&fr=aladdin)

- 对线性回归再加一层非线性函数  
![LR](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/LR.png)

![LR1](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/LR1.png)

### [支持向量机(Support Vector Machine, SVM)](https://baike.baidu.com/item/%E6%94%AF%E6%8C%81%E5%90%91%E9%87%8F%E6%9C%BA?fromtitle=svm&fromid=4385807)  
- 获取线性超平面  
![SVM1](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/SVM1.png)  
- 核函数核方法


### [朴素贝叶斯(Naive Bayes Classifier)](https://baike.baidu.com/item/%E6%9C%B4%E7%B4%A0%E8%B4%9D%E5%8F%B6%E6%96%AF/4925905?fr=aladdin)  
- 条件概率  
- 多用于自然语言处理  

### [K临近(K nearest neighbours, KNN)](https://baike.baidu.com/item/%E9%82%BB%E8%BF%91%E7%AE%97%E6%B3%95/1151153?fr=aladdin)  
- Vote  


### [K均值(K means)](https://baike.baidu.com/item/K%E5%9D%87%E5%80%BC%E8%81%9A%E7%B1%BB%E7%AE%97%E6%B3%95?fromtitle=Kmeans&fromid=10932719)  
- 无监督聚类算法  
![Kmeans](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/Kmeans.png) 

### [Adaboost](https://baike.baidu.com/item/adaboost/4531273?fr=aladdin)
- 三个臭皮匠定个诸葛亮  
- 天鹅、梭子蟹和鲤鱼  

### [主成分分析](https://baike.baidu.com/item/%E4%B8%BB%E6%88%90%E5%88%86%E5%88%86%E6%9E%90/829840)  
- 无监督降维方法  

![PCA](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/PCA.jpg)  
![PCA1](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/PCA1.jpg)  

### [神经网络](https://baike.baidu.com/item/%E4%BA%BA%E5%B7%A5%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C/382460)  

## **深度学习**  
- 语音
- 语意（自然语言处理）
- 图像  

### [卷积神经网络(Convolutional Neural Networks, CNN)](https://baike.baidu.com/item/%E5%8D%B7%E7%A7%AF%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)  
![CNN](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/CNN.png)  
重要参数：
  
- 卷积核  
- 步长  
- 填充值  

[IBM Cloud](https://cloud.ibm.com/)  

### [循环神经网络(Recurrent Neural Networks, RNN](https://baike.baidu.com/item/%E5%BE%AA%E7%8E%AF%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)  
![RNN](https://github.com/zhaoyuanfang/python-training/tree/master/pictures/RNN.png)  

[IBM Lab](https://labs.cognitiveclass.ai/profile)