# arbo CODE Generator


# Générateur d'Arborescence de Projet à partir d'un fichier Markdown

## Présentation

Ce projet fournit un script Python permettant de **générer automatiquement une arborescence de fichiers et dossiers** à partir d’un fichier `.md` contenant la structure sous forme texte, au format style `tree` (avec des symboles `├──`, `└──` et des indentations).

L'objectif est d'automatiser la création rapide d'une structure de projet à partir d'un squelette textuel, pour faciliter les phases d'initialisation ou de prototypage.

---

## Fonctionnalités principales

- Lecture d’un fichier `.md` contenant l’arborescence
- Analyse et interprétation de la structure avec indentation et symboles
- Création des dossiers et fichiers vides correspondants dans un dossier de sortie
- Gestion des dossiers racine, sous-dossiers, et fichiers
- Gestion automatique des dossiers parents manquants
- Messages d’erreur clairs (ex : fichier `.md` introuvable)

---

## Utilisation

1. Préparez un fichier texte `structure.md` avec votre arborescence au format `tree`. Exemple :

    ```
    project-flask-sales/
    ├── app.py
    ├── requirements.txt
    └── templates/
        ├── base.html
        ├── index.html
        └── resultats.html
    ```

2. Placez ce fichier `structure.md` dans le même dossier que le script Python.

3. Lancez le script Python :

    ```bash
    python create_structure.py
    ```

4. L’arborescence sera créée sous le dossier `./output_project`.

---

## Détails techniques

- Le script utilise la fonction `create_tree_from_text(base_path, tree_text)` qui parse la chaîne de caractères pour :
  - Identifier le dossier racine
  - Calculer les niveaux d'indentation
  - Créer récursivement dossiers et fichiers
- Le format attendu respecte les conventions des arbres générés par la commande Linux `tree`.
- Le script est robuste face aux erreurs courantes (fichier absent, lignes vides, mauvaise indentation).

---

## Backlog réalisé

- [x] Lecture d’un fichier `.md` contenant la structure
- [x] Parsing des symboles `├──`, `└──` et indentation en espaces multiples de 4
- [x] Création du dossier racine
- [x] Création des sous-dossiers et fichiers (vides)
- [x] Gestion d’une pile pour suivre les parents et niveaux
- [x] Messages d’erreur pour fichier `.md` manquant
- [x] Commentaires détaillés dans le code source
- [x] Fonctionnement en Python standard sans dépendances externes

---

## Prochaines versions / améliorations à venir

- [ ] Ajouter une option pour remplir les fichiers créés avec un contenu par défaut (ex : template HTML, script Python minimal)
- [ ] Supporter des niveaux d'indentation flexibles (tabs et multiples d'espaces autres que 4)
- [ ] Ajouter une interface en ligne de commande (CLI) avec options pour :
    - Spécifier le fichier d’entrée `.md`
    - Choisir le dossier de sortie
    - Afficher l’arborescence sans création (mode simulation)
- [ ] Gérer les fichiers binaires (ex : copier depuis un dossier source)
- [ ] Validation syntaxique plus stricte du fichier `.md` pour détecter erreurs de structure
- [ ] Supporter d’autres formats d’entrée (ex : JSON, YAML)
- [ ] Intégrer la création dans un outil plus large de scaffolding de projets
- [ ] Ajouter des tests unitaires pour chaque fonction
- [ ] Permettre la suppression/réinitialisation de l’arborescence avant création
- [ ] Générer un log détaillé des opérations effectuées

---

## Licence

Ce projet est sous licence MIT.

---

## Contact

Pour toute question ou suggestion, merci d’ouvrir un ticket sur le dépôt GitHub ou de me contacter directement.

---


