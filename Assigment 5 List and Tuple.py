"""
Python Programming Questions - LIST Basic Level
1. Write a Python program to create a list of integers and print its elements.
    li = [1 ,2 , "Aakash" , True , 22.8]
    print(li)

2. Write a program to find the sum and average of all elements in a list.
    li = [1 ,2 , 4, 5,10]
    x = sum(li)
    print(x)
    print(x//len(li))


3. Write a program to find the largest and smallest element in a list.
    li = [1, 2, 3, 4, 5]
    print(min(li))
    print(max(li))
    
    
4. Write a Python program to count the number of elements in a list without using len().
    li = [1,2,3,1,31,2]
    count = 0
    for a in li:
        count+=1
    print(count)

5. Write a program to reverse a list without using built-in functions.
    li = [1,2,3,4,5]
    li2 = []
    for a in li:
        li2 = [a] + li2
    print(li2)
    
    or
    li = [1,2,3,4,5]
    li2 = []
    for a in range(len(li) , 0 , -1):
        li2.append(a)
    print(li2)
    
6. Write a program to check if an element exists in a list.
    num = 10
    li = [1,2,3,4,5,6]
    if num in li:
        print("valid")
    else:
        print("Invalid")

7. Write a Python program to remove duplicate elements from a list.
    li =[ 1 , 2, 3, 4,5,  6,7 , 22,3 , 4,2] 
    print(list(set(li)))

                    OR
    li = [1,2,4,5,4,3,2,1,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
    result = [] 
    for a in li:
        if a not in result:
            result.append(a)
    print(result)

8. Write a program to sort a list in ascending and descending order.
    li =[ 1 , 2, 3, 4,5,  6,7 , 22,3 , 4,2] 
    print(sorted(li))
    print(sorted(li,reverse=True))
    print(li)
    
=================================================================================================================

Intermediate Level 

9. Write a program to merge two lists and remove duplicates. 
    li1 = [1,2,3,4,5,6]
    li2 = [4,5,6,7,8,9]

    li1.extend(li2)
    print(li1)
    result = []
    for a in li1:
        if a not in result:
            result.append(a)
    print(result)

10. Write a program to find common elements between two lists. 
    li1 = [1,2,3,4,5,6]
    li2 = [4,5,6,7,8,9]
    result = []

    for a in li1: 
        if a  in li2:
            result.append(a)
    print(result)

11. Write a program to split a list into even and odd numbers. 
    li = [9,8,7,6,5,4,3,2,1] 
    even = []
    odd= []
    for a in li:
        if a%2==0:
            even.append(a)
        else:
            odd.append(a)
    print(even)
    print(odd)
    
12. Write a program to rotate a list by n positions.
    li = [1,2,3,4,5]
    x = 2
    result  = li[-x:] + li[:-x]
    print(result)

                                      OR 
    
    li  = [1,2,3,4,5]
    x=  2
    for a in range(x):
        last = li.pop()
        li.insert(0, last)
        print(last)
    print(li)


13. Write a Python program to find the second largest number in a list. 
    li = [21,22,3,44,45,5,78, 78] 
    largest  = 0
    secondlargest = 0
    for a in li:
        if a > largest :
            secondlargest = largest
            largest = a
        elif a > secondlargest and a != largest:
            secondlargest = a
    print(secondlargest)

14. Write a program to flatten a nested list. 
    li = [1,2,[3,4],5,6]
    result = []
    for a in li :   
        if type(a)== list:
                for item in a: 
                result.append(item)
        else:
            result.append(a)
    print(result)

15. Write a program to count frequency of each element in a list.
    li = [1,2,3,4,14,5,3,15,5,2]
    visited = []
    for item in li:
        if item not in visited:
            visited.append(item)
            print(item, " : ",  li.count(item))
 
16. Write a program to replace all negative numbers with zero in a list. 
    li = [1,2,-3,-7 ,4]
    for i in range(len(li)):
        if li[i] < 0:
            li[i] = 0
    print(li)

            OR
            
    li = [1,2,-3,-7 ,4]
    result = []
    for i in range(0 , len(li)):
        if li[i] < 0:
            result.append(0)
        else:
            result.append(li[i])
    print(result)

            OR

    li = [1,2,-3,-7 ,4]
    result = []
    for i in li :
        if i < 0:
            result.append(0)
        else:
            result.append(i)
    print(result)
====================================================================================================================
Advanced Level 
17. Write a program to remove all occurrences of a given element from a list. 
    li = [1,2,3,4, 5 ,2 ,2]     # This method is not suitable because of indexing ( list is mutabble )
    x  = 2
    for a in li : 
        if a == x:
            li.remove(a)
    print(li)

ANSWER  li = [1,2,3,4, 5 ,2 ,2]
        result = []
        x =  2
        for a in li:
            if a != x:
                result.append(a)
        print(result )


18. Write a program to check if a list is a palindrome. 
    li  = [1,2,1,2]
    if li == li[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

19. Write a Python program to find missing numbers in a given list of consecutive integers. 
    li  = [1,2,4, 8,5]
    result  = [] 
    for a in range(1  , max(li)+1):
        if a not in li:
            result.append(a)
    print(result)
    
    
20. Write a program to perform element-wise addition of two lists. 
    li1 = [1, 2, 3]
    li2 = [4, 5, 6]
    x = []
    for a in range (len(li1)):
    x.append(li1[a] + li2[a])
    print(x)
    
21. Write a Python program to find the longest increasing subsequence in a list. 

22. Write a program to group elements based on frequency. 




============================================================================================


23. Write a Python program to create a tuple and print its elements. 
    # t = (1,2,3,"Aakash" ,  True ,22.6)

    t= tuple([1,2,3,4,4])
    print(t)
    
24. Write a program to find the length of a tuple. 
    t =  (1,2,31,2,1,3)
    x = len(t)
    print(x)
    
25. Write a program to find the maximum and minimum element in a tuple. 
    t =  (1,2,1,5,0,3,6,2,64,46,1231)
    print(max(t))
    print(min(t))
    
26. Write a program to convert a tuple into a list. 
    t = (1,2,3,4,5,6)
    print(t)
    print(type(t))

    t= list(t)
    print(t)
    print(type(t))

                                        OR

    t = (1,2,3,4,5,6,7)
    li = []
    for a in t:
        if a not in li:
            li.append(a)
    print(li)
    print(type(li))
    
27. Write a program to check if an element exists in a tuple. 
    t = (1,2,3,4,5,6,7,8)

    if 8 in t:
        print("Yes")
    else:
        print("no")
        
                            OR

    t = (1,2,3,4,5,6,7,8)
    x = 70
    flag = False

    for i in t:
        if i == x:
            flag = True
            break

    if flag:
        print("Element Exist ")
    else:
        print("Not Exist")      
        
28. Write a program to count occurrences of an element in a tuple. 
    t = (1,2,3,2,1,2,1,4)
    x = t.count(2)
    print(x)
    
                        OR
    t = (1,2,3,2,1,2,1,4)
    x = 4
    count = 0
    for i in t:
        if i == x:
            count+=1
    print(count)


29. Write a program to slice a tuple and display the result. 
    t = (1,2,3,4,5,6,7,8,9)
    print(t[2:8]) 
    
30. Write a program to find repeated elements in a tuple. 
    t = (1,2,3,4,5,6,1,2,3,4,1)
    originall = []
    repeated = []
    for i in t:
        if i not in originall:
            originall.append(i)
        elif i not in repeated:
            repeated.append(i)
    print(repeated)

31. Write a program to merge two tuples. 
    t = (1,2,3,4)
    t2  = (4,5,6)
    res = ()
    for a in t:
        if a not in res:
            res = res +(a,)
    for b in t2:
        res  = res + (b,)
    print(res)
    
                                         # With Remove Duplicate value
    t = (1,2,3,4)
    t2  = (4,5,6)
    res = ()
    for a in t:
        if a not in res:
            res = res +(a,)
    for b in t2:
        if b not in res:
            res  = res + (b,)
    print(res)

32. Write a program to unpack elements of a tuple into variables.
    t = ( "Aakash" , 23 , "Ghaziabad")
    Name , Age , City = t
    print(Name) 
    print(Age) 
    print(City)  
    
                            OR
    t = ( "Aakash" , 23 , "Ghaziabad")
    a =t [0]
    b = t [1]
    c = t [2]
    print(a)
    print(b)
    print(c)
    
33. Write a Python program to sort a tuple.
    t = (1,3,2,4,6,5,9,7,8)  
    res =  tuple(sorted(t))
    print(sorted(res))  # Ascending 
    print(type(res))
    print(sorted(t ,  reverse= True))   # Discending 
    
34. Write a program to convert a list of tuples into a dictionary.
    li = [("a" ,  1 , 12) , ("b" , 2 ,  3), ("c" , 3,4)]
    x =  dict(li)
    print(x)
    
                OR
                
    li = [("a" ,  1 ) , ("b" , 2 ), ("c" , 3)]
    d = {}
    for k , V in li:
        d[k]= V
    print(d)
                OR
                
    li = [("a" ,  1  , 2) , ("b" , 3 ,4 ), ("c" , 5, 6)]
    d = {}
    for item in li:
        d[item[0]]= item[1:]
    print(d)
    
                OR

    li = [("a" ,  1  , 2) , ("b" , 3 ,4 ), ("c" , 5, 6)]
    d = {}
    for k , V , v2 in li:
        d[k] = (V,v2)
    print(d)
    
35. Write a program to find the index of an element in a tuple.
    t = (21,22,23,24,25)
    x = 23
    res = t.index(x)
    print(res) 
    
                OR
                
    t = (21,22,23,24,25)
    x = 23
    for i in range ( len(t)):
        if t[i] == x:
            print(i)
            break
            
36. Write a program to remove an element from a tuple (without directly modifying it). 
    t = (21,22,23,24,25)
    x =  23
    t2 = ()
    for i in t :
        if i != x:
            t2 = t2 + (i,)
    print(t2)
    
                        OR

    t = (21,22,23,24,25)
    x =  23
    t2 = []
    for i in t :
        if i == x:
            continue
        t2.append(i)
        # t2 = tuple(t2)                                    Gives Error 
                                                            # 1. Lekin ab t2 list nahi hai.
                                                            # 2. yaani tuple hai.
                                                            # 3. Tuple ke paas append() method nahi hota.=> Isliye error:
    t2 = tuple(t2)
    print(t2)
    print(type(t2))

    
37. Write a program to find common elements between two tuples.
    t1 = (1,2,3,4,5,6)
    t2 = (4,5,6,7,8,9)
    res = ()            # if you need output in tuple 
    for i in t1:
        if i in t2:
            print(i)    # normal ans without in Tuple
            res = res + (i,)                
    print(res)          # Answer in Tuple

38. Write a Python program to check if a tuple is a palindrome. 
    t = ('a' , 'k' , 'a')
    if t == t[::-1]:
            print("Palindrome")
    else:
        print("Not Palindrome")
        
39. Write a program to find the element with maximum frequency in a tuple. 
    t = (1,2,1,2,2)
    max_count = 0
    max_element = None
    for i in t:
        res =t.count(i)
        
        if res > max_count:
            max_count = res
            max_element = i
    print("Element = "  , max_element)
    print("Frequency = " ,  max_count)
    
40. Write a program to create a nested tuple and access its elements. 
    t = (1,2, (2,3) , 5,6 , (7,(8,9)))
    print(t[5][1][1])



""" 





        
        

    







        
        

        



    
    

    

           

       
 

        

        

        
    


        





