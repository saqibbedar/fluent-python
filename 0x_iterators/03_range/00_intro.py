"""
Range iterator: It stores only three integers that's why its memory efficient:
    start=1
    stop=1000
    step=1

    syntax: range(start, stop, step) this is equivalent to an object like 

    class myrange:
        
        def __init__(self, start : int = 0, stop : int, step : int = 1) -> None:
            self.start = start
            self.stop = stop
            self.step = step



Quick facts:

    1. If we pass single value then it is stop value 
        
        for i in range(5)       # here 5 is stop value, it stops before 5, range automatically set start = 0

        Mathematically: [0, 5)      
        
        Inclusive start and Exclusive stop

        0 included       |  5 excluded

    
    2. range(3, 8)          # start from 3 and stop before 8

        output: 3, 4, 5, 6, 7


    3. Default start value is 0 and step value is 1


    4. step is jump, set how much value be added into start for next iteration

        range(2, 10, 2)

        output: 2, 4, 6, 8

        internally: start += 2 
        And condition is checked against stop is (current >= stop)


    5. Countdown example: range(10, 0, -1)          # golden trick: whatever value of stop is i.e., 0, -1 etc will never printed.

        for i in range(10, 0, -1):
            print(i)

        # Output: start=10, end=0, step=-1

        10
        9
        8
        7
        6
        5
        4
        3
        2
        1  

        (0 not printed because at 0 it has to be stopped)


        
        for i in range(10, -1, -1)
            print(i)

        output:
        10
        9
        8
        7
        6
        5
        4
        3
        2
        1
        0

        why 0? because -1 is stop value so it has keep iterate until it is checked against the stop value

        

"""