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


# Complete OS:
'''A software that controls the computer hardware,software resources, program services is called OS'''

# -> OS sits in btw both and abstracts the thing which are not required and only make the required things available to appliacations making it simpler and light weight
# -> OS manages the processes like:
# 1.when to delete them, 
# 2.when to schedule them to use CPU,
# 3.whom to alloacte storage, ram or resources securely to make overall performance better, 
# 4.manages devices by interruptions, I/O mechanisms,etc


'''Kernel vs OS
Kernel: System level tasks, process management, memory management=>(resource management)
OS: It offers gui and also handles app security and system resources,file system=>(Kernel + file management + Utility programs + User Interface)
'''
# Kernel is a mandatory core engine(Primary part) which runs always in the background at all times(eg:linux kernel)
# OS is Kernel + other things or tools which require to control overall hardware.(may be some tools like cli,gui,or inbuilt applications)
# Kernel is the one which controls/manages how the software and the hardware communicates with each other.
# OS can be accessed by user with the help of cli,gui but the kernel operates in background and cannot be accessed by anyone(Independent).
# Kernel runs only on priveldged kernel mode while the OS runs on kernel + user modes


'''Types of modes:'''
# 1. Kernel(Priviledged mode): Kernel executes in this mode where it has full hardware control commands are available.(Can modify hardware freely)
# 2. User(Restricted mode): Apps executes in this mode where there are many restrictions unlike kernel mode.(Cannot modify harware freely)

#SO, Apps cannot access harware easily so, they use kernel in between.
# Application
#     ↓ read()
# System Call       -> So, applications uses system calls to communicates with kernel to do necessary
#     ↓
# CPU privilege transition
#     ↓
# Kernel
#     ↓             ->  perform privileged operation on hardware after their request is validated
# Filesystem
#     ↓
# Device Driver
#     ↓
# Storage Device


'''System calls: It is the controlled interface through which a user program requests services from the OS kernel.'''
import os,sys
pid=os.fork() #type:ignore
open('r','./')
# read()
# write()
# close()
# exec()
# wait()        # These all system calls are different in different OS.
# mmap()

# System Calls are generally more machinary related and the priviledge level of it is changing mny times from app to kernel whereas the normal calls will remain in same priviledge most of time and executes.


'''Interrpt mechanisms: interrupt is an asynchronous signal sent by hardware or software to the processor, indicating an event that requires immediate attention'''
# Device
#     ↓ Interrupt by a flag
#   CPU
#     ↓
# Halts its current execution flow and store operational data
#     ↓
# Transfers control to Interrupt service routine(Interrupt handler)->Gives CPU resource
#     ↓
# executes its commands
#     ↓
# release resources and sends the control to the CPU ->by removing the interrupt flag
#     ↓
# Load the last operational data and execute from that point


# This Interrupt is so better because hardware tells when it requires attention from cpu instead of CPU continuously checking each harware time to time.
#  The process above mentioned is called Polling which is inefficient compared to Interrupt handling


'''System calls are generated by the applications in order to acess hardware while the Interrupt is raised by hardware in order to get control of CPU to do something'''

'''Program vs Process'''
# Program: It is a passive set of instructions stored in the disk which can be executed.
# Process: A program which is running along with it's resources,execution state,etc(A program in execution is called process)
# -> For a same program there can be multiple instances(processes)


# Each process will have their own:
'''
1.registers/state 
2.stack
3.heap
4.open resources
5.process ID and Process Control Block(PCB)
6.address space   ->It has its own logical address space(stack,heap,BSS,Data,code) in same order from higher to lower addresses'''

# Process states:
#              admitted
#  1.NEW ----------------→2.READY
#                          |
#                          | scheduler
#                          ↓
#                       3.RUNNING ---exit--->5.TERMINATED
#                       /       \
#                      /         \
#               I/O wait         |                              -> 1.NEW: Process is created
#                   ↓            |                                 2.READY: Process is ready to run but waiting for CPU.
#              4.WAITING         |                                 3.RUNNING: Currently executing on CPU.
#                   |            |                                 4.WAITING: Waiting for something, such as: disk I/O, network I/O, lock, event
#                   | I/O done   |                                 5.TERMINATED: Finished execution
#                   ↓            |                                 -> See how the process goes from each state to other when high priority process comes or Interrupt occurs or I/O needed.
#                 READY ←--------


