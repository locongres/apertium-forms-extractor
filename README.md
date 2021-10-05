# apertium-forms-extractor

## Introduction
Apertium forms extractor is a set of python programs to generate an inflected forms lexicon from a monolingual dictionary of the open-source machine translation platform Apertium (https://wiki.apertium.org).
It was developed by Lo Congrès (https://locongres.org) among a set of tools to build datas for NLP applications for poorly endowed languages.

## How to use ?
First, you need to generate a .dix file and extract datas from it :
1) Open a terminal window in your apertium language directory (ex. : apertium-oci)
2) Type ./autogen.sh
3) Type make
4) Type lt-expand .deps/[your_language_code].dix > flexionLexicon.txt

You can then use apertium_form_extractor programs on your flexionLexicon.txt file.

formateLexicon.py converts your flexionLexicon.txt file in a csv file. You can use it with the command : cat flexionLexicon.txt | python3 formateLexicon.py > csvLexicon.csv

extractForms.py extracts all inflected form in your csvLexicon.csv file, without duplications. You can use it with the command : cat csvLexicon.csv | python3 extractForms.py > formsList.txt
