def sloveLeetHotSheet(input_path:str,output_file_path:str):
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