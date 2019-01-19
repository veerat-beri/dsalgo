# Question1
# Max. Marks 6.00
# In the given nested representation of binary trees, (A B C), B and C are left and right sub trees of node A.
# B and C may be NULL or further nested. Which of the following representations is a valid binary tree?
#
# (1 2 (4 5 6 7))
# (1 (2 3 4) 5 6) 7)
# (1 (2 3 4)(5 6 7))
# (1 (2 3 NULL) (4 5))


# Question2
# Max. Marks 6.00
# What is the output of the following Java code:
#
# class TestClass {
#
#     int a =100;
#
#     public static void main(String args[] ) throws Exception {
#
#         int a = 200;
#         TestClass t= new TestClass();
#         System.out.println(a);
#         t.m();
#
#     }
#
#     void m(){
#         System.out.println(a);
#     }
# }
# 100 100
# 200 100
# 100 200
# Compilation error

# Question3
# Max. Marks 4.00
# If a machine needs 200 seconds to sort 200 bills by using bubble sort, how many bills will it sort in 800 seconds?
#
# 400
# 800
# 750
# 1000

# Question4
# Max. Marks 4.00
# Choose the correct option from the following regarding Iaas
#
# a)It has virtual machines with software preinstalled
#
# b)Scaling can be increased or decreased easily
#
# c)Snapshot of the data cannot be done hence increases the security
#
# d)Softwares in Virtual machines are generally open sourced ones
#
# ab
# bd
# ba
# cd


# Question5
# Max. Marks 2.00
# Which of the following statements about data structures is incorrect?
#
# Arrays are dense lists and static data structures.
# The data elements in a linked list need not be stored in adjacent spaces in the memory.
# Pointers store the next data element of a list.
# Linked lists are a collection of nodes that contain data and a pointer to the next node.


# Question6Max. Marks 100.00
# Count the Solutions
# Given an integer . Now, you have to count the total number of integral solutions of the equation a + b^2 +c^3 + d^4
# such that 0 <= a, b, c, d <= 10^3.
#
# Input Format
#
# The only single line of the input contains an integer , as mentioned in the problem statement.
#
# Output Format
#
# In the single line of the output print the count of the total number of integral solutions of the given equation.
#
# Constraints
# 0 <= S <= 10^18
#
# Sample Input
# 2
# Sample Output
# 12
# Explanation
# Following are the possible number of solutions:
#
#
#
#
#
#
#
#
#
#
#
#
#
# Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.
# Time Limit: 2.0 sec(s) for each input file
# Memory Limit: 256 MB
# Source Limit: 1024 KB

class A:
    def xy(self):
        print('in A')


class B:
    def xy(self):
        print('in B')


class C(A, B):
    def xy(self):
        super(C, self).xy()

C().xy()