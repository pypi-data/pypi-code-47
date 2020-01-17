#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ecomet as ecomet

def main():
    #1 Create connector

    host="174.138.4.86"
    #host="localhost"
    port="4000"

    a=ecomet.EcometClient(host, port, login="demo", password="demo")

    #2 Get archive names

    archives = a.get_names()

    print(archives)

    #3 Get all data

    data = a.get_data(id_count=1, archives=archives, start_date="2020-01-13T08:46:16Z", step_count=100, step_size=10)

    print(data)

if __name__ == '__main__':
    main()