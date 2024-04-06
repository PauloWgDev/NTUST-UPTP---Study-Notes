# Threads & Concurrency

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/78555d43-680f-49f1-91e3-a9c491611583)

## Benefits of multithreaded Programming
- Responsiveness: Multithreading an interactive application may allow a program to continue running even if part of tit is blocked or is performing a lengthy operation, thereby increasing responsiveness to the user.
- Resouce Sharing: Process can share resource only through techniques such as shared memory and message passing.
- Economy: Allocating memory and resources for process creation is constly. Because threads share the resource of the process to which they belong, it is more economical to create and context-switch threads.
- Scalability: the benefits of multithreading can be even greater in a multiprocessor architecture, whre threads may be running in parallel on different processing cores.

## Multicore Programming

Multicore and multithread programming provides a mechanism for more efficient use of these multiple computing cores and improved concurrency.
On a system with multiple core, however, concurrency means that some threads can run in parallel, because the system can assign a separate thread to each core.
There is a distiction between concurrecnty and parallelism. Concurrency means that the system supports more than one task by allowing all the tasks to make progress. In contrast, a parallel system can perform more than one task simultaneously. Thus, it is possible to have concurrency witout paralellism.

### Programming Challenges
In general there are five areas that present challenges in multicore programming:
- Identifying Tasks: This involves examining application to find areas that can be divided into separate, concurrent tasks.
- Balance: Ensuring that the tasks perform equal work of equal value. In some instances, a certain task may not contribute as much value to the overall process as other tasks.
- Data Splitting: The data accessed and manipulated by the tasks must be divided to run on separate cores.
- Data Dependency: The data accessed by the tasks must be examined for dependencies between two or more tasks. When one task depends on the other, programmers must ensure that the execution of the tasks is synchronized to accomodata the data dependency.
- Data Splitting: The data accessed and manipulated by the tasks must be divided to run on separate cores.
- Data Dependency: The data accessed by the tasks must be examined for dependencies between two or more tasks. When one task depends on data from another, programmers must ensure that the execution of the tasks is synchronized to acommodate the data dependency.
- Testing and Debugging: When a programmer is running in parallel on multiple cores many different execution paths are possible. Testing and Debuggin such concurrent paths becomes more difficult.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/84a3c495-01ca-42f7-8082-41746779d8ca)


#### Amdahl's Law

Amdahl's law is a formula that identifies potential performance gains from adding additional computing cores to an application that has both serial and parallel components. If S is the portion on the application that is Serial and N is the processing cores. The formula is as follows:

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/d03fb62f-f5a2-4bc3-9c57-5d562bb37488)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/9da6de8a-ad33-49c8-8efe-666b3abdcdfb)

### Types of Parallelism 

**Data Parallelism** focuses on distributing subsets of the same data across multiple computing cores and performing the same operation on each core.
For example, lets say you have an array of size N and you want to calculate the sum of all its elements, with data parallelism you would use one core to calculate the sum of all the elements from elemnt [0] to element [N/2 - 1], and in the second core you would calculate the sum of all the elements from [N/2] to [N - 1].

**Task Parallelism** involves distributing not data but tasks (threads) accross multiple computing cores. Each thread is performing a unique operation. Different threads may operate on the same data or may operate on different data.

**In summary, data parallelism involves the distribution of data across multiple cores, and tasks parallelism involves the distribution of tasks across multiple cores.**

## Multithreading Models

A relationship must exist among a user thread and a kernel thread, there are different approaches for creating this relationship:

### Many to One Model
Many user threads to one kernel thread. In this model the entire process will block if a thread makes a blocking system call. Also, because only one thread can access the kernel at a time, multiple threads are unable to run in parallel on multicore systems.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/6342740d-2822-4f46-8d06-03dd260bf827)

### One to One Model
This model maps each user thread to a kernel thread. It provides more concurrency and allows another thread to run when a thread makes a blocking system call. It also allows threads to run in parallel in multiprocessor systems. The only drawback is that creating a user thread requires also creating a kernel thread, and a large number of kernel threads may burden the perfornmance of the system.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/0acfd9c1-f4c3-4c26-a764-338fc6804795)


### Many to Many

Multiplexes many user-level threads to aa smaller or equal number of kernel threads. The many to one model allows the developer to create as many user threads as he wishes, it does not result in parallelism, because the kernel can schedule only one kernel thread at a time. So the one to one model provides more concurrency.

Also, when a thread performs a blocking system call, the  kernel can schedule another thread for execution. 

One variation still multiplexes many user threads to a smaller or equeal number of kernel threads but also allows a user level thread to be bounded to a kernel thread. This variation is sometimes referred to as the two-level model. 

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/c9cd6e71-d550-4fae-9955-37b9e093aee7)

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/4f1633a3-f3d4-4bf0-826f-877a9494cb01)


## Thread Libraries

A thread library provides the programmer with an API for creating and managing threads.

There are two approaches for implementing a thread library:
- First approach is to provide a library entirely in user space with **no kernel support**.
- Second approach is to **implement a kernle-level library** supported directly by the operating system.

