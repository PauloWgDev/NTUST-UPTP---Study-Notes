# CPU Scheduling

On modern operating systems it is kernel-level threads (not processes) that are in fact bing scheduled by the operating system. However, the terms "process scheduling" and "thread scheduling" are often interchangeably.


## Basic Concept of Multiprogramming

The objective of multiprogramming is to have some process running at all times in order to maximize the CPU utilization. 
The idea is that a process is executed until it must wait. In a simple system, the CPU would just sit idle and all that waiting time would be wasted. With multiprogramming, we try to use this time productively. Several processes are kept in memory at once so that when one has to wait, the operating system takes the CPU away from that process and assigns it another process. Everytime a process has to wait, another process can take over use uf the CPU.

### CPU I/O Burst Cycle

Process execution consists of a cycle of CPU execution and I/O wait. Process alternate between these two states. PRocess execution begins with a CPU burst. That is followed by an I/O butst, which is followed by another CPU burst, and so on. Eventually the final CPU bust ends with a system request to terminate execution.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/4f583157-c12c-4ccd-9eb2-c1f53a90bdc5)


![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/20411cca-6709-4346-b1cc-d2f97e55c561)
An I/O-bound program typically has many short CPU busts. A CPU-bound program might have a few long CPU bursts. 

### CPU Scheduler

Whenever the CPU becomes idle, the operating system must select one of the processes in the ready quue to be executed. The selection process is carried out by the CPU scheduler. 

The ready queue is not necessarly a FIFO queue. 

A ready queue can be a FIFO queue, priority queue, a tree, or simply an unordered linked list.

The records in the queue are generally process contorl blocks (PCB) of the process.

### Preemptive and Nonpreemptive Scheduling

CPU-Scheduling decision may take place under the following circumstances:

1. When a process switches from the running state to the waiting state.
2. When a process switches from the running state to the ready state. (ex: when an interrupt occurs)
3. When a process switches from the waiting state to the ready state. (ex: at completion of I/O)
4. When a process is terminated.

For situation 1 and 4, there is no choice.

For situation 2 and 3, there is a choice.

When scheduling takes place **only** under circumnstances 1 and 4, we say that the scheduling scheme is **nonpreemptive** or **cooperative**. Otherwise, it is **preeemptive**.


Under non preemptive scheduling, once the CPU has been allocated to a process, the process keeps the CPU until it realeases it either by terminating or by switching to the waiting state.


### Dispatcher

The distpatcher is the module that gives control of the CPU's core to the process selected by the CPU scheduler. This function involves:
- Switching context from one process to another
- Switching to user mode
- Jumping to the proper location in the user program to resume that program.

The dispatcher is invoked during every context switch. 
The time it takes for the dipatcher to stop one process and start another running is known as the **dispatch latency**.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/ca08a19b-315b-4a3b-88d6-e076a49f4457)


## Scheduling Criteria

Many Criteria have been suggested for comparing CPU-scheduling algorithms.
The cirteria include the following:
- CPU utilization. We want to keep the CPU as busy as possible
- Throughput. If the CPU is busy executing processes, then work is being done. One measure of work is the number of processes that are completed per time unit, called throughput
- Turnaround time.  The interval from the time of submission of a process to the time of completion is the turnaround time. Turnaround time is the sum of the periods spent waiting in the ready queue, executing on the CPU, and doing I/O.
- Waiting time. The CPU-scheduling algorithm does not affect the amount of time during which a process executes or does I/O. It affects only the amount of time that a process spends waiting in the ready queue.
- Response time. nother measure is the time from the submission
of a request until the first response is produced. This measure, called response time, is the time it takes to start responding, not the time it takes to output the response.

## Scheduling Algorithms

CPU scheduling deals with the problem of deciding which of thee processes in the ready quue i to be allocated the CPU's core.

### First-Come, First Served Scheduling (FCFS)

Is the simples CPU-scheduling algorithm. With this scheme, the process that request the CPU first is allocated the CPU first. It is managed using a FIFO queue.

On the negative side, the average waiting time under the FCFS policy is often quite long.

Ex:

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/25dbced6-1e0e-49e9-815d-8a9304ccfd56)

If the processes arrive in the order P1, P2, P3:

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/9777647d-b324-4398-99d6-5874375de393)


The waiting time would be: (o + 24 + 27)/3 = 17 milliseconds



another case:

