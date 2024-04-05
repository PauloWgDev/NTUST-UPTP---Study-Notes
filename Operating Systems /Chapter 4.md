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



