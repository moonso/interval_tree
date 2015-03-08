#Interval Tree#

Just a python implementation of interval tree.

##Description##

An interval tree is a data structure that is built of intervals with id:s.
One can query the interval tree with an interval and get the ids of the overlapping intervals.

##Usage##

An interval tree is created from a list of lists and the start and stop of the interval tree.
The sublist looks like ```[<interval_start>, <interval_stop>, <interval_id>]```.
Start is the lower bound of the intervals and stop is the upper bound.

The interval trees is then queried with a list that represents an interval and returns the ids of the overlapping intervals.

```python
>from interval_tree import IntervalTree
>features = [
        [20,400,'id01'], 
        [20,400,'id12'], 
        [500,700,'id01'], 
        [1020,2400,'id02'], 
        [35891,29949,'id03'], 
        [899999,900000,'id04'], 
        [999000,999000,'id05']
    ]
>my_tree = IntervalTree(features, 1, 1000000)
>print('Ranges between 200 and 1200: %s' % my_tree.find_range([200, 1200]))
>Ranges between 200 and 1200: ['id02', 'id01', 'id12']
>print('Range in only position 90000: %s'  % my_tree.find_range([900000, 900000]))
>Range in only position 90000: ['id04']
>print('Range in only position 300: %s'  % my_tree.find_range([300, 300]))
>Range in only position 300: ['id01', 'id12']
```