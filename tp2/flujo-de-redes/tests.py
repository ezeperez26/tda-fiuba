#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from max_flow import Flow
from project_selection import ProjectSelection


class FlowPathTest(unittest.TestCase):

    def test_flow_path_returns_correct_path_for_initial_flow(self):
        g = Flow(4)
        g.add_edge(0, 1, 10)
        g.add_edge(1, 2, 0)
        g.add_edge(1, 3, 10)

        f = g.get_empty_flow()
        self.assertEqual([e.dst for e in g.flow_path(0, 3, f)], [1, 3])
        self.assertIsNone(g.flow_path(0, 2, f))


class MaxFlow(unittest.TestCase):

    def test_simple_max_flow(self):
        f = Flow(3)
        f.add_edge(0, 1, 10)
        f.add_edge(1, 2, 20)

        flow = f.get_max_flow(0, 2)
        self.assertEqual(max(flow.values()), 10)

    def test_max_flow_with_some_more_paths(self):
        f = Flow(4)
        f.add_edge(0, 1, 10)
        f.add_edge(0, 2, 30)
        f.add_edge(1, 3, 20)
        f.add_edge(2, 3, 20)

        self.assertEqual(f.repr_max_flow(0, 3), ('0 -> 1: 10\n'
                                                 '0 -> 2: 20\n'
                                                 '1 -> 3: 10\n'
                                                 '2 -> 3: 20\n'))


class ProjectSelectionTest(unittest.TestCase):

    def setUp(self):
        self.definition = '2\n3\n50\n100\n100 1\n200 1 2\n300 2'

    def test_constructor_reads_definition_correctly(self):
        ps = ProjectSelection(self.definition)
        self.assertEqual(ps.n, 2)
        self.assertEqual(ps.m, 3)
        self.assertListEqual(ps.areas, ['50', '100'])
        self.assertListEqual(ps.proyects, [['100', '1'], ['200', '1', '2'], ['300', '2']])

    def test_simple_selection(self):
        ps = ProjectSelection(self.definition)
        self.assertEqual(ps.selectedProyects, [1,2,3])
        self.assertEqual(ps.selectedAreas, [1,2])

    def test_no_selection(self):
        no_problem_definition = "1\n2\n200\n100 1\n50 1\n"
        ps = ProjectSelection(no_problem_definition)
        self.assertListEqual(ps.areas, ['200'])
        self.assertListEqual(ps.proyects, [['100', '1'], ['50', '1']])
        self.assertEqual(ps.selectedAreas, [])
        self.assertEqual(ps.selectedProyects, [])

    def test_hard_selection(self):
        definition = "3\n4\n8\n8\n10\n10 1 2\n10 2\n4 3\n4 3\n"
        ps = ProjectSelection(definition)
        self.assertEqual(ps.selectedAreas, [1,2])
        self.assertEqual(ps.selectedProyects, [1,2])

    def test_hard_2(self):
        definition = "3\n4\n8\n8\n10\n10 1 2\n10 2\n5 3\n6 3\n"
        ps = ProjectSelection(definition)
        self.assertEqual(ps.selectedAreas, [1,2,3])
        self.assertEqual(ps.selectedProyects, [1,2,3,4])

    def test_low_cost(self):
        uno_def = "1\n3\n1\n100 1\n100 1\n100 1\n"
        ps = ProjectSelection(uno_def)
        self.assertEqual(ps.selectedAreas, [1])
        self.assertEqual(ps.selectedProyects, [1,2,3])

    def test_saturated_project(self):
        saturated_def = "1\n3\n100\n100 1\n100 1\n100 1\n"
        ps = ProjectSelection(saturated_def)
        self.assertEqual(ps.selectedAreas, [1])
        self.assertEqual(ps.selectedProyects, [1,2,3])

def main():
    return unittest.main()


if __name__ == '__main__':
    main()
