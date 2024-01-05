from fastapi import FastAPI

app = FastAPI()

# Health check route
@app.get('/health')
def health_check():
    return {"status": "ok"}
    
# Home route
@app.get('/')
def home():
    return {"message": "Hello World!"}