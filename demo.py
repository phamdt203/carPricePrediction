import joblib
import gradio as gr
import pickle

loaded_model = joblib.load('random_forest_model.pkl')
with open('important_features.pkl', 'rb') as file:
    features = pickle.load(file)

def predict_price(*feature):
    predicted_price = loaded_model.predict([list(feature)])
    return predicted_price[0]

iface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.inputs.Number(label="Year"),
        gr.inputs.Number(label="Kilometers_Driven"),
        gr.inputs.Number(label="Seats"),
        gr.inputs.Number(label="mileages"),
        gr.inputs.Number(label="engine"),
        gr.inputs.Number(label="power"),
        gr.inputs.Number(label="New Price"),
        gr.inputs.Number(label="Name"),
        gr.inputs.Number(label="Location"),
        gr.inputs.Number(label="Fuel_Type"),
        gr.inputs.Number(label="Transmission"),
        gr.inputs.Number(label="Owner_Type")
    ],
    outputs="text",
    live=True,
    title="Car Price Prediction"
)

iface.launch()