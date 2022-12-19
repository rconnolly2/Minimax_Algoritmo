# Minimax_Algoritmo

En este proyecto mi objetivo era crear un simple juego de tres en raya con la libreria Pygame
que se pueda utilizar con raton miplementar y entender el agloritmo minimax:

Pseudo codigo:
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
(* Initial call *)
minimax( origin, depth, TRUE )

Fuente: https://en.wikipedia.org/wiki/Minimax

