from fastapi import APIRouter
import pickle
import numpy as np
import random

router = APIRouter()

model = pickle.load(open('model.pkl', 'rb'))

@router.post('/predict')
async def predict():
    int_features =  [int(x) for x in random.sample(range(1, 30), 3)]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    print("sucesss result : " )
    print(output)
    print(model);
    return {"output":output}

@router.post('/alive')
async def predict():
    return "ok"