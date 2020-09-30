import file_search
import os

i = 0
def finder(str):
    for i in range(1):
        # try:
        #     file_search.set_root('C:\\')
        #     input__ = str
        #     files = file_search.searchFile(input__)
        #     os.startfile(files[0])    
        # except Exception as c:      
        #     print('oops! File not found in C drive.')
        #     i = i+1  
        try:
            file_search.set_root('E:\\')
            input__ = str
            files = file_search.searchFile(input__)
            os.startfile(files[0])
            break    
        except Exception as e:      
            print('oops! File not found in E drive.')
            # i = i+1  
        try:
            file_search.set_root('F:\\')
            input__ = str
            files = file_search.searchFile(input__)
            os.startfile(files[0])
            break    
        except Exception as f:      
            print('oops! File not found in F drive.')
            break
            # i = i+1 
            # if i == 3:
            #     print("Soory! File not found") 
if __name__ == "__main__":

    a = input("Enter: ")
    finder(a)

















# def e(val, val2, val3):
#     file_search.set_root('E:\\')
#     try:
#         input__ = val
#         files = file_search.searchFile(input__)
#     except expression as identifier:
#         pass
#     try:
#         input__ = val2
#         files = file_search.searchFile(input__)
#     except expression as i:
#         pass
#     try:
#         input__ = val3
#         files = file_search.searchFile(input__)
#     except expression as ide:
#         pass
#     try:
#     os.startfile(files[0])    
# except Exception as e:      
#     print('oops! File not found.') 






# def val_find(name):
#     low = name.lower()

#     hig = name.upper()

#     length_ = int(len(name))
#     p1 = name[0]
#     p2 = p1.upper()
#     p3 = name[1:length_]
#     p4 = p3.lower()

#     total = p2+p4

#     e(low, hig, total)
    


# a = "aadarsh"

# val_find(a)


    



