
# Introduction

## Operating System

An operating system is a software that manages a computer's hardware. It acts as an intermediary between the computer and the user.

# What operating Systems Do

A computer system can be divided roughly into four components:
- hardware
- operating system
- application programs
- user

"An operating systems is similar to a government. Like a government, it performs no useful function by itself. It simply provides an environment within which other programs can do useful work."

## User View

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/ecd4e577-c3aa-4dd3-9eb0-715ea0a6c4e7)


## Systems View

From the computer's pov, the operating system is the program most intimately involved with the hardware. In this context, we can view an operating system as a resource allocator.

An operating system is a control program. Meaning that it manages the execution of user programs to prevent errors and improper use of the computer.

## Defining Operating Systems.

There is no universally accepted definition of what is part of the operating system. A simple viewpoint is that it includes everything a vendors ships when you order "the operating system". The systems included however vary greatly across systems. *(I consider this a very poor and bad definition)*

A more common definition, and the one that we usually follow, is that the operating system is the one program running at all times on the computer - usually called the kernel.0 *(I would say this is a more acceptable definition)*

Mobile operating systems often include not only a core kernel but also middleware - a set of software frameworks that provide additional services to application developers.
For example, IOS or Android provide not only the core kernel but also provide middleware that supports databases, multimedia, and graphics (to name only a few).

In summary, for our purposes, the operating system includes the always running kernel, middleware frameworks that easy application development and provide features, and system programs that aid in managing the system while it is running.

## Computer-System Organization

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/d8630df7-02d0-415b-8db4-4d1358fe339a)


### Interrupts

Let's consider a typical computer operation, for example a program performing I/O. To start a I/O operation, the device driver loads the appropriate registers in the device controller. The device controller, in turn, examines the contents of these registers to determine what action to take (such as reading a character from the keyboard). The controller starts the transfer of data from the device to its local buffer. Once the transfer of data is complete, the device controller informs the device driver that is has finished its operation. 
But how des the controller informs the device driver that is has finish its operation? This is accomplished via an **interrupt**.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/6be4a5dd-339b-45e3-ba61-5cd4e5daac14)


When the CPU is interrupted, it stops what it is doing and immediately transfers execution to a fixed location. The fixed location usually contains the starting address where the service routine for the interrupt is located. The interrupt service routine executes; on completion, the CPU resumes the interrupted computation.

Each computer design has its own interrupt mechanism, but several functions are common. The interrupt must transfer control to the appropriate interrupt service routine. The straightforward method for managing this transfer would be to invoke a generic routine to examine the interrupt information. The routine, in turn, would call the interrupt-specific handler.

The interrupt architecture must also save the state information of whatever was interrupted, so that it can restore this information after servicing the interrupt. If the interrupt routine needs to modify the processor state, it must explicitly save the current state and then restore that state before running.

#### Implementation of Interrupt

The basic interrupt mechanism works as follows. The CPU hardware has a wire called the interrupt-request line that the CPU senses after executing every instruction. When the CPU detects that a controller has asserted a signal on the interrupt-request line, it reads the interrupt number and jumps to the interrupt-handler routine by using that interrupt number as an index into the interrupt vector. It then starts execution at the address associated with that index. The interrupt handler saves any state it will be changing during its operation, determines the cause of the interrupt, performs the necessary processing, performs a state restore, and executes a return from interrupt instruction to return the CPU to the execution state prior to the interrupt.

We say that the device controller raises an interrupt by asserting a signal on the interrupt request line, the CPU catches the interrupt and dispatches it to the interrupt handler, and the handler clears the interrupt by servicing the device.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/5c9457aa-e542-4479-91f1-2ea72c51297b)



**In summary, interrupts are used throughout modern operating systems to handle asynchronous events. Device controllers and hardware faults raise interrupts. To enable the most urgent work to be done first, modern computers use a system of interrupt priorities. Because interrupts are used so heavily for time-sensitivity processing, efficient interrupt handling is required for good system performance.**

### Storage Structure

