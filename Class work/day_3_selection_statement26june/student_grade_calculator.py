#A school assigns grades based on the marks obtained by students according to the following criteria:
#please write a Python program to accept marks from the user and display the corresponding grade.
'''problem statement :Write a Python program to accept marks from the user and display the corresponding grade.

------Marks 90 and above → Grade A-----
------Marks 75 to 89 → Grade B------
------Marks 50 to 74 → Grade C------
------Below 50 → Grade F-------

-----Sample Input-----
-----Enter Marks: 92-----
-----Sample Output-----
-----Grade A---

-----Sample Input-----
-----Enter Marks: 80-----
-----Sample Output-----
-----Grade B------

-----Sample Input-----
-----Enter Marks: 65-----
-----Sample Output-----
-----Grade C-----

-----Sample Input-----
-----Enter Marks: 35-----
-----Sample Output-----
-----Grade F-----
'''


marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade F")