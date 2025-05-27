import os
import re

def create_tree_from_text(base_path, tree_text):
    """
    Crée une arborescence de dossiers et fichiers à partir d'un texte au format style 'tree'.

    Arguments :
    - base_path : chemin racine où créer l'arborescence (ex: './output_project')
    - tree_text : texte contenant l'arborescence au format 'tree' (ex: projet, fichiers, dossiers)

    Fonctionnement :
    - La première ligne du texte correspond au dossier racine (ex: project-flask-sales/)
    - Les lignes suivantes représentent l'arborescence avec indentation et symboles ├── et └──
    - L'indentation détermine la profondeur dans l'arborescence (niveau)
    - Les dossiers finissent par '/' et fichiers sont sans '/'
    """
    # On découpe le texte en lignes individuelles, on enlève espaces inutiles en début/fin
    lines = tree_text.strip().splitlines()
    if not lines:
        # Si le texte est vide, on quitte la fonction, rien à faire
        return

    # --- 1. Traitement de la racine ---
    # La première ligne est le dossier racine à créer
    root_name = lines[0].strip()

    # On s'assure que le nom du dossier racine finit bien par '/' (indique un dossier)
    if not root_name.endswith('/'):
        root_name += '/'

    # On construit le chemin complet vers le dossier racine sous base_path
    root_path = os.path.join(base_path, root_name.rstrip('/'))

    # Création du dossier racine (avec tous les parents si besoin)
    os.makedirs(root_path, exist_ok=True)

    # --- 2. Initialisation de la pile (stack) ---
    # La pile va contenir des tuples (chemin_dossier, niveau_indent)
    # Permet de savoir à quel dossier parent rattacher le fichier/dossier courant
    # On commence par mettre le dossier racine avec niveau 0
    stack = [(root_path, 0)]

    # --- 3. Parcours des autres lignes ---
    # On traite toutes les lignes sauf la première (qui est la racine)
    for line in lines[1:]:
        # On ignore les lignes vides ou composées uniquement d'espaces
        if not line.strip():
            continue

        # --- 4. Calcul du niveau (profondeur) dans l'arborescence ---
        # Le niveau est déterminé par le nombre d'espaces au début de la ligne
        # Chaque indentation de 4 espaces correspond à un niveau
        indent = len(line) - len(line.lstrip(' '))
        level = indent // 4 + 1  # +1 car la racine est au niveau 0

        # --- 5. Extraction du nom fichier/dossier ---
        # On cherche le nom après les symboles ├── ou └──
        match = re.search(r'[├└]──\s*(.+)', line)
        if match:
            name = match.group(1).strip()
        else:
            # Au cas où le format est différent, on prend la ligne telle quelle
            name = line.strip()

        # --- 6. Recherche du parent ---
        # On doit remonter dans la pile tant que le dernier niveau est >= niveau courant
        # Cela permet de retrouver le bon parent pour ce fichier/dossier
        while stack and stack[-1][1] >= level:
            stack.pop()

        # Le parent est maintenant au sommet de la pile, sinon la racine
        parent_path = stack[-1][0] if stack else root_path

        # --- 7. Construction du chemin complet ---
        path = os.path.join(parent_path, name)

        # --- 8. Création fichier ou dossier ---
        if name.endswith('/'):
            # C'est un dossier : on le crée si besoin
            os.makedirs(path, exist_ok=True)
            # On ajoute ce dossier à la pile avec son niveau
            stack.append((path, level))
        else:
            # C'est un fichier : on crée un fichier vide
            # On s'assure que le dossier parent existe bien
            os.makedirs(parent_path, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                pass  # on crée le fichier sans contenu

def main():
    # --- Dossier racine où créer le projet ---
    base_dir = './output_project'

    # --- Nom du fichier .md contenant la structure de l'arborescence ---
    structure_file = 'structure.md'

    # --- Lecture du fichier .md ---
    try:
        with open(structure_file, 'r', encoding='utf-8') as f:
            skeleton = f.read()
    except FileNotFoundError:
        print(f"Erreur : le fichier '{structure_file}' est introuvable.")
        return

    # --- Appel de la fonction pour créer l'arborescence à partir du texte lu ---
    create_tree_from_text(base_dir, skeleton)

    print(f"Arborescence créée sous {base_dir}")

if __name__ == "__main__":
    main()
