#Programmer_name = Ahmad Bin Abu
#Matric. No = MS2025123499
#Problem Description = Program to print student details, star pattern, indented text and calculate marks using escape characters

#Store student details in variables
student_name = "Ahmad Bin Abu"
matric_no = "MS2025123499"

#Perform arithmetic to calculate marks
mark1 = 2
mark2 = 10
total_mark = mark1 * mark2

#Print the output using escape characters(\n for new lines, \t for tab)
print(
    f"Name: {student_name}\t\t\tMatric. No: {matric_no}\n\n",
    f"*\t\t\t*\n",
    f"**\t\t**\n",
    f"***\t***\n",
    f"********\n",
    f"***\t***\n",
    f"**\t\t**\n",
    f"*\t\t\t*\n\n",
    f"This is my\n",
    f"\tsecond\n",
    f"\t\tassignment\n",
    f"I want 2x10 marks, which is {total_mark} full marks"
)
