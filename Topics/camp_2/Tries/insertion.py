class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        cur = self.root
        word = word.lower()
        pos = -1
        for char in word:
            pos = ord(char) - 97
            if not cur.children[pos]:
                cur.children[pos] = TrieNode(); 
            cur = cur.children[pos]

        if pos != -1:
            cur.is_end = True

    def searchPrefix(self, prefix):
        cur = self.root

        for char in prefix:
            pos = ord(char) - 97
            if not cur.children[pos]:
                return False
            cur = cur.children[pos]
        
        return True
    
    def searchWord(self, word):

        cur = self.root

        for char in word:
            pos = ord(char) - 97
            if not cur.children[pos]:
                return False
            cur = cur.children[pos]
        
        return cur.is_end

    def printTrie(self):
        for idx, child in enumerate(self.root.children):
            if child:
                print(chr(idx + 97))
                self.root = child
                self.printTrie()

class TrieNode:

    def __init__(self) -> None:
        self.is_end = False
        self.children = [None for _ in range(26)]



myTrie = Trie()
myTrie.insert("date")
# myTrie.printTrie()
myTrie.insert("data")
myTrie.printTrie()
