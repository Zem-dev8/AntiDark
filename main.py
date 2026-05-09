from core.scanner import calculer_hash, scanner_dossier
import json
import os

def charger_signatures():
    # On simule une base de données de virus (Hash SHA-256)
    # Dans le futur, tu mettras ça dans database/signatures.json
    signatures_virus = {
        "e99a18c428cb38d5f260853678922e03": "Trojan.Exemple",
        "5e884898da28047151d0e56f8dc62927": "Malware.Test"
    }
    return signatures_virus

def lancer_antivirus():
    print("--- 🛡️  MON ANTIVIRUS MOBILE ---")
    
    chemin = input("Entrez le chemin du dossier à scanner (ex: /sdcard/Download) : ")
    
    if not os.path.exists(chemin):
        print("❌ Erreur : Le dossier n'existe pas.")
        return

    print(f"🔍 Analyse en cours dans : {chemin}...")
    
    base_virus = charger_signatures()
    fichiers = scanner_dossier(chemin)
    menaces_trouvees = 0

    for f in fichiers:
        hash_f = calculer_hash(f)
        if hash_f in base_virus:
            print(f"⚠️  ALERTE : {base_virus[hash_f]} détecté dans {f} !")
            menaces_trouvees += 1
        else:
            # Optionnel : afficher les fichiers sains
            # print(f"✅ {f} est sain.")
            pass

    print("\n--- 🏁 Scan terminé ---")
    print(f"Fichiers analysés : {len(fichiers)}")
    print(f"Menaces détectées : {menaces_trouvees}")

if __name__ == "__main__":
    lancer_antivirus()
