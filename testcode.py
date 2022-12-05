requirment_file = open("requirments.txt", "r")
requirments = requirment_file.readlines()
requirment_list = [requirments_name.replace("\n" , "") for requirments_name in requirments]
print(requirment_list)
