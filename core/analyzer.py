import json

def charger_base_signatures(chemin_db="database/signatures.json"):
    """Charge les signatures depuis le fichier JSON."""
    try:
        with open(chemin_db, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ Base de données introuvable, création d'une base vide.")
        return {}

def verifier_menace(hash_fichier, base_signatures):
    """Vérifie si un hash est présent dans la base de données."""
    if hash_fichier in base_signatures:
        return base_signatures[hash_fichier]  # Retourne le nom du virus
    return None
