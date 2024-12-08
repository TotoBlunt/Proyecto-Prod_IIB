from supabase_connector import crear_cliente

client = crear_cliente()

def crear_prediccion(predicction_data):
    data = {
        'peso_sem3' : predicction_data['feature_3'],
        'peso_sem4' : predicction_data['feature_1'],
        'agua' : predicction_data['feature_2'],
        'consumo_acabado' : predicction_data['feature_4'],
        'mortalidad_std' : predicction_data['feature_5'],
        'created_at' : predicction_data['created_at']
    }

    response = client.table('datos_predicciones').insert(data).execute()
    return response

def read_prediccion():
    response = client.table('datos_predicciones').select('*').execute()
    return response.data

def update_prediccion(prediction_id,new_data):
    response = client.table('datos_predicciones').update(new_data).eq('id',prediction_id).execute()
    return response

def delete_prediccion(prediction_id):
    response = client.table('datos_predicciones').delete().eq('id',prediction_id).execute()
    return response