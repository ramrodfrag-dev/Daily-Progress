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

'''Some basic file Descripters:
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


# Complete OS(1/6):
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

'''Program vs Process(2/6)'''
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

# fork returns 0 for child process and pid no for parent to keep track of child but the execute does not return anything.

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


'''Threads: These are the smallest unit of CPU execution in the system'''
# A process provides the resource container and the threads provides the execution.
# Why use them?
# 1.These are responsive as if one thread is waiting other threads can work
# 2.These share common resources so, creating them and managing them is easy.
# 3.Multiple threads can run on a single CPU core which improves our system's Parallelism and concurrency

''' ****Process vs Thread (So so Important)(3/6)'''
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

# 1,2,3,4 are shared among all threads(So, these are light weight than processes), But each thread has its own execution state, including:
# - program Counter
# - registers
# - stack

# Threads are needed beacuse If everything were one execution path, one blocking operation could make the entire application appear stuck.
# Threads allow multiple execution flows within a process.

'''Threads Types: 1.User level threads and 2.Kernel level threads'''
#1.User level threads: These are managed by the User Thread Library(User-space) only
# Advantages: Fast thread creation and switching as these are managed by user so, no system calls(less kernel involvement),
# Disadvantages: Kernel cannot map directly to the threads. so, if 1 thread is blocking then all threads needs to wait.

# [ User Thread 1 ]   [ User Thread 2 ]   [ User Thread 3 ]
#         \                   |                   /
#          \                  |                  /
#   ═════════════════════════════════════════════════════  [ User Space ]
#                      User Thread Library 
#                  (Schedules threads locally)
#   ═════════════════════════════════════════════════════  [ Kernel Boundary ]
#                             │
#                      1 Kernel Thread
#                             │
#                             ▼
#                         CPU Core

#2.Kernel level threads: These are managed by the kernel direclty
# Advantages: Better support for multi parallesim and the kernel can handle/manage all threads independently
# Disadvantages: Slow execution as all threads are managed by the Kernel itself so, switching takes time.

# [ User Thread 1 ]    [ User Thread 2 ]    [ User Thread 3 ]
#         │                    │                    │
#   ══════│════════════════════│════════════════════│════  [ User Space ]
#         │                    │                    │
#   ══════│════════════════════│════════════════════│════  [ Kernel Boundary ]
#         ▼                    ▼                    ▼
# [ Kernel Thread 1 ]  [ Kernel Thread 2 ]  [ Kernel Thread 3 ]
#         │                    │                    │
#         ▼                    ▼                    ▼
#     CPU Core 1           CPU Core 2           CPU Core 3


'''a. Concurrency vs b. Parallelism Note: Concurrency does not require multiple cores. Parallelism does.'''
#a.Multiple tasks are in progress during overlapping periods.   ->Progressing
# Ex: CPU core 1: A A B B A B A
#b.Multiple tasks execute simultaneously on different CPU cores ->Executing
# Ex: CPU core 1: A A A
    # CPU core 2: B B B
    

'''CPU Scheduling: It is the process of selecting some ready process out of many for execution ->Selection Process'''
# Representation of all process and time for understanding is done in a chart named as 'ghantt chart'.

# Evaluation metrics:
# AT = Arrival Time ->When it arrives
# BT = Burst Time ->Amount it takes to complete it's execution
# CT = Completion Time  ->When its execution completes
# TAT = Turn around time=> CT-AT    ->Total time spend in the system
# WT = Waiting time=> TAT-BT    ->It's wait in the Ready queue
# RT = Response time=> First CPU start time-AT  ->Time until the process gets CPU for the first time (or) Time until first CPU allocation

#Types:
# 1. Preemptive: The OS can interrupt a running process and give the CPU to other process
# Ex:
# a.SRTF(Shortest remaining time first): At the current time which process has the minimum remaining time to execute that is selected and executed
# b.Round Robin: So, time is divided in to quadrons and Each process receives a fixed time quantum. Designed primarily for time-sharing systems. IF not completed in that quadron it gets after all gets a chance

# 2. Non-Preemptive: Once a process gets CPU then it keeps the CPU with it until it's execution is done
# Ex:
# a.FCFS(First Come First serve): Whichever comes first will be executed and in an order. ***Convoy effect***So if there is a large process then many short processes later can starve
# b.SJP(Shortest job first): At the current time which processes has the lowest burst time then that is taken and executed completely.

# Priority shceduling is present in both preemptive and non-preemptive ones and it is nothing but each process gets a priority number and based on that number the processes are executed
# But the process with lower priority never executes if higher priority processes keep commming->This is called ***Starvation***
# To counter attact starvation we have ***Aging***: this is a process to increase the priority value if it stays in redy queue for long time which makes it to execute at any time gaurantely.

#Note: SJF  → burst time SRTF → remaining time and SRTF ia the non-preemptive part of SJF




''' Synchronization and Critical section(4/6)'''
# When 2 or more threads aceess a same part concurrently then the final result can depend on execution order, as both threads are working on same vvariables and performing different operations
# So, the whole code will be divided into the 2 parts. one is non-critical code which does not have to acess any shared memory of others and the critical one which requires the shared memory for its execution.

# SOlution for the critical section thing will be, it should provide:
# 1.Mutual Exclusion: only one thread enters critical section at one time
# 2.Progress: If there is no thread is inside the critical section then selection of next one must nt be delyed
# 3. Bounded Waiting: A thread should not wait indefinitely to enter critical section.

'''***Mutex(Mutual exclusion lock)***'''
# It allows only 1 thread to own a lock at a time
#Ex:
lock.acquire()
# Critical section
lock.release()

# This is ownership based mutual exclusion. Only the thread which locks a mutex should unlock it.

'''***Semaphore***'''
# It is a synchronization primite based on a counter
#Operations:
wait() / P()
signal() / V()
# wait->decrement/possibly block
# signal->increment/wake a waiter

#Types:
#a.Binary semaphore: 0 or 1. It can provide the mutual exclusion even though they are not related to the mutex conceptually.
#b.Countng semaphore: Can represent multiple available resourrces.
#Ex: Semaphore=3    =>Up to 3 units of the resource can be acquired concurrently.

'''Monitor'''
# It is a high level synchronization where everything is done autoomatically instead of manually.
# The code to allocate the lock to the current process is directly injected by the monitor and looks after it.
# We just need to mention the monitor abstract class and intialize it, inner functions it will fill up automatically

#-> Condition variables allow a thread to sleep until a particular condition becomes true.
# A condition variable is generally used with a lock/monitor, not as an independent replacement for one.
# Typicall operations are: wait() and signal() operations


'''Dead Lock'''
# A deadlock occurs when a set of processes/threads are permanently blocked because each is waiting for resources/events that cannot become available due to the same dependency cycle.
# It needs 4 conditions:
# a.Mutual Exclusion: Atleast there must be one resource which cannot be shared simultaneously.
# b.Hold and wait: A process holds 1 resources while waiting for another.
# c.No-Preemption: Resources cannot be forcibly taken away, they must release resources themselves.
# d.Circular-wait: A circular chain exists of hold and wait of resources

# ->Deadlock Prevention: means Designing system so that atleast 1/4 conditions can never hold(static method)
# ->Deadlock Avoidance: means Solving the probelm dynamically(If I gave resouce to this process will the state be safe)
#   It uses Banker's Algorithm see in word file
# ->Deadlock Detection: Instead of preventing/avoiding, the OS allows it and periodically check for dependency cycle of these processes
# ->Deadlock Recovery: After detection we will use possible approaches like terminating struck process and so on.

#Some terms:
# 1.Starvation: A process waits indefinitely because scheduling/resource allocation favours others.
# 2.Safe state: It is the state of all the process which have atleast one possible safe sequence.
# 3.Unsafe state: It is the state of all the process which does not have a possible safe sequence
#   ->There might be dead lock or not for the unsafe state. we cannot guarantee.
# 4.Safe sequence: It is the sequence of the execution of all the process such that it lead to all execution of process without Deadlock
# 5.Live lock: Unlike deadlock where there is not action(only waiting) here there is some work happening here no noticable progress is happening
#   ->Ex:If there are 2 persons standing opposite way and expecting other to move aside and standing still is deadlock whereas moving in the sae direction such that they end up in same opposite way is called livelock

# Synchronization problem solves coordination problems but create additional deadlock problems.



'''Memory Management:(5/6)'''
# Physical Memory: It is the actual ram installed in the machine
# Virtual memory: Each process sees its own virtual address space, which hardware and the OS maps it to the Physical address
# Uses: Isolation, Larger logical adress space than physical ram, efficent memory management by only loading required pages, cannot need to get larger ram in a contiguous locations as we can store each page in different locations

# Processes Virtual Address
#       ↓
#   Page Table / MMU(Memory Management Unit)
#       ↓
# Physical Address
#       ↓
#      RAM

# Note: The process normally doesn't need to know the actual physical RAM location.
# Each process get's a Logical address space:
# High Address
# +----------------+    
# | Stack          |    ->These are parts of process's Virtual space(contains function call frames, local variables, return info,function states)->usually grows as the functional calls increases
# +----------------+
# |                |
# | Free space     |
# |                |
# +----------------+
# | Heap           |    ->Used for dynamically allocated memory(which is allocated by the runtime only unlike stack which got storage by function execution state)
# +----------------+
# | Data           |
# +----------------+
# | Code           |
# +----------------+
# Low Address

# Two processes can use the same virtual address while mapping to different physical locations. See this how exactly this works out
# Due to the above thing Isolation works

# MMU performs the hard-ware supported address translation using information supplied by the OS.

'''Paging: It divides memory into fixed-size blocks'''
# The Virtual memory is divided into P0,P1,P2,... where each are pages and each has same size.
# These are accessed by the virtual address which is generally asked or storeed by the process
# +------------------+--------------+
# |   Page Number    |    Offset    |   ->Virtual Address Stucture
# +------------------+--------------+
# Base address/page number identifies the virtual page. and the offset identifies the exact byte within that page.

# Just like the Pages are made in the virtual address **Frames** are made from the actual ram which are of fixed size
# Note: The size of Frame and the Page is same in the concept of Paging and also each page is mapped to each frame(Its not necessary pages are occupying the contiguous physical memory)
# The frames are divided based on the hardware. its not in our hands, so to keep the page size same as the frame size is known as paging
# Uses as each page is fit into 1 frame so, we can manage and retrive required frames from anywhere in ram
# Without paging, allocating large contiguous physical regions can cause external fragmentation.
# As the size of both of frame and page size are same so, the virtual and physical address offests are same because it represents how many bytes are there in each block(These are same as they have same size)

'''Page Table: It is the concept of keeping the relation btw virtual page and physical frame.'''
# It is usually maintained by OS
# These page tables are also stored in the ram like pages.SO first it checks page table and get frames

# Numericals see in the dox file
''' CPU Execution Layer: Virtual Address Request'''
#                         │
#                         ▼
#             [ Split: VPN vs Offset ]
#                         │
#                         ▼
#              Check TLB Hardware Cache
#                         │
#         ┌───────────────┴───────────────┐
#         ▼                               ▼
#     [ TLB HIT ]                     [ TLB MISS ]
#         │                               │
#         │                       Walk Page Table in RAM
#         │                               │
#         │               ┌───────────────┴───────────────┐
#         │               ▼                               ▼
#         │        [ Valid Bit = 1 ]              [ Valid Bit = 0 ]
#         │               │                               │
#         │        Update TLB Cache                [ PAGE FAULT ]
#         │               │                               │
#         └───────┬───────┘                    Trap to OS Kernel to
#                 │                            load page from Disk
#                 ▼                                       │
#     [ Combine PFN + Offset ]                            ▼
#                 │                            Retry Instruction
#                 ▼
#   [ Access Physical Hardware RAM ]


''' And the convertion looks like:'''
# Virtual Address:  [ Virtual Page Number (20 bits) ] [ Offset (12 bits) ]
#                                  │                         │
#                        (Look up in Page Table)             │
#                                  │                         │
#                                  ▼                         ▼
# Physical Address: [ Physical Frame Number (12 bits) ] [ Offset (12 bits) ]

# Important steps to remember: Unallocated pages take no space in the storage.
# ->Frames are never on the hard disk.
#1. Hardware RAM is divided into fixed physical slots called Frames.
#2. Programs are divided into matching virtual chunks called Pages.
#3. When a program runs, its Pages are stored on the Hard Disk/SSD (in files or swap space).
#4. When the CPU needs a specific page, the Operating System copies that Page from the hard disk and drops it into an empty Frame in RAM.

'''TLB(Translation lookaside Buffer):'''
# It is a small buffer which store the fast cache storing the mappings of the page no to the frame no.
# If OS finds the required page here then it hits otherwise it misses and go to the mapping in the ram.
# Generally CPU asks from it(physical frame by giving the virtual address) as it is faster and then if it misses check the ram and load it into the TLB by removing some existing mapping.

'''Page Fault'''
# It is the error stating the required page is not in the main memory, so OS brings the required page from harddisk.
# This occurs after TLB miss occurs generally. see the flow of how the cpu requirement of page is done through tlb,ram,disk
# When a new page/pages comes into memory then all the mappings in the main memory and the tlb mappings must be updated.IF not then the stale tlb problem occurs that it gives other pages which are not the required ones
# Majority of time the pages are present in both the ram and the disk but the data in the disk may be outdated, so it must be updatted continuously. It's done by the dirty bit
# If the Dirty bit(Hardware bit)==1 then the data is outdated and if it is 0 then the data is current one
# After a page fault occurs os will bring the page from drive and update tables as well as restart instrcution to make it work in next try.

# **Demand Paging: It is a process where we only bring the required pages to the ram instead of bringing every page.It makes the startup faster and efficient use of memory.

'''Page Replacement'''
# It is the process of replacing the new page which is required by the CPU with that of other page.
# The page which is going to be removed is called the victim page and when removing that page we have to see its dirty bit is 1 or 0 if it is 1 then we have to update the page in disk storage as there are some changes ocured in ram
# The common ways to select the vistim page(which is going to be removed):
# 1.FIFO, 2.LRU(Least recently used or whose previous use is farthest in the past), Optimal(replace with page whose next use is very far in future)
# In reality the optimal method will not work as our system cannot identify which may be used in the future(It just cannot simply predict the future)

'''Thrashing'''
# If a system spends more of its time in handling page faults instead of executing the instructions
# This happens when the system has insufficient number of frames requird to complte their processes
# Disadvantages: Very poor System throughput, Low CPU utilization, high disk usage

'''Segmentation'''
# It is similar to the Paging but here the pages are not the same size as that of frame as here the pages are divided based on the user logic instead just by their fixed size.
# It only contains segments. No frames or pages
# Ex: If there are 5 functions then in the paging part first 2.5 is in one page and the other in another, so the function is divided which is not good as we cannot execute whole process without it but
# In the segmentation each function is stored in a page so, all their variables and required data will be in 1 single page.
# Because segments have different sizes, physical RAM cannot be divided into uniform frames.
# Instead, a segment is placed directly into a contiguous block of RAM, starting at an exact physical byte location called the Base Address.

# Logical Address = Segment Number + offset

# SO, the segment table contains the main physical address(Base) + limit(Until where it needs to capture it) instead of only frame number like in paging
# If the limit> segment size then it return trap(which is handled by the OS) otherwise it gives the exact values required

# Cons of Segmentations and Paging:
#1. Internal Fragmentation: Allocated block contains unused space inside it, Paging can produce internal fragmentation, especially in the last page of an allocation.
#2. External Fragmentation: Free memory exists but is split into separate regions, making a sufficiently large contiguous allocation difficult.


# ->In paging the we can place the whole process in to different frames as it needs not to be contiguous but only thing is that each frame must be allocated to only one page.
# For more details about Segmentation,paging, Fixed partioning(Old approach) see dox file
# Segment can have any thing(Data,stack,heap)

'''Some Calculations'''
page = virtual_address // page_size
offset = virtual_address % page_size

physical_address = frame * page_size + offset

# For bit-based questions:
Page_size = 2^n(bytes)
Offset = n(bits)

# Then:
Page-number_bits = Virtual-address_bits - Offset_bits

# -> A page fault is therefore a control transfer to the OS, potentially followed by storage I/O.

'''Belady's Anomoly'''
# It is an unusual property of FIFO where the increasing the no.of frames will also increases the no. of page faults.
# Generally it must be opposite but for some reason it happens oppositely for FIFO.
# For the LRU and the Optimal algos have the stack-based behaviour which prevents the anomoly

