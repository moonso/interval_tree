from interval_tree import IntervalTree

def test_empty():
    """docstring for test_empty"""
    
    empty_interval = [0,0,None]
    empty_tree = IntervalTree([empty_interval],0,0)
    
    assert empty_tree.find_range([1,1]) == []

def test_empty_float():
    """docstring for test_empty"""
    
    empty_interval = [0.0,0.0,None]
    empty_tree = IntervalTree([empty_interval],0,0)
    
    assert empty_tree.find_range([1,1]) == []

def test_simple():
    """docstring for test_empty"""
    
    empty_interval = [1,1,3]
    empty_tree = IntervalTree([empty_interval],0,1)
    
    assert empty_tree.find_range([1,1]) == [3]

def test_simple_float():
    """docstring for test_empty"""
    
    empty_interval = [0.0,1.0,1]
    empty_tree = IntervalTree([empty_interval],0,1)
    
    assert empty_tree.find_range([0.5,0.6]) == [1]

def test_float_tree():
    """docstring for test_empty"""
    
    first_interval = [0.0,0.01,1]
    second_interval = [0.01,0.02,2]
    third_interval = [0.02,1,3]
    
    empty_tree = IntervalTree([
        first_interval,
        second_interval,
        third_interval
    ],0,2)
    
    assert empty_tree.find_range([0.001,0.001]) == [1,2,3]
