# Documentación anterior

Archivo histórico conservado para mantener contexto y atribución. Sus cifras, enlaces y afirmaciones no sustituyen el estado de validación del README actual. Los enlaces relativos se interpretaban desde la raíz del repositorio.

# Predicción de Fuga de Clientes Bancarios (Churn) 🏦

Proyecto de Machine Learning de punta a punta: análisis exploratorio, modelos de clasificación, segmentación de clientes y **optimización del umbral de decisión según costos reales del negocio**.

> Proyecto Integrador del Módulo 4 (Machine Learning) de la carrera de Data Science en **Henry**.

![Python](https://img.shields.io/badge/Python-3.11-blue) ![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8-orange) ![XGBoost](https://img.shields.io/badge/XGBoost-3.1-green) ![CatBoost](https://img.shields.io/badge/CatBoost-1.2-yellow) ![LightGBM](https://img.shields.io/badge/LightGBM-4.6-lightgrey)

---

## 🎯 Problema de negocio

Un banco digital (caso ficticio: *FinanceGuard*) pierde al **20.4%** de sus clientes. Retener a un cliente es mucho más barato que conseguir uno nuevo, así que el banco necesita:

1. **Predecir** qué clientes tienen mayor riesgo de irse.
2. **Entender** qué tipos de clientes existen y por qué se van.
3. **Decidir** a quién contactar para maximizar la ganancia, no solo la precisión del modelo.

**Dataset:** [Bank Customer Churn](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling): 10,000 clientes y 10 variables (edad, país, saldo, productos, actividad, etc.).

---

## 📊 Resultados principales

### 1. Los modelos de árboles superan al baseline

![Comparación de modelos](images/readme_model_comparison.png)

| Modelo | ROC-AUC | F1 (churn) | Recall (churn) |
|---|---|---|---|
| Regresión Logística (baseline) | 0.777 | 0.50 | 0.70 |
| XGBoost optimizado (GridSearchCV) | 0.855 | 0.62 | 0.70 |
| Stacking (RF + XGB + LGBM + CatBoost) | **0.870** | 0.60 | 0.77 |
| **CatBoost** | 0.868 | **0.62** | 0.75 |

*Métricas en el set de prueba (2,000 clientes, 20% estratificado) con umbral 0.5.*

**Conclusión:** los modelos de boosting suben el AUC de 0.78 a ~0.87. Las diferencias entre ellos son pequeñas (±0.02), así que el Stacking **no justifica su complejidad extra** frente a CatBoost.

### 2. Qué impulsa la fuga de clientes (Regresión Logística, Odds Ratios)

| Factor | Efecto en el riesgo de fuga |
|---|---|
| 🇩🇪 Vivir en **Alemania** | **×2.3** (32% de churn vs. 16% en Francia y España) |
| 📈 **Edad** (+10 años aprox.) | **×2.1**. El grupo de 50–60 años tiene un 56% de churn |
| 💤 Ser **miembro activo** | **−40%** |
| 👤 Ser **hombre** | −41% (16.5% vs. 25.1% en mujeres) |
| 📦 **3 o 4 productos** | 83–100% de churn (relación **no lineal**: 2 productos = solo 7.6%) |

### 3. Segmentación de clientes (K-Means, K = 4)

| Segmento | Clientes | Churn |
|---|---|---|
| **Inactivos con saldo alto** ⚠️ | 2,436 | **32%** |
| Sin tarjeta de crédito | 2,899 | 20% |
| Activos con saldo alto | 2,482 | 16% |
| Saldo casi cero, multiproducto | 2,183 | 13% |

**Insight:** a igual saldo, **los clientes inactivos tienen el doble de churn** que los activos. Las campañas de **reactivación** son la palanca principal.

*Nota honesta:* la silueta es baja (~0.11), así que los grupos no están naturalmente separados. Es una segmentación útil para negocio, no una estructura "real" de los datos.

### 4. Optimización financiera del umbral 💰

Supuestos: perder a un cliente cuesta **$500** y una campaña de retención cuesta **$50**.

| | Umbral 0.5 (por defecto) | Umbral óptimo 0.08 |
|---|---|---|
| Clientes que se iban y fueron detectados | 285 / 407 (70%) | 393 / 407 (97%) |
| Falsas alarmas | 234 | 1,194 |
| **Beneficio neto (set de prueba)** | **$55,550** | **$110,150** |

<img src="images/4_Extra_credit_c10_0.png" width="600">

- El umbral se eligió con **validación cruzada sobre los datos de entrenamiento** y se evaluó una sola vez en el set de prueba (sin data leakage).
- Un umbral tan bajo tiene sentido porque una falsa alarma ($50) es 10 veces más barata que perder un cliente ($500).
- **Limitación:** se asume que todo cliente contactado se retiene, así que la cifra es un límite superior. En un caso real habría que validar la tasa de éxito con un A/B test.

---

## 🛠️ Metodología

```
data/ ──► 1. EDA + Regresión Logística ──► 2. Boosting + GridSearch + Stacking
                                                       │
          3. PCA + t-SNE + K-Means + DBSCAN ◄──────────┘
                                                       │
          4. Optimización del umbral por costos ◄──────┘
```

| Notebook | Contenido |
|---|---|
| [`1_EDA_RegresionLogistica`](notebooks/1_EDA_RegresionLogistica.ipynb) | EDA, VIF, Regresión Logística (scikit-learn + statsmodels), Odds Ratios, ROC, Precision-Recall y calibración |
| [`2_GradientBoosting_Optimizacion`](notebooks/2_GradientBoosting_Optimizacion.ipynb) | Random Forest, XGBoost, LightGBM, CatBoost, GridSearchCV (720 fits) y Stacking |
| [`3_AprendizajeNoSupervisado`](notebooks/3_AprendizajeNoSupervisado.ipynb) | PCA, t-SNE, método del codo, silueta, K-Means, DBSCAN y perfilado de segmentos |
| [`4_Extra_credit`](notebooks/4_Extra_credit.ipynb) | Matriz de costos, curva de beneficio y umbral óptimo con validación cruzada |

**Buenas prácticas aplicadas:**
- Split estratificado 80/20 y `ColumnTransformer` (StandardScaler + OneHotEncoder).
- Manejo del desbalance con `class_weight='balanced'` y `scale_pos_weight`.
- Sin data leakage: el set de prueba no se usa para early stopping ni para elegir el umbral.
- Métricas apropiadas para clases desbalanceadas: Recall, F1, ROC-AUC y Average Precision.

---

## 🚀 Cómo ejecutarlo

```bash
git clone https://github.com/dodysalim/churn-prediction-financeguard.git
cd churn-prediction-financeguard
pip install -r requirements.txt
jupyter lab
```

Ejecuta los notebooks en orden (1 → 4) desde la carpeta `notebooks/`.

## 📁 Estructura

```
├── data/Churn_Modelling.csv
├── notebooks/        # 4 notebooks ejecutados con resultados
├── images/           # Gráficas exportadas
├── requirements.txt
└── README.md
```

## 🔮 Próximos pasos

- Explicabilidad por cliente con **SHAP**.
- Recalibrar probabilidades (`CalibratedClassifierCV`).
- Desplegar el modelo como API (**FastAPI**) o dashboard (**Streamlit**).

---

## 🇺🇸 English summary

End-to-end churn prediction project on 10,000 bank customers. Gradient boosting models (CatBoost, XGBoost, Stacking) raised ROC-AUC from 0.78 (logistic regression baseline) to ~0.87. K-Means segmentation found that inactive high-balance customers churn at 32% (vs. 20% average). A cost-based decision threshold (0.08, selected via cross-validation on training data) doubled the estimated net benefit on the test set, from $55,550 to $110,150, compared with the default 0.5 threshold.

---

## 👤 Autor

**Dody Dueñas Remache**: Data Analyst / Data Scientist Jr. · Ecuador 🇪🇨

[LinkedIn](https://www.linkedin.com/in/dody-duenas/) · [Portafolio](https://dodysalim.github.io/) · [GitHub](https://github.com/dodysalim) · [dodydurema67@gmail.com](mailto:dodydurema67@gmail.com)
