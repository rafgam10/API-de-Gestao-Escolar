from fastapi import FastAPI


app = FastAPI(title="API de Gestão Escoler", version="1.0")


@app.get("/")
async def root():
    return {"message": "Olá mundo"} 