The CPU can load instructions only from main memory (RAM), so any programs must first be loaded into memory to run. 

Computers use other forms of memory as well. For example the first program to run on computers power-on is a bootstrap program, which then loads the operating system. Since RAM is volatile we cannot trust it to hold the bootstrap. Instead for this and other puposes, the computer uses electrically erasable programmable read only memory (EEPROM).

Interaction is achieved through a sequence of load or store instructions to specific memory addresses. The load instruction moves a byte or word from memory to an internal register within the CPU, whereas the store instruction moves the content of a register to main memory.

Ideally, we want the programs and data to reside in main memory permanently. This arragement usually is not possible on most system for two reasons:
- Main Memory is usually too small to store all needed programs and data permanently.
- Main memory, as mentioned is volatile - it loses its contents when power is turned off.

Thus, most computers systems provide secondary storage as an extension of main memory. The main requirement for secondary storage is that it be able to hold large quantities of data permanently. 
The most common secondary-storage devices are hard-disk drives (HDDs) and nonvolatile memory (NVM) devices, which provide storage for both programs and data.


##### Storage Device Hierarchy:

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/5ac1f7a7-5703-44c7-9c88-c56164714806)


The top four levels of memory in the figure are constructed using semi-conductor memory. 


The design of a complete storage system must use only as much expensive memory as necessary while providing as much inexpensive, nonvolatile storage as possible. Caches can be installed to improve performance where a large disparity in access time or transfer rate exists between two components.

## I/O Structure

A large portion of operating system code is dedicated to manage I/O because of its importance to the reliability and performance and because of the varying nature of the devices.

The form of interrupt-driven I/O is fine for moving small amounts of data but can produce high overhead when used for bulk data movements. To solve this problem, direct memory access (DMA) is used. 


## Computer System Architecture


### Single-Processor Systems

The core is the component that executes instructions and registers for storing data locally.

If there is only one general-purpose CPU with a single processing core, then the system is a single-processor system. According to this definition, however, very few contemporary computer systems are single-processors systems.


### Multiprocessor Systems

The primary advantage of multiprocessor systems is increased throughput. That is, by increasing the number of processors, we expect to get more work done in less time.

The most common multiprocessor systems use **symmetric multiprocessing (SMP)**, in which each peer CPU processor performs all tasks, including operating-system functions and user processes.

The benefit of this model is that many processes can run simultaneously (N processes can run if there are N CPUs) without causing performance to deteriorate significantly. However, since the CPUs are separate, one may be sitting idle while another is overloaded, resulting in inefficiencies. 

The definition of multiprocessor includes multicore systems. In which multiple computing cores reside on a single chip.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/c5156e4b-4f22-4ce4-9d7f-c73e40d9b38b)



Additional CPUs to a multiprocessor system will increase computing power; however, the concept does not scale very well, and once we add too many CPUs, contention for the system bus becomes a bottleneck and performance begins to degrade. An alternative approach in instead to provide each CPU with its own local memory that is accessed via a small, fast local bus. The CPUs are connected by a shared system interconnect, so that all CPUs share one physical address space. This approach is known as **non-uniform memory access (NUMA)** 
![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/01712006-b936-4b45-a623-aa929ebac6c2)


The advantage is that, when a CPU accesses its local memory, not only is it fast, but there is also no contention over the system interconnect. Thus, NUMA systems can scale more effectively as more processors are added.
A potential drawback with a NUMA system is increased latency when a CPU must access remote memory across the system interconnect, creating a possible performance penalty. In other words, for example, CPU0 cannot access the local memory of CPU3 as quickly as it can access its own local memory, slowing down performance.

Finally, **blade servers** are systems in which multiple processor boards, I/O boards, and networking boards are placed in the same chassis.
In essence, these servers consist of multiple independent multiprocessor systems.

### Clustered Systems

Another type of multiprocessor system is a clustered system, which gathers together multiple CPUs. Clustered systems differ from the multiprocessor systems in that they are composed of two or more individual systems joined together.

