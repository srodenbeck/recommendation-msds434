# [START gae_python38_app]
# [START gae_python3_app]

from flask import Flask
import pandas as pd

app = Flask(__name__)
    
@app.route('/')
def get_recommendations(item='PARTY BUNTING'):
    df_items = pd.read_pickle('items.pkl')
    recommendations = df_items.corrwith(df_items[item])
    recommendations.dropna(inplace=True)
    recommendations = pd.DataFrame(recommendations, columns=['correlation']).reset_index()
    recommendations = recommendations.sort_values(by='correlation', ascending=False)
    return recommendations.head(10).to_dict()

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

# [END gae_python3_app]
# [END gae_python38_app]
