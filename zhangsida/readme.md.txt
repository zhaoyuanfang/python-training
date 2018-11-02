此代码参考《机器学习实战》一书，使用决策树实现一个简单预测模型。
根据：'年龄', '有工作', '有自己的房子', '信贷情况'的情况来决定是否放贷。
--------------------------------------------------------------
就是根据信息论的方法找到最合适的特征来划分数据集。
首先要计算所有类别的所有可能值的香农熵，
根据香农熵来我们按照取最大信息增益的方法划分我们的数据集。
--------------------------------------------------------------
下面对程序进行简单解释：

def calcShannonEnt(dataSet)
	计算给定数据集的经验熵(香农熵)
	参数：
	dataSet - 数据集
	
def createDataSet()
	创建测试数据集

def splitDataSet(dataSet, axis, value)
	按照给定特征划分数据集
	参数：
	dataSet - 待划分的数据集
    axis - 划分数据集的特征
    value - 需要返回的特征的值
	
def chooseBestFeatureToSplit(dataSet)
	选择最优特征
	参数：
	dataSet - 数据集
	
def majorityCnt(classList)
	统计classList中出现此处最多的元素(类标签)
	参数：
	classList - 类标签列表
	
def createTree(dataSet, labels, featLabels)
	创建决策树
	参数：
	dataSet - 训练数据集
    labels - 分类属性标签
    featLabels - 存储选择的最优特征标签
	
def classify(inputTree, featLabels, testVec)
	使用决策树分类
	参数：
	inputTree - 已经生成的决策树
    featLabels - 存储选择的最优特征标签
    testVec - 测试数据列表，顺序对应最优特征标签