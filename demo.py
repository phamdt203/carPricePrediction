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
        gr.inputs.Number(label="Wheelbase"),
        gr.inputs.Number(label="Length of Car"),
        gr.inputs.Number(label="Width of Car"),
        gr.inputs.Number(label="Height of Car"),
        gr.inputs.Number(label="Weight of Curb"),
        gr.inputs.Number(label="Size of Engine"),
        gr.inputs.Number(label="Ratio of Compression"),
        gr.inputs.Number(label="Horse Power"),
        gr.inputs.Number(label="Peak rpm"),
        gr.inputs.Number(label="High way mpg")
    ],
    outputs="text",
    live=True,
    title="Car Price Prediction"
)

iface.launch()
