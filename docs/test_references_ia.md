# Activité 2 : la chasse aux références inventées. Bilan

- **Date :** 12/11/2026
- **Assistant testé :** Claude (Anthropic)
- **Consigne :** 5 références récentes sur les antennes RFID pour la santé (implantables et ingérables), sans recherche web
- **Outils de vérification :** PubMed, Google Scholar, archives ouvertes (HAL, IRIS Unipa, ART Tor Vergata), doi.org

| # | Référence proposée par l'IA | Vérification | Classement |
|---|---|---|---|
| 1 | Kiourti & Nikita, IEEE TBME, 64(7):1422-1430, 2017 | Titre, auteurs, revue, volume et pages confirmés par PubMed (PMID 28212074, DOI 10.1109/TBME.2017.2668612) | **Exacte** |
| 2 | Das & Yoo, *IEEE Trans. Microwave Theory Tech.*, 65(6):2816-2826, 2017 | L'article existe, mais il est paru dans **IEEE Trans. Antennas and Propagation** (DOI 10.1109/TAP.2017.2694700), pas dans T-MTT | **Partiellement fausse** (mauvaise revue) |
| 3 | Nikolayev et al., IEEE TAP, 65(11):6107-6119, 2017 | Confirmée par HAL (hal-01684558, DOI 10.1109/TAP.2017.2755764) | **Exacte** |
| 4 | Occhiuzzi, Contri & Marrocco, IEEE TAP, 60(7):3146-3154, 2012 | Confirmée (DOI 10.1109/TAP.2012.2198189) | **Exacte** (mais pas « récente ») |
| 5 | Marrocco, IEEE Antennas Propag. Mag., 50(1):66-79, 2008 | Confirmée (DOI 10.1109/MAP.2008.4494504) | **Exacte** (2008 : ne respecte pas la consigne « récente », et c'est un tutoriel général, pas une étude santé) |

**Résultat : 4 exactes, 1 partiellement fausse, 0 inventée.**

## Observations

- L'erreur porte sur un détail plausible : le nom de la revue. C'est le piège le plus dangereux, car le titre et les auteurs exacts donnent une fausse impression de fiabilité.
- L'IA n'a pas respecté la consigne « récentes » : 2 références sur 5 datent de 2012 et 2008. Elle propose surtout des articles très cités et anciens, et ignore la littérature 2023-2026.
- Aucune DOI n'était fournie. Chaque référence a dû être retrouvée à la main.
- Les références exactes ont été ouvertes. Leur sujet correspond bien au titre, mais l'IA ne donnait aucune affirmation sur leur contenu, donc aucune affirmation n'a pu être contrôlée.
