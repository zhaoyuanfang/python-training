# 函数式编程
## 返回函数
- 接受函数作为返回值，返回值再调用的时候闭包内函数才会调用
- 感觉这个东西挺厉害的，但是没想到能怎么用

## 匿名函数
- 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突
- 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。

- decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。

# 类和实例
## 继承
- 所有的类最终都要继承object类，那么python的object类长什么样？
- python是动态语言允许对实例变量绑定任何数据
- 也就是说，对于两个实例变量，虽然它们是同一个类的不同实例，但是拥有不同变量
- 双下划线开头的是private变量，既有双下划线开头又有双下划綫结尾的是特殊变量
* ** python本身没有任何机制阻止你干坏事，一切全靠自觉  ** *

- 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

- 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的 

