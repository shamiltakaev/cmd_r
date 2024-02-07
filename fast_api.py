from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root(a: int, b: int):
    return {"result": [a * b, a + b], 
            "check": "jasodfpjpoasdfjp123123klj12nj312"}