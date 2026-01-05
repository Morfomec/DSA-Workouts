# class TrieNode:

#     def __init__(self):
#         self.children = {}
#         self.is_end = False

# class Trie:

#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root

#         for ch in word:
#             if ch not in node.children:
#                 node.children[ch] = TrieNode()
#             node = node.children[ch]
#         node.is_end = True


#     def search(self, word):
#         node = self.root

#         for ch in word:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return node.is_end

#     def search(self, word):

#         node = self.root

#         for ch in word:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return node.is_end

#     def startsWith(self, prefix):

#         node = self.root

#         for ch in prefix:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return True

#     def print_all(self):
#         # result = []
#         def dfs(node, path):
#             if node.is_end:
#                 print(path)
#                 # result.append(path)

#             # for ch, child in node.children.items():
#             #     dfs(node.children[ch], path + ch)

#             for ch in sorted(node.children):
#                 dfs(node.children[ch], path + ch)

#         dfs(self.root, "")
#         # return result


# t = Trie()
# t.insert("Shif")
# t.insert("Shaf")
# t.insert("Shifil")
# print(t.search('Shif'))
# print(t.startsWith('S'))
# print(t.print_all())

# longest prefix, auto complete
    
# class TrieNode:

#     def __init__(self):

#         self.children = {}
#         self.is_end = False
    
# class Trie:

#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root

#         for ch in word:
#             if ch not in node.children:
#                 node.children[ch] = TrieNode()
#             node = node.children[ch]
#         node.is_end = True

#     def insert(self, word):

#         node = self.root

#         for ch in word:
#             if ch not in node.children:
#                 node.children[ch] = TrieNode()
#             node = node.children[ch]
#         node.is_end = True

#     def search(self, word):

#         node = self.root

#         for ch in word:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return node.is_end

#     def startsWith(self, prefix):
#         node = self.root

#         for ch in prefix:
#             if ch not in node.children:
#                 return False
#             node = node.children[ch]
#         return node.is_end

#     def print_all(self):

#         def dfs(node, path):
#             if node.is_end:
#                 print(path)

#             for ch in sorted(node.children):
#                 dfs(node.children[ch], path + ch)

#         dfs(self.root, "")


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
        
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.is_end

    def print_all(self):

        def dfs(node, path):
            if node.is_end:
                print(path)

            for ch in sorted(node.children):
                dfs(node.children[ch], path + ch)

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
        pref = ""

        while True:
            if node.is_end or len(node.children) != 1:
                break
            
            ch = next(iter(node.children))
            prefix += ch
            node = node.children[ch]

        return prefix

    
    def lcp(self):

        node = self.root
        prefix = ""

        while True:
            if node.is_end or len(node.children) != 1:
                break

            ch = next(iter(node.children))
            prefix += ch
            node = node.children[ch]


        return prefix













t = Trie()
words = ["Shif", "Shifil", "Shaf", "Shadow", "Shell"]

for w in words:
    t.insert(w)

print(t.autocomplete('Shi'))



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
    
    def insert(self, word):
        node =self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end=True


    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

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
        return node.is_end

    def print_all(self):

        def dfs(node, path):
            if node.is_end:
                print(path)

            for ch in node.children:
                dfs(node.children, path+ch)

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
                result.append[path]
            
            for ch in sorted(node.children):
                dfs(node.children[ch], path +ch)
            dfs(node, prefix)
            return result


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
            
            for ch in node.children:
                dfs(node.children[ch], path+ch)
            
        df(self.root, "")

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

        while True:
            if node.is_end or len(node.children) != 1:
                break

            ch = next(iter(node.children))
            prefix += ch
            node = node.children[ch]
        return prefix

    def lcp(self):
        node = self.root
        prefix = ""

        while True:
            if node.is_end or len(node.children) > 1:
                break
            ch = next(iter(node.children))
            perfix += ch
            node = node.children[ch]
        return prefix
    
    def lcp(self):

        node = self.root
        prefix = ""

        while True:
            if node.is_end or len(node.children) > 1:
                break
            ch = next(iter(node.childre))
            prefix += ch
            node = node.children[ch]
        return prefix


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
        return node.is_end

    def print_all(self):
        
        def dfs(node, path):
            if node.is_end:
                print(path)

            for ch in reversed(node.children):
                dfs(node.children[ch], path + ch)
        dfs(self.root, '')


    def print_all(self):

        def dfs(node, path):
            if node.is_end:
                print(path)

            for ch in reversed(node.children):
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

            for ch in reversed(node.children):
                dfs(node.children[ch], path+ch)

        dfs(node, prefix)
        return result


    def autocomplete(self, prefix):

        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        def dfs(node, path):
            if node.is_end:
                result.append(path)

            for ch in reversed(node.children):
                dfs(node.children[ch], path+ch)

        dfs(node, prefix)
        return result

    def lcp(self):

        node = self.root
        prefix = ""

        while True:
            if node.is_end or len(node.children) > 1:
                break

            ch = next(iter(node.children))
            prefix += ch
            node = node.children[ch]

        return prefix

    
    def lcp(self):

        node = self.root
        prefix = " "

        while True:
            if node.is_end or len(node.children) > 1:
                break

            ch = next(iter(node.children))
            prefix += ch
            node = node.children[ch]

        return prefix
    