'''Locality of Reference'''
# Page replacements works beacuse programs tend to exhibit locality patterns.
# There are 2 types:
# a. Temporal Locality: Recently acsessed data are likely to be accessed again(A->B->A so, A or B is going to be acessed soon)
# b. Spatial Locality: Nearby address are likely to be accessed again(1000->1004->1012 so, here the address which are in the range of (1000-1025) are likely to be accessed)
# a is based on values and the b is based on the address
# LRU benefits from both as it is similar to both of these as it sees removes the ones which are used fartheset in the past


## Some concepts:
# ->***Working Set***: It is the set of pages that a active process is working on during in a particular's time window
# So, if there are enough pages for the processes to work on then it will execute without any error otherwise it results in more page faults and thrashing
# ->If the pages are more then managing is difficult as there will be many pages so, then we use the multi-level Pages instead of the Single level pages
# ->***Multi-level pages***: The table is spread to 2 levels. Level 1 says is the data is present in level 2 or not and level 2 will say what is the frame no. So, if the level 1 says there is no page then we raise page fault instead of checking other level
# Disadvantage: We have to check more level tables so, accessing the ram many times, this could lead to overhead.
# Advantages: Avoiding allocating the page-table memory for unused regions, and also better scalability for large virtual address
# ->Demand Paging: Indivisual pages are loaded when required
# ->Swapping: An entire process or image of it may be moved between the ram and the storage when required


