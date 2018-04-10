#! /usr/bin/env python

somelist = [(1,2,4,'mama'), (2,4324,34,'krzys'),(23,34,25,'rys')]

n = int(raw_input("Ktory element list chcesz posortowac "))

def sortby(somelist,n):
        nlist = [i[n] for i in somelist]
         
