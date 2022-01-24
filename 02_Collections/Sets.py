# SETS
pokemon = {'Bulbasaur', 'Squirtle', 'Charmander'}

print(pokemon, type(pokemon))

pokemon.add("Pikachu")

print(pokemon)

# Sets are unordered and mutable

pokemon.discard('Bulbasaur')
print(pokemon)

pokemon.add('Bulbasaur')
pokemon.add('Bulbasaur')
print(pokemon)

# NO DUPLICATES

l = [1, 2, 3, 4, 5, 6, 6, 7]
print(l)
print(set(l))


# Frozen Set

x = frozenset(['let', 'it', 'go'])
print(x)

