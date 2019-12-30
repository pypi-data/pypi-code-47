import requests
import datetime
import json
from html.parser import HTMLParser


def _liste_prenom_nom(chaine):
    liste = chaine.split(" ")
    nom = liste[-1]
    return [" ".join(liste[:-1]), nom.upper()]


class motd():
    def __init__(self, day=None, delta=0):
        MyHTMLParser.liste_evenements = []
        MyHTMLParser.evt_actuel = None
        MyHTMLParser.lien = 0
        MyHTMLParser.evenement = 2
        MyHTMLParser.date = False
        self.parser = MyHTMLParser()
        #
        self.jour = day
        self.decalage = int(delta)
        self.sortie_json = {}
        self.j, self.jr, self.js = self._lejour()
        self.page_du_jour = ""
        self._requete()
        self._sortie()

    def _lejour(self):
        aujourdhui = datetime.date.today()
        if self.jour is None:
            jour_reference = aujourdhui
        else:
            date = self.jour.split('/')
            date = list(map(int, date))
            annee = aujourdhui.year
            jour_reference = datetime.date(annee, date[1], date[0])
        #
        jour_choisi = jour_reference + datetime.timedelta(days=self.decalage)
        jour_choisi_requete = jour_choisi.strftime("%m%d").lstrip('0')
        jour_choisi_sortie = jour_choisi.strftime("%d/%m")
        return [jour_choisi, jour_choisi_requete, jour_choisi_sortie]

    def _requete(self):
        url_le_jour = f"Day{self.jr}.html"
        site = "http://mathshistory.st-andrews.ac.uk/Day_files/"
        self.page_du_jour = requests.get(site + url_le_jour)
        return self.page_du_jour.status_code

    def _sortie(self):
        self.parser.feed(self.page_du_jour.text)
        self.sortie_json = json.dumps({self.js: self.parser.liste_evenements})

    def sortie(self):
        return self.sortie_json

    def out(self):
        return self.sortie()


class Evt():
    id = 0

    def __init__(self):
        self.renseignements = {'year': None,
                               'fname': None,
                               'name': None,
                               'event': None}
        self.fourretout = []

    def annee(self, annee):
        self.renseignements['year'] = int(annee)

    def prenom(self, prenom):
        self.renseignements['fname'] = prenom

    def nom(self, nom):
        self.renseignements['name'] = nom

    def nmd(self, t):
        self.renseignements['event'] = t

    def liste(self):
        return self.renseignements


class MyHTMLParser(HTMLParser):
    # liste_evenements = []
    # evt_actuel = None
    # lien = 0
    # evenement = 2
    # date = False

    def handle_starttag(self, tag, attrs):
        if tag == "font":
            if attrs[0][1] == "green":
                MyHTMLParser.evenement = 1
            elif attrs[0][1] == "purple":
                MyHTMLParser.evenement = 0
            else:
                MyHTMLParser.evenement = 2
            # on n'a pas encore rencontré <p>
            MyHTMLParser.date = False
        if tag == "p":
            MyHTMLParser.date = True
        if tag == "a":
            for a in attrs:
                if a[0] == "onclick":
                    MyHTMLParser.lien = 1

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        data = data.strip()
        # la date est de la forme : "AAAA :"
        data = data.strip(" :")
        if MyHTMLParser.evenement != 2:
            if MyHTMLParser.date and data != "":
                # si None, on a fini l'événement précédent
                if MyHTMLParser.evt_actuel is None:
                    MyHTMLParser.evt_actuel = Evt()
                # détermination du champ à ajouter
                # date ou prenom/nom
                if data.isdigit():
                    MyHTMLParser.evt_actuel.annee(data)
                else:
                    prenom, nom = _liste_prenom_nom(data)
                    MyHTMLParser.evt_actuel.prenom(prenom)
                    MyHTMLParser.evt_actuel.nom(nom)
        #
        if MyHTMLParser.lien == 1 and MyHTMLParser.evt_actuel is not None:
            if MyHTMLParser.evenement == 1:
                evt = "birth"
            else:
                evt = "death"
            MyHTMLParser.evt_actuel.nmd(evt)
            # fin de l'evt actuel
            MyHTMLParser.liste_evenements.append(
                MyHTMLParser.evt_actuel.liste())
            MyHTMLParser.evt_actuel = None
            MyHTMLParser.lien = 0
