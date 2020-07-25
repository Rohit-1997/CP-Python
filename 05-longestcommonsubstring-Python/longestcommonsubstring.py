# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    if s1 == "" or s2 == "":
        return ""
    s1_size = len(s1)
    s2_size = len(s2)
    dp_table = [[0 for j in range(s2_size+1)] for i in range(s1_size+1)]
    max_value = 0
    row_des = -1
    col_des = -1

    # building the tabel to find the max common string
    for i in range(1,s1_size+1):
        for j in range(1,s2_size+1):
            print("The current comparision: ", s1[i-1], s2[j-1])
            if s1[i-1] == s2[j-1]:
                dp_table[i][j] = 1 + dp_table[i-1][j-1]
                if dp_table[i][j] >= max_value:
                    row_des = i
                    col_des = j
                    max_value = dp_table[i][j]
    
    if max_value == 0:
        return ""

    # the last character
    print("The dp table: ", dp_table)
    print("The max value: ", max_value)
    print("The row and col value: ", row_des, col_des)
    current_cell_value = dp_table[row_des][col_des]
    result = ""

    while current_cell_value != 0:
        result += s2[col_des - 1]
        row_des -= 1
        col_des -= 1
        current_cell_value = dp_table[row_des][col_des]
    print("The longest common substring is: ", result[::-1])
    return result[::-1]


print(longestcommonsubstring("abcdef", "ghi"))
    
    





