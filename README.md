# Antennes RFID pour la santé : dispositifs portables, implantables et ingérables

Dépôt de travail de la thèse de doctorat de **Nabil Belli** (laboratoire IDS, Université Abdelmaâlek Essaâdi, Tétouan).
ORCID : [0009-0005-2200-0583](https://orcid.org/0009-0005-2200-0583) · Encadrant : Pr. Otman El Morabet.
Bibliothèque Zotero publique : https://www.zotero.org/groups/6759663/these_rfid_sante

## Objet

Conception, simulation et caractérisation d'antennes UHF RFID passives pour des applications médicales sur et dans le corps humain. Le cas d'étude principal est une **antenne conforme à 868 MHz pour capsule ingérable**, adaptée à l'impédance de la puce EM4325 en mode passif. Ce travail s'accompagne d'une **revue systématique (PRISMA)** des dispositifs RFID portables, implantables et ingérables publiés entre 2010 et 2026.

## Arborescence

```
these-rfid-sante/
├── README.md            ce fichier
├── LICENSE              licences : code MIT, documents et données CC BY 4.0
├── CITATION.cff         comment citer ce dépôt
├── .gitignore           fichiers exclus (résultats lourds de simulation, caches)
├── biblio/              bibliothèque Zotero exportée (.bib)
├── docs/                plan de gestion des données, charte IA, notes
├── simulations/
│   ├── cst/             projets CST Studio Suite 2025 (.cst)
│   └── hfss/            projets Ansys HFSS 2024 R1 (.aedt)
├── mesures/
│   ├── brutes/          fichiers VNA bruts (.s1p, .s2p), jamais modifiés
│   └── traitees/        données nettoyées (.csv) et métadonnées
├── scripts/             scripts Python de post-traitement
└── figures/             figures générées par les scripts
```

## Utilisation

```bash
git clone https://github.com/nabilbelli-crypto/these-rfid-sante.git
cd these-rfid-sante
python -m pip install numpy matplotlib
python scripts/coef_transmission.py --za 3.8+139j --zc 23.3-145j
```

`scripts/coef_transmission.py` calcule le coefficient de transmission de puissance τ entre l'antenne (Za) et la puce RFID (Zc) :
τ = 4·Ra·Rc / |Za + Zc|².

## Conventions

- Les noms de fichiers suivent le format `AAAA-MM-JJ_objet_version` (exemple : `2026-11-02_capsule-868_v3.cst`).
- Les données brutes ne sont jamais modifiées. Tout traitement produit un nouveau fichier dans `mesures/traitees/`.
- Les fichiers de résultats lourds (`*_Results/`, `*.aedtresults/`) ne sont pas versionnés : ils sont archivés sur Zenodo.

## Licence

- Code (`scripts/`) : licence MIT
- Documents, figures et données : licence CC BY 4.0

Voir le fichier [LICENSE](LICENSE).
