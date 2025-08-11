from fastapi import FastAPI

app = FastAPI(title='Flight Advisor API')

@app.get('/health')
def health():
    return {'status': 'ok'}
