import numpy
from scipy import stats
 
##  Maschinelles Lernen
#   Aufgabe 1

zahlen_aufg01 = [8, 2, 5, 1, 10]

def berechene_mittelWert(liste):
    mittelWert = numpy.mean(liste)
    return mittelWert
 
print(berechene_mittelWert(zahlen_aufg01))
 
#   Aufgabe 2

zahlen1_aufg02 = [7, 5, 3, 5]
zahlen2_aufg02 = [1, 2, 3, 4, 5]

def berechne_median(liste):
    median = numpy.median(liste)
    return(median)
 
print(berechne_median(zahlen1_aufg02))
print(berechne_median(zahlen2_aufg02))
 
#   Aufgabe 3

zahlen_aufg03 = [4, 1, 2, 2, 3, 1]

def berechne_modus(liste):
    modus = stats.mode(liste)
    return(modus)
 
print(berechne_modus(zahlen_aufg03))
 
#   Aufgabe 4

zahlen_aufg04 = [1, 2, 3, 4, 4, 5, 5, 5]

def kombinierte_statistik(liste):
    mittelWert = numpy.mean(liste)
    median = numpy.median(liste)
    modus = stats.mode(liste)
    tuple = (mittelWert, median, modus)
    return tuple
 
print(kombinierte_statistik(zahlen_aufg04))
 
#   Aufgabe 5

zahlen_aufg05 = [10, 20, 30, 40, 50, 60, 70]

def filter_und_statistik(liste:list, minWert, maxWert):
    for zahl in liste:
        if zahl < minWert or zahl > maxWert:
            liste.remove(zahl)
    mittelWert = numpy.mean(liste)
    median = numpy.median(liste)
    modus = stats.mode(liste)
    tuple = (mittelWert, median, modus)
    return tuple
 
print(filter_und_statistik(zahlen_aufg05, 20, 60))
 
##  Standardabweichung
#   Aufgabe 1

zahlen_aufg06 = [4, 8, 6, 5, 3, 2]

def berechne_varianz(liste):
    mittelWert = numpy.mean(liste)
    differenz = [(wert - mittelWert) **2 for wert in liste]
    varianz = numpy.mean(differenz)
    return varianz
       
print(berechne_varianz(zahlen_aufg06))
 
#   Aufgabe 2

zahlen_aufg07 = [9, 2, 5, 4, 12, 7, 8, 11]

def berechene_standardabweichung(liste):
    standardabweichung = numpy.sqrt(berechne_varianz(liste))
    return(standardabweichung)
 
print(berechene_standardabweichung(zahlen_aufg07))

 
#   Berechnung von Perzentile

schulstrecke = [20, 30, 5, 10, 40, 20]

def percentile(liste):
     percentile = numpy.percentile(liste, 75)
     print(percentile)
 
percentile(schulstrecke)