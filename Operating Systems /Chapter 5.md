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









