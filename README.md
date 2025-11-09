# ecommerce-sales-group
## Roller/ansvar i teamet: 
# Tobias: 
Funktioner:
AOV (Average Order Value);
Top-3 kategorier efter intäkt (eventuella avvikelser).
Visualiseringar:
Intäkt per stad.
README.md file,
 
# Ben:
Funktioner:
Total intäkt;
totalt antal enheter.
Visualiseringar:
intäkt per kategori (stapeldiagram).
README.md file
 
 
# Milda:
Funktioner:
Intäkt per kategori;
Intäkt per stad.
Visualiseringar:
försäljning över tid (linje/vecka eller månad).
README.md file.

## Projektbeskrivning
 
Detta projekt är en analys av försäljningsdata för en fiktiv e-handelsplattform.
Syftet är att ge ledningen ett snabbt beslutsunderlag inför nästa kampanjperiod.
 
Analysen är gjord i en Jupyter Notebook och visar nyckeltal, figurer och rekommendationer baserat på datasetet ecommerce_sales.csv.

## I notebooken analyseras bland annat:
 
Total intäkt och antal enheter
AOV (Average Order Value)
Intäkt per kategori och per stad
Försäljning över tid (månadsvis)
Top-3 kategorier efter intäkt
 
Visualiseringar:
Intäkt per stad
Intäkt per kategori (stapeldiagram)
Försäljning över tid (linje/vecka eller månad).

## Miljö
- **Python:** 3.13.7
- **Paket:** `Pandas`, `matplotlib` (se `requirements.txt`)
 
## Hur kör
 
```bash
# klona projetet
git clone https://github.com/LillaLaila/ecommerce-sales-group.git
cd ecommerce-sales-group
 
# Skapa och aktivera virtuell miljö
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate
# bash
source .venv/Scripts/activate
 
# installera beroenden
python -m pip install -r requirements.txt
```