Lets now asume that the process arrive in the order P2, P3, P1:

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/b6778873-72fb-491b-acd5-3ace2e5a5a2e)

The average waiting time now would be: (6 + 0 + 3)/3 = 3 milliseconds

### Shortest Job First Scheduling (SJF)

This algorithms with each process the length of the process's next CPU burst. When the CPU si available, it is assigned to the process that ahs the smalles next CPU burst. IF the next CPU bust of two process are the same, FCFS scheduling is used to break the tie.
A more appropiate term for this scheduling mehtod would be the "shortest next CPU burst" algorithm.

Example:

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/371b1d46-e2b5-491a-827e-4abbaee18fa7)

Using SFJ scheduling:

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/848ae29e-f734-4b43-be7e-db209686e9d9)

average waiting time = (3 + 16+ 9 + 0)/4 = 7 milliseconds

### Round-Robin Scheduling 

Similar to FCFS scheduling, but preemption is added to enable the system to switch between processes. A small unit of time called **time quantum** or **time slice** is defined. 

To implement the RR scheduling, we again use a FIFO queue of proceses.

The CPU scheduler pickes the first process from the ready queue and sets a timer to interrupt after 1 time quantum, and distpatch the process.

The process may have a CPU burst of less than 1 time quantum, in this case the process itself will release the CPU voluntarly. 
If the CPU burst of the current running process is longer than 1 time quantum, the timer will go off and will cause an interrupt to the operating system. A context switch will be executedn and the process will be put at the tail of the queue.

Ex:

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/28ed2912-992e-42fe-b90e-c09aa7568ac3)


Using RR schedule:

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/7a53a807-02cd-406f-831b-011110558a13)

P1 waits for (10 - 4) = 6 ms, P2 waits for 4 ms, P3 waits for 7 ms
Average waiting time = 17/3 = 5.66 ms

### Priority Scheduling

The SJF algorithms is a special case of the general priority-scheduling algorithm. 

A priority is associated with each process, and the CPU is allocated to the process with highest priority. Equal proprity use FCFS scheduling.

Priorities can be defined either internally or externally, 

Internally defined priorities use some measurable quantity to compute the priority. For example it may use time limits, memory requirementes, number of open files, etc. 

External priorities are set by criteria outside the operating system, often times are political factors. 

Priority scheduling can be either preemptive or nonpreemptive 

A major problem with priority scheduling algorithms is indefinit blocking or **starvation**. A priority scheduling algorithm can leave some low priority process waiting indefinitely.

### Multilevel Queue Scheduling

In a priority scheduling, depending on how the queues are manages an O(n) search may be necessary to determine the highest priority process. In practice it is often easier to have separate queues for each distinctive priority.
This approach is known as multilevel queue. 
Also works well when priority scheduling is combined with RR scheduling.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/cad871dc-8b7d-4980-a407-c959ef6227e7)

Multilevel queue scheduling algorithm canalso be used to partition processes into several separate queues based on the process type. For example you could divide foreground process in a queue and background process in another.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/12251510-4bf0-4be9-be52-c1d50f26ee7b)


### Multilevel Feedback Queue Scheduling

Normally, when the multilevel queue scheduling algorithm is used, processes are permanently assigned to a queue when they enter the system.
This setup has the advantage of low scheduling overhead, but it is inflexible.

The **multilevel feedback queue**, in contrast, allows a process to move between queues. The idea is to separate processes according to the characteristics of their CPU burst. If a process uses too much CPU time, it will be moed to a lower-priority queue.

In addition, a process that waits too long in a lower priority queue may be moved to a higher priority queue. This form of aging provents starvation.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/b5b61839-9af8-49c1-b746-2de7a311b612)

In general, a multilevel feedback queue scheduler is defined by the following parameters:

- Number of queue
- Scheduling algorithms for each queue
- The method used to determine when to upgrade a process to a higher priority queue
- The method used to determine when to demote a process to a lower priority queue
- The method used to determine which queue a process will enter when that process needs service


The definition of a multilevel feedback queue scheduler makes it the most
general CPU-scheduling algorithm


## Thread Scheduling

On most modern operating systems it is kernel-level threads (not processes) that are being scheduled by the operating system. To run on a CPU, user level threads must ultimately be mapped to an associated kernel-level thread.

### Contention Scope

On systems implementing the many-to-one or many-to-many models, the thread library schedules user-level threads to run on an available LWP (light weight process). This scheme is known as process contention scope (PCS). 

