RPN
===

convert an expression to reverse Polish notation

This is just a simple implement,and I do this refer the algorithm in http://baike.baidu.com/view/2582.htm.

================
中序表达转逆波兰式
算法参考了百度百科，主要用到了栈操作。
思路如下：
stack：存放运算符
list：存放逆波兰式
（1）若取出的字符是数字，则分析出完整的数值，该数值直接送入队列list
（2）若取出的字符是运算符，则将该运算符与stack的栈顶元素比较，如果该运算符优先级大于stack的栈顶运算符优先级，则将该运算符进stack，否则，将stack的栈顶运算符弹出，送入list，直至stack栈顶运算符低于（不包括等于）该运算符优先级，则将该运算符送入stack
（3）若取出的字符是“（”，则直接送入stack。
（4）若取出的字符是“）”，则将距离stack栈顶最近的“（”之间的运算符，逐个出栈，依次送入list，此时抛弃“（”。
（5）重复上面的1~4步，直至处理完所有的输入字符
（6）若取出的字符是“#”，则将stack内所有运算符（不包括“#”），逐个出栈，依次送入list中。
