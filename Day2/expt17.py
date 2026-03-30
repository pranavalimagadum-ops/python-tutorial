#1. rstrip()===>To remove spaces at right hand side
#2. lstrip()===>To remove spaces at left hand side
#3. strip() ==>To remove spaces both sides
programming =input("enter your programming name:")
p_name=programming.strip(0)
if p_name=='python' :
    print(p_name)
elif p_name=='java':
    print(p_name)
elif p_name=="Cpp" :
    print(p_name)
else:
    print("wrong programming name")                      