"""
Program: FIRST and FOLLOW implementation for final project of Formal languages and compilers - EAFIT 2024-1
Authors: David Alejandro Ramírez Agudelo and Ana Sofia Alfonso Moncada
Professor: Sergio Steven Ramírez Rico
Date: 28/05/24

"""
#imports
import Grammar
import sys

#Create the list of the nonterminal symbols
def searchNonterminals(G):
   productions = G.productions
   nonterminals = productions.keys()  # Keys of productions (supposed to be the nonterminals of the grammar)
   if(G.initial in nonterminals) and (all(i.isupper() for i in nonterminals)):  # If the grammar has the initial nonterminal and all of them are uppercase, then, the grammar is well-defined
      G.nonterminals=nonterminals
   else:
      print("La grámatica no contiene el simbolo inicial S.")
      sys.exit(1)

#Create the list of the terminal symbols
def searchTerminals(G):
   productions = G.productions
   nonterminals = G.nonterminals
   terminals = []

   for i in nonterminals:
      p=productions[i]
      for a in p:
         for b in a:
            if (b not in terminals) and (b not in nonterminals) and (b.islower()) and (b!='e'):
               if (b!='$'):
                  terminals.append(b)
               else:
                  print("El simbolo $ no está permitido en la gramática.")
                  sys.exit(1)
   G.terminals = terminals

#Reads the grammar input
def readInput():
   n_cases = int(input())  # Number of grammars to analize
   for _ in range(0,n_cases,1):
      n_nterminals = int(input())  # Number of nonterminals of the grammar
      j=0
      productions={}
      while(j<n_nterminals):
         l= input().split()  # Productions of the nonterminal
         productions[l[0]]=[]
         for i in range (1,len(l)):
            productions[l[0]].append(l[i])
         j += 1
      G = Grammar.Grammar()  # Creation of the grammar to analize
      G.productions = productions
      G.initial ='S'
      G.first={}
      G.follow={}
      searchNonterminals(G)
      searchTerminals(G)
      G.computeFirst()
      G.computeFollow()
      G.printSolution()  # Prints the first and follow solution


if __name__ == '__main__':
  readInput()


