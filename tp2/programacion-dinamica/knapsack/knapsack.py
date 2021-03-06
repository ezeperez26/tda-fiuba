#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

from knapsack_file_parser import Parser
from knapsack_solution_container import KnapsackSolution

def knapsack_bottom_up(items_value, items_weight, knapsack_weight):

    # Inicializo mi matriz de resultados
    cant_items = len(items_value)
    results = [[0 for x in range(knapsack_weight + 1)] for y in range(cant_items + 1)]

    # Corro el algoritmo en si, midiendo el tiempo    
    knapsack_bottom_up_core(items_value, items_weight, knapsack_weight, results)

    #return KnapsackSolution(results[cant_items][knapsack_weight], knapsack_get_solution(cant_items, knapsack_weight, items_value, items_weight, results))
    return results[cant_items][knapsack_weight]

def knapsack_bottom_up_core(items_value, items_weight, knapsack_weight, results):

    for i in range(1, len(items_value) + 1):

        for w in range(1, knapsack_weight + 1):

            if (w < items_weight[i - 1]):
                results[i][w] = results[i - 1][w]
            else:
                results[i][w] = max(results[i - 1][w], items_value[i - 1] + results[i - 1][w - items_weight[i - 1]])

def knapsack_get_solution(n, W, items_value, items_weight, optimum_values):

    result = []

    if n == 0 or W == 0:
        return None
    else:

        for i in range(n, 0, -1):
            if items_value[i - 1] + optimum_values[i - 1][W - items_weight[i - 1]] == optimum_values[i][W]:
                result.append(i)
                W -= items_weight[i - 1]

    return list(reversed(result))

def knapsack_top_down(items_value, items_weight, knapsack_weight):

    # Inicializo mis variables (se hacen globales para no pasarlas siempre en la recursividad)
    cant_items = len(items_value)
    global td_results
    td_results = [[None for x in range(knapsack_weight + 1)] for y in range(cant_items + 1)]
    global td_items_value
    td_items_value = items_value
    global td_items_weight
    td_items_weight = items_weight
    global td_knapsack_weight
    td_knapsack_weight = knapsack_weight

    # Corro el algoritmo top-down midiendo el tiempo
    knapsack_top_down_core(cant_items, knapsack_weight)

    return td_results[cant_items][knapsack_weight]

def knapsack_top_down_core(cant_items, knapsack_weight):

    if ((cant_items <= 0) or (knapsack_weight <= 0)):
        return 0

    if (td_results[cant_items][knapsack_weight] is not None):
        return td_results[cant_items][knapsack_weight]
    elif (td_items_weight[cant_items - 1] > knapsack_weight):
        td_results[cant_items][knapsack_weight] = knapsack_top_down_core(cant_items - 1, knapsack_weight)
        return td_results[cant_items][knapsack_weight]
    else:
        td_results[cant_items][knapsack_weight] = max(knapsack_top_down_core(cant_items - 1, knapsack_weight), td_items_value[cant_items - 1] + knapsack_top_down_core(cant_items - 1, knapsack_weight - td_items_weight[cant_items - 1]))
        return td_results[cant_items][knapsack_weight]