The definition of clustered is not concrete but the generally accepted definition is that clustered computers share storage and are closely linked via a local area network (lan) or a faster interconnect.

Clustering is usually used to provide high-availability service (service that will continue even if one or more systems in the cluster fails).

Clustering can be structured asymmetrically or symmetrically. In asymmetric clustering, one machine is in hot-standby mode while the other is running the applications. The hot-standby host machine does nothing but monitor the active server. If that server fails, the hot-standby host becomes the active server. In symmetric clustering, two or more hosts are running applications and are monitoring each other.

Clusters can also be used to provide high performance computing environments. Such systems can supply significantly greater computational power than single-processor or even SMP systems because they can run an application concurrently on all computers in the cluster. The application must have been written specifically to take advantage of the cluster, however. This involves a technique known as parallelization.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/75aedcc2-cd08-4d45-96d8-63f3463d6029)



storage-area networks (SANs): allow many systems to attach to a pool of storage. If the applications and their data are stored on the SAN, then the cluster software can assign the application to run on any host that is attached to the SAN.

## Operating-System Operations

Once the kernel is loaded and executing, it can start providing services to the system and its users. Some services are provided outside of the kernel by system programs that are loaded into memory at boot time to become system daemons, which run the entire time the kernel is running.

Another for of interrupt is a trap or exeption, which is a software-generated interrupt caused either by an error or by a specific request from a user program that an operating system service be performed by executing a special operation named **system call**.

### Multiprogramming and Multitasking

 In multiprogrammed systems, a program in execution is termed a process.

The idea of multiprogrammed systems is that the operating system keeps several processes in memory simultaneously. The operating system picks and begins to execute one of these processes. Eventually, the process may have to wait for some task. At that point the system simply switches to, and executes another process. When that process needs to wait, the CPU switches to another process, and so on.

In multitasking systems, the CPU executes multiple processes by switching among them, but the switch occur frequently, providing the user with a fast response time.

In a multitasking system, the operating system must ensure reasonable response time. A common method for doing so is virtual memory, a technique that allows the execution of a process that is not completely in memory. The main advantage of this scheme is that it enables users to run programs that are larger than actual physical memory.

### Dual-Mode and Multimode Operation

To ensure the proper execution of the system, we must be able to distinguish between the execution of operating-system code and user-defined code.


At the very least we need two separete modes of operation, user mode and kernel mode (also called supervisor mode or privileged mode). A bit called mode bit indicates the current mode: kernel (0), user (1). With the mode bit, we can distinguish between a task that is executed on behalf of the operating system and one that is executed on behalf of the user.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/602052f8-8a3d-4ef3-a6a2-a296960f79c4)



### Timer

We cannot allow a user program to get stuck in an infinite loop or to fail to call system services and never return control to the operating system. To accomplish this goal, we can use a timer. A timer can be set to interrupt the computer after a specified period.


## Resource Management

### Process Management

An operating system is a resource manager.

A program in execution is a process, you can consider a process to be an instance of a program in execution. A program by itself is not a process.

A process is the unit of work in a system.

The operating system is responsible for the following activities in connection with process management: 
- Creating and deleting both user and system processes
- Scheduling processes and threads on the CPUs 
- Suspending and resuming processes
- Providing mechanisms for process synchronization
- Providing mechanisms for process communication

### Memory Management


The operating system is responsible for the following activities in connection with memory management:
- Keeping track of which parts of memory are currently being used and which process is using them.
- Allocating and deallocating memory space as needed.
- Deciding which processes and data to move in and out of memory.


### File-System Management

The operating system is responsible for the following activities in connection with file management:

- Creating and deleting files
- Creating and deleting directories to organize files
- Supporting primitives for manipulating files and directories
- Mapping files onto mass storage
- Backing up files on stable (nonvolatile) storage media


### Mass-Storage Management

The operating system is responsible for the following activities in connection with secondary storage management:

- Mounting and unmounting
- Free-Space management
- Storage allocation
- Disk scheduling
- Partitioning
- Protection

### Cache Management

