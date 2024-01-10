valid_java = ['1.6','1.7','1.8','1.9']
host_java = input("Enter a java version you want to valid : ") 

if host_java in valid_java:
    print(f"Host has a valid Java Version {host_java}")
else:
    print(f"Host doesn't have a valid Java Version { host_java}")

db_user = ['db_admin', 'df_conf', 'db_install']
check_db_user = input("Enter DB User ID: ")

if check_db_user in db_user:
    print( "Your allowed to manage DB instance")
else:
    print("You are not allowed to manager DB")