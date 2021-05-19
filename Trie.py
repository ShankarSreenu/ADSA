class TrieNode:
  def __init__(self,ch):
    self.char=ch
    self.childnode=[None]*27
    self.end=False

class Trie:
  def __init__(self):
    self.root=TrieNode('*')
  
  def getascii(self,ch):
    i=26-(122-ord(ch))
    return i

  
  def insert(self,string):
    root=self.root
    for ch in  string:
      i=self.getascii(ch)
      if root.childnode[i]==None:
        root.childnode[i]=TrieNode(ch)
        root=root.childnode[i]
      else:
        root=root.childnode[i] 
    root.end=True

  def search(self,string):
    root=self.root
    for ch in string:
      i=self.getascii(ch)
      if root.childnode[i]==None:
        return False
      else:
        root=root.childnode[i]
    return root.end
  
  def startsWith(self,string):
    root=self.root
    for ch in string:
      i=self.getascii(ch)
      if root.childnode[i]==None:
        return False
      root=root.childnode[i]
    return True