'''Some things to remember'''
# 1.If the degree of multi programming has increased then the no.of processes will increase and then they need more pages for their execution and hence it is prone to thrashing if enough frames are not provided
# - So, always the Multi-programming will not improve results
# 2.Thrashing can be reduced by:
    #a.Reduce degree of multiprogramming
    #b.Give nough frames to work for the processes
    #c.Monitor the page-faults and make the frame allocation and the Victim page selection correctly to get less no.of page faults
# 3.Page Size factor:
    #a.If the Page size increases then managing the page table will be easy(less pages), greater internal fragmentation, fewer pages to manage
    #b.If the page size decreases then managing the page table will be hard(many pages), less internal fragmentation, More pages to manage
# 4.Increasing the RAM reduces the page faults to some extent but the page faults depends on working set, access patterns, pages of processes


'''EAT(Effective Acess Time): Amount of time spent on accessing the memory and other resources instead of executing instructions'''

TLB_lookup = t
Memory_access = m
TLB_hit_ratio = h
page_table_lookup=p
EAT = (h * (t + m)) + ((1-h) * (t + m + p)) #see If the TLB Lookup is maximum then the avg of the Page faults and page_table_lookups will be reduced


'''File System(6/6)'''
# It is a part of the Kernel and it helps in managing all files
# It organizes and manages data stored on persistent storage.
# It handles Files, Directories, Metadata, Permissions, File access, Naming, Links,etc
WorkFlow,
#Python program
    #   ↓
