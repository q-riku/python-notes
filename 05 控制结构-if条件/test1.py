#语法：if boolean表达式: <代码块>
#这种if条件，有可能没有输出；（注意缩进）
if 1>2:
    print('这是对的')
print('这个输出跟上面if条件没关系！')
print("============================")
if 2<4:
    if 3>2:
        print('我是内部if条件')
    print('我是外部if条件') #Tab