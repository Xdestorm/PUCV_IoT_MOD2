def cadena_al_azar(n):
    from random import choice
    i = 0
    final = ''
    while i < n:
        final += choice('atcg')
        i += 1
        return final

