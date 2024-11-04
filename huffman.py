import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def print_codes(node, code=''):
    if not node.left and not node.right:
        print(f"{node.symbol} -> {code}")
        return
    if node.left:
        print_codes(node.left, code + '0')
    if node.right:
        print_codes(node.right, code + '1')

def huffman_encoding(chars, freq):
    nodes = [Node(freq[i], chars[i]) for i in range(len(chars))]
    heapq.heapify(nodes)

    while len(nodes) > 1:
        left, right = heapq.heappop(nodes), heapq.heappop(nodes)
        heapq.heappush(nodes, Node(left.freq + right.freq, left.symbol + right.symbol, left, right))

    print("Huffman Codes for the given characters:")
    print_codes(nodes[0])

if __name__ == "__main__":
    chars = list(input("Enter characters (space-separated): ").split())
    freq = list(map(int, input("Enter frequencies (space-separated): ").split()))
    huffman_encoding(chars, freq)