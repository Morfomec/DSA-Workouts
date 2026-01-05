class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def search(self, word):

        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
    
    def startsWith(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


    def startsWith(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def print_all(self):

        def dfs(node, path):
            if node.is_end:
                print(path)

            for ch in sorted(node.children):
                dfs(node.children[ch], path +ch)
        dfs(self.root, " ")


    def print_all(self):

        def dfs(node, path):
            if node.is_end:
                print(path)

            for ch in sorted(node.children):
                dfs(node.children[ch], path+ch)
            
        dfs(self.root, "")



    def autocomplete(self, prefix):

        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        result = []

        def dfs(node, path):
            if node.is_end:
                result.append(path)
            
            for ch in sorted(node.children):
                dfs(node.children[ch], path+ch)
        
        dfs(node, prefix)
        return result

    def lcp(self):

        node = self.root
        prefix = ""

        while len(node.children) == 1 and not node.is_end:
            ch = next(iter(node.children))
            prefix += ch
            node = node.children[ch]
        return prefix

t = Trie()
t.insert('Shifil')
t.insert('Shifal')
t.insert('Shifgal')
t.insert('Shiflla')
print(t.search('Shifal'))
# print(t.print_all())
print(t.autocomplete('Shifi'))
print(t.lcp())


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
    
    def startsWith(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
    
    def print_all(self):

        def dfs(node, path):
            if node.is_end:
                print(path)

            for ch in sorted(node.children):
                dfs(node.children[ch], path+ch)
        dfs(self.root, "")

    def autocomplete(self, prefix):

        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        result = []
        def dfs(node, path):
            if node.is_end:
                result.append(path)
            
            for ch in sorted(node.children):
                dfs(node.children[ch], path+ch)
        dfs(node, prefix)
        return result

    def lcp(self):

        node = self.root
        prefix =""

        while len(node.children) == 1 and not node.is_end:
            ch = next(iter(node.children))
            prefix += ch
            node = node.children[ch]
        return prefix

tt = Trie()
tt.insert("ap")
tt.insert("apel")
tt.insert("appla")
tt.insert("apla")
tt.insert("apil")
print(tt.print_all())
print(tt.autocomplete('ap'))
print(tt.lcp())