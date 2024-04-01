import os


def sloveLeetHotSheet(input_path:str,output_file_path:str):
    '''对于每种题目的难度做标记处理
        删除标记之后的文字
    '''
    target1 = ", Easy"
    target2 = ", Medium"
    target3 = ", Hard"
    processed_lines = []
    with open(file=input_path,mode='r') as f:
        lines = f.readlines()
        with open(output_file_path, 'w') as s:
            for line in lines:
                if line.find(target1) != -1 :
                    processed_line = line[:line.find(target1)]+' | Easy\n'
                    processed_lines.append(processed_line)
                    s.writelines(processed_line)
                if line.find(target2) != -1 :
                    processed_line = line[:line.find(target2)]+' | Medium\n'
                    processed_lines.append(processed_line)
                    s.writelines(processed_line) 
                if line.find(target3) != -1 :
                    processed_line = line[:line.find(target3)]+' | Hard\n'
                    processed_lines.append(processed_line)
                    s.writelines(processed_line) 

def readFileName(input_path:str,target_path:str,output_file_path:str):
    '''
    input_path:读取目录的路径
    target_path:待处理文件的路径
    output_file_path:写出路径
    for dirpath, dirnames, filenames in os.walk(input_path):
        print("目录路径:", dirpath)
        print("子目录名字:", dirnames)
        print("文件名字:", filenames)
        '''
    lst = []
    writed = {}

    #获取目录下所有的文件名，放入数组中
    for dirpath, dirnames, filenames  in os.walk(input_path):
        for file in filenames:
            name = int(file.split('.')[0])
            lst.append(name)

    #读取需要处理的文件
    with open(file=target_path,mode='r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('\n','')
            #截取每行的题目序号和目录下解决的题目进行比较
            #转换成数字便于排序，已经解决的题目打上标记
            number = int(line.split('. ')[0])
            if number in lst:
                writed[number] = line.split('. ')[1] + '| Finished\n'
                #result = line.replace('\n','') + '| Finished\n'
                #writed.append(result)
            else:
                writed[number] = line.split('. ')[1] + '| \n'
                #result = line.replace('\n','') + '\n'
                #writed.append(result)
    # 写入目标路径 
    with open(output_file_path, 'w') as s:
        for i in sorted(writed):
            result = str(i)+'. '+ writed[i]
            #print(result)
            s.write(result)        