# Process Control Block(PCB):
# ->Each process can go to any state and come to cpu at any time, so how will it know from where to start its execution as some part is done. to keep track of it, it needs PCB
    # +-----------------------------+
    # |          PCB                |
    # +-----------------------------+
    # | Process ID (PID)            |
    # | Process State               |
    # | Program Counter             |                -> Program counter says from where exactly we need to start our execution(Specific Istruction)
    # | CPU Registers               |                -> Registers are required to store the important values that came and required by other instructions in same process before handling an Interrupt
    # | Scheduling information      |
    # | Memory management info      |
    # | Open file information       |
    # | Accounting information      |
    # | Other OS-specific data      |
    # +-----------------------------+


# Context Switching:
# ->It is the process of saving the execution context of one process/thread and restoring the context of another when serving other by stopping current process.
# The shifting is required because there may be some high priority processes which requires faster attention,etc
# Here the context can be retrived and stored into the PCB block.
# When a context is switched is switched then it's state and data is put in pcb and put that in ready state and take the other process out of ready state and load it's context and continue execution
# It is expensive because the CPU does unnecesary work of loading and unloading data instead of executing many instrcutions.

# It has many types: 1. Process switching and 2. threads switching,etc
# Threads switching is considered more faster and less expensive as here only some parts are loaded and unloaded each time because the address space is same for all threads in a process



# Process Creation:
    # Parent
    # |
    # fork()                    ->Both parent and child continue execution, but with different return values from fork().
    # |                         -> So, whenever a fork system call is used then the processes doubles
    # +--------+                Ex: If a process has 1 child and including it 2 and now fork is done total 4 processes continue to exist
    # ↓        ↓
    # Parent    Child
    
import os
os.fork()   #type:ignore
print("Hello", flush=True)      # -> 2 hello are printed as 2 processes are running from the line after fork()


# fork() creates a new process and return 0 to child process and the pid of the child to the parent in order to keep track of it.
# exec() replaces the current process's program image with another program, so with same pid only the program in it is completely changed.

executable = "/bin/ls"
args = ["ls", "-la"]
env = os.environ

print("Child: Executing /bin/ls now...")
os.execve(executable, args, env)

# Reached only if execve fails
print("Exec failed!", file=sys.stderr)
sys.exit(1)

# See how the code works and if it fails to replace then it prints failure message as the message is in same old process


# Termination:
# -> A process is terminated if it completes normally or an error occurs or another process terminates  or it calls an exit mechanism.
# Some times the parents might wait for the result of the child with the wait() system call. But if the child has terminated earlier without giving a responce,
#then this parent process will become zombie process.

# Zombie process: A terminated child whose parent has not yet collected its termination status can remain as a zombie.
# Note: A zombie is not actively executing.


'''Inter Process Communication: It is the communication between processes'''
# Processes usually have isolated address spaces. That is good for protection. But processes sometimes need to communicate for required data,then methods used are:
# 1.Pipes: It provides a communication channel.
# 2. Shared memory: Both processes access a shared memory region.   ->This can be very fast but there will be synchronization errors in it when both acess at same time
# 3.Sockets
# 4.Signals
# 5.Message Queues

''' ****Process vs Thread (So so Important)'''
# A process is an independent execution environment with its own address space.
# A thread is an execution unit within a process.
PROCESS
# +--------------------------------+
# | Address Space   ->1            |
# |                                |
# | Code            ->2            |
# | Data            ->3            |
# | Heap            ->4            |
# |                                |
# | Thread 1                       |
# | Thread 2                       |
# | Thread 3                       |
# +--------------------------------+

# 1,2,3,4 are shared among all threads, But each thread has its own execution state, including:
# - program Counter
# - registers
# - stack

# Threads are needed beacuse If everything were one execution path, one blocking operation could make the entire application appear stuck.
# Threads allow multiple execution flows within a process.