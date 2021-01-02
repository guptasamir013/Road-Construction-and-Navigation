from django.shortcuts import render, redirect
import pickle

# Create your views here.
def home(request):
    return render(request, "accounts/home.html", {})

def add_road(request):
    if request.method=="POST":
        handle = open("static/accounts/my_graph.pickle", "rb")
        graph = pickle.load(handle)

        data = request.POST

        graph.add_road(int(data.get("v1")), int(data.get("v2")), int(data.get("build")), int(data.get("travel")))
        handle = open("static/accounts/my_graph.pickle", "wb")
        pickle.dump(graph, handle, protocol=pickle.HIGHEST_PROTOCOL)

        return redirect("accounts-home")

    return render(request, "accounts/add_road.html", {})

def del_road(request):
    if request.method=="POST":
        handle = open("static/accounts/my_graph.pickle", "rb")
        graph = pickle.load(handle)

        data = request.POST

        graph.del_road(int(data.get("v1")), int(data.get("v2")))
        handle = open("static/accounts/my_graph.pickle", "wb")
        pickle.dump(graph, handle, protocol=pickle.HIGHEST_PROTOCOL)

        return redirect("accounts-home")

    return render(request, "accounts/del_road.html", {})

def reconstruct(request):
    handle = open("static/accounts/my_graph.pickle", "rb")
    graph = pickle.load(handle)

    graph.reconstruct()
    handle = open("static/accounts/my_graph.pickle", "wb")
    pickle.dump(graph, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return redirect("accounts-home")


def navigate(request):
    if request.method=="POST":
        handle = open("static/accounts/my_graph.pickle", "rb")
        graph = pickle.load(handle)

        data = request.POST

        graph.navigate(int(data.get("v1")), int(data.get("v2")))
        handle = open("static/accounts/my_graph.pickle", "wb")
        pickle.dump(graph, handle, protocol=pickle.HIGHEST_PROTOCOL)

        return redirect("accounts-home")

    return render(request, "accounts/navigate.html", {})

def clear(request):
    handle = open("static/accounts/my_graph.pickle", "rb")
    graph = pickle.load(handle)

    graph.clear()
    handle = open("static/accounts/my_graph.pickle", "wb")
    pickle.dump(graph, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return redirect("accounts-home")
