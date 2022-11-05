# [START gae_python38_app]
# [START gae_python3_app]

from flask import Flask
import pandas as pd

app = Flask(__name__)
    
@app.route('/')
def get_recommendations(item='PARTY BUNTING'):
    #df_items = pd.read_pickle('items.pkl')
    #recommendations = df_items.corrwith(df_items[item])
    #recommendations.dropna(inplace=True)
    #recommendations = pd.DataFrame(recommendations, columns=['correlation']).reset_index()
    #recommendations = recommendations.sort_values(by='correlation', ascending=False)
    #return recommendations.head(10).to_dict()
    return {'Description': {1231: 'PARTY BUNTING',
        1428: 'RED RETROSPOT PURSE ',
        1402: 'RED GINGHAM TEDDY BEAR ',
        159: 'BASKET OF TOADSTOOLS',
        544: 'DINOSAUR KEYRINGS ASSORTED',
        384: 'CHERRY BLOSSOM  DECORATIVE FLASK',
        1317: 'PINK PAINTED KASHMIRI CHAIR',
        1112: 'MORE BUTTER METAL SIGN ',
        1227: 'PAPERWEIGHT CHILDHOOD MEMORIES',
        368: 'CERAMIC STRAWBERRY TRINKET TRAY'},
        'correlation': {1231: 0.9999999999999999,
        1428: 0.6616590076604353,
        1402: 0.6321359265315367,
        159: 0.6297343962563305,
        544: 0.6281913997082801,
        384: 0.6048176702070914,
        1317: 0.601053517859109,
        1112: 0.6010535178591088,
        1227: 0.6010535178591087,
        368: 0.6010535178591087}}
        
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

# [END gae_python3_app]
# [END gae_python38_app]
