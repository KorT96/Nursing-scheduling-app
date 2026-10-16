from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse("index.html")

@app.get("/index.html", response_class=FileResponse)
async def allocated_page():
    return FileResponse("index.html")

app.mount("/assets", StaticFiles(directory="assets"), name="static")

@app.get("/result.html", response_class=FileResponse)
async def result_page():
    return FileResponse("result.html")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host = "127.0.0.1", port = 8000, reload = True)