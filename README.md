# Test in C per SO2

## Scelte di implementazione
- Il compito e il numero di processi viene deciso tramite degli input da linea di comando:
    - per il compito: [-1, -2]
    - per il numero di processi: -p

- Gli unici caratteri consentiti sono:
    - Range: (48-57), (65-90), (97-122)


## Specifiche del prof
- Il testo contiene solo caratteri in ASCII a 1 byte [0-127]

- Nella tabella ```csv``` le parole con maiuscole e minuscole sono considerate uguali, cioè oggi e OGGI saranno nella stessa riga

- Bisogna escludere tutte le punteggiature che non siano ```.```, ```!``` o ```?``` che sono terminatori di linea e vanno considerati come parole singole nella tabella ```csv```

- Inoltre l'apostrofo ```'``` viene considerato come parte di una parola, cioè la parola ```l'esame``` verrà considerata come ```l'``` e ```esame```

- La prima parola viene considerata come dopo un ```.```

- L'ultima parola precede la prima cioè se nel caso in cui la prima parola sia ciao e l'ultima domani nella tabella avremo una riga con: ```domani,ciao,1```

- Quando scrivo il testo dopo ```.```, ```!``` o ```?``` la prima lettera deve essere maiuscola

- Nel caso non si inserisca una parola da cui iniziare nel compito 2 viene selezionata casualmente una punteggiatura tra ```.```, ```!``` o ```?``` e viene generata la prima parola tramite le probabilità della tabella

## Casi speciali (scelte a mia discrezione)

- Apostrofi:
    - Nel caso in cui un apostrofo non sia alla fine di una parola verrà considerato come l'inizio della successiva
    - Se non avesse neanche una parola successiva per esempio ```parola1 ' parola2``` verrebbe cancellato
    - Se una parola ha due apostrofi prima o dopo viene considerato solo 1, cioè ```''ciao''``` è uguale a ```'ciao'```
    - Se due parola hanno più apostrofi in mezzo il primo viene considerato come appartenente alla prima parola e l'ultimo alla seconda, cioè ```ciao'''domani``` è uguale a ```ciao'``` e ```'domani```

- Ultima parola precedente alla prima:
    - Nel caso in cui l'ultima parola sia ```.``` non verrà considerata nuovamente come precedente alla prima per non duplicare l'occorenza

- Appossimazioni nel file ```csv```:
    - Le probabilità vanno approssimate a 4 cifre decimali cioè ```0.666666``` diventa ```0.6667```
    - Le probabilità uguali a 1 vanno lasciate come ```1```
