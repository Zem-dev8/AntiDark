import os
import datetime

def effacer_ecran():
    """Nettoie le terminal pour un affichage propre."""
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_logo():
    """Affiche un titre stylé au démarrage."""
    print("="*30)
    print("🛡️  MOBILE SHIELD ANTIVIRUS")
    print("="*30)

def enregistrer_log(message, chemin_log="logs/scan_reports.txt"):
    """Enregistre les événements importants avec l'heure."""
    horodatage = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(chemin_log, "a") as f:
        f.write(f"[{horodatage}] {message}\n")