To decide which kernel-level thread to schedule onto a CPU, the kernel uses system-contention scope (SCS).

## Multi-Processor Scheduling

If multiple CPUs are available, **load sharing**, where multiple threads may run in parallel, becomes possible, however shceduling issues become correspondingly more complex.

*multiprocessors* apply to the following system architectures:

- Multicore CPUs
- Multithreaded cores
- NUMA systems
- Heterogenous multiprocessing


### Approaches to Multiple-Processor Scheduling

One approach to CPU scheduling in a multiprocessor system has all scheduling decisions, handled by a single processor (the master server). The other processors execute only user code. This **asymmetric multiprocessing** is simple because only one core accesses the system data structures, reducing the need fo data sharing. The downfall of this approach is that the master server becomes a potential bottleneck.

The standard approach for supporting multiprocessor is **Symmetric multiprocessing (SMP)**, where each processor is self-scheduling.
This provides two possible strategies:
1. All threads may be in common ready queue.
2. Each processor may have its own private queue of threads.

The first option must ensure that two separate processors do not choose to schedule the same thread and that threads are not lost from the queue.

The second option permits each processor to schedule threads from its private run queue and threrefore does not suffer from the possbile performance problems associated with a shared run queue. For this reason it is the most common approach.

### Multicore Processors

Multiple computing cores on the same phusical chip, resulting in a multicore processor.

SMP systems that use multicore processors are faster and consume less power than systems in which each CPU has its own physical chip.

Multicore processors may complicate scheduling issues.
When a processor accesses memory, it spends a significan tammount of time waiting for the data to become available. This situation, known as memory stall, occurs primarily because modern processors operate at much faster speeds than memory.

To remedy this situation, many recent hardware designs have implemented multithreaded processing cores in which two or more hardware threads are assigned to each core. That way, if one hardware thread stalls while waiting for memory, the core can switch to another thread.
This technique is known as chip multithreading (CMT).


![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/7f31bb86-af5f-4140-be63-bc4c801b953b)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/01427f48-775b-43a9-bd21-daa689f26053)

In general, there are two ways to multithread a processing core: **coarse-grained** and **fine-grained** multithreading. With coarse-threading multithreading, a thread executes on a core until a long-latency event such as a memory stall occurs. Because of the delay caused by the long-latency event, the core must switch to another thread to begin execution. However, the cost of switching between threads is high, since the instruction pipeline must be flushed before the other thread van begin execution.

Fine-grained (or interleaved) multithreading switches between threads at a much finer level of granularity. Tipically at the boudary of an instruction cycle. However, the architectural design of fined-grained systems includes logic for thread switching. As a result, the cost of switching between threads is small.

The resources of the physical core (such as cache and pipelines) must be shared among its hardware threads, and therefore a processing core can only execute one hardware thread at a time.

Multicore processor require two different levels of scheduling:

- One one level are the scheduling decisions that must be made by the operating system as it chooses which software thread to run on each hardware thread.
- A second LEvel of scheduling specifies how each core decides which hardware thread to run.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/52c70e3b-17ca-4fc8-a11a-52e5b662f57f)


### Load Balancing

It is important to note that load balancing is typically necessary only ob systems where each processor has its own private ready quue of eligible threads to execute. On systems with a common run queue, load balancing is unnecessary, because once a processor becomes idle, it immediately extracts a runnable thread from the common ready queue.

THere are tow general aprproaches to load balancing:
- **Push Migration**: a specific task periodically checks the lead on each processor and if it finds an imbalance, evely distributes the load by moving (pushing) threads from overloaded to less busy processors.
- **Pull Migration**: occurs when a n idle processor pulls a waiting task from a busy processor.

### PRocessor Affinity

The data most recently accessed by the thread populate the cache for the processor. As a result, successive memory accesses by the thread are often satisgied in cache memory (known as warm cache). Now, if the trhead migrates to another processor (for load balancing for example). The contents of cache memory must be invalidated for the first processor and repopulated for the second, this process has a very high cost, so most operating system with SMP try to avoid it and instead atttempt to keep a thread running on the same processor and take advantage of a warm cache. This is known as processor afinit (that is, a process has an affinity for the processor on which it is currently running).

Processor affinity takes several forms:

- Soft Affinity: When an operating system has a policy of attempting to keep a process running on the same processor but not guaranteeing that it will do so.
- Hard Affinity: allowing a process to specify a subset of processor  on which it can run.

