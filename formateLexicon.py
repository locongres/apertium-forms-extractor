""" This program converts the result of the lt-expand command on an apertium monolingual dictionary in a csv file. Command : cat file_got_from_apertium.txt | python3 formateLexicon.py > file_csv.csv """

import sys
import re

for ligne in sys.stdin:
	ligne=ligne.rstrip('\n')
	
	if re.search('^([^:<]*?)(:|:>:|:<:)([^:<]*?)(<.+)$', ligne):
		ligne=re.sub('^([^:<]*?)(:|:>:|:<:)([^:<]*?)(<.+)$', '\g<1>\t\g<2>\t\g<3>\t\g<4>', ligne)
		
		if ':<:' not in ligne and not re.search('^([^:]*?)[ \-]', ligne):
			ligne=re.sub('\t:>:\t', '\tnot standard\t', ligne)
			ligne=re.sub('\t:\t', '\t\t', ligne)
			print(ligne)
