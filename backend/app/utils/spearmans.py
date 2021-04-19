class Spearman:

    def __init__(self):
        self.rho = 1


    def calculate(self, a: list, b: list):
        """ Calculate how different b is from a """
        diffs = []
        for i in range(len(a)):
            index = b.index(a[i])
            diffs.append(index-i)
        
        sum_diffs = sum(map(lambda i: i*i, diffs))

        self.rho = self.rho - (6*sum_diffs)/(len(a)*(len(a)**2 - 1))

        return self.rho
