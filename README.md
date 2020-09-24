# 02229-Systems-Optimization-exercise

Exercise code for course 02229 Systems Optimization

Assignment of real-time tasks to the multicores of an autonomous vehicle platform using simulated annealing + response time analysis

## Explanation on code

* main.py: the entrance of the project

* Entity.py: defines the classes which represents tasks, cores and final solution

* data_loader.py: handle the input and output

* algorithms.py: defines the algorithms that used in the project like simulated annealing and response time analysis

* solutions/: where the program put output files

## How to run the code

(The code was writen and tested in Python3.7, should be working on any Python 3.x interpreter)

All commands should be running in the root path(path that contains this readme file)

The results in the solutions folder are calculated by running the following commands

* small.xml: `python main.py small`

* medium.mxl: `python main.py medium`

* large.xml: `python main.py large`

The first parameter means the file name of the input, other than that one can put another parameter which indicates the initial temperature to use, for example

`python main.py large 100000`

If no value of this parameter the default one is going to be used which is 10000
