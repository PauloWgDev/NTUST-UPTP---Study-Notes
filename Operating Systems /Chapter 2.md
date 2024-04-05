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

During the course of execution, a process may create several new process. The creating process is called a parent process, and the new processes are called the children of that process. Each of these new processes may in turn create other process, forming a tree of processes.

Most operating systems indentify processes according to a unique process indetifie (pid) wich is tipically an int.

When a process creates a new process, two possiblities for execution exist:
- The parent continues to execute concurrently with its children.
- The parent waits until some or all of its children have terminated.

There are also two address-space possibilities for the new process:
- The child process is a duplicate of the parent process (has the same program and data as the parent)
- The child process has a new program loaded into it.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/df6679fe-7a2c-41a3-9c6a-e9221c866e81)


### Process Termination

A process terminates when it finishes executing and asks the operating system to delete it by using the exit() system call. At that point, the process may return a status value to its waiting parent.

A parent may terminate the execution of one of its children for a variety of reasons such as:
- The child has exceeded its usage of some of the resources that it has been allocated
- The task assigned to the child is no longer required.
- The parent is exiting, and the operating system does not allow a child to continue if its parent terminates.

Some systems do not allow a child to exist if its parent has terminated. 
In such systems, if a process terminates, then all its children must also be terminated. This phenomenon, refered to as cascading termination.

Whenever a process terminates, its resources are deallocated by the operating system. However, its entry in the process table must remain there until the parent calls wait(). A process that has terminated, but whose parent has not yet called wait(), is known as a zombie process.

If a parent did not invoke wait() and instead terminated, its children woudl be orphans processes. 

#### Android Process Hirearchy

Because of resource constraints, mobile operating systems may have to terminate existing process to reclaim limited system resources. Rather than terminating an arbitrary process, Android has indentified an importance hierarchy of process. 
From most to least important: 
- Foreground Process: The current process visible on the screen.
- Visible Process: A process that is not directly visible on the foreground but that is performing an activity that the foreground is referring to.
- Service Process: A process similar to a background process but its performing activity is apparent to the user (such a streaming music)
- Background Process: A process that may be performing an activity but is not apparent to the user.
- Empty Process: a process that holds no active components associated with any application

If a system resource must be reclaimed, it will begin terminating a empty process and if necessary will procede with a background process and so on.

## Interprocess Communication

A process is independent if it does not share data with any other process executing in the system. A process is cooperating if it can affect or be affected by the other processes executing in the system.
There are several reasons for providing an environment that allows process cooperation:
- Information Sharing: Application may be interested in the same piece of information, we must provide an environment to allow concurrent access to such information.
- Computation Speed: If we want a particular task to run faster, we must break it into substasks.
- Modularity: We may want to construct the system in a modular fashion, dividing the system function into separate process or threads.

Cooperating process requires and interprocess communication (IPC) mechanism. 
There are two fundamental models of interprocess communication: shared memory and message passing. In the shared memory model, a region of memory that is shared by the cooperating processes is established. In the message-passing model, communication takes place by means of messages exchanged between the cooperating processes.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/9ea1def5-3132-45f3-959c-c2bb975a2f90)

## IPC in Shared-Memory Systems

Normally, the operating system tries to preven one process from acessing another process's memory. Shared memory requires that two or more processes agree to remove this restriction.

A producer process produces information that is consumed by the consumer process.
For example a compiler produces assembly code that is consumed by an assembler.

To allow producer and consumer processes to run concurrently, we must have available a buffer of items that can be filled by the producer and emptied by the consumer. Two typer of buffer can be used. 
- **UNbounded Buffer**: places no practical limit on the size of the buffer
- **Bounded Buffer**: Assumes a fixed buffer size. In this case the consumer must wait if the buffer is empty and the producer must wait if the buffer is full.

## IPC in Message-Passing Systems

Message-Passing provides a mechanism to allow processes to communicate and to synchronize their actions without sharing the same address space. IT is particularly useful in a distributed environment, where the communicating processes may reside on different computers connected by a network.

If process P and Q want to communicate, they must send message to and revieve messages from each other, a **communication link** must k must exist between
them.

Here are several methods for logically implementing a link
and the send()/receive() operations:
- Direct or indirect communication
- Synchronous or asynchronous communication
- Automatic or explicit buffering

### Naming
Processes that want to communicate must have a way to refer to each other

Under direct communication, each process that wants to communicate
must explicitly name the recipient or sender of the communication

- send(P, message)—Send a message to process P.
- receive(Q, message)—Receive a message from process Q

A communication link in this scheme has the following properties:

- A link is established automatically between every pair of processes that
want to communicate. The processes need to know only each other’s
identity to communicate.
-  A link is associated with exactly two processes
-  Between each pair of processes, there exists exactly one link

This scheme exhibits symmetry in addressing; that is, both the sender process and the receiver process must name the other to communicate. A variant
of this scheme employs asymmetry in addressing. Here, only the sender names
the recipient.

