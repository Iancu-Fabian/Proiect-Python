Descriere: 
Aplicatie web de tip Habit Tracker care permite utilizatorului sa isi creeze cont si sa introduca diferite obiceiuri din viata de zi cu zi pentru a le tine evidenta si pentru a vedea statistici privind tipurile de obiceiuri pe care le are.

Mod de rulare:
Se deschide fisierul app.py si se ruleaza serverul Flask din terminal folosind comanda "python app.py"

Mod de utilizare:
Cand utilizatorul deschide prima data aplicatia, se incarca pagina home, de unde poate apasa pe butonul "Get Started" pentru a-si crea cont. Sunt impuse conditii de lungime minima pentru datele completate in formular. Dupa ce este creat contul, userul este logat automat si poate sa inceapa folosirea aplicatiei. Din noua pagina home pentu utilizatori logati, poate sa adauge obiceiuri in lista alegand nume, tip, categorie si interval orar, dupa caz. Dupa ce termina de adaugat obiceiurile dorite, poate accesa pagina "To do Today" pentru a vedea lista cu obiceiuri pentru ziua curenta ordonate dupa ora si poate bifa checkboxul in functie de starea lor (completate sau necompletate). Apoi, in functie de obiceiurile completate in ziua respectiva, poate vedea graficul asociat zilei accesand pagina "My statistics". Graficul este realizat in functie de categoriile obiceiurilor introduse de user, pentru a-i oferi informatii privind cantitatea de obiceiuri zilnice pe care le atribuie diferitelor sfere ale vietii (sanatate, munca, divertisment etc).

Cerinte:
Pentru a rula serverul, trebuie ca pe dispozitiv sa fie instalate urmatoarele module:
-Flask
-SQLAlchemy
-Passlib
-Migrate
