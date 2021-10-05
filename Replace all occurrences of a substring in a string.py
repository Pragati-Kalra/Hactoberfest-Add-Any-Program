test_str = "hactoberfesthacktoberfest"
  
# printing original string
print("The original string is : " + test_str)
  
# Swap Binary substring
# Using translate()
temp = str.maketrans("es", "er")
test_str = test_str.translate(temp)
  
# printing result 
print("The string after swap : " + str(test_str)) 
