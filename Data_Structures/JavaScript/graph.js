/*
A set of nodes and connections
Uses: Everywhere: Routing algorithms, Location/Mapping, Social Networks, recommendation engines
Terminology: Vertex = node and edge = connections
Undirected graph: No direction associated with a vertex, can be back and forth
Directed graph: There's a direction associated with a vertex
Weighted graph: Each edge has a weight
*/

// Undirected Graph
class Graph {
  constructor() {
    this.adjacencyList = {};
  }

  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];
  }

  addEdge(v1, v2) {
    this.adjacencyList[v1].push(v2);
    this.adjacencyList[v2].push(v1);
  }
  removeEdge(v1, v2) {
    this.adjacencyList[v1] = this.adjacencyList[v1].filter((v) => v != v2);
    this.adjacencyList[v2] = this.adjacencyList[v2].filter((v) => v != v1);
  }
  removeVertex(vertex) {
    for (let i = 0; i <= this.adjacencyList[vertex].length; i++) {
      let closeVertex = this.adjacencyList[vertex].pop();
      this.removeEdge(vertex, closeVertex);
    }
    delete this.adjacencyList[vertex];
  }
  DFS_R(start) {
    const result = [];
    const visited = {};
    const adjacencyList = this.adjacencyList;
    function dfs(vertex) {
      if (!vertext) return null;
      visited[vertex] = true;
      result.push(vertex);
      adjacencyList[vertex].forEach((neighbor) => {
        if (!visited[neighbor]) {
          return dfs(neighbor);
        }
      });
    }
    dfs(start);
    return result;
  }

  BFS(start) {
    const data = [];
    let queue = [start];
    const visited = {};
    let curVertex;

    while (queue.length) {
      let curVertex = queue.shift();
      data.push(curVertex);

      this.adjacencyList[curVertex].forEach((neighbor) => {
        if (!visited[neighbor]) {
          visited[neighbor] = true;
          queue.push(neighbor);
        }
      });
    }
  }
}

let g = new Graph();
g.addVertex("Philly");
g.addVertex("NewYork");
g.addVertex("Dallas");
g.addEdge("Philly", "NewYork");
g.addEdge("Philly", "Dallas");
g.addEdge("NewYork", "Dallas");
g.removeVertex("NewYork");
console.log(g);
