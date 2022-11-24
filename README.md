# Crop Recommendation Model on GCP

To run locally, simply run "streamlit run crop_streamlit.py".  

GCP deployments will automatically rebuild upon code being pushed to the respective branch (main for prod; crop-dev for dev).

### Selected Resources and Tutorials used throughout 434
* App Engine: https://cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service
* BigQuery ML: https://cloud.google.com/bigquery-ml/docs/logistic-regression-prediction
* Vertex AI: https://cloud.google.com/vertex-ai/docs/tutorials/text-classification-automl
* Cloud Run with Continuous Deployment: https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build
* Billing Export to BigQuery: https://cloud.google.com/billing/docs/how-to/export-data-bigquery
* Exporting BigQuery ML Models: https://cloud.google.com/bigquery-ml/docs/export-model-tutorial
* Monitoring: https://cloud.google.com/monitoring/monitor-compute-engine-virtual-machine