# Python runtime
#       ↓
# OS interface / system calls
#       ↓
# Kernel
#       ↓
# Filesystem
#       ↓
# Storage/device layer
#       ↓
# SSD/HDD

'''Some Important Trerminologies'''
# 1.File: It is a named collection of persistent data managed by the filesystem -> It has both data and metadata
# 2.Directory: A Directory organizes file names and references to filesystem objects ->It provides hierarchial organization and naming
# 3.File Descriptor: It is a small integer used by a process to refer to an open file/resouce
#   0->stdin 1->stdout 2->stderr 3,4,.. for next files  ->Process uses these fd for operations such as reading and writing
#   File descriptor!=file   ->It'sjust a process-level handle to an open source

'''File System Calls'''
# Common Calls are: (Execution order is 1->2/3->4)
'''open()  ->used to check file what os asked and check permissions and if allowed then returns a file descriptor to it for more functionalities of it''' 
'''read()  ->used to read the contetns of the file '''
'''write()  ->used to write contents to the file'''
'''close()  ->used to release the process's refernce to the open file'''
# Mode Uses: 'a' for append, 'w' for write/replacing older content, 'r' for reading

# Python can expose these from os interface:
import os
fd = os.open("data.txt", os.O_RDONLY)
data = os.read(fd, 100)
os.close(fd)                            # Here we are manually closing the refernce but if we forget then it could lead to resource leaks

