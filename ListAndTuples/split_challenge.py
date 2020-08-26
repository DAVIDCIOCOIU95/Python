# separate challenge
num_string = "9,223,372,036,854,775,806"
num_list = num_string.split(",")
for i, v in enumerate(num_list):
    num_list[i] = int(v)
print(num_list)