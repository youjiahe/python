
######################################################################
●VIM下实现python自动缩进功能
[root@proxy ~]# vim ~/.vimrc 

set filetype=python
au BufNewFile,BufRead *.py,*.pyw setf python
set autoindent " same level indent
set smartindent " next level indent
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set number
######################################################################
●Python文件 
   &格式
     open(file, mode='r')
   &mode
      r:只读打开
	  w:只写打开，会覆盖原来的内容；没有文件则创建
	  a：打开只能追加
	  r+：读写打开
	  w+：读写打开
	  a+：读写打开
   &例子：拷贝文件
      from sys import argv
      from os.path import exists
      script, fn1, fn2=argv
      open(fn2,"w").write(open(fn1).read())
######################################################################  
●Python函数注意事项
   1. 函数定义是以 def 开始的吗？ 
   2. 函数名称是以字符和下划线 _ 组成的吗？
   3. 函数名称是不是紧跟着括号 ( ？
   4. 括号里是否包含参数？多个参数是否以逗号隔开？
   5. 参数名称是否有重复？（不能使用重复的参数名）
   6. 紧跟着参数的是不是括号和冒号 ): ？
   7.跟着函数定义的代码是否使用了 4 个空格的缩进 (indent)？
   8. 函数结束的位置是否取消了缩进 (“dedent”)？
  
  当你运行（或者说“使用 use”或者“调用 call”）一个函数时，记得检查下面的要点：
  1. 调运函数时是否使用了函数的名称？
  2. 函数名称是否紧跟着 ( ？
  3. 括号后有无参数？多个参数是否以逗号隔开？
  4. 函数是否以 ) 结尾？
  按照这两份检查表里的内容检查你的练习，直到你不需要检查表为止。
  最后，将下面这句话阅读几遍：
  “‘运行函数 (run)’、‘调用函数 (call)’、和‘使用函数 (use)’是同一个意思”