# (Simple way) With open keyword which handles close itself even our program runs successfully or ended in between(Safe):
with open("data.txt", "r") as f:
    data = f.read()
# for write use the 'a' or 'w' mode and also file.write("hi") for 1 single line or lines=['l1','l2'] file.writelines(lines)

'''File Permissions:'''
# Generally we have 3 Permissions: read,(r) write(w), execute(x)
# We have 3 users each having differnt fucntionalities:
# 1.Owner: rwx
# 2.Group: r-x
# 3.Others: r--
# All together permissions we can write then as rwxr-xr--

#Ex:
r,w,x=4,2,1
# then the Owner will become rwx => 4+2+1 => 7
# Group becomes r-x => 4+1 =>5 similarly Other becomes 4

'''Inode: It is a filesystem data structure containing metadata about file and info used to locate file'''
# Each Inode has a unique number.
# File name != Inode as File name is a directory entry that refers to an inode while the indoe has all info except where is blocks stored and file name

# Linux File System Structure Architecture Diagram
# --------------------------------------------------
"""
+-------------------------------------------------------------------------+
|                              DIRECTORY                                  |
|                                                                         |
|  Maps human-readable file names to system inode numbers                 |
|                                                                         |
|  +------------------------+------------------------------------------+  |
|  | File Name              | Inode Number                             |  |
|  +------------------------+------------------------------------------+  |
|  | "my_file.txt"          | #10482                                   |  |
|  +------------------------+------------------------------------------+  |
+-----------------------------------|-------------------------------------+
                                    |
                                    v
+-------------------------------------------------------------------------+
|                           INODE (#10482)                                |
|                                                                         |
|  +-------------------------------------------------------------------+  |
|  | 1. METADATA                                                       |  |
|  |                                                                   |  |
|  |   - Permissions   : -rw-r--r-- (0644)                             |  |
|  |   - File Size     : 4096 bytes                                    |  |
|  |   - Owner (UID)   : 1000 (user)                                   |  |
|  |   - Group (GID)   : 1000 (user)                                   |  |
|  |   - Timestamps    : Access (atime), Modify (mtime), Change (ctime)|  |
|  |   - Link Count    : 1                                             |  |
|  +-------------------------------------------------------------------+  |
|  | 2. BLOCK REFERENCES (Pointers)                                    |  |
|  |                                                                   |  |
|  |   - Direct Pointers    : [ Block #501 ] ---> Data Block 501       |  |
|  |                        : [ Block #502 ] ---> Data Block 502       |  |
|  |   - Indirect Pointers  : [ Block #789 ] ---> Multi-level Index     |  |
|  +-----------------------------------|-------------------------------+  |
+--------------------------------------|----------------------------------+
                                       |
                                       v
+-------------------------------------------------------------------------+
|                             DATA BLOCKS                                 |
|                                                                         |
|  +-------------------------+      +----------------------------------+  |
|  | DATA BLOCK #501         |      | DATA BLOCK #502                  |  |
|  | "Hello, World! This..." |      | "...is actual file contents."    |  |
|  +-------------------------+      +----------------------------------+  |
+-------------------------------------------------------------------------+
"""

