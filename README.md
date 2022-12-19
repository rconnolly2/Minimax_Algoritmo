
# Minimax Algoritmo 3 en raya

En este proyecto mi objetivo era crear un simple juego de tres en raya con la libreria Pygame,
pero el objetivo mas grande de este proyecto era implementar y entender el algoritmo minimax:



## Características

- Pygame
- Clickable con raton utilizando Bounding box collision https://learnopengl.com/In-Practice/2D-Game/Collisions/Collision-detection
- Utiliza el algoritmo minimax


## Como funciona minimax

![App Screenshot](https://i.postimg.cc/tRW39gzM/minimax.png)


## Pseudocódigo
```
function  minimax( node, depth, maximizingPlayer ) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max( value, minimax( child, depth − 1, FALSE ) )
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min( value, minimax( child, depth − 1, TRUE ) )
        return value

```

[Wikipedia](https://en.wikipedia.org/wiki/Minimax#Example_2)

