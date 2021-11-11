import constraint

problem = constraint.Problem()

#variables 
farben = "rot grün blau weiss gelb".split()
zigarette = "kools oldGold lucy chester parliment".split()
nationalitat = "england spanier ukrainer norweger japan".split()
getranken = "tee kaffee milch wasser orangensaft".split()
haustier = "hund pferd schnecken fuchs zebra".split()

#wertebereiche
hauser = [1,2,3,4,5]

#add variables to our problem
variables = farben + zigarette + nationalitat + getranken + haustier
problem.addVariables(variables, hauser)

#add constraints to our problem
problem.addConstraint(constraint.AllDifferentConstraint(), farben)
problem.addConstraint(constraint.AllDifferentConstraint(), zigarette)
problem.addConstraint(constraint.AllDifferentConstraint(), nationalitat)
problem.addConstraint(constraint.AllDifferentConstraint(), haustier)
problem.addConstraint(constraint.AllDifferentConstraint(), getranken)

problem.addConstraint(lambda england, rot: england == rot, ["england","rot"]) #Der Engländer wohnt im roten Haus.
problem.addConstraint(lambda spanier, hund: spanier == hund, ["spanier","hund"]) #Der Spanier hat einen Hund.
problem.addConstraint(lambda kaffee, grun: kaffee == grun, ["kaffee","grün"]) #Kaffee wird im grünen Haus getrunken.
problem.addConstraint(lambda ukrainer, tee: ukrainer == tee, ["ukrainer","tee"]) #Der Ukrainer trinkt Tee.
problem.addConstraint(lambda grun, weiss: grun + 1 == weiss, ["grün", "weiss"]) #Das grüne Haus ist direkt links vom weißen Haus.
problem.addConstraint(lambda oldGold, schnecken: oldGold == schnecken, ["oldGold", "schnecken"]) #Der Raucher von Old-Gold-Zigaretten hält Schnecken als Haustiere
problem.addConstraint(lambda kools, gelb: kools == gelb, ["kools", "gelb"]) #Die Zigaretten der Marke Kools werden im gelben Haus geraucht.
problem.addConstraint(constraint.InSetConstraint([3]), ["milch"]) #Milch wird im mittleren Haus getrunken.
problem.addConstraint(constraint.InSetConstraint([1]), ["norweger"]) #Der Norweger wohnt im ersten Haus.
problem.addConstraint(lambda chester, fuchs: abs(chester - fuchs) == 1, ["chester", "fuchs"]) #Der Mann, der Chesterfields raucht, wohnt neben dem Mann mit dem Fuchs.
problem.addConstraint(lambda kools, pferd: abs(kools - pferd) == 1, ["kools", "pferd"]) #Die Marke Kools wird geraucht im Haus neben dem Haus mit dem Pferd.
problem.addConstraint(lambda lucy, orangensaft: lucy == orangensaft, ["lucy", "orangensaft"]) #Der Lucky-Strike-Raucher trinkt am liebsten Orangensaft.
problem.addConstraint(lambda japan, parliment: japan == parliment, ["japan", "parliment"]) #Der Japaner raucht Zigaretten der Marke Parliaments.
problem.addConstraint(lambda norweger, blau: abs(norweger - blau) == 1, ["norweger", "blau"]) #Der Norweger wohnt neben dem blauen Haus.
problem.addConstraint(lambda chester, wasser: abs(chester - wasser) == 1, ["chester", "wasser"]) #Der Chesterfields-Raucher hat einen Nachbarn, der Wasser trinkt.

#get all possible solutions (this case just one solution)
solution = problem.getSolution()
print(solution)