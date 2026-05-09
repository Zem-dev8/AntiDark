import hashlib
import os

def calculer_hash(chemin_fichier):
    """Calcule le hash SHA-256 d'un fichier pour l'identifier."""
    hash_sha256 = hashlib.sha256()
    try:
        with open(chemin_fichier, "rb") as f:
            # On lit le fichier par petits morceaux (4096 octets) 
            # pour ne pas faire ramer ton Samsung A06
            for morceau in iter(lambda: f.read(4096), b""):
                hash_sha256.update(morceau)
        return hash_sha256.hexdigest()
    except Exception as e:
        return None

def scanner_dossier(chemin_dossier):
    """Liste tous les fichiers d'un dossier pour les analyser."""
    fichiers_a_scanner = []
    for racine, dossiers, fichiers in os.walk(chemin_dossier):
        for nom in fichiers:
            chemin_complet = os.path.join(racine, nom)
            fichiers_a_scanner.append(chemin_complet)
    return fichiers_a_scanner
