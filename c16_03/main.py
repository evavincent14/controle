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
def moyenne_tuples(liste, eleve='vide', matiere='vide'):
  som = 0
  comp = 0
  if eleve == 'vide':
    if matiere == 'vide':
        for i in range(len(liste)):
           som = som + liste[i][2]
        moy = som/len(liste)
        return moy
    else:
      for i in range(len(liste)):
        if liste[i][1] == matiere:
          som = som + liste[i][2]
          comp = comp +1
      moy = som/comp
      return moy  
  else :
    if matiere == 'vide':
        for i in range(len(liste)):
          if liste[i][0] == eleve:
           som = som + liste[i][2]
           comp = comp +1
        moy = som/comp
        return moy
    else:
      for i in range(len(liste)):
        if liste[i][0] == eleve:
          if liste[i][1] == matiere:
            som = som + liste[i][2]
            comp = comp +1
      moy = som/comp
      return moy  


print(moyenne_tuples(notes,'eleve1', 'math'))
print(moyenne_tuples(notes))
print(moyenne_tuples(notes, 'eleve1'))
print(moyenne_tuples(notes, matiere='math'))
print(moyenne_tuples(notes, matiere='eco'))