'''File Allocation'''
# The File system must determine where file data is stored on disk, so it only allocates space for the files in different ways:
# a.Contiguous allocation: A file Occupies consecutive blocks
# ex:[10][11][12][13][14]
#           +ve's                                                      -ve's
#   -Excellent sequential access                              External fragmentation
#   -Efficient direct/random access         Growing a file can be difficult if adjacent space is unavailable
#   -Simple addressing

# b.Linked Allocation: Fileblocks can be scattered. Each block points to the next block
# ex:[10] → [27] → [4] → [19]
#           +ve's                                                      -ve's
#   -No need for contiguous free space                             Pointer overhead
#   -Files can grow easily                                        Poor random access
#                                                               A damaged pointer can affect the chain and get wrong results

# c.Indexed Allocation: A seperate index block stores pointers to the file's data blocks
# Ex:        Index Block
        #    /    |    \
        #   ↓     ↓     ↓
        # [10]  [27]  [4]
#           +ve's                                                                   -ve's
#   -Supports direct access better than linked allocation         Index structure consumes additional storage.
#   -File blocks need not be contiguous


'''Links: Hard and Soft/Symbolic Links'''
# See the links parts in the dox for more picture representation


'''Mounting'''
# A filesystem may exist on a disk partition, logical volume, network resource, etc.
# Mounting makes that filesystem accessible at a directory in the existing filesystem hierarchy.
# OS can combine filesystems into a unified directory hierarchy instead of seperate file systems, that's why mounting matters

