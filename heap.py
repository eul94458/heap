# Heap
from math import log, ceil, floor
from collections import defaultdict, deque
from operator import le, lt, ge, gt


class Heap:
    
    NAME = 'heap'
    
    def __init__(self, *things):
        self.h = deque()
        self += things
            
    def __iadd__(self, iterable):
        for x in iterable:
            self.append(x)
        return self
        
    def __len__(self):
        return len(self.h)
        
    def __iter__(self):
        for x in self.h:
            yield x
        
    def _packstr(self, a_deque):
        a_deque.appendleft(f"{self.NAME} {'v'*12}")
        a_deque.append('^'*20)
        return a_deque
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        pack = self._packstr
        h = self.h
        n_layers = ceil( log( len(h)+1, 2 ) )

        if n_layers < 1:
            return '\n'.join(pack(deque()))
        elif n_layers == 1:
            stack = deque([str(h[0])])
            stack = pack(stack)
            return '\n'.join(stack)
        else:
            stack = deque()
            ele_per_layer = [2**x for x in range(n_layers)]
            # +2 account for space encompass each element
            span_per_ele = max(len(str(x)) for x in h) + 1
            # The real number of element for the last layer is in [-1]
            graph_width = ele_per_layer[-1] * (span_per_ele)
            start = 0
            for epl in ele_per_layer:
                end = start + epl
                ele_span = graph_width // epl
                # every element is center-aligned
                this_layer = ''.join( f"{x:^{ele_span}}" for x in list(h)[start:end] )
                stack.append(this_layer)
                start = end
            stack = pack(stack)
            # right-align all layers
            return '\n'.join(f"{row:<{graph_width}}" for row in stack)

    def append(self, x):
        self.h.append(x)
        self.up(len(self.h)-1)
        return self

    def appendleft(self, x):
        self.h.appendleft(x)
        return self

    def pop(self):
        return self.h.pop()
    
    def popleft(self):
        # Must have at least one element to pop()
        h = self.h
        if len(self.h) >= 1:
            h[0], h[-1] = h[-1], h[0]
            out = h.pop()
            if len(h) > 0:
                self.down(0)
            return out
        else:
            raise ValueError("Heap is empty.")
    
    def copy(self):
        from copy import copy
        return copy(self)
    
    def deepcopy(self):
        from copy import deepcopy
        return deepcopy(self)
    
    def up(self, child_k):
        h = self.h
        compare = self.UP_COMPARE
        child_v = h[child_k]
        # If index i == 0, no need to do anthing.
        while child_k >= 1:
            parent_k = (child_k-1)//2
            parent_v = h[parent_k]
            if compare(child_v, parent_v):
                h[child_k] = parent_v
                child_k = parent_k
            else:
                break
        h[child_k] = child_v

    def down(self, parent_k):
        max_or_min, compare = self.MAX_OR_MIN, self.DOWN_COMPARE
        h = self.h
        end = len(h)-1
        parent_v = h[parent_k]
        previous_parent_k = -1
        while previous_parent_k != parent_k:
            previous_parent_k = parent_k
            lchild_k = parent_k*2+1
            rchild_k = lchild_k+1
            # Child may not exist for one node,
            #  so need to check before getting the value
            if lchild_k <= end:
                lchild_v = h[lchild_k]
                if rchild_k <= end:
                    rchild_v = h[rchild_k]
                    max_v = max_or_min(lchild_v, rchild_v)
                    swap_k, swap_v = (
                        (lchild_k, lchild_v) 
                        if max_v==lchild_v else
                        (rchild_k, rchild_v)
                        )
                    h[parent_k], h[swap_k] = swap_v, parent_v
                    parent_k = swap_k
                else:
                    # Only exist lchild, so only compare to lchild.
                    if compare(parent_v, lchild_v):
                        h[parent_k], h[lchild_k] = lchild_v, parent_v
                        parent_k = lchild_k


class MaxHeap(Heap):

    NAME = "MaxHeap"
    UP_COMPARE = gt
    MAX_OR_MIN = max
    DOWN_COMPARE = lt


class MinHeap(Heap):
    
    NAME = "MinHeap"
    UP_COMPARE = lt
    MAX_OR_MIN = min
    DOWN_COMPARE = gt