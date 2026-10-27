<p align="center"><img src="https://dodysalim.github.io/assets/project-covers/m4.webp" alt="FinanceGuard" width="100%"></p>

<h1 align="center">FinanceGuard</h1>

<p align="center"><b>Models and business scenarios to anticipate bank-customer churn.</b></p>

<p align="center"><img src="https://img.shields.io/badge/Henry_·_Module_4_·_Capstone-75E6CE?style=for-the-badge&labelColor=0b1222" alt="Henry · Module 4 · Capstone"></p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="pandas"> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn"> <img src="https://img.shields.io/badge/XGBoost-1F6FEB?style=flat-square&logoColor=white" alt="XGBoost"> <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter"> <img src="https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logoColor=black" alt="Power BI">
</p>

<p align="center"><a href="https://dodysalim.github.io/"><b>🌐 Portfolio</b></a> · <a href="README.md"><b>🇪🇸 Versión en español</b></a></p>

---

## 📌 At a glance

| | |
| --- | --- |
| **🎯 Problem** | Compare churn models and pick a decision threshold that balances false positives and retention cost. |
| **🛠️ Solution** | Reusable `financeguard` package: data, features, model registry, evaluation and cost matrix. |
| **📈 Deliverables** | 4 notebooks, `train.py` CLI and a 3-page Power BI dashboard. |
| **💰 Business result** | Cost-based threshold (0.10) raises test-set net benefit from $58.4K to $111.7K under the stated cost assumptions. |
| **🗂️ Data** | Churn_Modelling: 10,000 customers. |

## 🏗️ Architecture

```mermaid
flowchart LR
    CSV[(Churn_Modelling.csv<br/>10.000 clientes)] --> DATA[data<br/>split estratificado]
    DATA --> FEAT[features<br/>escalado + one-hot]
    FEAT --> REG{models<br/>registro}
    REG --> LR[Logística]
    REG --> RF[Random Forest]
    REG --> XGB[XGBoost optimizado]
    LR --> EVAL[evaluation<br/>AUC · AP · F1]
    RF --> EVAL
    XGB --> EVAL
    XGB --> COST[costs<br/>umbral de negocio]
    EVAL --> CLI[train.py]
    COST --> CLI
    DATA --> NB[Notebooks 1-4]
    DATA --> PBI[Power BI]
```

## 🚀 How to run

```bash
pip install -r requirements.txt
python train.py
pip install pytest nbclient ipykernel && python -m pytest tests -q
```

## ⚖️ Scope

Retention ROI figures are scenarios under assumptions, not recovered revenue.

---

<p align="center">
<b>Dody Dueñas Remache</b> · Data Analyst / Data Scientist · Guayaquil, Ecuador (remote LATAM)<br>
<a href="https://dodysalim.github.io/">Portfolio</a> · <a href="https://github.com/dodysalim">GitHub</a> · <a href="https://www.linkedin.com/in/dody-duenas/">LinkedIn</a> · <a href="mailto:dodydurema67@gmail.com">dodydurema67@gmail.com</a>
</p>
