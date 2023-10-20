# In DNA strings, symbols "A" and "T"
# are complements of each other, as "C" and "G".
# Your function receives one side of the DNA
# (string, except for Haskell); you need to return
# the other complementary side.
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).
# "ATTGC" --> "TAACG"
#
#
def DNA_strand(dna: str):
    a = {"A": "T",
         "T": "A",
         "C": "G",
         "G": "C"}
    return "".join([f'{a.get(i) if i in a.keys() else i}' for i in dna])


print(DNA_strand("FGTFFAT"))
