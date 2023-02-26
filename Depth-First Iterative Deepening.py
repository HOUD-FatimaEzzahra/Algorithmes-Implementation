def expand(node):
    if node == "A":
        return ["B", "C","D"]
    elif node == "B":
        return ["E","F"]
    elif node == "C":
        return ["G"]
    elif node == "E":
        return ["H"]
    else:
        return []

def dfid(node, destination):
    depth = 0
    while True:
        result = dls(node, destination, depth)
        if result is not None:
            return result
        depth += 1

def dls(node, destination, depth):
    if depth == 0 and node == destination:
        return node
    elif depth > 0:
        for child in expand(node):
            result = dls(child, destination, depth - 1)
            if result is not None:
                return result
    return None

# Test example problem
start = "A"
end = "H"
result = dfid(start, end)
print(result)  # Output: F