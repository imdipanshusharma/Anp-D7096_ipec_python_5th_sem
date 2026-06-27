"""------------------Problem Statement-------------------------------
Students are allowed to enter the examination hall only if they are carrying their admit card. 
Accept input as: 
• 1 → Admit Card Available  
• 0 → Admit Card Not Available  
If the input is 1, display: 
Enter Examination Hall 
Otherwise, do not display anything. 
-----------------------------------------------------
Sample Input 
1
----------------------------------------------------- 
Sample Output 
Enter Examination Hall
 """
#------------------------------Coding------------------------------------
# Exam Hall Entry
print("----------------------------------------------------")
admit_card = int(input("Enter 1 if Admit Card is Available, otherwise 0: "))
#------------------check validation of admit card----------------------------------
if admit_card !=1 and admit_card !=0:
    exit("Only enter 1 or 0")
#--------------------------chaking Condition -------------------------
if admit_card == 1:
    print("Enter Examination Hall")
#-------------------------------------------------------------------

print("----------------------------------------------------------------")
"""
Output :
----------------------------------------------------
Enter 1 if Admit Card is Available, otherwise 0: 1
Enter Examination Hall
----------------------------------------------------------------
"""


