from Queue import LifoQueue
  
def RPN():
    expression = raw_input("Please input your expression:\n")
    expression = expression.replace(' ','')
    opStack = LifoQueue(100)
    result = list()
    i = 1
    token = expression[0]
    while token != '#':
        if token == '(':
            opStack.put(token)
        elif token == ')':
            topToken =opStack.get()
            while topToken !='(':
                result.append(topToken)
                if not opStack.empty():
                    topToken =opStack.get()
                else:
                    break
        elif token in '+-':
            topToken = opStack.get()
            while topToken != '(':
                result.append(topToken)
                if not opStack.empty():
                    topToken =opStack.get()
                else:
                    break
            opStack.put(topToken)
            opStack.put(token)
        elif token in '*/':
            while not opStack.empty():
                topToken = opStack.get()
                if topToken in '*/':
                    result.append(topToken)
                else:
                    opStack.put(topToken)
            opStack.put(token)
        else:
            tmp = 0
            while token in '0123456789':
                tmp = tmp * 10 + int(token)
                token = expression[i]
                i += 1
            result.append(tmp)
            i -= 1
        token = expression[i]
        i += 1
    while not opStack.empty():
        result.append(opStack.get())
    print result
 
if __name__ == '__main__':
    test = '(1+29)*(37-4)/5#'
    RPN()
