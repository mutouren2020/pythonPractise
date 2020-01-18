1.用引号括起来的就是字符串，引号可以是双引号，可以是单引号
2.字符串的一些常用方法：title(),upper(),lower()
3.字符串通过“+”拼接
4.制表符\t,换行符\n
5.rstrip()去除尾部空白字符串，lstrip()去除开头空白字符串，strip()去除两端空白字符串

列表：
1.Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1 ，可让Python返回最后一个列表元素：bicycles[-1]
  这种语法很有用，因为你经常需要在不知道列表长度的情况下访问最后的元素。这种约定也适用于其他负数索引，例如，索引-2 返回倒数第
  二个列表元素，索引-3 返回倒数第三个列表元素，以此类推。
2.如果你不确定该使用del 语句还是pop() 方法，下面是一个简单的判断标准：如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del 语句；如果你要在删除元
  素后还能继续使用它，就使用方法pop() 。
  如果你只知道要删除的元素的值，可使用方法remove() 。方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值
  remove()的参数是变量，不能直接是要删除的字符串。
3.sort() 正序 ，这两个函数会改变原列表的顺序。sort(reverse=True) 逆序
  sorted() 返回值正序排列，不改变原列表的顺序，sorted(names)  正序，sorted(names, reverse=True) 逆序
4.注意，reverse() 不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序。
  方法reverse() 永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用reverse() 即可
5.使用函数len() 可快速获悉列表的长度：len(cars)


1.通过缩进确定遍历执行的内容
2.两个星号（** ）表示乘方运算: square = value**2
3.数组复制：friend_foods = my_foods[:]
4.Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组 。元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。


1.一个等号复制，两个等号相等比较
2.使用and 和 or 检查多个条件
3.要判断特定的值是否已包含在列表中，可使用关键字in 。检查特定值是否不包含在列表中,可使用关键字not in
4.if-elif-else 结构。Python并不要求if-elif 结构后面必须有else 代码块。
  else 是一条包罗万象的语句，只要不满足任何if 或elif 中的条件测试，其中的代码就会执行，这可能会引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用
  一个elif 代码块来代替else 代码块。这样，你就可以肯定，仅当满足相应的条件时，你的代码才会执行。
5.在if 语句中将列表名用在条件表达式中时，Python将在列表至少包含一个元素时返回True ，并在列表为空时返回False 。


1.遍历字典：for key, value in user_0.items():
  要编写用于遍历字典的for 循环，可声明两个变量，用于存储键—值对中的键和值。对于这两个变量，可使用任何名称。可以定义一些有意义的变量名，而不仅仅时key和value这两个变量。
2.在不需要使用字典中的值时，方法keys() 很有用。for name in favorite_languages.keys():
  遍历字典时，会默认遍历所有的键，因此，如果将上述代码中的for name in favorite_languages.keys(): 替换为for name in favorite_languages: ，输出
  将不变。
  如果显式地使用方法keys() 可让代码更容易理解，你可以选择这样做，但如果你愿意，也可省略它。
  方法keys() 并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键。if 'erin' not in favorite_languages.keys():
3.可使用函数sorted() 来获得按特定顺序排列的键列表的副本：
  for name in sorted(favorite_languages.keys()):
  只是排序，不一定是字典中的顺序
4.遍历字典中的所有值：可使用方法values() ，它返回一个值列表，而不包含任何键。
  for language in favorite_languages.values():
5.为剔除重复项，可使用集合（set）。集合 类似于列表，但每个元素都必须是独一无二的。
  for language in set(favorite_languages.values()):


1.while 循环中可以使用 break   continue
2.如果程序陷入无限循环，可按Ctrl + C，也可关闭显示程序输出的终端窗口。


1.文档字符串用三引号括起，Python使用它们来生成有关程序中函数的文档。"""文档注释"""
2.在函数greet_user() 的定义中，变量username 是一个形参 ——函数完成其工作所需的一项信息。在代码greet_user('jesse') 中，值'jesse' 是一个实参 。
3.if ''  判断为false
4.将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的
5.可向函数传递列表的副本而不是原件；这样函数所做的任何修改都只影响副本，而丝毫不影响原件。function_name(list_name[:])
6.传递任意数量的实参：形参名*toppings 中的星号让Python创建一个名为toppings 的空元组，并将收到的所有值都封装到这个元组中。
  如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后：def make_pizza(size, *toppings):
