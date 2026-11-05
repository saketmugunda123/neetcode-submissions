class TrieNode:
    def __init__(self):
        self.children = {}
        self.isTerminal = False
   
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root

        for i in range(0, len(word)):
            if word[i] not in currNode.children:
                currNode.children[word[i]] = TrieNode()

            currNode = currNode.children[word[i]]
        
        currNode.isTerminal = True


    def search(self, word: str) -> bool:
        currNode = self.root

        #Seeing if we can progress through the trie
        for i in range(0, len(word)):
            if word[i] in currNode.children:
                currNode = currNode.children[word[i]]
            else:
                return False
        
        #Checking to see if the last letter is terminal
        return currNode.isTerminal
        
            
    def startsWith(self, prefix: str) -> bool:
        currNode = self.root

        #Seeing if we can progress through the trie
        for i in range(0, len(prefix)):
            if prefix[i] in currNode.children:
                currNode = currNode.children[prefix[i]]
            else:
                return False
        return True
        