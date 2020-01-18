import os
import csv
import re


def readFile(file_path):
    contacts = []
    # if os.name != "nt":
    here = os.environ.get("HERE")
    file = here + file_path
    if os.path.isfile(file):
        with open(file, "r") as read_file:
            data = eval(read_file.read())
            read_file.close()
            return data


def read_file(file_name):
    if os.path.isfile(file_name):
        with open(file_name) as stream:
            data = stream.read()
            stream.close()
            return data
    # else:
    #     self.error("File not found: " + file_name)


def read_csv(file_name, delimiter=';', quoting=csv.QUOTE_MINIMAL, errors="ignore"):
    try:
        with open(file_name) as stream:
            # CSV otimizado para formato do MS Excel
            data = csv.reader(
            stream,
            delimiter=delimiter,
            quoting=quoting
        )

        # Cabecalho sem caracteres especiais ou espacos
        header = map(
            lambda x: re.sub(r'\W', '', unicode(x, errors=errors)),
            data.next()
        )

        for line in data:
            # Trata incompatibilidades de codificacao
            safe = map(
                lambda x: unicode(x, errors="ignore"),
                line
            )

        this_row = dict(zip(header, safe))
        yield this_row

    except Exception as e:
        # self.error("Erro ao ler CSV", e)
        print(e)


def get_receivers():
    # Leitura do CSV
    groups_file = app.dir + "/../../../Data/Import/Current/groups-notification.csv"
    with open(groups_file) as stream:
        # CSV otimizado para formato do MS Excel
        data = csv.reader(
            stream,
            delimiter=';',
            quoting=csv.QUOTE_MINIMAL
        )

        # Cabecalho sem caracteres especiais ou espacos
        header = map(
            lambda x: re.sub(r'\W', '', unicode(x, errors="ignore")),
            data.next()
        )

        # Retorna os grupos
        groups = {}
        for group in data:
            # Trata incompatibilidades de codificacao
            safe = map(
                lambda x: unicode(x, errors="ignore"),
                group
            )

            this_group = dict(zip(header, safe))
            if this_group["id_alerta"] not in groups:
                groups[this_group["id_alerta"]] = []
            groups[this_group["id_alerta"]].append(this_group)

        app.info("Contatos dos grupos encontrados", groups)
        return groups