# =========================
# OPERATING SYSTEM TYPES
# =========================

# 1. TIGHTLY COUPLED / MULTIPROCESSOR SYSTEM
# - Multiple CPUs in one computer system.
# - CPUs share memory/resources.
# - Enables parallel execution and better performance.
#
# SMP (Symmetric Multiprocessing):
# - All CPUs are equal.
# - Any CPU can execute OS/user tasks.
#
# AMP (Asymmetric Multiprocessing):
# - Master CPU controls/assigns work.
# - Other CPUs execute assigned tasks.
#
# MEMORY: Many CPUs + One System


# 2. MULTIPROGRAMMING
# - Multiple programs kept in memory.
# - If one program waits for I/O, CPU switches to another.
# - Main goal: maximize CPU utilization.
#
# MEMORY: Switch when I/O wait


# 3. MULTITASKING
# - CPU rapidly switches among multiple tasks.
# - Uses small time slices/time quanta.
# - Gives the appearance of simultaneous execution.
# - Main goal: quick response.
#
# MEMORY: Switch after TIME SLICE


# 4. DISTRIBUTED / LOOSELY COUPLED SYSTEM
# - Multiple independent computers connected by a network.
# - Each computer has its own CPU and memory.
# - Computers cooperate and share work/resources.
#
# MEMORY: Many Computers + Network


# 5. BATCH OPERATING SYSTEM
# - Similar jobs are grouped into batches.
# - Jobs are processed with little/no user interaction.
# - Reduces repeated setup/loading overhead.
#
# MEMORY: Batch = Group Similar Jobs


# 6. MULTIUSER SYSTEM
# - Multiple users can use the system/resources.
# - Resources are shared among users/processes.
#
# MEMORY: Many Users + Shared Resources


# 7. TIME-SHARING SYSTEM
# - CPU time is divided into small time slices (quantum).
# - Each process/user gets a turn.
# - Round Robin is commonly used.
# - Designed for interactive/fair CPU sharing.
#
# DIFFERENCE:
# Multiprogramming -> Switch when I/O wait
# Time-sharing    -> Switch after fixed time quantum
#
# MEMORY: Fair CPU Time


# 8. REAL-TIME OPERATING SYSTEM (RTOS)
# - Must produce a response within a specified deadline.
# - Correctness = Correct result + Correct timing.
#
# HARD REAL-TIME:
# - Deadline is strict.
# - Missing deadline may be unacceptable.
#
# SOFT REAL-TIME:
# - Deadline is important.
# - Occasional delay can be tolerated.
#
# MEMORY: Finish Within Deadline

# =========================
# QUICK REVISION
# =========================
#
# Tightly Coupled  -> Many CPUs in one system
# Multiprogramming -> Switch when I/O wait
# Multitasking     -> Switch among tasks using time slices
# Distributed      -> Independent computers + network
# Batch OS         -> Group similar jobs
# Multiuser        -> Multiple users share resources
# Time-sharing     -> Fair CPU time using quanta
# Real-time OS     -> Must meet deadlines
#
# KEY DIFFERENCE:
#
# Multiprogramming:
#     I/O wait -> switch
#
# Multitasking:
#     Time slice -> switch
#
# Time-sharing:
#     Fair time slices for interactive users/processes

'''Exception vs Interrupt'''
# Interrput occurs due to outside entity user, or hardware while the Exception occurs due to the error in the process itself

'''Maskable and non-maskable Interrupts'''
# If a high priority interrupt signal comes then it is non maskable so, these must be resolved first inorder to resume previous execution
# While a low priority interrupt comes then we can mask it(Disable and then enable) to do it in later stages
# There will be a Interrupt flag so, if one process is being handled then then interrupt flag is 1. If it is handled then the flag is set to 0 and others can not raise interrupts.

