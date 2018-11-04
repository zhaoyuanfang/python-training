# 引入相关模块（math模块和tkinter模块）
import math
import tkinter


class MyCalculator:
    # 初始化对象
    def __init__(self):
        # 设置主界面
        self.root = tkinter.Tk()
        self.root.title('calculator')
        self.root.minsize(400, 550)
        # 禁止调节窗口大小
        self.root.resizable(0,0)

        # 为label标签设置一个变量
        self.var = tkinter.StringVar()
        # 设置初始值为0
        self.var.set('0')

        # 设置用于存储运算数据的列表
        self.operation_lists = []
        # 设置空字符串，用于截取
        self.metastrs = ''
        # 设置是否按下运算符的变量
        self.isoperation = False
        # 调用设置界面的方法
        self.set_main_interface()
        self.root.mainloop()

    # 主界面布局方法
    def set_main_interface(self):
        # 显示结果和操作的区域
        # frame = tkinter.Frame(self.root, width=400, height=100, )
        # frame.pack()
        label = tkinter.Label(self.root, bg='white', textvariable=self.var, anchor='se', font=('黑体', 35), bd=10)
        label.place(x=10, y=10, width=380, height=100)

        # 设置数字按钮
        button11 = tkinter.Button(self.root, text='%', font=('黑体', 20), command=self.percent)
        button11.place(x=10, y=130, width=90, height=60)

        button12 = tkinter.Button(self.root, text='√', font=('黑体', 20), command=self.square)
        button12.place(x=105, y=130, width=90, height=60)

        button13 = tkinter.Button(self.root, text='x²', font=('黑体', 20), command=self.power)
        button13.place(x=200, y=130, width=90, height=60)

        button14 = tkinter.Button(self.root, text='1/x', font=('黑体', 20), command=self.backwords)
        button14.place(x=295, y=130, width=90, height=60)

        button21 = tkinter.Button(self.root, text='CE', font=('黑体', 20), command=self.clear_CE)
        button21.place(x=10, y=195, width=90, height=60)

        button22 = tkinter.Button(self.root, text='C', font=('黑体', 20), command=self.clear_C)
        button22.place(x=105, y=195, width=90, height=60)

        button23 = tkinter.Button(self.root, text='←', font=('黑体', 20), command=self.strip)
        button23.place(x=200, y=195, width=90, height=60)

        button24 = tkinter.Button(self.root, text='÷', font=('黑体', 20), command=lambda: self.symbol('/'))
        button24.place(x=295, y=195, width=90, height=60)

        button31 = tkinter.Button(self.root, text='7', font=('黑体', 20), command=lambda: self.change('7'))
        button31.place(x=10, y=260, width=90, height=60)

        button32 = tkinter.Button(self.root, text='8', font=('黑体', 20), command=lambda: self.change('8'))
        button32.place(x=105, y=260, width=90, height=60)

        button33 = tkinter.Button(self.root, text='9', font=('黑体', 20), command=lambda: self.change('9'))
        button33.place(x=200, y=260, width=90, height=60)

        button34 = tkinter.Button(self.root, text='×', font=('黑体', 20), command=lambda: self.symbol('*'))
        button34.place(x=295, y=260, width=90, height=60)

        button41 = tkinter.Button(self.root, text='4', font=('黑体', 20), command=lambda: self.change('4'))
        button41.place(x=10, y=325, width=90, height=60)

        button42 = tkinter.Button(self.root, text='5', font=('黑体', 20), command=lambda: self.change('5'))
        button42.place(x=105, y=325, width=90, height=60)

        button43 = tkinter.Button(self.root, text='6', font=('黑体', 20), command=lambda: self.change('6'))
        button43.place(x=200, y=325, width=90, height=60)

        button44 = tkinter.Button(self.root, text='－', font=('黑体', 20), command=lambda: self.symbol('-'))
        button44.place(x=295, y=325, width=90, height=60)

        button51 = tkinter.Button(self.root, text='1', font=('黑体', 20), command=lambda: self.change('1'))
        button51.place(x=10, y=390, width=90, height=60)

        button52 = tkinter.Button(self.root, text='2', font=('黑体', 20), command=lambda: self.change('2'))
        button52.place(x=105, y=390, width=90, height=60)

        button53 = tkinter.Button(self.root, text='3', font=('黑体', 20), command=lambda: self.change('3'))
        button53.place(x=200, y=390, width=90, height=60)

        button54 = tkinter.Button(self.root, text='＋', font=('黑体', 20), command=lambda: self.symbol('+'))
        button54.place(x=295, y=390, width=90, height=60)

        button61 = tkinter.Button(self.root, text='±', font=('黑体', 20), command=self.opposite_num)
        button61.place(x=10, y=455, width=90, height=60)

        button62 = tkinter.Button(self.root, text='0', font=('黑体', 20), command=lambda: self.change('0'))
        button62.place(x=105, y=455, width=90, height=60)

        button63 = tkinter.Button(self.root, text='.', font=('黑体', 20), command=lambda: self.change('.'))
        button63.place(x=200, y=455, width=90, height=60)

        button64 = tkinter.Button(self.root, text='=', font=('黑体', 20), command=self.equal)
        button64.place(x=295, y=455, width=90, height=60)

    # 计算器各种操作的函数
    # 按下数字的函数
    def change(self, num):
        # 全局化
        global isoperation
        # 判断是否按下了运算符号
        # 如果按下运算符号
        if self.isoperation:
            # 将面板中的数据归0
            self.var.set('0')
            # 设置运算符状态
            self.isoperation = False
        # 获取原来的数据
        metadata = self.var.get()
        # 判断原数字是否为0
        if metadata == '0' and num == '.':  # 如果为0,判断输入的数据是否为符号’.'
            self.var.set('0' + num)
        elif metadata == '0' and num != '.':  # 将按下的数字显示到标签中
            self.var.set(num)
        elif metadata in ['除数不能为0', '无效输入', '结果未定义']:
            self.var.set(num)
        # 如果不是0,判断原数字中是否存在符号’.'
        elif '.' in metadata and num == '.':
            return
        # 原数字不是0, 且符号'.' 不在原数字中
        else:
            # 将原有数字和当前按下的数字拼合到一起，显示到标签中
            self.var.set(metadata + num)
        # 获取面板中的数值，截取最后一个字符
        foredata = self.var.get()[-1]
        # 判断操作列表中的元素
        # 如果操作列表不为空，且操作列表最后一元素为运算符号
        if self.operation_lists != [] and self.operation_lists[-1] in ['+', '-', '*', '/']:
            # 将面板中的字符加入列表
            self.operation_lists.append(foredata)
            # print(self.operation_lists)
        else:
            # 如果操作列表为空
            if self.operation_lists == []:
                # 将截取的字符串加入列表
                self.operation_lists.append(foredata)
                # print(self.operation_lists)
            else:
                # 如果操作列表不为空，更新列表最后一个元素
                self.operation_lists[-1] += foredata
                # print(self.operation_lists)

    # 按下运算符号的函数
    def symbol(self, sign):
        # 全局化
        global isoperation

        # 判断列表是否为空，不为空时，最后输入的是否为运算符
        if self.operation_lists != [] and self.operation_lists[-1] in ['+', '-', '*', '/']:
            self.operation_lists[-1] = sign
            return
        # 如果列表为空，将当前面板中的数据加入到列表中

        elif self.operation_lists == []:
            # 获取面板中的数据
            foredata = self.var.get()
            # 将当前面板中的数据添加到列表中
            self.operation_lists.append(foredata)

        # 将列表中的数据连接成字符串，使用eval函数进行运算
        result = eval(''.join(self.operation_lists))
        # 将运算结果显示到面板中
        self.var.set(result)
        # 清空列表，将运算结果添加到列表中
        self.operation_lists.clear()
        self.operation_lists.append(str(result))
        # 将按下的运算符也存入列表中
        self.operation_lists.append(sign)
        # 设置运算符的状态
        self.isoperation = True

    # 按下等号的函数
    def equal(self):
        # 全局化
        global isoperation
        # 判断除数是否为0
        if '/' in self.operation_lists and self.operation_lists[-1] == '0':
            self.var.set('除数不能为0')
            self.operation_lists.clear()
            return
        elif self.operation_lists != [] and self.operation_lists[-1] in ['+', '-', '*', '/']:
            self.var.set('结果未定义')


        # 如果为空列表
        # 这里是有问题的 ：3==-->>33,33==-->>3333
        # 对不含运算符操作表取equal操作时，清空操作表，此时连做equal操作，之前的数字会作为字符读入操作表
        elif self.operation_lists == []:
            # 获取当前面板中的值
            value = self.var.get()
            # 将面板中的值加入列表
            self.operation_lists.append(value)
            self.operation_lists += self.metastrs
            # 将列表中的数据组合成字符串，通过eval函数进行运算操作
            strs_num = ''.join(self.operation_lists)
            result = eval(strs_num)
            # 判断整数位为长度是否大于13
            if len(str(round((result)))) > 13:
                self.var.set('溢出')
            else:
                result = str(result)[0:13]
                # 将运算结果显示到面板中
                self.var.set(result)

        else:
            # 将列表中的数据组合成字符串，通过eval函数进行运算操作
            strs_num = ''.join(self.operation_lists)
            result = eval(strs_num)
            # 判断整数位为长度是否大于13
            if len(str(round((result)))) > 13:
                self.var.set('溢出')
            else:
                result = str(result)[0:13]
                # 将运算结果显示到面板中
                self.var.set(result)
        self.metastrs = self.operation_lists[-2:]
        # print(self.metastrs)
        # 清空操作列表，便于下次运算使用
        self.operation_lists.clear()

        # 设置运算符状态
        self.isoperation = True

    # 设置清空操作:计算器中的C
    def clear_C(self):
        # 将面板中的数据添加到列表里
        self.operation_lists.append(self.var.get())
        # 清空用于存储运算数据的列表
        self.operation_lists.clear()
        # print(self.operation_lists)
        # 将面板中的数据归零
        self.var.set('0')

    # 设置删除当前数据的操作：计算器中的CE
    def clear_CE(self):

        # 清空用于存储运算数据的列表
        self.operation_lists.pop()
        # print(self.operation_lists)
        # 将面板中的数据归零
        self.var.set('0')

    # 设置删除键
    def strip(self):
        # 获取当前面板中的数据
        present_data = self.var.get()
        print(present_data)
        # 判断面板中的数据是否为0
        if present_data == '0':
            return
        # 设置删除数据的操作
        present_data = present_data[:len(present_data) - 1]
        print(present_data)
        # 判断删除后的字符串是否为空
        if present_data == '':  # 如果为空，设置为0
            self.var.set('0')
            self.operation_lists[-1] = ''
        else:  # 如果不为空，将删除后的数据显示到面板中
            self.var.set(present_data)
            self.operation_lists[-1] = present_data

    # 设置1/x键
    def backwords(self):
        # 全局化
        global isoperation
        # 获取当前面板中的数据
        global present_data
        present_data = self.var.get()
        # 判断列表中数据运算结果是否为0
        if present_data == '0':
            self.var.set('除数不能为0')
        else:
            # 将当前数据取倒数，设置到面板中
            data = '(1' + '/' + present_data + ')'
            ##判断整数位为长度是否大于13
            if len(str(round((eval(data))))) > 13:
                self.var.set('溢出')
            else:
                result = str(eval(data))[0:12]
                self.var.set(result)
            # print(self.operation_lists)
            # 将操作列表中的最后一个元素更新为倒数的结果
            self.operation_lists[-1] = str(eval(data))
            print(self.operation_lists)
        # 设置运算符状态
        self.isoperation = True

    # 设置一个数的平方的函数
    def power(self):
        # 全局化
        global isoperation
        # 获取当前面板中的数据
        present_data = self.var.get()
        # print(present_data)
        # 将当前数据进行平方运算后，设置到面板中
        data = 'math.pow' + '(' + present_data + ',' + '2' + ')'
        # 判断整数位为长度是否大于13
        if len(str(round(eval(data)))) > 13:
            self.var.set('溢出')
        else:
            result = str(eval(data))[0:12]
            self.var.set(result)
        self.operation_lists[-1] = str(eval(data))
        # 设置运算符状态
        self.isoperation = True

    # 设置一个数据的开平方运算
    def square(self):
        # 全局化
        global isoperation
        # 获取当前面板中的数据
        present_data = self.var.get()
        # 判断数值的正负
        if present_data[0] == '-':
            self.var.set('无效输入')
        else:
            # 将当前数据进行平方运算后，设置到面板中
            data = 'math.sqrt' + '(' + present_data + ')'
            result = str(eval(data))[0:12]
            self.var.set(result)
            self.operation_lists[-1] = str(eval(data))
        # 设置运算符状态
        self.isoperation = True

    # 设置’%‘的运算
    def percent(self):
        # 全局化
        global isoperation
        # 获取当前面板中的数据
        present_data = self.var.get()
        # 将当前数据进行%运算后，设置到面板中
        data = present_data + '*' + '0.01'
        result = str(eval(data))[0:12]
        self.var.set(result)
        self.operation_lists[-1] = str(eval(data))
        # 设置运算符状态
        self.isoperation = True

    # 求反的运算
    def opposite_num(self):
        # 全局化
        global isoperation
        # 获取当前面板中的数据
        present_data = self.var.get()

        if present_data[0] == '-':
            self.var.set(present_data[1:])
        elif present_data[-1] == '0':
            self.var.set('0')
        else:
            self.var.set('-' + present_data)
        self.operation_lists[-1] = self.var.get()
        print(self.operation_lists)
        # 设置运算符状态
        self.isoperation = True


# 实例化对象
if __name__ == '__main__':
    my = MyCalculator()