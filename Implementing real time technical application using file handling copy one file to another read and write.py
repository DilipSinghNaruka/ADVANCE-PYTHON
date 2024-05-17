# Implementing real time/technical application using file handling /copy one file to another read and write.


# Step 1: Create a new file and write some content to it
file_path = "example.txt"
with open(file_path, "w") as file:  # Open the file in write mode
    file.write("This is the original content of the example file.\n")
    file.write("Adding a second line of content.\n")

# Step 2: Read content from the file
with open(file_path, "r") as file:  # Open the file in read mode
    content = file.readlines()  # Read all lines into a list

print("Original file content:")
for line in content:
    print(line.strip())  # Strip newline characters for clean output

# Step 3: Copy content from one file to another
backup_file_path = "example_backup.txt"
with open(backup_file_path, "w") as backup_file:  # Open the backup file in write mode
    backup_file.writelines(content)  # Write all lines to the backup file

print("\nBackup file content:")
with open(backup_file_path, "r") as backup_file:  # Read the backup file to verify
    backup_content = backup_file.readlines()

for line in backup_content:
    print(line.strip())
