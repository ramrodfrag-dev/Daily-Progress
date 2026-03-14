# This contain some important information about the Operating system which can be asked in the interviews
# maximum based on the linux operating system

'''1. Commands to terminate the process in execution'''
#linux->killall <process_name>
#linux->pkill <process_name>
#linux->kill <PID_number>
#windows->taskkill /IM <image_name> /F

#Ex: Use python3 and the vim processes to run in the terminal and in the other terminal terminate them by killall



'''2. Which system call cretes a new child process'''
#linux->fork()
#windows->CreateProcess()



'''3. To know current process executing'''
#linux: To know processes in current terminal->ps
#linux: To know all processes->ps aux
#linux: Live process monitoring->top

#windows: To know process->tasklist
#windows: Live process monitoring->Task Manager



'''4. Bankers Algorithm'''
# This algorithm checks whether the resource allocation will result the system in a safe state or not
# If the system goes to unsafe state after resource allocation then the permission for the resource allocation is denied, which prevents the dead lock in system

# safe state: It is a system state where there exists a particular sequence in which all teh processes executes without falling into the deadlock situation, even if all processes requests maximum resources




''' 5. I/O Multiplexing mechanisms used by OS to monitor multiple file descriptors simultaneously'''
# Select,poll,epoll are used.
# File descripter is a number which represents open files

# Select() Uses old model to get the socket which is ready to connect. It maximum checks about 1024 sockets at max
# Poll() It is a improved version of the select but  also poorly performs when there are many thousands of the connections
# epoll() It is the new version which is scalablew to many ports.

#epoll() uses a red-black tree like data structure in it.

#-> These functionalities are just returning the socket which is currently available for the connection.


'''6. Difference between the Dangling pointer and the Memory leak'''
# The memory leak is nothing but we are assigning a pointer a value then later if we are directly giving the pointer another value before freeing up the space then the location is not accessible, so it is a memory leak.
# The Dangling pointer is nothing but if we are freeing only the location by free(pointer) and not the variable then the variable contains the old location which cannot be accessible.


'''7. '''