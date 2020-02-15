# !/usr/bin/env python3
"""
Code for training before Google Hashcode 2020
"""
import random


def sort_pizzas(nb_of_pizzas, nb_of_slices_in_pizzas):
    """
    Sort pizzas
    :param nb_of_pizzas: Number of pizza
    :param nb_of_slices_in_pizzas: Number of slices in pizza
    :return: array with pizzas indexes and amount of slices
    """

    #  Liste à remplir
    pizza_array = []

    # Index
    index = 0

    # Association numéro de pizzas, nombre de parts
    for _ in range(nb_of_pizzas):
        print(f"Index : {index}")
        print(f"Nombre de parts : {nb_of_slices_in_pizzas[index]}")
        pizza_array.append([index, nb_of_slices_in_pizzas[index]])
        index += 1

    return pizza_array


def get_random_pizza(nb_of_pizzas):
    """
    Select random pizza
    :param nb_of_pizzas:
    :return: random pizza
    """

    # Chiffre aléatoire
    return random.randint(0, nb_of_pizzas)


def order(nb_of_required_slices, nb_of_pizzas, nb_of_slices_in_pizzas):
    """
    Calcul de la meilleure commande
    :param nb_of_pizzas:
    :param nb_of_required_slices:
    :param nb_of_slices_in_pizzas:
    :return:
    """
    # Run boolean
    run = True

    # Enumération
    print(f"Nombre de parts attendues : {nb_of_required_slices}")
    print(f"Nombre de pizzas : {nb_of_pizzas} ")
    ordered_pizzas = []

    # Pour le nombre de parts attendues
    for _ in range(nb_of_required_slices + 1):

        # Tableau pour les pizzas
        pizzas_array = sort_pizzas(nb_of_pizzas, nb_of_slices_in_pizzas)

        # Reste t-il des pizzas ?
        while len(pizzas_array) > 0 and run:

            # Exemple : [[0, 2], [1, 5], [2, 6], [3, 8]]
            print(f"Pizzas restantes : {pizzas_array}")

            #  Sélection du numéro de la pizza
            index = get_random_pizza(nb_of_pizzas - 1)
            pizza_number = pizzas_array[index][0]
            lack_of_slice = pizzas_array[index][1]

            # Indication des valeurs associées à la pizza
            print(f"Je lance le dé : {index}")
            print(f"Je tombe sur la pizza numéro {pizza_number}")
            print(f"Cette pizza a {lack_of_slice} parts!")

            # Récupération pizza
            print("Je vais la prendre...")

            # Ajout dans la liste des pizzas à commander
            ordered_pizzas.append(pizzas_array[index])

            # Retrait de la pizza de la liste
            del pizzas_array[index]
            print(f"Pizzas_array updated : {pizzas_array}")
            print(f"nb_of_required_slices {nb_of_required_slices}")

            # On veut vérifier s'il y a encore des besoins de parts
            if nb_of_required_slices - lack_of_slice <= 0:
                run = False

            else:

                #  Non on retire les parts
                print(f"...baisser à {lack_of_slice} le nombre de parts attendues.")
                nb_of_required_slices -= lack_of_slice

                # Retrait de la pizza
                print(f"...et le nombre de pizza que l'on peut commander {nb_of_pizzas - 1} ")
                nb_of_pizzas -= 1

    return nb_of_pizzas, nb_of_required_slices, ordered_pizzas


def count_amount_of_pizzas(pizzas):
    """
    Compte le nombre de pizzas (évite de convertir une chaîne de caractère)
    :param pizzas: liste de pizzas
    :return: nombre de pizza
    """
    # Counter
    pizzas_counter = 0

    # Pizzas count
    for _ in pizzas:
        pizzas_counter += 1
    print(f"Nous avons {pizzas_counter} pizzas.")
    return pizzas_counter


def main():
    """
    Main program for training before Google Hashcode 2020
    :return: 
    """
    nb_of_required_slices = 17
    nb_of_slices_in_pizzas = [2, 5, 6, 8]
    nb_of_pizzas = count_amount_of_pizzas(nb_of_slices_in_pizzas)

    nb_of_pizzas, nb_of_required_slices, ordered_pizzas = order(nb_of_required_slices,
                                                                nb_of_pizzas,
                                                                nb_of_slices_in_pizzas)

    print(ordered_pizzas, nb_of_required_slices)


if __name__ == '__main__':
    main()
