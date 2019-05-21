
linguistico_verbal(A):-profesion(no_linguistico_verbal),!,fail.
linguistico_verbal(A):-redactar_documentos(A).
linguistico_verbal(A):-profesion(leer_autodidacta).
linguistico_verbal(A):-profesion(bueno_hablar).



mamifero(A):-tiene_pelo(A),!.
mamifero(A):-da_leche(A).
mamifero(A):-assert(animal(no_mamifero)),fail.

ave(A):-animal(no_ave),!,fail.
ave(A):-tiene_plumas(A),!.
ave(A):-vuela(A),pone_huevos(A).
ave(A):-assert(animal(no_ave)),fail.

carnivoro(A):-animal(no_carnivoro),!,fail.
carnivoro(A):-come_carne(A),!.
carnivoro(A):-dientes_agudos(A),ojos_al_frente(A).
carnivoro(A):-assert(animal(no_carnivoro)),fail.

felino(A):-animal(no_felino),!,fail.
felino(A):-carnivoro(A),garras(A),vista_nocturna(A).
felino(A):-assert(animal(no_felino)),fail.

ungulado(A):-animal(no_ungulado),!,fail.
ungulado(A):-mamifero(A),rumia(A),!.
ungulado(A):-mamifero(A),tiene_pezu�as(A).
ungulado(A):-assert(animal(no_ungulado)),fail.

