#!/usr/bin/env python
import csv
import matplotlib.pyplot as plt
import networkx as nx
import os
from app import create_app
from app.extensions import db, socketio
from app.seeds.seed_schedules import seed_schedules
from collections import defaultdict

# app = create_app()

def find_paths(graph, node, slackTimes, paths):
    if not graph[node]:
        paths[-1].append(node)
        paths.append([])
        #print(node)
        return
    elif slackTimes[node] == 0:
        paths[-1].append(node)
        #print('{} -> '.format(node), end = '')
        for nxt in graph[node]:
            find_paths(graph, nxt, slackTimes, paths)

def make_pert_chart(graph, startTimes, completionTimes, slackTimes, criticalPaths):
    
    criticalEdges = defaultdict(list)
    
    for path in criticalPaths:
        for i in range(len(path) - 1):
            criticalEdges[path[i] + path[i+1]] = True
    
    g = nx.DiGraph()
    labelsDict = {}
    for parent in graph:
        for child in graph[parent]:
            parentStr = '{}/{}/{}'.format(startTimes[parent], completionTimes[parent], slackTimes[parent])
            childStr = '{}/{}/{}'.format(startTimes[child], completionTimes[child], slackTimes[child])
            labelsDict[parent] = parentStr
            labelsDict[child] = childStr
            if criticalEdges[parent + child]:
                g.add_edge(parent,child, color = 'red')
            else:
                g.add_edge(parent,child, color = 'black')
    pos=nx.shell_layout(g)
    for task in startTimes:
        x, y = pos[task]
        plt.text(x,y+0.1,s=labelsDict[task], bbox=dict(facecolor='red', alpha=0.5),horizontalalignment='center')
    # print(nx.info(g)) # DEPRECATED
    print('Number of nodes', len(g.nodes))
    print('Number of edges', len(g.edges))
    print('Average degree', sum(dict(g.degree).values()) / len(g.nodes))

    edges = g.edges()
    colors = [g[u][v]['color'] for u,v in edges]
    
    # nx.draw(g, pos, edges = edges,with_labels = True, edge_color = colors)
    # plt.savefig('pert.png', bbox_inches = 'tight')
    # plt.show()




def main(filename):

    graph = defaultdict(list)
    duration = {}

    try:
        with open(filename, newline = '') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                nodes = row[2].split(' ')
                for node in nodes:
                    graph[node].append(row[0])
                duration[row[0]] = int(row[1])
    except:
        return -1
    
    tasks = duration.keys()

    #initialize start times
    startTimes = {}
    for task in graph['NONE']:
        startTimes[task] = 0
    graph.pop('NONE', None)

    # calculate start times
    while len(startTimes) < len(tasks): # while any node doesn't have a start time
        for task in tasks: # loop through all tasks
            if task not in startTimes: # if the task doesn't have a start time yet
                startTime = 0 # initialize start time to be some minimum value
                flag = True
                for parent in graph: # look for all tasks it depends on i.e. all nodes pointing to it
                    if task in graph[parent]: # we found a parent
                        if parent in startTimes: # if the parent has a start time, compare it to current max
                            startTime = max(startTime, startTimes[parent] + duration[parent])
                        else: # else, one of the parents doesn't have a start time, so we can't calculate start time of current task yet
                            flag = False
                if flag:
                    startTimes[task] = startTime

    # calculate completion times
    completionTimes = {}
    for task in tasks:
        completionTimes[task] = startTimes[task] + duration[task]

    # calculate slack times
    slackTimes = {}
    for task in tasks:
        slackTime = 9999999999999999999;
        for node in graph[task]:
            slackTime = min(slackTime, startTimes[node] - completionTimes[task])
        if not graph[task]:
            slackTimes[task] = 0
        else:
            slackTimes[task] = slackTime
    
    print('start times: {}'.format(startTimes))
    print('completion times: {}'.format(completionTimes))
    print('slack times: {}'.format(slackTimes))

    # find critical paths
    criticalPaths = [[]]
    for node in graph:
        if startTimes[node] == 0:            
            find_paths(graph, node, slackTimes, criticalPaths)
    criticalPaths.pop()
    print(criticalPaths)

    make_pert_chart(graph, startTimes, completionTimes, slackTimes, criticalPaths)
    # make_gantt_chart(graph, startTimes, completionTimes, duration, slackTimes)   

if __name__ == "__main__":
    # socketio.run(app)
    main('tasks.csv')
    #with app.app_context():
    #    seed_schedules()
      
