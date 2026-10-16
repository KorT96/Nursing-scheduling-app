from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class ShiftBreakdown(BaseModel):
    gen: int
    x2: int
    x4: int
    x6: int
    wesx1: int
    wesx2: int
    wesx4: int

class ShiftRequest(BaseModel):
    staff: int
    shift: str ="Morning"
    beds: int
    breakdown: ShiftBreakdown


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers={"*"},
)

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

@app.post("/api/allocate")
def allocated_shift(data: ShiftRequest):
    print("Recieved shift allocation payload:", data)
    return{
        "status": "Success",
        "message": "Data succesfully received at the backend engine",
        "received_data": data
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host = "127.0.0.1", port = 8000, reload = True)