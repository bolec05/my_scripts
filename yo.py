#! /usr/bin/env python
a = 'Hello World'
b = 'in maximo world :) i powodzenia w dalszej pracy'
c=15
print a + b + ' ' + str(c)
#print b[0:6]
print "%s %s %d \n" % (a, b, c)
d=30

if c > d:
 print "liczba %d jest wieksza od liczby %d" % (c, d)
else:
 print "liczba %d jest wieksza od liczby %d" % (d, c)

kolory = [ "bialy", "czarny", "zolty"]
kolory.append("czerwony")
#print kolory + " " + str(len(kolory))
print kolory
print len(kolory)
#tupla

zbior = (1,2,"jasio")
print zbior

for i in zbior:
 print i

#Methods for lists
#    list(s) - konwertuje sekwencję s na listę
#    s.append(x) - dodaje nowy element x na końcu s
#    s.extend(t) - dodaje nową listę t na końcu s
#    s.count(x) - zlicza wystąpienie x w s
#    s.index(x) - zwraca najmniejszy indeks i, gdzie s[i] == x
#    s.pop([i]) - zwraca i-ty element i usuwa go z listy. Jeżli nie podamy parametru to usunięty zostanie ostatni element
#    s.remove(x) - odnajduje x i usuwa go z listy s
#    s.reverse() - odwraca w miejscu kolejność elementów s
#    s.sort([funkcja]) - Sortuje w miejscu elementy. "funkcja" to funkcja porównawcza
#Methods writer
#    s.capitalize() - zmienia pierwszą literę na dużą
#    s.center(długość) - Centruje napis w polu o podanej długości
#    s.count(sub) - zlicza wystąpienie podciągu sub w napisie s
#    s.encode(kodowanie) - zwraca zakodowaną wersję napisu ('utf-8', 'ascii', 'utf-16')
#    s.isalnum() - sprawdza czy wszystkie znaki są znakami alfanumerycznymi
#    s.isdigit() - sprawdza czy wszystkie znaki są cyframi
#    s.islower() - sprawdza czy wszystkie litery są małe
#    s.isspace() - sprawdza czy wszystkie znaki są białymi znakami
#    s.isupper() - sprawdza czy wszystkie litery są duże
#    s.join(t) - łączy wszystkie napisy na liście t używając s jako separatora
#    s.lstrip() - usuwa początkowe białe znaki
#    s.replace(old, new) - zastępuje stary podciąg nowym
#    s.rstrip() - usuwa końcowe białe znaki
#    s.split(separator) - dzieli napis używają podanego separatora
#    s.strip() - usuwa początkowe i końcowe białe znaki
