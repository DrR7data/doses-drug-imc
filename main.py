from fastapi import FastAPI
import uvicorn
from fastapi import HTTPException

app = FastAPI()


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello Alice"}


@app.get("/calc_dosis/pesos/dosis/")
async def calc_dosis(peso: float, dosis: float, pres_ml: float, interval: int):
    """Esta es una funcion para calcular dosis pediatrica.
    Espero que sea de mucha ayuda.
    """

    dosis_calc = (peso * dosis / pres_ml) / interval

    return f"Dosis = {dosis_calc} ml Peso multiplicado por dosis en mg dividido de acuerdo a la presentación en mg/ml del medicamentos y calculado por número de dosis durante el día"


@app.get("/calcc_dosis/pesos/dosis/")
async def calcc_dosis(peso: float, dosis: float, pres_ml: float, interval: int):
    """Esta es una funcion para calcular dosis pediatrica."""

    if peso <= 0 or dosis <= 0 or pres_ml <= 0 or interval <= 0:
        raise HTTPException(
            status_code=400, detail="Todos los parámetros deben ser mayores a cero"
        )

    try:
        dosis_calc = (peso * dosis / pres_ml) / interval
        return {"dosis_calculada": dosis_calc}
    except ZeroDivisionError as exc:
        # Corregido: usando 'from exc' para preservar el traceback
        raise HTTPException(
            status_code=400, detail="Error en cálculo: división por cero"
        ) from exc


if __name__ == "__main__":

    print("Running!")
    uvicorn.run(app, port=8000, host="0.0.0.0")
