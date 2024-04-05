'''Power Hungry
============

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with doomsday devices take even more power. 
To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. 
But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. 
You and your team of henchmen have been assigned to repair the solar panels, but you'd rather not take down all of the panels at once if you can help it, 
since they do help power the space station and all!You need to figure out which sets of panels in any given array you can take offline 
to repair while still maintaining the maximum amount of power output per array, and to do THAT, you'll first need to 
figure out what the maximum output of each array actually is. 
Write a function solution(xs) that takes a list of integers representing the power output levels of each panel in an array, 
and returns the maximum product of some non-empty subset of those numbers. 
So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], 
then the maximum product would be found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  
So solution([2,-3,1,0,-5]) will be "30".Each array of solar panels contains at least 1 and no more than 50 panels, 
and each panel will have a power output level whose absolute value is no greater than 1000 
(some panels are malfunctioning so badly that they're draining energy, but you know a trick with the panels' 
wave stabilizer that lets you combine two negative-output panels to produce the positive output of the multiple of their power values). 
The final products may be very large, so give the solution as a string representation of the number.

Input:solution.solution([2, 0, 2, 2, 0])Output:    8

Input:solution.solution([-2, -3, 4, -5])Output:    60'''



# Completed in: 1 hr, 43 mins, 29 secs..
def solution(xs):
    if len(xs) < 1 or len(xs) > 50:
        raise ValueError('Wrong dimensionality. Enter the correct number of values.')
    if len(xs) == 1:
        return str(xs[0])
    if all(x == 0 for x in xs):
        return str(0)
    if all(x <= 0 for x in xs):
        return str(0)
    
    positives = []
    negatives = []
    negative = 0
    for el in xs:
        if abs(el) > 1000:
            raise ValueError('Wrong power output level.')
        elif el > 0:
            positives.append(el)
        elif el < 0:
            negative += 1
            negatives.append(el)

    if negative == 1:
        return str(negatives[0])
    
    summa = sum(xs)
    if negative == 1 and summa == negative:
        return str(0)
    
    if negative == 1 and len(positives) == 0:
        return str(0)
    
    negatives.sort()
    # if no negatives and no ones
    if negative == 0 and not any(x == 1 for x in positives):
        mult_n = 1
    elif negative == 0 and any(x==1 for x in positives):
        positives.sort()
        positives = positives[1:]
        mult_n = 1
    elif negative % 2 == 0:
        mult_n = negatives[0]
        for el in negatives[1:]:
            mult_n *= el
    else:
        negatives.pop(-1)
        mult_n = negatives[0]
        for el in negatives[1:]:
            mult_n *= el

    for el in positives:
        mult_n *= el 
    return str(mult_n)