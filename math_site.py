'''
本模块内含有一些和数学有关的函数
作为对python内置math模块的功能补充
'''
import time
import turtle as t#导入turtle库
from math import sin,cos,pi,e
t.speed(100)
class Not_found_in_domain_of_definationError(Exception):#定义错误类型
    def __init__(self,string):
        self.string=string

class Range:#范围
    def __init__(self,minimum,maxim):
        self.minimum=minimum*100
        self.maxim=maxim*100
    def __contains__(self,other):
        if self.minimum<=other and self.maxim>=other:
            return True
        else:
            return False

class Vec3D(tuple):#空间向量
    def __new__(cls,x,y,z):
        return tuple.__new__(cls,(x,y,z))
    def __add__(self,other):
        return Vec3D(self[0]+other[0],self[1]+other[1],self[2]+other[2])
    def __sub__(self,other):
        return Vec3D(self[0]+other[0],self[1]+other[1],self[2]+other[2])
    def __mul__(self,other):
        if isinstance(other,Vec3D):
            return self[0]*other[0]+self[1]*other[1]+self[2]*other[2]
        if isinstance(other,int) or isinstance(other,float):
            return Vec3D(self[0]*other,self[1]*other,self[2]*other)
    def __rmul__(self,other):
        return Vec3D(self[0]*other,self[1]*other,self[2]*other)
    def __abs__(self):
        return ((self[0])**2+(self[1])**2+(self[2])**2)**0.5
    def __neg__(self):
        return Vec3D(-self[0],-self[1],-self[2])
    def cos(self,other):
        return (self*other)/(abs(self)*abs(other))
    @staticmethod
    def nor_vec(vec1,vec2):
        return Vec3D(vec2[1]*vec1[2]-vec1[1]*vec2[2],vec1[0]*vec2[2]-vec2[0]*vec1[2],vec2[0]*vec1[1]-vec1[0]*vec2[1])

class Complex(complex):              #复数
    def __new__(cls,realpart,imagpart):
        if imagpart!=0:
            return complex.__new__(cls,complex(realpart,imagpart))
        else:
            return realpart
        return theta
    
    @staticmethod
    def arg(number):
        tg=number.imag/number.real
        theta=degrees(atan(tg))
        return theta
    @staticmethod
    def rotate(theta,number):
        return number*complex(cos(theta),sin(theta))

print('注意自变量不要太大，不然会很卡')

def formula(x):#质数通项公式
    num=2#令整数为2
    final=[2]#结果列表（质数列表）
    for i in range(x):#重复执行x次
        index=0#结果列表索引为零
        device=final[index]#除数为结果列表的第索引项
        while num>device:#当整数大于除数时重复执行
            if num%device==0:#判断整数/除数是否为整数
                num=num+1#若是，整数增加1
                index=0#索引为0
            else:#否则
                if index+1==len(final):#索引增加1等于列表长度
                    device=device+1#除数增加1
                else:#否则
                    index=index+1#索引增加1
                    device=final[index]#除数为列表的第索引项
        final.append(num)#在列表最后一位添加num
        num=num+1#num增加1
    return final.pop()#返回列表最后一项

def generate():#质数生成器
    zhengshu=2
    toolnumber=2
    while 1:
        if zhengshu==toolnumber:
            zhishu=zhengshu
            zhengshu=zhengshu+1
            toolnumber=2
            yield zhishu
        else:
            if zhengshu%toolnumber==0:
                zhengshu+=1
                toolnumber=2
            else:
                toolnumber+=1
        
        
def inverse(prime_num,iterble=generate):#质数通项公式
    result=[]
    for i in iterble():
        result.append(i)
        if i==prime_num:
            return len(result)
        if i>prime_num:
            raise Not_found_in_domain_of_definationError('不在定义域')
        
def assertion(number):#判断质数
    toolnumber=2
    _bool=True
    while _bool:
        if number==toolnumber:
            return 'True'
        else:
            if number%toolnumber==0:
                return 'False'
            else:
                toolnumber=toolnumber+1

