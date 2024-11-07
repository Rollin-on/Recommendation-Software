import csv

#create node structure
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False
        self.data = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    #Insert Cuisine & Data into Trie
    def insert(self, cuisine, row):
        node = self.root
        for char in cuisine:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word_end = True
        #Cleaning Data
        row['Ingredients'] = row['Ingredients'].replace('\n', ' ')
        row['Instructions'] = row['Instructions'].replace('\n', ' ')
        #Adds each {} data to its corresponding cuisine
        node.data.append(row)

    #Searching Prefix or full word
    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        
        results = []
        self.dfs(node, results)
        return results
    
    #DFS Search to continue where prefix left off
    def dfs(self, node, results):
        if node.word_end:
            for recipe in node.data:
                results.append(recipe)
        for child in node.children.values():
            self.dfs(child, results)


#parsing recipes_data.csv

def cookbook(file):
    with open (file, mode='r', encoding='utf8') as csvfile:
        recipes = csv.DictReader(csvfile)
        trie = Trie()
        for row in recipes:
            cuisine = row['Cuisine'].lower()
            trie.insert(cuisine, row)
    return trie

#Calling csv data
trie = cookbook("recipes_data.csv")

