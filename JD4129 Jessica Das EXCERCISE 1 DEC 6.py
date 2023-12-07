#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Jessica Das
#jd4129


# In[ ]:


# Write a function that takes two lists representing sets (with no duplicates) which returns a list of the intersection.
# (use only loops and sequence indexing with no method calls except append).
# Use a nested loop in your implementation. Test on the list A = [2, 4, 5, 6] and B = [4, 6, 7, 8].
#


# In[1]:


def intersect(ListA, ListB):
    result = []
    for a in ListA:
        for b in ListB:
            if a == b:
                result.append(a)
    return result

ListA = [2, 4, 5, 6]
ListB = [4, 6, 7, 8]

result_intersect = intersect(ListA, ListB)
print(result_intersect)

