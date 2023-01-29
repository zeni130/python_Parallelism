# python_Parallelism
##### **Python Concurrency/Parallelism**

_Programs that solve the same
problem using threading and multiprocessing._ 

______

______

#### Task:

_Parallel download of data from [jsonplaceholder](https://jsonplaceholder.typicode.com).
Download parallel posts in separate files.
That is, requests https://jsonplaceholder.typicode.com/posts/1, https://jsonplaceholder.typicode.com/posts/2 
and so on must be executed in parallel and save data to files post_1.json, post_2.json and so on.
A total of 100 posts must be downloaded._



#### Additional task:

_Find a way to limit concurrent tasks (queries and saves) to N (for example, up to 10). 
That is, no more than N tasks should be performed at one time. When one task is completed, 
the next one should start immediately._

______

______

### Run comparison script:
````
python console_test.py
````