### Heterogenous Multiprocessing

Some systems are now designed using cores that run the same instruction set, yet vary in terms of their clock speed and power management, including the ability to adjust the power consumption of a core to the point of idling the core. Such systems are known as heterogenous multiprocessing (HMP).


## Real Time CPU scheduling

We can distinguish between soft real-time systems and hard real-time systems:

- SOft real-time systems: provide no guarantee as to when a critical real-time process will be scheduled. They guarantee only that the process will be given proference over noncritical process.
- Hard real-time systems have stricter requirements. A task must be services by its deadline; service after the deadline is the same as no service at all.

### Minimizing Latency

We refer to **event latency** as the amount of time that elapses from when an event occurs to when it is serviced.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/52d1654a-09d3-4d01-9034-9481e5322e28)

Two typea of latency affect the performance of real-time systems:
1. Interrupt latency
2. Dispatch latency

Interrupt latency refers to the perdio of time from the arrival of an interrupt at the CPU to the start of the routine that services the interrupt.

The amount of time required for the scheduling distpatcher to stop one process and start another is known as dispatch latency.


![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/d3f20986-8a09-4f11-9310-327b571a633b)


![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/7de25b05-ee49-415b-a76f-85424631372e)


The most effective technique for keeping dispatch latency low is to provide preemptive kernels. For hard real-time systems, dispatch latency is typically measured in several microseconds.
The conflicphase of dispatch latency has two components: 
1. Preemption of any process running in the kernel
2. Release by low-priority processes of resources needed by a high-priority process.

### Priority-Based Scheduling

The most important feature of a real-time operating system is to reapons immediately to areal itme process as soon as that proces requres the CCPU. As a result, the scheduler for a real time operating systemmsut support a priority based algorithms with preemption.

Providing a preemptive, priority based scheduler only guarantees soft real time funcitonality. 

Before we proceed with the detail of the individual schedulers, we must define certain characteristics of the processes that are to be scheduled.
First, the processes are considered periodic. That is, they require the CPU at constant intervals (periods). Once a periodic process has acquired the CPU, it has a fixed processing time t, a deadline d and a period p. the relationship of these characteristics is: 
0 <= t <= d <= p

The rate of a periodic task is 1/p.

Then, using a technique known as admission-control algorithm, the scheduler does one of two thigns.  It eaither admits the process, guaranteeing that the process will complete on time, or rejects the request as impossible if it cannot guarantee that the task will be services by its deadline.


### Rate=Monotonic Scheduling

The rate-monotonic scheduling algorithm schedules periodic tasks using a static priority policy with preemption. if a lower-priority process is runing and a higher priority proces becomes available to run, it will preempt the lower-priority process.


![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/d47627e2-28cf-4824-98af-b130de6435e3)


![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/eab29d43-7a4d-420e-9a0e-eb7a2ca9b1d3)

### Earlies-Deadline-First Scheduling

Earliest-deadline-first (EDF) scheduling assigns priorities dynamically according to deadline.


![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/852d825e-989f-4048-824f-64bde0e7fe89)

### Proportional Share Scheduling

Proportional share schedulers operate by allocating T shares among all applications. An application can receieve N shares of time, thus ensuring that the application will have N/T of the total processor time.

Proportional share schedulers msut work in conjuction with an admission-control policy to guarantee that an application receives its allocated shares of time. An admission control policy will admit a client requesting a particular number of shares only if sufficient shares are available.

## Algorithms Evaluation

Criteria for selectiong an alogorithm are often defined in terms of CPU utilization, response time or throughput. To select an alorithm, we must first define the relative importance of these elements.


### Deterministic Modeling

One major class of evaluation methods is analytic evaluation. Analytic evaluation uses the given algorithms and the systems workload to produce a formula or number to evaluate the performance of the algorithm for that workload.

Deterministic modeling is one type of analytic evaluation. This method takes a particular predetermined workload and defines the performance of each algorithm for that workload.


### Queueing Models

On many systems, the processes that are run vary form day to day, so there is no static set of prcesses to use for deterministic modeling.

The computer system is described as a network of servers. Each server has a queue of waiting processes. The CPU is a server with its ready queue, as is the I/O system with its device queues. Knowing arrival rates and services rates, we can compute utilization, average queue length, average wait time, and so on. 
This area of study is called queueing network analysis.

We expect taht during the time W that a aprocess waits, λ × W new processes will arrive in the queue. If the syste is in steady state, then the number of processes leaving the queue must be equal to the number of proceses that arrive. 


