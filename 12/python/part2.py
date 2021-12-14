import sys

connections = {}

for line in sys.stdin:
    a, b = line.rstrip().split('-')
    connections[a] = connections.get(a, []) + [b]
    connections[b] = connections.get(b, []) + [a]

def doubled_already(history):
    counts = {}
    for location in history:
        if not location.isupper():
            counts[location] = counts.get(location, 0) + 1
            if counts[location] == 2:
                return True
    return False

def can_visit(connection, history):
    if connection == 'start':
        return False
    if connection.isupper():
        return True
    if connection not in history:
        return True
    return not doubled_already(history)

def all_paths_from(start, connections, history):
    if start == 'end':
        print(','.join(history + ['end']))
        return
    for connection in connections[start]:
        if can_visit(connection, history + [start]):
            all_paths_from(connection, connections, history + [start])

all_paths_from('start', connections, [])
