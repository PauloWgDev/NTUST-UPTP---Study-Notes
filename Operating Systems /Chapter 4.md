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









