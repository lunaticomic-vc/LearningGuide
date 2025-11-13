# Concurrency

Sequential vs Parallel computing
Sequential - a single processor
Parallel - break down tasks to run at the same time

## Flynn's Taxonomy

                               Instruction streams                             
                              single        multiple                              
data streams   single          SISD          MISD
               multiple        SIMD          MIMD


Threads and Processes
Concurrent vs Parallel

Scheduling

Lock
Reentrant Lock
ReadWrite Lock
DeadLock
Putting critical sessions in Try blocks

Dining philosopher's example

Fairness in Starvation. Workload management.

Livelock.

Context Manager
Starvation
