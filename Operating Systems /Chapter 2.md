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








