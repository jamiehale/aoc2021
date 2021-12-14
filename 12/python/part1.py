import sys

connections = {}

for line in sys.stdin:
    a, b = line.rstrip().split('-')
    connections[a] = connections.get(a, []) + [b]
    connections[b] = connections.get(b, []) + [a]

def all_paths_from(start, connections, history):
    if start == 'end':
        print(','.join(history + ['end']))
        return
    for connection in connections[start]:
        if connection.isupper() or connection not in history:
            all_paths_from(connection, connections, history + [start])

all_paths_from('start', connections, [])
