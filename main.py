from core.scanner import calculer_hash, scanner_dossier
from core.analyzer import charger_base_signatures, verifier_menace
from core.utils import effacer_ecran, afficher_logo, enregistrer_log
import os

def lancer_antivirus():
    # 1. Préparation
    effacer_ecran()
    afficher_logo()
    
    # Charger la base de données
    base_virus = charger_base_signatures()
    
    # 2. Entrée utilisateur
    chemin = input("📂 Dossier à scanner (ex: /sdcard/Download) : ")
    
    if not os.path.exists(chemin):
        print("❌ Erreur : Chemin introuvable.")
        return

    # 3. Analyse
    print(f"\n🔍 Analyse de {chemin} en cours...")
    fichiers = scanner_dossier(chemin)
    menaces_trouvees = 0

    for f in fichiers:
        hash_f = calculer_hash(f)
        if hash_f:
            resultat = verifier_menace(hash_f, base_virus)
            
            if resultat:
                msg = f"⚠️ ALERTE : {resultat} détecté dans {f}"
                print(msg)
                enregistrer_log(msg)
                menaces_trouvees += 1
    
    # 4. Résumé
    print("\n" + "="*30)
    print(f"✅ Scan terminé.")
    print(f"📊 Fichiers analysés : {len(fichiers)}")
    print(f"🚨 Menaces trouvées : {menaces_trouvees}")
    print("="*30)
    
    enregistrer_log(f"Scan terminé sur {chemin}. Menaces : {menaces_trouvees}")

if __name__ == "__main__":
    lancer_antivirus()
