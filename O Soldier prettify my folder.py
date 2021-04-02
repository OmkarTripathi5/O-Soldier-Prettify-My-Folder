import os


def soldier(path,file,format):
    os.chdir(path)
    dir_list = os.listdir()
    format_list = []
    with open(file,"r") as f:
        obj = f.readlines()
    list_obj =  list(map(lambda x:x.replace("\n",""),obj ))
    for item in dir_list:
        if item.endswith(format):
            format_list.append(item)

        if item in list_obj:
            continue

        else:
            new_file = item.capitalize()
            os.renames(item,new_file)

    for index,file1 in enumerate(format_list):
        if file1 in list_obj:
            continue
        else:
            new_file1 = f"{index}{format}"
            os.renames(old=file1,new=new_file1)


soldier("path://","file name","format_file")

