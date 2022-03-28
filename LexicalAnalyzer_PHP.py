import re
if __name__ == "__main__":
    phpcode = ''' <?php
    class MyClass {
    function abc(){ $i=5;
    $z=$i*2;
    echo "One '$=".$z;}
    }
 ?>'''

    arr = phpcode.split()
    linedetarr = phpcode.split('\n')
    print(linedetarr)
    dict_lines ={}
    counter = 1
    for i in linedetarr:
        dict_lines[i] = counter
        counter +=1
    print(dict_lines)
    print(arr)
    operators = ['+','-','*', '/']
    currentline = 1
    for syntax in range(len(arr)):
        if arr[syntax] == '<?php':
            print('1,1,php-opening-tag')
        elif arr[syntax] == "class":
                print('2,1class')
                print(arr[syntax+1])
        elif arr[syntax] == "{":
            print('curly brace opening')
        elif arr[syntax] == "}":
            print("curly brace closing")
        elif arr[syntax] == "function":
            print("function")
           # if re.search('[A-Z]',arr[syntax]):
            print('type-identifier', arr[syntax+1][0:3])
            print('bracket-opening')
            print('beacket-closing')
        if '$' in arr[syntax]:
            print('variable')
            if '=' in arr[syntax]:
                print('assign')

        elif arr[syntax] == '?>':
            print('7,1,php-closing-tag')