def rel_prime(num2,num1):
    if not(isinstance(num1,int) or isinstance(num2,int)):
        raise Not_found_in_domain_of_definationError('请输入整数')
    if num2==1 or num1==1:
        return 'True'
    device=2
    xlist=[]
    numlist=[]
    while num1>device:
        if num1%device==0:
            numlist.append(device)
            num1=num1//device
        else:
            device=device+1
    numlist.append(num1)
    if num2 in numlist:
        return 'False'
    device=2
    while num2>device:
        if num2%device==0:
            xlist.append(device)
            num2=int(num2//device)
        else:
            device=device+1
    xlist.append(num2)
    if num1 in xlist:
        return 'False'
    _bool='True'
    for xindex in xlist:
        if xindex in numlist:
            _bool='False'
            return _bool
    return _bool

def Euler(x):#欧拉函数
    final=[]
    if x==1:
        final.append(num)
        return len(final)
    xlist=[]
    device=2
    while x>device:
        if x%device==0:
            xlist.append(device)
            x=int(x/device)
        else:
            device=device+1
    xlist.append(x)
    for num in range(1,x):
        numlist=[]
        num1=num
        if num in xlist:
            continue
        while num>device:
            if num1%device==0:
                numlist.append(device)
                num1=int(num1/device)
            else:
                device=device+1
        numlist.append(num1)
        for numindex in numlist:
            continue
        final.append(num)
    return len(final)

def graphinit():#直角坐标系初始化
    t.clear()
    t.penup()
    t.goto(-700,0)
    t.pendown()
    for m in range(14):#叙述建系
        t.fd(100)
        t.stamp()
        t.write(-6+m)
    t.penup()
    t.goto(0,-700)
    t.left(90)
    t.pendown()
    for n in range(14):
        t.fd(100)
        t.stamp()
        t.write(6+n)
    t.speed(100)
    t.penup()
    return None

def _graphinit():#极坐标系初始化
    t.clear()
    t.pendown()
    for m in range(7):#叙述建系
        t.fd(100)
        t.stamp()
        t.write(m+1)
    return None

types=t.textinput('输入窗口','请输入坐标系类型（极坐标或平面直角坐标系）')
if types=='极坐标':
    _graphinit()
elif types=='平面直角坐标系':
    graphinit()
else:
    pass

def functiongraph(func,color,*Rangement):#函数图像绘制
    t.pencolor(color)
    for defination in Rangement:
        for i in range(int(defination.minimum),int(defination.maxim)):
            try:
                t.goto(i,func((i)/100)*100)
                t.pendown()
            except ValueError:
                pass
    time.sleep(5)
    t.penup()
    return 'finish'

def func_zero_point(least,maxim,function,accuracy=0.001):#函数求零点
    if least>=maxim:
        return 'Error'
    while (maxim-least)>accuracy and function(least)*function(maxim)<0:
        medium=(maxim+least)/2
        if function(least)<0:
            if function(medium)<0:
                least=medium
            elif function(medium)>0:
                maxim=medium
            else:
                return medium
        elif function(maxim)<0:
            if function(medium)<0:
                maxim=medium
            elif function(medium)<0:
                least=medium
            else:
                return medium
    return medium

def creve(equx,equy,*Rangement):#曲线的参数方程
    graphinit()
    for defination in Rangement:
        for i in range(int(defination.minimum),int(defination.maxim)):
            try:
                t.goto(equx(i/100)*100,equy(i/100)*100)
                t.pendown()
            except:
                pass
    time.sleep(5)
    return 'finish'

def calulus(func,_min,_max):#微积分粗略计算
    S=0
    dx=10**(-5)
    for i in range(int((_max-_min)/dx)):
        _min=_min+dx
        S=S+dx*func(_min)
    return S

def coordinate(equ,*Rangement):#曲线极坐标方程
    _graphinit()
    for defination in Rangement:
        t.penup()
        for theta in range(int(defination.minimum),int(defination.maxim)):
            try:
                t.goto(100*equ((theta)/100)*cos((theta)/100),100*equ((theta)/100)*sin((theta)/100))
                t.pendown()
            except ZeroDivisionError:
                pass
            except ValueError:
                pass

            
                
    
    
    
