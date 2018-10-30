# interview_preparation
Interview Preparation with Python3

Tips:

* For OR condition if first condition is True, then second position is never checked.
```
a = [10, 20]
if len(a) < 10 or a[100]:
    print("second condition is not checked")
```

* For AND condition if first condition is False, then second position is never checked.
```
a = [10, 20]
if len(a) > 10 and a[100]:
    print("second condition is not checked")
```

* order of condition check: Always put strictest condition in the beginning:
```
a = 1
b = 1
if a==1 and b==1:
    print ("both are 1")
elif a == 0 and b == 0:
    print ("both are 0")
elif a == 1:
    print ("only a is 1")
else:
    print ("only b is 1")        
```    
If we put a==1 (or b==1) first, we will mistakenly execute strictest condition in less strict condition.

*  If a set a sorted list, it is not necessary that resulted set will also be sorted.
```python
>>> a = [1000, 1]
>>> a.sort()
>>> a
[1, 1000]
>>> set(a)
set([1000, 1])
>>> list(set(a))
[1000, 1]

``` 
