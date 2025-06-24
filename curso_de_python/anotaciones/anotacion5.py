# las anotaciones de tipo son una forma de documentar el tipo de datos que se espera en los parámetros y el tipo de dato que se devuelve.
from typing import Union 

def process_salary(salary: Union[int, float]) -> float: #esta anotacion dice que el parametro salary puede ser un entero o un flotante
                                                        # y que la funcion devuelve un flotante.
    """
    Procesa un salario que puede ser entero o flotante y lo devuelve como flotante.

    Parámetros:
    salary (Union[int, float]): Un salario que puede ser un entero o flotante.

    Retorna:
    float: El salario convertido a flotante.
    """
    return float(salary)