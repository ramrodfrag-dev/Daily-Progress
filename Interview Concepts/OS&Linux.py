# This contain some important information about the Operating system which can be asked in the interviews
# maximum based on the linux operating system

'''1. Commands to terminate the process in execution'''
#linux->killall <process_name>
#linux->pkill <process_name>
#linux->kill <PID_number>   Here it shutdowns gracefully
#linux->kill -9 <PID_number>    Here it forcefully kills it and removes from memory
#windows->taskkill /IM <image_name> /F

#Ex: Use python3 and the vim processes to run in the terminal and in the other terminal terminate them by killall

'''Notes regarding their signals also:
1.SIGKILL: forcefully kills the process
2.SIGTERM: politely asks the process to terminate
3.SIGSTOP: pause execution
4.SIGINT: It is signal interrupt thing(ctrl+C)
'''
# We execute the commands and then these convert to the signals and then they go to kernel and then they go to the process to stop or termianate


'''2. Which system call cretes a new child process'''
#linux->fork()
#windows->CreateProcess()



'''3. To know current process executing'''
#linux: To know processes in current terminal->ps
#linux: To know all processes->ps aux
#linux: Live process monitoring->top

#windows: To know process->tasklist
#windows: Live process monitoring->Task Manager


'''Note:(some important commands)
a.free: gives all cpu, memory consumption and also tells how much is available now to use
b.free -h: gives the abogve info but in the human redeable format that is in gigabytes
'''


'''4. Bankers Algorithm'''
# This algorithm checks whether the resource allocation will result the system in a safe state or not
# If the system goes to unsafe state after resource allocation then the permission for the resource allocation is denied, which prevents the dead lock in system

# safe state: It is a system state where there exists a particular sequence in which all teh processes executes without falling into the deadlock situation, even if all processes requests maximum resources




''' 5. I/O Multiplexing mechanisms used by OS to monitor multiple file descriptors simultaneously'''
# Select,poll,epoll are used.
# File descripter is a number which represents open files

# 1.Select() Uses old model to get the socket which is ready to connect. It maximum checks about 1024 sockets at max
# 2.Poll() It is a improved version of the select but  also poorly performs when there are many thousands of the connections
# Poll asks OS everytime then it checks all lists and gives the available sockets, it is not suitable for large systems
# 3.epoll() It is the new version which is scalablew to many ports.
#epoll uses the event-based mechanism, all the sockets are registerd in OS once then if the socket is ready to take input then OS notifies us. so it is scalable
#epoll() uses a red-black tree like data structure in it.
#Ex: Ngnix, Redis,Node.js are examples for the epoll()

#-> These functionalities are just returning the socket which is currently available for the connection.

'''Some basic file descripters:
0->stdin
1->stdout
2->stderr
Ex: read(0,buffer,100)  ->It reads from the keyboard as the file descripter is 0 which is stdin
'''



'''6. Difference between the Dangling pointer and the Memory leak'''
# The memory leak is nothing but we are assigning a pointer a value then later if we are directly giving the pointer another value before freeing up the space then the location is not accessible, so it is a memory leak.
# The Dangling pointer is nothing but if we are freeing only the location by free(pointer) and not the variable then the variable contains the old location which cannot be accessible.


'''
Notes: Important system calls
1. fork(): It creates a child process
2. exec(): replace the process code (or) replaces the process memory with a new program
3. wait(): parent waits for the child
4. exit(): terminate the process
'''


