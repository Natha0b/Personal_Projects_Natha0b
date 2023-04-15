
list = [1,1,1,12,2,2,3,5,7,8,8,9,5,3]
number = []
count = 0

for i in range(0, len(list)):
    if list[i] not in number:
        for n in range(0, len(list)):
            if list[i] == list[n]:
                count += 1
        print("El numero {} se repite {} veces" .format(list[i], count))
    number.append(list[i])
    count = 0
     
            
    
        
        

            


    

    






# for i in range(len(list)):

#     if i == 1:
#         print("3 unos hay ")

#     elif i == 2:
#         print("2 dos hay")

#     elif i == 3:
#         print("2 tres hay")
    
#     elif i == 12:
#         print("1 doce hay")
    
#     elif i == 7:
#         print("1 siete hay") 

#     elif i == 8:
#         print("2 ochos hay")
    
#     elif i == 9:
#         print("1 nueve hay")