Three main Librarires are use today: 
- **POSIX Pthreads**: may be provided as user-level or kernel-level library
- **Windows**: is a kernel-level library available on windows
- **Java**: because in most instances the JVM is running on top of a host operating system, the Java thread API is generally implemented using a thread library available on the host system.

**Two general Strategies for creating Threads:**
- **Asynchronous threading**: Once the parent creates a child thread, the parent resumes its execution, so te parent and child execute concurrently and independently of one another.
- **Synchronous threading**: the parent thread creates one or more children and must wait for all of its children to terminate before it resumes.

### Pthread

```c
#include <pthread.h>
#include <stdio.h>

#include<stdlib.h>

int sum;
void *runner(void *param); // thread call this function
int main()
{
	pthread_t tid; // thread indentifier
	pthread_attr_t attr; // set of thread attributes

	// set the default attributes of the thread
	pthread_attr_init(&attr); 

	// create the thread
	pthread_create(&tid, &attr, runner, argv[1]);

	//wait for the thread to exit
	pthread_join(tid, NULL);
}

void *runner(void *param)
{
	// logic happens here

	pthread_exit(0);
}

```

## Implicit Threading

One way to address the difficulties of and better support the design of concurrent and parallel application is to transfer the creation and management of threading from application developers to compilers and run-time libraries. This strategy is called **implicit threading**.


### Thread Pools

Although creating a separeate thread is more efficient that createing a separate process, a multithreaded system still has problems. One is the time it takes to create a thread along with the fact that once this thread is completed it will be discarted. The second problem is more serious, and is that if we are not keeping track of the amount of threads currently active in the system, Unlimited threads could exhaust the system resources. One solution to this problems is to use a **thread pool.**

The **general idea** behind a thread pool is to create a number of threads at start-up and place them into a pool, where they sit and wait to be assigned a task. When a the system recieves a request, instead of creating a thread from scratch, it will simply submit the requesto to the thread pool and if a thread is available it will use it. If there is no thread available, the task is queued until one becomes free.

**Thread Pool Benefits:**

- Using an existing thread is often faster than waiting to create a thread.
- A thread pool limits the number of existing threads at any point.
- Separating the task to be performed from the mechanism of creating the task allows us to use different strategies for running thr task. For example, the task could be scheduled to execute after a time delay.

The number of threads in the pool can be set based on factors such as the number of CPUs in the system, the amount of physical memory, and the expected number of concurrent client requests.

### Fork Join

**Fork Join**: the parent thread creates (forks) one or more child threads and then waits for the children to terminate and **join** with it.

![image](https://github.com/PauloWgDev/NTUST-UPTP---Study-Notes/assets/133529935/ffd9a3e6-80e8-48c0-8c29-703a7d7537ba)

## Summary

// to do: search for a video that clearly explains the difference between a thread and a process

- A thread represents a basic unit of CPU utilization, and threads belonging to the same process share many of the process resources, including code and data.
- Primary benefits of multihreaded applications are: (1) respoonsiveness, (2) resource sharing, (3) economy, and (4) scalability.
- Concurrency exists when multiple threads are making progress, whereas parallelism exists when multiple threads are making progress simultaneously. A single core system is capable of concurrency, but for parallelism a multicore system is required.
- Challenges in designing multithreaded applications include: divinding and balancing the work, divinding the data between different threads, identifying any data dependencies and testing and debugging.
- Data parallelism distributes subsets of the same data across multiple cores and performs the same operation in those cores. Task parallelism distributes the task across multiple cores, this tasks could be using a shared memory.
- User applications create user-level threads that must ultimately be mapped to kernel threads to execute on a CPU.
- A thread library provides an API for creating and managing threads. Three common thread librarries include Windows, Pthreads and Java threading.
- Implicit threading involves identifying tasks (not threads) and allowing langugage or API frameworks to create and amange threads. Essentially freeing applications developers from the duty of implementing a multithread system.
- Thread can by terminated using asynchronous or deferred cancelation. Asynchronous cancellation stops a thread immediately, even if it is in the middle of performing an update. Deferred cancellation informs a thread that it should terminate but allows the thread to terminate in a orderly fashion.
- Unlike many other operating systems, the Linux system does not distinguish between process and threads; insted it refers to each as task.

---

# Extra


## Process vs Thread

### Program
A program is the executable file that containts the instruction that are store in the disk.


### Process
A process include the resouces a program needs to run

It includes:
- Processor Register
- Program Counters
- Stack Pointers
- Memory pages

Each process has its own memory address space, one process cannot corrupt the memory address space of another process.
This means that when one process malfuncitons other process can keep running.

### Thread

A thread is the unit of execution wihtin the process. 
A process usually has a main thread and then other subthreads.

Each Thread has its own:
- Stack
- Registers
- Program counters

Threads usually hace a shared memory address space.

However one corrupted thread could corrupt the entire system.

**Context Switch:**

During a context switch, one process is switch out of the CPU so another can run.
The OS stores the state of the thread so it can then resume its execution. 

Context Switching is expensive. 

Is usually cheaper to switch threads than to switch processes.






