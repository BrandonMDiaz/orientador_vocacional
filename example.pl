:- style_check(-singleton).

identifica(X):-assert(animal(pendiente)),id_animal(X),purgar.

persona(A):- assert(pers(caca)).
person:- assert(comida(persona)).
comida(caca).

purgar:-nl,write("..:: Limpiando memoria de trabajo ::.."),nl,nl,retractall(animal(_)),write(".: Memoria limpia :."),nl,nl.
