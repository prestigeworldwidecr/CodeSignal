'''

However, we have a challenge: suppose you're studying the lineage of a royal family, where each node represents a family member. '1' is the current monarch, with '2', '3', and '4' their immediate heirs. Others are descendants.

Can you implement the BFS algorithm on this family tree, showing the level for each vertex, i.e., how far away each vertex is from the family tree root?

'''

from collections import deque

def BFS(graph, root) :
# {
    visited = []
    queue = deque()
    queue.append(root)
    level_of_vertex = 0

    # TODO: initialize levels dictionary
    level = {
            '1' : 0
            }

    while (queue) :
    # {
        vertex = queue.popleft()
        visited.append(vertex)

        # TODO: set the current level of vertex
        level_of_vertex = level_of_vertex + 1

        for child in graph[vertex] :
        # {
            if (child in visited) :
            # {
                None
            # }

            else :
            # {
                queue.append(child)
                # TODO: set the level of the child ** child is vertex
                level.update({child : level_of_vertex})
            # }

        # }

    # }

    print("\nTraversing completed!")

    return level

# }

graph = {
        '1' : ['2', '3', '4'],
        '2' : ['5', '6'],
        '3' : ['7'],
        '4' : ['8', '9'],
        '5' : [],
        '6' : ['10'],
        '7' : ['11', '12'],
        '8' : [],
        '9' : [],
        '10' : [],
        '11' : [],
        '12' : []
        }

print(BFS(graph, '1')) 

'''

***** BONEYARD *****

# print('!', graph, root.values())

    # levels = set()
    # levels = []
                # level["royal_family_member"] = child
                # level["level_of_vertex"] = level_of_vertex

Let's refine your approach a bit:

Level Dictionary: Initialize level as a dictionary with the root node having a level of 0. This will help you track the level of each node.

Updating Levels: When you dequeue a node, use its level to determine the level of its children. For each child, set its level to be the parent's level plus one.

Visited Check: Ensure that you check if a node is not in visited before adding it to the queue and updating its level.

Here's a small hint:

Use level[child] = level[vertex] + 1 to set the level of each child.
Try implementing these changes and see how it goes! 🌟

Cosmo • 5:39 AM
Read message out loud
Good try, but that's not exactly right.

Here are a few things to consider:

Use the level dictionary to track each node's level relative to the root, like {'1': 0, '2': 1, ...}.
Ensure each node's level is based on its parent's level using level[child] = level[vertex] + 1.
Avoid using a set for levels; instead, directly update the level dictionary.
Would you like some help with these adjustments? 🤔


c • 5:40 AM
yes
Cosmo • 5:40 AM
Read message out loud
Let's refine your approach a bit:

Level Dictionary: Initialize level as a dictionary with the root node having a level of 0. This will help you track the level of each node.

Updating Levels: When you dequeue a node, use its level to determine the level of its children. For each child, set its level to be the parent's level plus one.

Visited Check: Ensure that you check if a node is not in visited before adding it to the queue and updating its level.

Here's a small hint:

Use level[child] = level[vertex] + 1 to set the level of each child.
Try implementing these changes and see how it goes! 🌟

# print(str(level))
            # levels.append(level)
            levels.add(str(level))
print(len(levels))
    # return sorted(levels)

# test = [None] * 20

    # print('@', len(levels))
    # print(test)
    # print('$', levels)                
                            
        # levels.append(level)
        # print(level)
            # print(child, level_of_vertex)
                # level[child] ["level_of_vertex"] = level_of_vertex
                # level[child] = level_of_vertex
                
                # print(level)
                # levels.append(level)
                # print('$', levels)
                # test[level_of_vertex] = level
                # print(level_of_vertex)

                # levels[level_of_vertex] = level
                # levels.extend(level)
                # levels.insert(level)

                # print(child, level_of_vertex, level)

                # print(child[1]["level_of_vertex"])
                # print(child[1])
                # child ["level_of_vertex"] = level_of_vertex

Read message out loud
Good try, but there are a few issues to address.

The data structure for levels should be a dictionary, not a list.
Ensure each node's level is based on its parent's level.
Would you like some guidance on how to proceed? 🤔


c • Just now
yes
Cosmo • Just now
Read message out loud
It looks like you're trying to use a list for the level data structure, but it should be a dictionary. This is causing the TypeError because you're trying to use strings as indices for a list.

Here's a hint to get you back on track:

Initialize level as a dictionary with the root node having a level of 0.
When you visit a child node, set its level to be the parent's level plus one.
Try adjusting your code with these pointers and see how it goes! 🚀

You could use such a list comprehension:

result = [{**page, 'author': get_author(page['url'])} 
          for page in pages]

# This works too:

result = [dict(**page, author=get_author(page['url'])) 
          for page in pages]

# but is less preferred because it will fail for input containing non-string keys
This creates a new dict for each original dict with an extra key, author, based on the value of get_author as applied to the value corresponding to the url key.

Note that it does not modify the original list.

Example:

def get_author(i):
    if i == 1:
        return 'hello'

    else:
        return 'bye'

pages = [{'url': 1},
         {'url': 2}]

result = [{**page, **{'author': get_author(page['url'])}} for page in pages]
print(result)
Output:

[{'url': 1, 'author': 'hello'}, {'url': 2, 'author': 'bye'}]

'''