from fastapi import FastAPI

app = FastAPI(
    title="AP3 Backend",
    version="1.0.0",
    description="Backend API for AP3"
)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "AP3 Backend is Running 🚀"
    }