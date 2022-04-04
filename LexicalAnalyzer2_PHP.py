import re
# function for finding the column of the row
def findcolumn(line,string):
    filled = ""
    columnfinal = 0
    for i in line:
        if i not in string:
            columnfinal += 1
        elif i in string:
            filled += line[columnfinal]
            if filled == string:
                break
            else:continue

    return columnfinal

if __name__ == "__main__":
    php_code = ''' <?php
    class MyClass {
    function abc(){ $i=5;
    $z=$i*2;
    echo "One '$=".$z;}
    }
 ?>'''
    math_operations = {'+': 'math-plus', "*": "math-times", "/": "math-divide", "-": "math-subtraction"}
    fragments = php_code.splitlines()
    print(list(enumerate(fragments)))
    # iterating each line
    for line, syntax in enumerate(fragments):
        print(str(line)+ str(syntax))
        # display the opening tag in PHP
        if '<?php' in syntax:
            print(str(line+1) +" "+ str(findcolumn(syntax, '<?php')) + " php-opening tag")
        # for displaying the class tokens
        if 'class' in syntax:
            print(str(line+1)+ " "+str(findcolumn(syntax, 'class'))+ ' class')
            print(str(line + 1) + " "+str(findcolumn(syntax, '{'))+" curly-bracket-opening")
        # for displaying the function tokens
        if 'function' in syntax:
            print(str(line+1) + " "+str(findcolumn(syntax, 'function')) + " function")
            temp_list = syntax.split()
            #print(temp_list)
            for word in temp_list[1:]:
                func_variable =""
                for i in word:
                    if ord(i) >= 65 and ord(i) <= 90:
                        func_variable += i
                    elif ord(i) >= 97 and ord(i) <= 122:
                        func_variable += i
                print(str(line+1) + " "+str(findcolumn(syntax, func_variable)) + ' type-identifier ' + str(func_variable))
                if '(' in word:
                    print(str(line+1) +" "+ str(findcolumn(syntax, '(')) + " bracket-opening")
                if ')' in word:
                    print(str(line+1) +" "+ str(findcolumn(syntax, ')')) +" bracket-closing")
                if '{' in word:
                    print(str(line + 1) +" "+ str(findcolumn(syntax, '{')) + " curly-bracket-opening")
                if '$' in word:
                    print(str(line+1)+" "+str(findcolumn(syntax, '$')) +' variable')
                    for char in word:
                        if ord(char) >= 65 and ord(char) <= 90 :
                            print(str(line+1) + " "+str(findcolumn(syntax, char))+' type-identifier ' + str(char))
                        elif ord(char) >= 97 and ord(char) <= 122:
                            print(str(line + 1) + " "+str(findcolumn(syntax, char))+' type-identifier ' + str(char))
        if '$' in syntax and 'function' not in syntax and 'echo' not in syntax:
            print(str(line + 1) + " " + str(findcolumn(syntax, '$')) + ' variable')
            for char in syntax:
                if ord(char) >= 65 and ord(char) <= 90:
                    print(str(line + 1) + " "+str(findcolumn(syntax, char))+' type-identifier ' + str(char))

                elif ord(char) >= 97 and ord(char) <= 122:
                    print(str(line + 1) + " "+str(findcolumn(syntax, char))+' type-identifier ' + str(char))
        # for displaying the math operations
        for i in math_operations.keys():
            if i in syntax:
                print(str(line + 1) + " "+str(findcolumn(syntax, i))+ " " + math_operations[i])
        # displaying the print statements
        if 'echo' in syntax:
            print(str(line+1)+" "+str(findcolumn(syntax, 'echo'))+ ' print-output')
            string_lateral = syntax.replace("echo",'')
            #print(string_lateral)
            if '.' in string_lateral:
                sl2 = string_lateral.split('.')
               # print(sl2)
            for i in sl2:
                i = i.strip()
                if i.startswith('"') and i.endswith('"'):
                    i.replace('"',' ')
                    i.replace('"',' ')
                    print(str(line+1)+ " "+ str(findcolumn(syntax, i))+ " String-Lateral "+ i)
        # for displaying closing bracket
        if '}' in syntax:
            print(str(line + 1) +" "+str(findcolumn(syntax, '}'))+ " closing-curly-braces")
        # for the closing tag
        if '?>' in syntax:
            print(str(line+1)+ " " + str(findcolumn(syntax, '?>'))+ "php-closing-tag")