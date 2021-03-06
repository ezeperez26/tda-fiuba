#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from max_flow import Flow


class ProjectSelection(object):
    """
    Esta es la clase que va a resolver el problema de ganancias por proyecto.
    En el Kleinberg-Tardos aparece bajo ese nombre.

    Necesita un string que tenga el siguiente formato:

        N
        M
        c1
        c2
        ...
        g1 r11 r12
        g2 r21 r22
        ...

    Donde N es la cantidad de capacidades, M es la cantidad de proyectos,
    c1 es el nombre de la capacidad 1, g1 es la ganancia de proyecto uno, y
    r11..r1k son las capacidades requeridas del proyecto 1.
    """

    def __init__(self, definition, solve = True):
        self.proyects = []

        lines = definition.split('\n')
        self.n = int(lines[0])
        self.m = int(lines[1])
        self.areas = lines[2:2 + self.n]
        self.proyects = [x.split(' ') for x in lines[2 + self.n:2 + self.n + self.m]]
        self.selectedProyects = []
        self.createNet()
        if solve:
            self.solve()

    def createNet(self):
        # Armado de la red.
        self.source = 0
        self.target = self.n + self.m + 1
        self.f = Flow(self.target + 1)

        for i, proy in enumerate(self.proyects):
            # proy es una lista del estilo [ganancia, capacidad1, capacidad2, ...]
            proyect_node = 1 + i
            self.f.add_edge(self.source, proyect_node, int(proy[0]))
            for req in proy[1:]:
                # Como los nodos se cuentan desde 0, y las capacidades requeridas
                # desde 1, necesito restar 1.
                area_node = 1 + self.m + int(req) - 1
                self.f.add_edge(proyect_node, area_node, float('inf'))

        for i, cap in enumerate(self.areas):
            area_node = 1 + self.m + i
            self.f.add_edge(area_node, self.target, int(cap))

    def solve(self):
        # Max-Flow, Min-Cut
        flow = self.f.get_max_flow(self.source, self.target)
        cut = self.f.get_min_cut(self.source, flow)

        # En el corte están los proyectos y las áreas a elegir.
        self.selectedProyects = [p for p in cut if 1 <= p <= self.m]
        self.selectedAreas = [a - self.m for a in cut if self.m < a <= self.n+self.m]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Por favor, pase un archivo!')
    else:
        with open(sys.argv[1]) as f:
            ps = ProjectSelection(f.read())
        ps.solve()
