from image_segmentation.pipeline.target_prediction import TargetPredictionPipeline
import sys
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from image_segmentation.config_manager import ConfigManager
from image_segmentation.exception import CustomException
from image_segmentation.logging import logger


config = ConfigManager()
prediction_pipeline = TargetPredictionPipeline(config)

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index(request: Request):
    return "Hello world"

@app.post("/predict")
async def predict(data: dict):
    try:
        text = data["input"]
        logger.info("PREDICTION STARTED")
        output = prediction_pipeline.run(text)
        logger.info("PREDICTION FINISHED")

        return {"output": output}
    except Exception as e:
        error_message = str(CustomException(e, sys))
        return {"output": error_message}
        # raise CustomException(e, sys) from e
    

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)

    
    