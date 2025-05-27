import itertools

class mathNotes:
    """
    This class is used to note all the mathematical notes by Eren.
    
    """
    class apriori:
        """
        This class implements the Apriori algorithm for association rule learning.
        It calculates the support of itemsets in a list of transactions.
        Args: liste: list of transactions, where each transaction is a dictionary with items as values.
        Returns:
            An instance of the apriori class with methods to get the list, calculate support, and show itemsets.
        """
        def __init__(self, liste:list):
            self.liste = liste
            """
            Taking a list of transactions, where each transaction is a dictionary with items as values.
            """
            
        def get_list(self):
            """

                list: The list of transactions.
            """
            return self.liste
            
        
        
        def support(self, *args):
            """
            Calculate the support of an itemset in the transactions.
            Args:
                *args: Items to check support for.
            """
            instance = 0
            wanted_set = set(args)
            for transaction in self.liste:
                for items in transaction.values():
                    if set(items).issuperset(wanted_set):
                        instance += 1
            return instance / len(self.liste)
        
        def show_list(self, confidence: float = 0.25):
            """
            Show the itemsets and their support from the transactions.
            """
            for komb in self.itercomb(self.liste):
                s = self.support(*komb)
                print(f"Itemset: {sorted(komb)}, Support: {s:.2f}")
        
        def itercomb(self, iter_list:list):
            """
            Secondary function to iterate through combinations of items in the transactions.
            Args:
                iter_list: List of transactions, where each transaction is a dictionary with items as values.
            
            """
            bos_Set = set()
            bos_set_exact = set()

            for fiş in iter_list:
                for item in fiş.values():
                    bos_Set.update(item)

            for _ in range(1, len(bos_Set) + 1):
                combination = itertools.combinations(bos_Set, _)
                for c in combination:
                    bos_set_exact.add(c)
                    
            return bos_set_exact 
     
new_instance = mathNotes.apriori([{"Fiş1": ["Ekmek", "Süt", "Yumurta"]},
    {"Fiş2": ["Süt", "Kahve", "Şeker"]},
    {"Fiş3": ["Ekmek", "Yumurta", "Tereyağı"]},
    {"Fiş4": ["Kahve", "Süt", "Çikolata", "Bisküvi"]},
    {"Fiş5": ["Ekmek", "Çikolata"]},
    {"Fiş6": ["Yumurta", "Süt", "Bisküvi"]},
    {"Fiş7": ["Ekmek", "Kahve"]},
    {"Fiş8": ["Tereyağı", "Bal", "Süt"]},
    {"Fiş9": ["Bisküvi", "Çikolata", "Kahve"]},
    {"Fiş10": ["Yumurta", "Süt", "Kahve", "Ekmek"]}])

new_instance.show_list(confidence=0.25)
print(new_instance.get_list())






