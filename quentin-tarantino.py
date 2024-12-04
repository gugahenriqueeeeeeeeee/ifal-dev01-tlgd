filmes = {
    "bastardos inglórios" : {
        "Nome Original" : "Inglorious Bastards",
        "Tempo" : "2h 33m",
        "Restrição" : "18 anos",
        "Lançamento" : "2009",
        "Atores" :  "Brad Pitt / Eli Roth / Mélaine Laurent / Chriatoph Waltz"
    },
    
    "django livre" : {
        "Nome Original" : "Django Unchained",
        "Tempo" : "2h 45m",
        "Restrição" : "16 anos",
        "Lançamento" : "2012",
        "Atores" : "Jamie Foxx, Christoph Waltz, Leonardo DiCaprio, Samuel L. Jackson, Kerry Washington, Don Johnson",
    },
        

    "os 8 odiados" : {
        "Nome Original" : "The Hateful Eight",
        "Tempo" : "3h 7m",
        "Restrição" : "18 anos",
        "Lançamento" : "2015",
        "Atores" : "Tim Roth / Jennifer Jason Leigh / Kurt Russel / Samuel L. Jackson / Walton Goggins",
     },

    "a prova de morte" : {
        "Nome Original" : "Death Proof",
        "Tempo" : "1h 50m",
        "Restrição" : "16 anos",
        "Lançamento" : "2007",
        "Atores" : "Zoë Bell / Mary Elizabeth / Kurt Russel / Vanessa Ferlito / Rosario Dawson"
    },

    "era uma vez em hollywood" : {
        "Nome Original" : "Once Upon a Time In Hollywood",
        "Tempo" : "2h 40m",
        "Restrição" : "16 anos",
        "Lançamento" : "2019",
        "Atores" : "Brad Pitt / Leonardo DiCaprio / Margot Robbie / Austin Butler / Margaret Qualley"
    },

    "pulp fiction" : {
        "Nome Original" : "Pulp Fiction",
        "Tempo" : "2h 29m",
        "Restrição" : "18 anos",
        "Lançamento" : "1994",
        "Atores" : "John Travolta / Uma Thurman / Samuel L. Jackson / Bruce Willis / Tim Roth"
    },
    
    "kill bill" : {
        "Nome Original" : "Kill Bill, Volume 1",
        "Tempo" : "1h 51m",
        "Restrição" : "16 anos",
        "Lançamento" : "2003",
        "Atores" : "Uma Thurman / David Carradine / Michael Madsen / Lucy Liu / Daryl Hannah"
    },

    "kill bill 2" : {
        "Nome Original" : "Kill Bill, Volume 2",
        "Tempo" : "2h 17m",
        "Restrição" : "16 anos",
        "Lançamento" : "2004",
        "Atores" : "Uma Thurman / David Carradine / Michael Madsen / Lucy Liu / Daryl Hannah"
    },
    "jack brown" : {
        "Nome Original" : "Jack Brown",
        "Tempo" : "2h 40m",
        "Restrição" : "14 anos",
        "Lançamento" : "1997",
        "Atores" : "Pam Grier / Brigdet Fonda / Robert de Niro / Samuel L. Jackson / Robert Foster"
    },
    "cães de aluguel" : {
        "Nome Original" : "Reservoir Dogs",
        "Tempo" : "1h 39m",
        "Restrição" : "18 anos",
        "Lançamento" : "1992",
        "Atores" :  "Harvey Keitel / Michael Madsen / Tim Roth / Steve Buscemi / Chris Penn / Edward Bunker"
    }
}

def exibir(nome):
    if nome in filmes:
        filme = filmes[nome]
        print(f"Nome: {nome}")
        print(f"Nome Original: {filme['Nome Original']}")
        print(f"Tempo: {filme['Tempo']}")
        print(f"Restrição: {filme['Restrição']}")
        print(f"Lançamento: {filme['Lançamento']}")
        print(f"Atores: {filme['Atores']}")
    else:
        print("filme não encontrado")

nome_filme = input("digite um filme do Quentin Tarantino: ").lower()

exibir(nome_filme)










