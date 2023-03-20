""" This program extracts all forms from a lexicon obtained with the formateLexicon.py program. Command : cat lexicon_from_formateLexicon.csv | python3 extractForms.py > formsList.txt """

import sys
import re

forms=set()

for ligne in sys.stdin:
	ligne=ligne.rstrip('\n')
	ligne=ligne.split('\t')
	
	forms.add(ligne[0])

forms=list(forms)
forms.sort()
for form in forms:
	print(form)