7.使用任意数量的关键字实参：def build_profile(first, last, **user_info):
8.导入整个模块：
  在pizza.py所在的目录中创建另一个名为making_pizzas.py的文件，这个文件导入刚创建的模块：
  import pizza
  pizza.make_pizza(16, 'pepperoni')
9.导入特定的函数: from module_name import function_0, function_1, function_2
10.使用as 给函数指定别名：如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的
   别名 ——函数的另一个名称，类似于外号。要给函数指定这种特殊外号，需要在导入它时这样做。
   from pizza import make_pizza as mp
   mp(16, 'pepperoni')
11.使用as 给模块指定别名:
   import pizza as p
   p.make_pizza(16, 'pepperoni')
12.导入模块中的所有函数: from pizza import *
   由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。然而，使用并非自己编写的大型模块时，最好不要采用这种
   导入方法：如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：Python可能遇到多个名称相同的函
   数或变量，进而覆盖函数，而不是分别导入所有的函数。
   最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。这能让代码更清晰，更容易阅读和理解
13.每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。文档良好的函数让其他程序员只需阅读文档字符串中的描述就能够使用
   它：他们完全可以相信代码如描述的那样运行；只要知道函数的名称、需要的实参以及返回值的类型，就能在自己的程序中使用它。



1.创建和使用类：
  class Dog():
  """一次模拟小狗的简单尝试"""
  def __init__(self, name, age):
  """初始化属性name和age"""
  self.name = name
  self.age = age
  def sit(self):
  """模拟小狗被命令时蹲下"""
  print(self.name.title() + " is now sitting.")
  def roll_over(self):
  """模拟小狗被命令时打滚"""
  print(self.name.title() + " rolled over!")
2. 根据类创建实例:my_dog = Dog('willie', 6)
   我们通常可以认为首字母大写的名称（如Dog ）指的是类，而小写的名称（如my_dog ）指的是根据类创建的实例。
   访问属性:my_dog.name
   调用方法:my_dog.sit()
3.给属性指定默认值:
  def __init__(self, make, model, year):
  """初始化描述汽车的属性"""
  self.make = make
  self.model = model
  self.year = year
  self.odometer_reading = 0
4.修改属性的值:
  1) 直接修改my_new_car.odometer_reading = 23
  2) 通过方法修改属性的值:
     def update_odometer(self, mileage):
         """将里程表读数设置为指定的值"""
         self.odometer_reading = mileage

     my_new_car.update_odometer(23)
5.继承:
  1)子类的方法__init__():
    class ElectricCar(Car):
        """电动汽车的独特之处"""
        def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
    首先是Car 类的代码（见❶）。创建子类时，父类必须包含在当前文件中，且位于子类前面
  2)给子类定义属性和方法
  3)重写父类的方法:对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子类中定义一个这样的方法，
    即它与要重写的父类方法同名。这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。
  4)将实例用作属性
6.导入类：
  1）导入单个类：from car import Car
  2）在一个模块中存储多个类：from car import ElectricCar
  3）从一个模块中导入多个类：from car import Car, ElectricCar
  4）导入整个模块：你还可以导入整个模块，再使用句点表示法访问需要的类。这种导入方法很简单，代码也易于阅读。由于创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突。
     import car
     my_beetle = car.Car('volkswagen', 'beetle', 2016)
  5）导入模块中的所有类：from module_name import * ，不推荐使用这种导入方式， 导入内容不明确。
     需要从一个模块中导入很多类时，最好导入整个模块，并使用 module_name.class_name 语法来访问类。这样做时，虽然文件开头并没有列出用到的所有类，但你清楚地知
     道在程序的哪些地方使用了导入的模块；你还避免了导入模块中的每个类可能引发的名称冲突。
  6）在一个模块中导入另一个模块：from car import Car
7.OrderedDict 实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序：from collections import OrderedDict
8.类名应采用驼峰命名法 ，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加上下划线。
9.类的使用规范：
  1）对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。每个模块也都应包含一个文
  2）档字符串，对其中的类可用于做什么进行描述。
  可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。
  3）需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import 语句，再添加一个空行，然后编写导入你自己编写的模块的import 语句。在包含多
    条import 语句的程序中，这种做法让人更容易明白程序使用的各个模块都来自何方。


