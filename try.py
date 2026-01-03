# 
#employees = "Fortune is a great girl, I love her so much."
employees = ["Eugene", "Fortune", "Mary"]
file_path = "C:/Users/DELL/OneDrive/Desktop/names.txt"

with open(file_path, "w") as file:
  for name in employees:
    file.write(name + " " )
    print(f"File path {file_path} was created.")
