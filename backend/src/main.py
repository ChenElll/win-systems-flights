from fastapi import FastAPI

app = FastAPI(title='FlySmart API (AirIsrael)')

@app.get('/health')
def health():
    return {
        'status': 'ok',
        'app': 'FlySmart',
        'brand': 'FlySmart by AirIsrael',
        'assistant': 'Wingman AI',
        'airline': 'AirIsrael',
    }
