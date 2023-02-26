def expand(node):
    """
    Cette fonction prend en entrée un noeud de l'arbre et retourne une liste de ses enfants.
    Elle définit l'arbre à explorer.
    """
    if node == "A":
        return ["B", "C", "D"]
    elif node == "B":
        return ["E", "F"]
    elif node == "C":
        return ["G"]
    elif node == "D":
        return ["H", "I"]
    elif node == "E":
        return ["J", "K"]
    elif node == "G":
        return ["L"]
    elif node == "I":
        return ["M"]
    elif node == "J":
        return ["N"]
    elif node == "K":
        return ["O", "P"]
    else:
        return []

def dfid(node, destination):
    """
    Cette fonction effectue une recherche itérative en profondeur limitée pour trouver la destination.
    Elle retourne le chemin trouvé sous forme de liste de noeuds visités.
    """
    depth = 0
    while True:
        result = dls(node, destination, depth)
        if result is not None:
            return result
        depth += 1

def dls(node, destination, depth):
    """
    Cette fonction effectue une recherche en profondeur limitée pour trouver la destination.
    Elle retourne le chemin trouvé sous forme de liste de noeuds visités.
    """
    if depth == 0 and node == destination:
        return [node]
    elif depth > 0:
        for child in expand(node):
            result = dls(child, destination, depth - 1)
            if result is not None:
                return [node] + result
    return None

# Test example problem
start = "A"
end = "M"
result = dfid(start, end)
print(result)  # Output: ['A', 'D', 'I', 'M']
