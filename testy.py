#!/bin/bash/python

var = "Mama i tata lubia babcie=hehe )                    "

nasza = var.find(u'babcie=')
nowa = var[nasza+7:].strip(')')
nowa = nowa.strip(')')
" ".join(nowa.split())
print nowa
print len(nowa)

var1 = """Moja babcia' mnie" kocha """

print var1