Information is normally kept in some storage system. As it is used, it is copied into a faster storage system (cache) on a temporary basis. When we need a particular piece of information, we first check whether it is in the cache. If it is, we use the information directly from the cache. If it is not, we use the information from the source, putting a copy in the cache under the assumption that we will need it again soon.

Data transfer from cache to CPU and registers is usually a hardware function, with no operating-system intervention.

In a multiprocessor system, since the various CPUs can all execute in parallel, there can be a variable A whose value is stored in the cache of the different CPUs. So when the value of A changes in one CPU, this has to be immediately reflected in all others CPUs. This situation is called cache coherency, and it is usually a hardware issue.

### I/O System Management

The I/O subsystem consists of several components:
- A memory-management component that includes buffering, catching and spooling.
- A general device-driver interface.
- Driver for specific hardware devices.

Only the device driver knows the peculiarities of the specific device to with it is assigned.


## Security & Protection

Protection is any mechanisms or controlling the access of processes or users to the resources defined by the computer system.
It is the job of security to defend a system from external and internal attacks.
Prevention of attacks is considered an operating system function for some systems.

Protection and Security require the system to be able to distinguish among all its users. Most operating systems maintain a list of user names and associated user IDs. 
Group functionality can be implemented as a system-wide list of group names and group identifier.

A user sometimes needs to escalate privileges to gain extra permission for activity. Operating systems provide methods to allow privilege escalation. 

## Virtualization

Virtualization is a technology that allows us to abstract the hardware of a single computer into several different execution environments, thereby creating the illusion that each separate environment is running on its own private computer (virtual machine).

Virtualization allows operating systems to run as applications within other operating systems.

Virtualization software are emulations. Emulation involves simulating computer hardware in software.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/4d15b62e-2ade-497f-9bf9-913219f0594f)



## Distributed Systems

A distributed system is a collection of physically separated computers systems that are networked to provide users with access to the various resources that the system maintains.

A network operating system is an operating system that provides features such as file sharing across the network, along with a communication scheme that allows different processes on different computers to exchange messages. A computer running a network operating system acts autonomously from all other computers on the network.
A distributed operating system provides a less autonomous environment. The different computers communicate closely enough to provide the illusion that only a single operating system controls the network.

## Kernel Data Structures

- List: collection of data values as a sequence (linked list)
- Stacks: sequentially ordered data structure that uses LIFO for adding and removing items.
- Queue: sequentially ordered data structure that uses FIFO.
- Trees: data structure organized hierarchically
- Hash functions: takes data as input, performs a numeric operation on the data, and returns a numeric value.
- Bitmaps: a string of n binary digits that can be used to represent the status of n items.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/40cf1375-d2ee-4aca-aaea-cf610289efe5)



## Computing Environments

### Traditional Computing

Your tipical laptop or PC.
### Mobile Computing

Mobile computing refers to computing on handheld smartphones and tablet computers

### Client-Server Computing

Contemporary network architecture features arrangements in which sever systems satisfy requests generated by client systems. This form of specialized distributed system is called client-server system.

- The **compute server system** provides an interface to which a client can send a request to perform an action. In response the server executes the action and sends the results to the client.
- The file-server system provides a file-system interface where clients can create, update, read and delete files.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/74da3183-73ac-4db1-aa6e-9de8648cefb4)



### Peer to Peer Computing

In this model, clients and servers are not distinguished from one another. Instead, all nodes within the system are considered peers, and each may act as either a client or a server, depending on whether it is requestion or providing a service. Peer to peer systems offer an advantage over traditional client-server systems. In a client-server system, the server is a bottleneck; but in a peer to peer system, services can be provided by several nodes distributed throughout the network.

Determining what services are available is accomplished in one of two general ways:

- When a node joins a network, it registers its service with a centralized lookup service on the network. Any node desiring a specific service first contacts this centralized lookup service to determine which node provides the service. The remainder of the communication takes place between the client and the service provider.
- An alternative scheme uses no centralized lookup service. Instead, a peer acting as a client must discover what node provides a desired service by broadcasting a request for the service to all other nodes in the network

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/5515983c-a806-436d-9040-69512cdc7845)



