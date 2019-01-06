# Min-Max Weighted Edge
# Given a tree with  nodes and  bidirectional edges, and given an integer . Now, you have to assign the weights to the edges of this tree such that:
#  the sum of the weights of all the edges is equal to
#  for every possible diameter of the tree, the maximum weight over all the edges covered by its path is the minimum possible
#
# You have to output this minimum possible edge weight.
#
# Note: The diameter of a tree is the number of nodes on the longest path between two leaves in the tree.
#
# Input Format
#
# The first line of the input contains an integer , the total number of test cases.
# The first line of each test case contains two space-separated integers  and , the number of nodes in a tree and the integer  as mentioned in the problem statement.
# Then the  lines follow, each containing two space-separated integers  and  representing that there is a bidirectional edge between the nodes  and .
#
# Output Format
#
# For each test case output the minimum possible edge weight which satisfies the above-mentioned conditions.
#
# Constraints
#
#
#
#
#
# Sample Input
# 2
# 8 18
# 1 2
# 1 3
# 2 4
# 2 5
# 2 6
# 3 7
# 3 8
# 7 15
# 1 2
# 1 3
# 1 4
# 2 5
# 2 6
# 3 7
# Sample Output
# 3
# 0
# Explanation
# Sample test case  Given below is one of the best ways to assign weights to the edges
#
#
#
# Sample test case  Note that there are only two possible diameters of the tree:  to  and  to  , so we can assign  to the edge  and for every possible diameter of the tree, the maximum weight over all the edges covered by its path is
#
#
#
# Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.
# Time Limit: 1.0 sec(s) for each input file
# Memory Limit: 256 MB
# Source Limit: 1024 KB