from supabase_connector import crear_cliente

client = crear_cliente()

def crear_prediccion(predicction_data):
    data = {
        'peso_sem3' : predicction_data['feature_3'],
        'peso_sem4' : predicction_data['feature_1'],
        'agua' : predicction_data['feature_2'],
        'consumo_acabado' : predicction_data['feature_4'],
        'mortalidad_std' : predicction_data['feature_5']
    }

    response = client.table('datos_predicciones').insert(data).execute()
    return response
    