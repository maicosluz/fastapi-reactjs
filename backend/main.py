from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI(title='Bcrud', version='0.1.0')


origins = [
    "*"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/")
async def root():
    return {"message": "Funciona o get!!!"}



if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:api', host='0.0.0.0', port=8701, reload=True)