1.从文件中读取数据：
  1）读取整个文件：
     with open('pi_digits.txt') as file_object:
         contents = file_object.read()
         print(contents)
  2）关键字with 在不再需要访问文件后将其关闭。
  3）相比于原始文件，该输出唯一不同的地方是末尾多了一个空行。为何会多出这个空行呢？因为read() 到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一
    个空行。要删除多出来的空行，可在print 语句中使用rstrip() ：print(contents.rstrip())
  4）文件路径：
     a. 相对文件路:with open('text_files/filename.txt') as file_object:
        在Windows系统中，在文件路径中使用反斜杠（\ ）而不是斜杠（/ ）：with open('text_files\filename.txt') as file_object:
     b.绝对文件路径
  5）逐行读取：
     filename = 'pi_digits.txt'
        with open(filename) as file_object:
        for line in file_object:
            print(line)
     我们打印每一行时，发现空白行更多了
     为何会出现这些空白行呢？因为在这个文件中，每行的末尾都有一个看不见的换行符，而print 语句也会加上一个换行符，因此每行末尾都有两个换行符：一个来自文件，另一
     个来自print 语句。要消除这些多余的空白行，可在print 语句中使用rstrip()
  6）创建一个包含文件各行内容的列表：
     with open(filename) as file_object:
        lines = file_object.readlines()
2.写入文件:
  1)写入空文件:
    filename = 'programming.txt'
        with open(filename, 'w') as file_object:
        file_object.write("I love programming.")
    调用open() 时提供了两个实参（见❶）。第一个实参也是要打开的文件的名称；第二个实参（'w' ）告诉Python，我们要以写入模式 打开这个文件。打开文件
    时，可指定读取模式 （'r' ）、写入模式 （'w' ）、附加模式 （'a' ）或让你能够读取和写入文件的模式（'r+' ）。如果你省略了模式实参，Python将以默认的只读模式打
    开文件。
  2）如果你要写入的文件不存在，函数open() 将自动创建它。然而，以写入（'w' ）模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空
    该文件。
  3）Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str() 将其转换为字符串格式。
  4）写入多行：要让每个字符串都单独占一行，需要在write() 语句中包含换行符： file_object.write("I love programming.\n")
     像显示到终端的输出一样，还可以使用空格、制表符和空行来设置这些输出的格式。
  5）附加到文件：如果你要给文件添加内容，而不是覆盖原有的内容，可以附加模式 打开文件。你以附加模式打开文件时，Python不会在返回文件对象前清空文件，而你写入到文件的行都将添加
          到文件末尾。如果指定的文件不存在，Python将为你创建一个空文件。
3.异常：
  1）异常是使用try-except 代码块处理的。try-except 代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。使用了try-except 代码块时，即便出现异常，
     程序也将继续运行：显示你编写的友好的错误消息，而不是令用户迷惑的traceback。
  2）使用try-except 代码块：
     try:
        print(5/0)
     except ZeroDivisionError:
        print("You can't divide by zero!")
  3）else 代码块：
     while True:
         first_number = input("\nFirst number: ")
         if first_number == 'q':
            break
         second_number = input("Second number: ")
            try:
                answer = int(first_number) / int(second_number)
            except ZeroDivisionError:
                print("You can't divide by 0!")
            else:
                print(answer)
  4)文件不存在异常处理:
    filename = 'alice.txt'
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)

  5)方法split() 以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
  6)要让程序在失败时一声不吭，可像通常那样编写try 代码块，但在except 代码块中明确地告诉Python什么都不要做。Python有一个pass 语句，可在代码块中使用它来让Python
    什么都不要做:
    try:
        --snip--
    except FileNotFoundError:
        pass
    else:
        --snip--
4.我们调用json.dump() ，并将用户名和一个文件对象传递给它，从而将用户名存储到文件中
  使用json.load() 将存储在username.json中的信息读取到变量username 中。
5.这是一种不错的做法：函数要么返回预期的值，要么返回None ；这让我们能够使用函数的返回值做简单测试

