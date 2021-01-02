import heapq
import sys
import pickle

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_road(self, v1, v2, build_time, travel_time):
        if self.adj_list.get(v1)==None:
            self.adj_list[v1] = {}
        if self.adj_list.get(v2)==None:
            self.adj_list[v2] = {}

        self.adj_list[v1][v2] = {"build": build_time, "travel": travel_time}
        self.adj_list[v2][v1] = {"build": build_time, "travel": travel_time}

    def del_road(self, v1, v2):
        if self.adj_list.get(v1)==None or self.adj_list.get(v2)==None or self.adj_list[v1].get(v2)==None:
            print("No such Road")
            return
        self.adj_list[v1].pop(v2)
        self.adj_list[v2].pop(v1)

    def reconstruct(self):
        if len(self.adj_list.keys())==0:
            return
        graph = self.adj_list
        self.adj_list = {}

        ## for each vertex [par, build_time, mst_present]
        track = {}
        for v in graph.keys():
            track[v] = [-1, sys.maxsize, 0]

        pq = [list(graph.keys())[0]]
        track[list(graph.keys())[0]][1] = 0
        heapq.heapify(pq)

        while(len(pq)>0):
            top = pq[0]
            heapq.heappop(pq)
            if track[top][2]==1:
                continue
            track[top][2] = 1
            for v in graph[top].keys():
                if track[v][2]==0 and graph[top][v]["build"]<track[v][1]:
                    track[v][0] = top
                    track[v][1] = graph[top][v]["build"]
                    heapq.heappush(pq, v)

        for v in track.keys():
            if track[v][2]==0:
                self.adj_list = graph
                print("MST Not Possible")
                return

        for v in track.keys():
            if track[v][0]!=-1:
                travel_time = graph[v][track[v][0]]["travel"]
                self.add_road(v, track[v][0], track[v][1], travel_time)

    def navigate(self, v1, v2):
        graph = self.adj_list

        if graph.get(v1)==None or graph.get(v2)==None:
            print("Not Possible")
            return

        ## for each vertex [par, travel_time, visited]
        track = {}
        for v in graph.keys():
            track[v] = [-1, sys.maxsize, 0]

        pq = [(0, v1)]
        track[v1][1] = 0
        heapq.heapify(pq)

        while(len(pq)>0):
            top = pq[0]
            heapq.heappop(pq)
            if track[top[1]][2]==1:
                continue
            track[top[1]][2] = 1
            for v in graph[top[1]].keys():
                if track[v][2]==0 and graph[top[1]][v]["build"]+top[0]<track[v][1]:
                    track[v][0] = top[1]
                    track[v][1] = graph[top[1]][v]["build"]+top[0]
                    heapq.heappush(pq, (track[v][1], v))

        if track[v2][2]==0:
            print("Not Possible")
            return

        v = v2
        while(track[v][0]!=-1):
            print(str(v) + "<-", end = "")
            v = track[v][0]
        print(v)

    def clear():
        self.adj_list = {}
        return

my_graph = Graph()

with open('static/accounts/my_graph.pickle', 'wb') as handle:
    pickle.dump(my_graph, handle, protocol=pickle.HIGHEST_PROTOCOL)


with open('static/accounts/my_graph.pickle', 'rb') as handle:
    graph = pickle.load(handle)
