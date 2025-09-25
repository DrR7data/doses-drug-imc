from fastapi import FastAPI
import uvicorn
from fastapi import HTTPException

app = FastAPI()


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello Alice"}


@app.get("/calc_dosis/pesos/dosis/")
async def calc_dosis(peso: int, dosis: int, pres_ml: int, interval: int):
    """Esta es una funcion para calcular dosis pediatrica.
    Espero que sea de mucha ayuda.
    """

    dosis_calc = (peso * dosis / pres_ml) / interval

    return f"Dosis = {dosis_calc} ml Peso multiplicado por dosis en mg dividido de acuerdo a la presentación en mg/ml del medicamentos y calculado por número de dosis durante el día"

@app.get("/calcc_dosis/pesos/dosis/")
async def calcc_dosis(peso: int, dosis: int, pres_ml: int, interval: int):
    """Esta es una funcion para calcular dosis pediatrica."""

    # Validaciones
    if peso <= 0 or dosis <= 0 or pres_ml <= 0 or interval <= 0:
        raise HTTPException(
            status_code=400, 
            detail="Todos los parámetros deben ser mayores a cero"
        )

    try:
        dosis_calc = (peso * dosis / pres_ml) / interval
        return {"dosis_calculada": dosis_calc}
    except  ZeroDivisionError:
        raise HTTPException(
            status_code=400, 
            detail="Error en cálculo: división por cero"
        )
if __name__ == "__main__":

    print("I was here")
    uvicorn.run(app, port=8000, host="0.0.0.0")