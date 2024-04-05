'''Hey, I Already Did That!
============

Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep minions on their toes. 
But you've noticed a flaw in the algorithm - it eventually loops back on itself, so that instead of assigning new minions as it iterates, 
it gets stuck in a cycle of values so that the same minions end up doing the same tasks over and over again. 
You think proving this to Commander Lambda will help you make a case for your next promotion. You have worked out that the algorithm has the following process: 
1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next minion ID, and go back to step 2. 
For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 
and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.
Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. 
For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] 
and it will stay in this cycle no matter how many times it continues iterating. Starting with n = 1211, the routine will reach the integer 6174, 
and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.
Given a minion ID as a string n representing a nonnegative integer of length k in base b, where 2 <= k <= 9 and 2 <= b <= 10, 
write a function solution(n, b) which returns the length of the ending cycle of the algorithm above starting with n. 
For instance, in the example above, solution(210022, 3) would return 3, since iterating on 102212 would return to 210111 when done in base 3. 
If the algorithm reaches a constant, such as 0, then the length is 1.

-- Python cases --
Input:solution.solution('1211', 10) Output:    1

Input:solution.solution('210022', 3) Output:    3'''

def get_base(number, n):
    rest = int(number)
    digits = []
    while rest >= n:
        r = rest % n
        digits.append(str(r))
        rest = (rest - r) // n
    digits.append(str(rest))
    digits = ''.join(digits[::-1])

    return digits


def get_base_10(number, n):
    x = list(number[::-1])
    res = 0
    for i, y in enumerate(x):
        res += (n ** i) * int(y)
        
    return str(res)
    
def solution(n, b):
    k = len(n)
    curr_n = n
    unique_ids = []
    
    while curr_n not in unique_ids:
        unique_ids.append(curr_n)
        s = sorted(curr_n)
        x = ''.join(s[::-1])
        y = ''.join(s)        
        if b == 10:
            curr_n_int = int(x) - int(y)
            curr_n = str(curr_n_int)
        else:
            curr_n10 = int(get_base_10(x, b)) - int(get_base_10(y, b))
            # Convert back into base b
            curr_n = get_base(str(curr_n10), b)

        curr_n =  (k - len(curr_n)) * '0' + curr_n
    # Length of the sequence until the first repetition of curr_n
    return len(unique_ids) - unique_ids.index(curr_n)
