# 🧠 ✅ MODEL CARD — VERSION AMÉLIORÉE (VERSION DÉFINITIVE)

## 1. Objectif du modèle
**Cas d’usage visé**
Prédiction du risque de démission des employés (turnover prediction) afin d’aider les équipes RH à anticiper les départs et améliorer la rétention des talents.

**Entrées**
- *Données tabulaires RH* : Salary, EngagementSurvey, Absences, PerformanceScore.
- *Texte (NLP)* : Feedback employés.

**Sorties**
- Probabilité de démission (score croisé, entre 0 et 1).
- Classe : `0` = Reste, `1` = Quitte.
- Explications des facteurs de décision via **SHAP**.

---

## 2. Données d’entraînement
**Dataset(s) utilisés**
Human Resources Dataset (inspiré de Kaggle – Rich Huebner) fusionné avec des données de feedback textuel.

**Taille / diversité**
- Nombre total : ~400 employés.
- Répartition des classes : Classe 0 (reste) ≈ 70% | Classe 1 (quitte) ≈ 30%.
- Diversité contrôlée : Genre (Sex), Ethnie (RaceDesc), Départements, Variabilité salariale.

**Limites connues**
- *Dataset synthétique* : Les données peuvent ne pas parfaitement refléter la réalité complexe d'entreprise.
- *Déséquilibre* : Les données peuvent nécessiter un rééquilibrage de classe pour éviter l'overfitting.
- *Présence de variables sensibles* : Exclues de l'entraînement, mais le risque de biais par proxy existe et est testé.

---

## 3. Performances
**Métriques utilisées**
- Accuracy
- Precision / Recall
- F1-score
- ROC-AUC

**Résultats de référence**
- Accuracy globale : > 0.80
- F1-score : > 0.75

**Analyse par sous-groupes (Fairness Audit)**
| Groupe | Taux prédiction démission |
|---|---|
| Homme | ~21% |
| Femme | ~23% |
*➡ Pas de biais significatif détecté lors des tests (Écart de traitement < 5%).*

---

## 4. Limites
**Risques d’erreur connus**
- Mauvaise prédiction pour des profils hautement atypiques.
- Sensibilité aux valeurs extrêmes (outliers).
- Corrélations trompeuses (ex : le salaire n'est pas toujours la cause directe d'un départ).

**Situations non couvertes**
- Nouveaux employés sans historique suffisant.
- Données manquantes massives.
- Changements organisationnels radicaux, fusions, etc.

**Risques de biais**
- Genre, Ethnie, Salaire (qui peut parfois servir de proxy social indirect). 
- *Même si ces variables sensibles (Sex, RaceDesc) ne sont pas utilisées directement, des biais par proxy peuvent émerger.*

---

## 5. Risques & mitigation
**Risques de mauvaise utilisation**
- Prise de décisions RH automatiques ou punitives sans validation humaine.
- Discrimination indirecte.
- Surinterprétation des probabilités comme des certitudes absolues.

**Contrôles mis en place (SecureFair AI Governance)**
- **Validation humaine obligatoire** (Human-in-the-loop).
- **Explicabilité** grâce à SHAP (aucun score n'est émis sans son facteur explicatif).
- **Audit de biais constant** inspiré des métriques AIF360.
- Seuils d'alerte configurés : Ex: `Score > 0.7` génère une alerte consultative pour recommandation RH, aucune décision n'est déclenchée sans l'humain.

---

## 6. Énergie et Frugalité (Frugal AI)
**Modèle principal**
Random Forest Classifier (réglage équilibré, très léger comparé aux réseaux neuronaux).

**Empreinte énergétique**
- Poids du modèle : ~1–5 MB.
- Temps d’inférence : < 50 ms (sur simple CPU).
- Entraînement local : ~0.01 kWh.
- Émission CO₂ estimée : Très faible.
*➡ Système conforme à une approche d'IA Frugale, volontairement éloigné des LLM coûteux en ressources pour une simple tâche de classification tabulaire.*

---

## 7. Cybersécurité
**Sécurisation des entrées**
- Validation stricte des inputs via type checking et bornage des valeurs (salary, absences…).
- **Protection NLP** : Censure active et filtrage des requêtes contre le Prompt Injection. Exemple : les phrases contenant "Ignore system", "reveal" ou "password" sont systématiquement rejetées.

**Protection des données**
- **Anonymisation RGPD by Design** : Suppression irréversible de `Employee_Name`, `Email`, `DOB` avant la zone de traitement.
- Utilisation exclusive d'ID d'anonymisation.
- Isolation stricte des secrets (`.env`) sans divulgation dans le code.

**Attaques IA considérées**
- Model inversion : Quasi impossible sur une forêt aléatoire avec des données tabulaires synthétiques.
- Data leakage : Protégé nativement via l'isolation pré-traitement.

---

## 8. Conformité "EU AI Act" 🇪🇺
**Classification**
Ce système est classé dans la catégorie **High-Risk AI** (intelligence artificielle à haut risque) au titre du *EU AI Act*, puisqu'il touche aux :
* Décisions relatives à l'emploi (RH) et au recrutement.
* Impacts potentiels sur les parcours professionnels.

**Mesures obligatoires intégrées et respectées :**
1. **Transparence** : L'utilisation de SHAP justifie chaque décision de manière lisible pour l'humain.
2. **Audit de Biais** : Test régulier sur le traitement égalitaire (Audit panel du dashboard).
3. **Documentation Complète** : Fourniture de cette Data Card et de l'architecture.
4. **Supervision Humaine** (Human oversight constraint) respectée.