### Cloud Computing

Cloud computing is a type of computing that deliver computin, sotorag, and even applicaitons as a service across a network. 

Types of cloud computing:

- Public cloud: a cloud available via the Internet to anyone willing to pay for the services
- Private Cloud: a cloud run by a company for that company's own use
- Hybrid Cloud: includes both public and private cloud components
- Software as a Service (SaaS): one or more applications available via the internet. (ex: google spreadsheets)
- Platform as a Service (PaaS): a software stack ready for application use via the internet.
- Infrastructure as a service (IaaS): servers or storage available over the Internet (ex: storage available for making backup copies).
![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/f1bf183c-ca8f-40bc-b2c8-9e5e393cba48)



### Real-Time Embedded Systems


Embedded computers are the most prevalen form of computers in existence. These devices are found everywhere, from car engines to microwaves. They tend to have very specific tasks. The systems they run on are usually primitive, an so the operating systems provide limited features.
These embedded systems vary considerably. Some are general-purpose computers, running standard operating systems (for example Linux) with special purpose application to implement the functionality. Others are hardware devices with a special-purpose embedded operating  system providing just the functionality desired. Yet other are hardware devices with application-specific integrated circuits (ASICs) that perform their tasks without an operating system.

Embedded systems almost always run real-time operating systems. A real time system has well-defined, fixed time constraints. Processing must be done within the defined constraints, or the system will fail. A real time system functions correctly only if it returns the correct result within its time constraints.


## Summary

- An operating system is software that manages the computer hardware, as well as providing an environment for application programs to run.
- Interrupts are a key way in which hardware interacts with the operating system. A hardware device triggers an interrupt by sending a signal to the CPU to alert the CPU that some event requires attention. The interrupt is managed by the interrupt handler.
- For a computer to do so its job of executin programs, the programs must be in main memory, which is the only large storage area that the processor can access directly.
- The main memory is usually a volatile storage device that loses its contets when power is turned off or lost.
- Nonvolatile storage is an extension of main memory and is capagble of holding large quantities of data permanently.
- The most common nonvolatile storage device is a hard disk, which can provide storage of both programs and data.
- The wide variety of storage systems in a computer system can ve organized in a hierarchy according to speed and cost. The higher levels are expensive, but they are fast. As we move down the hierarchy, the cost per bit decreases, whereas the accesss time increases.
- Modern computer architecture are multiprocessor systems in which each CPU contains several computing cores.
- To best utilize the CPU, modern oprating systems emply multiprogramming, which allows several josbs to be in memory at the same time, thus ensuring that the CPU always has a job to execute.
- Multitasking is an extension of multiprogramming wherein CPU scheduling algorithms rapidly switch between processes, providing users with a
fast response time
- To prevent user programs from interfering with the proper operation of
the system, the system hardware has two modes: user mode and kernel
mode.
- Various instructions are privileged and can be executed only in kernel
mode.
- A process is the fundamental unit of work in an operating system. Process management includes creating and deleting processes and providing mechanisms for processes to communicate and synchronize with each other
- An operating system manages memory by keeping track of what parts of memory are being used and by whom. It is also responsible for dynamically allocating and freeing memory space
- Storage space is managed by the operating system; this includes providing
file systems for representing files and directories and managing space on
mass-storage devices.
- Operating systems provide mechanisms for protecting and securing the
operating system and users. Protection measures control the access of
processes or users to the resources made available by the computer system.
- Virtualization involves abstracting a computer’s hardware into several
different execution environments.
- Data structures that are used in an operating system include lists, stacks,
queues, trees, and maps
- Computing takes place in a variety of environments, including traditional computing, mobile computing, client–server systems, peer-to-peer systems, cloud computing, and real-time embedded systems.
- Free and open-source operating systems are available in source-code format. Free software is licensed to allow no-cost use, redistribution, and modification. GNU/Linux, FreeBSD, and Solaris are examples of popular open-source systems







