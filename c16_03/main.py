note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

print(notes)
print(notes[0][2])


#Question 4 a/
def moyenne_eleve1(liste):
  res = 0
  comp = 0
  for i in range(len(liste)):
    if liste[i][0] == 'eleve1':
      res = res + liste[i][2]
      comp = comp +1
  moy = res/comp
  return moy

print(moyenne_eleve1(notes))

#Question 4 b/
def moyenne_eleve1_math(liste):
  res = 0
  comp = 0
  for i in range(len(liste)):
    if liste[i][0] == 'eleve1':
      if liste[i][1] == 'math':
        res = res + liste[i][2]
        comp = comp +1
  moy = res/comp
  return moy

print(moyenne_eleve1_math(notes))

#Question 4 c/
def moyenne_tuples(liste, eleve=None, matiere=None):
  liste_eleve = [x for x in liste if x[0] == eleve or eleve == None ]
  liste_eleve_matiere = [y for y in liste_eleve if y[1] == matiere or matiere == None ]
  notes = [z[2] for z in liste_eleve_matiere]
  return sum(notes)/len(notes)

print(moyenne_tuples(notes, 'eleve1', 'math'))
print(moyenne_tuples(notes, 'eleve1', 'eco'))
print(moyenne_tuples(notes, 'eleve2', 'math'))
print(moyenne_tuples(notes, 'eleve2'))
print(moyenne_tuples(notes, 'eleve1'))


class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)

  def __str__(self):
    return "Le nom de l'élève : {}, la matière : {} et la note : {}".format(self.eleve, self.matiere, self.valeur)

onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

#Question 5
onotes = [Note(*x) for x in notes]

#Question 6
print(onote)

#Question 7


#Question 8 
def moyenne_Notes(liste, eleve=None, matiere=None):
  liste_eleve = [x for x in liste if x.eleve == eleve or eleve == None ]
  liste_eleve_matiere = [y for y in liste_eleve if y.matiere == matiere or matiere == None ]
  notes = [z.valeur for z in liste_eleve_matiere]
  return sum(notes)/len(notes)

print(moyenne_Notes(onotes))
print(moyenne_Notes(onotes, 'eleve1', 'math'))