- send(P, message)—Send a message to process P.
- receive(id, message)—Receive a message from any process. The variable id is set to the name of the process with which communication has taken place.

With indirect communication, the messages are sent to and received from
mailboxes, or ports

-  send(A, message)—Send a message to mailbox A.
-  receive(A, message)—Receive a message from mailbox A.

In this scheme, a communication link has the following properties:
- A link is established between a pair of processes only if both members of
the pair have a shared mailbox
- A link may be associated with more than two processes.
- Between each pair of communicating processes, a number of different links
may exist, with each link corresponding to one mailbox

In contrast, a mailbox that is owned by the operating system has an existence of its own. It is independent and is not attached to any particular process.
The operating system then must provide a mechanism that allows a process to
do the following:
- Create a new mailbox
- Send and receive messages through the mailbox
- Delete a mailbox

### Synchronization

Communication between processes takes place through calls to send() and
receive() primitives.
Message passing may be either blocking or nonblocking—
also known as synchronous and asynchronous.

- **Blocking send.** The sending process is blocked until the message is
received by the receiving process
- **Nonblocking send.** The sending process sends the message and resumes
operation
- **Blocking receive.** The receiver blocks until a message is available
- **Nonblocking receive.** The receiver retrieves either a valid message or a
null.

### Buffering
Whether communication is direct or indirect, messages exchanged by communicating processes reside in a temporary queue.

Ways to implement the Queues:

- **Zero capacity.** The queue has a maximum length of zero; thus, the link
cannot have any messages waiting in it.
- **Bounded capacity.** The queue has finite length n.
- **Unbounded capacity.** The queue’s length is potentially infinite

## Communication in Client - Server Systems

### Sockets

A socket is defined as an endpoint for communication. 
A socket is identified by an IP address concatenated with a port number. In general, sockets use a client-server architecture. The server waits for incoming client request by listening to a specific port. 

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/1e6167ec-8910-42d5-83ec-c5c644f2adc0)

The IP address 127.0.0.1 is a special IP address known as the
loopback. When a computer refers to IP address 127.0.0.1, it is referring to itself

### Remote Procedure Calls

One of the most common forms of remote service is the RCP paradigm, which was designed as a way to abstract the procedure-call mechanism for use between systems with network connections. It is similar in many ways to the IPC, and it is usually build on top of such systems. However, because we are dealing with an environment in which the processes are executing on separate systems, we must use a message based communication scheme to provide remote service.

A port in this context in simply a number included at the start of a message packet.

The semantics of RPCs allow a client to invoke a procedure on a remote host as it would invoke a procedure locally.

Some systems known as **big-endian**, store the most significant byte first. Withe other systems known as **little-endian** store the leat significant byte first. 
To resolve difference like this, many RPC systems defina a machine-independent representation of data. One such representation is known as external data representation (XDR).

## Summary

-  A process is a program in execution, and the status of the current activity of a process is represented by the program counter, as well as other registers.
- The layout of a process in memory is represented by four different sections:
(1) text, (2) data, (3) heap, and (4) stack.
- As a process executes, it changes state. There are four general states of a
process: (1) ready, (2) running, (3) waiting, and (4) terminated.
- A process control block (PCB) is the kernel data structure that represents a
process in an operating system.
-  The role of the process scheduler is to select an available process to run on
a CPU
- An operating system performs a context switch when it switches from
running one process to running another
- The fork() and CreateProcess() system calls are used to create processes on UNIX and Windows systems, respectively
- When shared memory is used for communication between processes, two
(or more) processes share the same region of memory. POSIX provides an
API for shared memory
- Two processes may communicate by exchanging messages with one
another using message passing. The Mach operating system uses message
passing as its primary form of interprocess communication. Windows
provides a form of message passing as well
- A pipe provides a conduit for two processes to communicate. There are
two forms of pipes, ordinary and named. Ordinary pipes are designed for
communication between processes that have a parent–child relationship.
Named pipes are more general and allow several processes to communicate
- UNIX systems provide ordinary pipes through the pipe() system call.
Ordinary pipes have a read end and a write end. A parent process can, for
example, send data to the pipe using its write end, and the child process
can read it from its read end. Named pipes in UNIX are termed FIFOs.
- Windows systems also provide two forms of pipes—anonymous and
named pipes. Anonymous pipes are similar to UNIX ordinary pipes. They
are unidirectional and employ parent–child relationships between the
communicating processes. Named pipes offer a richer form of interprocess
communication than the UNIX counterpart, FIFOs
- Two common forms of client–server communication are sockets and
remote procedure calls (RPCs). Sockets allow two processes on different
machines to communicate over a network. RPCs abstract the concept of
function (procedure) calls in such a way that a function can be invoked on
another process that may reside on a separate computer
- The Android operating system uses RPCs as a form of interprocess communication using its binder framework.

