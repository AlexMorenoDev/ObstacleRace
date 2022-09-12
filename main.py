# Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
# carrera de obstáculos.
# - La función recibirá dos parámetros:
#      - Un array que sólo puede contener String con las palabras "run" o "jump"
#      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
# - La función imprimirá cómo ha finalizado la carrera:
#      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
#        variará el símbolo de esa parte de la pista.
#      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#      - Si hace "run" en "|" (valla), se variará la pista por "/".
# La función retornará un Boolean que indique si ha superado la carrera.
# Para ello tiene que realizar la opción correcta en cada tramo de la pista.

def check_format(target_list, valid_list):
    return all(elem in valid_list for elem in target_list)

def race_ok(movements, circuit):
    if len(movements) != len(circuit):
        print("ERROR: Movements list and circuit lenghts must be the same!")
        return None
    
    if not check_format(movements, ["RUN", "JUMP"]) or not check_format(list(circuit), ["_", "|"]):
        print("ERROR: Movements or circuit contain wrong elements!")
        return None

    right_moves = {"RUN": "_", "JUMP": "|"}

    status = ""
    success = True
    for index, move in enumerate(movements):
        if right_moves[move] != circuit[index]:
            if move == "RUN":
                status += "/"
            else:
                status += "x"
            
            if success:
                success = False
        else:
            status += circuit[index]

    print("Race end status: " + status)
    return success

print("------------------------------")
print(race_ok(["RUN", "JUMP", "RUN", "JUMP", "RUN"], "_|_|_")) # True
print("------------------------------")
print(race_ok(["RUN", "RUN", "JUMP", "RUN", "RUN", "JUMP", "RUN", "RUN"], "__|__|__")) # True
print("------------------------------")
print(race_ok(["RUN", "RUN", "JUMP", "JUMP", "RUN", "RUN", "RUN", "RUN"], "__|__|__")) # False
print("------------------------------")






