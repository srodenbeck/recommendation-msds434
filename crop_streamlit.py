import predict
from google.cloud import aiplatform


probs = predict.predict_custom_trained_model_sample(
    project="554698915331",
    endpoint_id="6625397584234020864",
    location="us-central1",
    #instance_dict={ "instance_key_1": "value", ...}
    instances={"instances":[[70,38,35,24.3,79,7,164.3]]}
)
print(probs)