#Grammar structure
class Grammar:
    def _init_(self):
        self.nonterminals = []  # Nonterminals list
        self.terminals = []  # terminals list
        self.first = {}  # First dictionary "nonterminal: list of its first"
        self.follow = {}  # Follow dictionary "nonterminal: list of its follow"
        self.productions = {}  # Productions dictionary "nonterminal: list of its productions"
        self.initial


# Rule 2: if x is a nonterminal and A->x, then the first of A will be the first of x
    def rule2(self):
        for d in range(0,len(self.nonterminals),1):  # to assure the first is right in the worst of the cases (talking about the order in which productions are read)
            for N in self.nonterminals:
                for a in self.productions[N]:
                    long = len(a)
                    cont = 0
                    for b in a:
                        if b in self.terminals:
                            if b not in self.first[N]:
                                self.first[N].append(b)
                            break
                        elif b in self.nonterminals:
                            if 'e' not in self.first[b]:
                                for c in self.first[b]:
                                    if (c != 'e') and (c not in self.first[N]):
                                        self.first[N].append(c)
                                break
                            elif 'e' in self.first[b]:  # if epsilon is into the first of x and A->xy, then fist(A)= first(x) + first(Y) without epsilon
                                for c in self.first[b]:
                                    if (c != 'e') and (c not in self.first[N]):
                                        self.first[N].append(c)
                                cont += 1
                    if (long == cont) and ('e' not in self.first[N]):
                        self.first[N].append('e')  # if A->xy and epsilon is into the first of both (x, y), then e is into the first of(A)

#Implements the rules to get the first of all nonterminals on the grammar
    def computeFirst(self):
        #In all cases the grammar needs to contain in at least one production, an epsilon or a terminal start symbol, if not the grammar won't make any string full of terminals
        for N in self.nonterminals:
            self.first[N] = []  # Creates de list of first of each nonterminal
            #Rule 3
            if 'e' in self.productions[N]:  # Rule 3: when N->e, then First(N) contains e
                self.first[N].append('e')

            for a in self.productions[N]:
                for b in a:
                    if b in self.nonterminals:
                        break
                    if b in self.terminals:  # When a terminal is at the start of a production, that terminal is into the first
                        if b not in self.first[N]:
                            self.first[N].append(b)
                        break
        self.rule2()


    #Count the number of nonterminals into a production
    #parameter a is the right side of the production
    def countNonterminals(self,a):
        cont = 0
        for b in a:
            if b in self.nonterminals:
                cont += 1
        return cont


    #Splits a string in three parts having in the middle one nonterminal
    #parameter b is the number of the nonterminal we are going to put in the middle
    #parameter a is the right side of the production
    def divideString(self,b,a):
        alfa=""  # left side
        n=""     # nonterminal
        beta = ""  # right side
        cont = 0
        for c in a:
            if c in self.terminals and cont<b:  # terminals on the left side
                alfa = alfa + c
            elif c in self.terminals and cont >= b:  # terminals on the right side
                beta = beta+c
            elif c in self.nonterminals:
                cont += 1
                if cont == b: # nonterminal in the middle
                    n = n+c
                elif cont > b:  # nonterminals on the right side
                    beta = beta+c
                elif cont < b:  # nonterminals on the left side
                    alfa = alfa+c

        #Replace right and left side whit epsilon in case they don't have either terminals or nonterminals
        if alfa=="":
            alfa='e'
        if beta=="":
            beta='e'

        #The result of dividing the string
        string = [alfa, n, beta]
        return string


    #Implements the three rules in order to have the follow set for all the nonterminals on the grammar
    def computeFollow(self):
        #Initializing follows
        for N in self.nonterminals:
            self.follow[N]=[]

        #First rule
        self.follow[self.initial].append('$')  # Always $ is into the follow of S(the initial symbol)

        #Second rule
        for N in self.nonterminals:  # For all the productions of the form A->aBb, first(b) is into follow(B)
            for a in self.productions[N]:
                n = self.countNonterminals(a)  # how many nonterminals are on the production, it determines the differnt posibilities we have to split the string
                if n > 0:  # if there aren't nonterminals, then the rule doesn't apply on the production
                    for b in range(0,n,1):
                        string = self.divideString((b+1),a)  # divide the string(right side of the production) depending on which nonterminal we want to be at B (in the middle)
                        beta = string[2]  # Right side of the division of the string
                        if beta == 'e':  # if b is equal to epsilon, then we the rule doesn't apply to de production with that division, try with the next one
                            continue
                        else:
                            for c in beta:  # the first set of the first terminal or nonterminal (on the rigth side of the string) is part of the follow of the nonterminal in the middle
                                if c in self.terminals and c not in self.follow[string[1]]:
                                    self.follow[string[1]].append(c)
                                    break
                                elif c in self.nonterminals:
                                    for h in self.first[c]:
                                        if h != 'e' and h not in self.follow[string[1]]:
                                            self.follow[string[1]].append(h)
                                    break

        #Third rule
        for i in range(0,len(self.nonterminals),1):  # helps to refresh the dependence of each follow set (avoid errors caused by the order of the lecture of the nonterminals)
            for N in self.nonterminals:  # for each production if A->aB or if A->aBb with epsilon into first(b), then follow(A) needs to be into follow(B)
                for a in self.productions[N]:

                    n = self.countNonterminals(a)

                    if n>0:
                        for b in range(0, n, 1):
                            string = self.divideString((b+1), a)
                            beta = string[2]
                            if beta == 'e':  # if the right part of the divide string is epsilon, then the rule is applied
                               for k in self.follow[N]:
                                   if k not in self.follow[string[1]]:
                                       self.follow[string[1]].append(k)

                            else:  # if the right part of the string starts with a nonterminal that contains epsilon in its first, then the rule is applied
                                for c in beta:
                                    if c in self.terminals:
                                        break
                                    else:
                                        if 'e' in self.first[c]:
                                            for c in self.follow[N]:
                                                if c not in self.follow[string[1]]:
                                                    self.follow[string[1]].append(c)
                                        break

#Prints the first and follow sets for each nonterminal of the grammar
    def printSolution(self):
        for a in self.nonterminals:
            print(f"First({a}): {self.firstToString(a)}")
        for a in self.nonterminals:
            print(f"Follow({a}): {self.followToString(a)}")


#Transform the first set in a string
    def firstToString(self,a):
        f= "{"
        for b in self.first[a]:
            if b != self.first[a][len(self.first[a])-1]:
                f=f+ b + ","
            else:
                f = f + b + "}"
        return f

    # Transform the follow set in a string
    def followToString(self, a):
        f = "{"
        for b in self.follow[a]:
            if b != self.follow[a][len(self.follow[a]) - 1]:
                f = f + b + ","
            else:
                f = f + b + "}"
        return f


