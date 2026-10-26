from build_powerbi import *
from build_powerbi import PROJECT_ROOT
import sys, ast, numpy as np
from sklearn.model_selection import train_test_split
from scipy.stats import ks_2samp, chi2_contingency

def finance():
 repo='churn-prediction-financeguard';r=Report(repo,'FinanceGuard','10.000 clientes · dataset Churn_Modelling · análisis de abandono observado, sin predicciones inventadas')
 d=pd.read_csv(PROJECT_ROOT/'data/Churn_Modelling.csv');d=d.drop(columns=['RowNumber','CustomerId','Surname']);d['GrupoEdad']=pd.cut(d.Age,[0,25,35,45,55,120],labels=['Hasta25','26-35','36-45','46-55','56+']).astype(str)
 r.table('Clientes',d,metrics('Clientes',[('Clientes','COUNTROWS(Clientes)'),('Abandonos','SUM(Clientes[Exited])'),('TasaChurn','DIVIDE(SUM(Clientes[Exited]), COUNTROWS(Clientes))'),('Saldo','SUM(Clientes[Balance])'),('Salario','AVERAGE(Clientes[EstimatedSalary])')]))
 for page,label,c1,c2 in [('resumen','01 · Resumen ejecutivo','Geography','Gender'),('riesgo','02 · Perfil de abandono','GrupoEdad','NumOfProducts'),('valor','03 · Valor y vinculación','Tenure','IsActiveMember')]:
  r.page(page,label,[('Clientes','Geography'),('Clientes','Gender'),('Clientes','Exited')]);r.cards('Clientes',['KPI_Clientes','KPI_Abandonos','KPI_TasaChurn','KPI_Saldo']);r.chart('Clientes',c1,'KPI_TasaChurn','Tasa de abandono · '+c1,30,270);r.chart('Clientes',c2,'KPI_TasaChurn','Tasa de abandono · '+c2,650,270);r.tablevisual('Clientes',[c1,c2,'KPI_Clientes','KPI_Abandonos','KPI_TasaChurn','KPI_Saldo'],'Diagnóstico por segmento',30,570,1220,260)
 return r.finish('El repositorio contiene notebooks, no una app Streamlit. Las páginas reflejan EDA: geografía/género, edad/productos, vinculación y saldo. `Exited` es la etiqueta observada. Las métricas de evaluación de modelos siguen en los notebooks, no se mezclan con la tasa de abandono.')
if __name__=='__main__':
    print(finance())
