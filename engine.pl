:- style_check(-singleton).

persona(a).


ling(A):- assert(persona(linguistico)), persona(linguistico).
inte(A):- assert(persona(interpersonal)).
esp(A):- assert(persona(espacio)).
mate(A):- assert(persona(matematico)).
cre(A):- assert(persona(creativo)).

linguistico(A):- persona(linguistico), A is 1.
interpersonal(A):- persona(interpersonal), A is 1.
espacio(A):- persona(espacio), A is 1.
matematico(A):- persona(matematico), A is 1.
creativo(A):- persona(creativo), A is 1.

abogado(A):- linguistico(A), interpersonal(A).
arquitecto(A):- espacio(A), matematico(A), creativo(A).
civil(A):- matematico(A), espacio(A), interpersonal(A).
electronico(A):- matematico(A), interpersonal(A).
informatico(A):- matematico(A), creativo(A).

getConocimientos(A):-persona(A).
purgar:- retractall(persona(_)).