![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/8397554b-548f-432b-82f4-468d2e001f04)


This equation is known as "Little's formula" and it is particularly useful because it is valid for any scheduling alogrithm and arrival distribution.
n could be number of customers for example

### Simulations

To get a more accurate evaluation of scheduling algorithms, we can use simulations. Running simulations involves programming a model of the computer
system

The data to drive the simulation can be generated in several ways. The most
common method uses a random-number generator that is programmed to
generate processes, CPU burst times, arrivals, departures, and so on, according
to probability distributions

A distribution-driven simulation may be inaccurate. To correct this problem, we can use trace files. We create a trace by monitoring the real systesm and recording the sequence of actual events. We then use this sequence to drive the simulations.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/db3c5942-6021-4aa1-982f-217794101d27)

### Implementation 

Even a simulation is of limited accuracy. The only completely accurate way
to evaluate a scheduling algorithm is to code it up, put it in the operating
system, and see how it works. This approach puts the actual algorithm in the
real system for evaluation under real operating conditions.
This method is not without expense. The expense is incurred in coding the
algorithm and modifying the operating system to support it.
There is also cost in testing the changes, usually in
virtual machines rather than on dedicated hardware. Regression testing confirms that the changes haven’t made anything worse, and haven’t caused new
bugs or caused old bugs to be recreated
Another difficulty is that the environment in which the algorithm is used
will change

## Summary

- CPU scheduling is the task of selecting a waiting process from the ready
queue and allocating the CPU to it. The CPU is allocated to the selected
process by the dispatcher.
- Scheduling algorithms may be either preemptive (where the CPU can be
taken away from a process) or nonpreemptive (where a process must
voluntarily relinquish control of the CPU). Almost all modern operating
systems are preemptive.
- Scheduling algorithms can be evaluated according to the following five
criteria: (1) CPU utilization, (2) throughput, (3) turnaround time, (4) waiting
time, and (5) response time
- First-come, first-served (FCFS) scheduling is the simplest scheduling algorithm, but it can cause short processes to wait for very long processes.
- Shortest-job-first (SJF) scheduling is provably optimal, providing the shortest average waiting time. Implementing SJF scheduling is difficult, however, because predicting the length of the next CPU burst is difficult
- Round-robin (RR) scheduling allocates the CPU to each process for a time
quantum. If the process does not relinquish the CPU before its time quantum expires, the process is preempted, and another process is scheduled
to run for a time quantum.
- Priority scheduling assigns each process a priority, and the CPU is allocated
to the process with the highest priority. Processes with the same priority
can be scheduled in FCFS order or using RR scheduling
- Multilevel queue scheduling partitions processes into several separate
queues arranged by priority, and the scheduler executes the processes in
the highest-priority queue. Different scheduling algorithms may be used
in each queue.
- Multilevel feedback queues are similar to multilevel queues, except that a
process may migrate between different queues
- Multicore processors place one or more CPUs on the same physical chip,
and each CPU may have more than one hardware thread. From the perspective of the operating system, each hardware thread appears to be a
logical CPU.
- Load balancing on multicore systems equalizes loads between CPU cores,
although migrating threads between cores to balance loads may invalidate
cache contents and therefore may increase memory access times.
- Soft real-time scheduling gives priority to real-time tasks over non-realtime tasks. Hard real-time scheduling provides timing guarantees for realtime tasks,
- Rate-monotonic real-time scheduling schedules periodic tasks using a
static priority policy with preemption
- Earliest-deadline-first (EDF) scheduling assigns priorities according to
deadline. The earlier the deadline, the higher the priority; the later the
deadline, the lower the priority.
- Proportional share scheduling allocates T shares among all applications. If
an application is allocated N shares of time, it is ensured of having N∕T of
the total processor time.
-  Linux uses the completely fair scheduler (CFS), which assigns a proportion
of CPU processing time to each task. The proportion is based on the virtual
runtime (vruntime) value associated with each task.
-  Windows scheduling uses a preemptive, 32-level priority scheme to determine the order of thread scheduling.
-  Solaris identifies six unique scheduling classes that are mapped to a global
priority. CPU-intensive threads are generally assigned lower priorities
(and longer time quantums), and I/O-bound threads are usually assigned
higher priorities (with shorter time quantums.)
- Modeling and simulations can be used to evaluate a CPU scheduling algorithm.
