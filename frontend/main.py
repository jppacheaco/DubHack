from fastapi import FastAPI
import driver

app = FastAPI()


@app.get("/")
async def root():
    return driver.makeconnections()
