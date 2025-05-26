import itertools
from collections import defaultdict

class mathNotes:
    """
    This class is used to note all the mathematical notes by Eren.
    
    Returns:
        _type_: _description_
    """
    class apriori:
        def __init__(self, liste:list):
            self.liste = liste
            
        def get_list(self):
            return self.liste
        
        def support(self, *args):
            instance = 0
            len_of_the_values = 0
            wanted_set = set(args)
            for transaction in self.liste:
                for items in transaction.values():
                    len_of_the_values += len(transaction.values())# veya doğrudan transaction.values() bir listeyse
                    if set(items).issuperset(wanted_set):
                        instance += 1
            return instance / len_of_the_values
        
        def show_list(self, confidence:float = 0.25):
            print(self.support(self.itercomb(self.liste)))
            return self.support(self.itercomb(self.liste))
        
        def itercomb(self, iter_list:list):
            bos_Set = set()
            bos_set_exact = set()

            for fiş in iter_list:
                for item in fiş.values():
                    bos_Set.update(item)

            for _ in range(1, len(bos_Set) + 1):
                combination = itertools.combinations(bos_Set, _)
                for c in combination:
                    bos_set_exact.add(c)
                    
            return set(bos_set_exact)

        
        
            
     
new_instance = mathNotes.apriori([{"Fiş1": ["Elma", "Armut", "Soğan"]}, {"Fiş2": {"Elma", "Armut", "Soğan"}}])
#print(new_instance.get_list())  # Output: {'key1': 'value1', 'key2': 'value2'}
            
new_list = new_instance.get_list()

# for j in range(len(new_instance.liste)):
#     print(new_instance.liste[j])  # Print each key in the dictionary
#     print(new_instance.liste[j].items())  # Print each key-value pair in the dictionary
#     print(new_instance.liste[j].keys())  # Print each key in the dictionary
#     print(new_instance.liste[j].values())  # Print each value in the dictionary
#     print(new_instance.support("Elma", "Armut", "b"))  # Calculate support for "Elma"
#     print(new_instance.support("Armut"))  # Calculate support for "Armut"
#     print(new_instance.support("a"))  # Calculate support for "Soğan"
    
#print(new_instance.support("Elma"))  # Show the list with confidence 0.25
print(new_instance.itercomb(new_instance.liste))  # Show the list with confidence 0.25
print(new_instance.show_list(0.25))  # Show the list with confidence 0.25

#print(list([{"Fiş1": ["Elma", "Armut", "Soğan"]}, {"Fiş2": {"Elma", "Armut", "Soğan"}}][0].values())[0])  # Access the first dictionary's values




