# Processes

A process is a program in execution. And it is the unit of work of modern computing systems.


## Process Concept

### The Process

As mentioned earlier, a process is a program in execution. The status of the current actity of a process is represented by the value of the program counter and the contents of the processor's registers. The memory layout of a process is typically divided into multiple sections:

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/1feba275-0471-4083-9410-52a78ccc725f)

- **Text Section**: The executable code
- **Data Section**: Global variables
- **Heap Section**: memroy that is dynamically allocated during program run time
- **Stack Section**: temporary data storage when invoking functions (for example funtion parameters, returns addresses and local variables)

As we can see in the previous graphic, text and data section have fixed size. However the stack and heap sections can shrink and grow dynamically during program execution.
Although the stack and heap sections grow towards each other, the operating system has to make sure that they do not overlap.

### Process State

A processor may be in one of the following states:
- **New**: The process is being created
- **Running**: Instructions are being executed
- **Waiting**: The process is waiting for some event to occur
- **Ready**: The process is waiting to be assigned to a processor
- **Terminated**: The process has finished execution

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/2362a89f-617d-4ed7-a0c5-c6c705c6b6d4)

### Process Control Block (PCB)

Each process is represented in the operating system by a process control block also task control block.

PCB contain the following information about processes:

- **Process State**
- **Program Counter**: The counter indicates the address of the next instruction to be executed for this process
- **CPU registers**
- **CPU-scheduling information**: this includes a process priority, pointers to scheduling queues and any other scheduling parameter.
- **Memory-management information**: This information may include such
items as the value of the base and limit registers and the page tables, or the
segment tables, depending on the memory system used
- **Accounting information**: This information includes the amount of CPU and real time used, time limits, account numbers, job or process numbers, and so on.
- ** I/O status information**: This information includes the list of I/O devices allocated to the process, a list of open files, and so on

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/6b55d62f-9a4d-4b72-8907-dcb8e25a5e79)


## Process Scheduling

The objective of multiporgramming is to have some process running at all times so as to maximize CPU utilization. The objective of time sharing is to switch a CPU core amoung process so frequently that users can interact with each program while running. To meet these objectives, the process scheduler selects an available process for program execution on a core.

The number of processes currently in memory is known as the degree of multiprogramming. 

In general process can be described as either I/O bound or CPU bound. I/O meanning that it spends most of its time doing I/O. While CPU bound process means that it generetes I/O requests infrequently and use most of its time doing computations.



### Scheduling Queues

As processes enter the system, they are put into a ready queue, where they are ready and waiting to execute. This queue is generally stored as a linked list.

A new process is initially put in the ready queue. It waits there untl it is selected for execution or dispatched. Once the process is allocated a CPU core and is executin, one of several events could occur:
- The process could issue an I/O request and then be placed in an I/O wait queue.
- The process could create a new child process and then be placed in a wait queue while it awaits the child's termination.
- The process could be removed forcibly from the core, as a result of an interrupt or having its time slice expire, and be but back in the ready queue.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/a05b7e5b-7d64-423f-b88b-81da89d0b686)



### CPU Scheduling

The role of the CPU scheduler is to select from among the processes that are in the ready queue and allocate a CPU core to one of them.

Some operating systems implement and intermediate form of scheduling known as swapping, the idea is that sometimes it can be advantegeous to remove a process from memory and thus reduce the degree of multiprogramming. Later, the process can be reintroduced into memory, and its execution can be continued where it left of. It is known as swapping because a process ca be "swapped out" from memory to disk, where its current status will be saved and later it can be "swapped in" from disk to memory restoring the status.

### Context Switch

When an interrupt occurs, the system needs to save the current context of the process running so that it can restore that context when its processing is done, essentially suspending the process and resuming it. Generally we perform a **state save** of the current state of the CPU core and then state restore to resume operations. This task is known as **context switch**. When a context switch occurs, the kernel saves the context of the old process in its PCB and loads the saved context of the new process scheduled to Run. 
(Context switch time is pure overhead since the system can not do any useful work while switching)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/b8135586-d4dd-43a6-9737-47dd4601d88a)

## Operations on Processes

### Process Creation

### Process Termination









