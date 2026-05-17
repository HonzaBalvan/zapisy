def najdi(mapa):
    if not mapa:
        return 0, 0, 0

    pocet_radku = len(mapa)
    pocet_sloupcu = len(mapa[0])
    visited = [[False for _ in range(pocet_sloupcu)] for _ in range(pocet_radku)]
    max_velikost = 0
    teziste_r = 0
    teziste_s = 0

    for r in range(pocet_radku):
        for c in range(pocet_sloupcu):
            if mapa[r][c] == "." and not visited[r][c]:
                # Inicializace pro novou jeskyni
                stack = [(r, c)]
                visited[r][c] = True
                soucet_r = 0
                soucet_s = 0
                pocet = 0

                # DFS pomocí stacku
                while stack:
                    curr_r, curr_c = stack.pop()
                    soucet_r += curr_r
                    soucet_s += curr_c
                    pocet += 1

                    # Prozkoumej sousedy
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < pocet_radku and 0 <= nc < pocet_sloupcu:
                            if mapa[nr][nc] == "." and not visited[nr][nc]:
                                visited[nr][nc] = True
                                stack.append((nr, nc))

                # Aktualizace největší jeskyně
                if pocet > max_velikost:
                    max_velikost = pocet
                    teziste_r = soucet_r // pocet
                    teziste_s = soucet_s // pocet

    return [max_velikost, teziste_r, teziste_s]

with open("vstup.blud") as f:
    mapa = [line.strip() for line in f if line.strip()]

print(*najdi(mapa))
