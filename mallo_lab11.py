
gradelist = []
passers = 0
for num in range(5):
    x = int(input("enter the student grade: "))
    if x < 40 or x > 100:
        break
    else:
        gradelist.append(x)
        if x >= 75:
            passers = passers + 1
if x < 40 or x > 100:
    print("invalid grade, the grade must be between 40 and 100")
else:
    sum= (gradelist[0]) + (gradelist[1]) + (gradelist[2]) + (gradelist[3]) + (gradelist[4])
    average = sum/len(gradelist)
    percent_passers = passers/ 5* 100
    print(f"average between all students: {average:}")
    print(f"passers: {passers:}")
    print(f"%: {percent_passers:.2f}%")
    print(f"grades: {gradelist}")
    
    
            
            
            
            
            
        
        

    
    
