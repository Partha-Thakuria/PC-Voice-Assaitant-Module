from PIL import Image
import os

# def trim_path(original_path=os.path.dirname(os.path.abspath(__file__)), target_path="JARVIS MAIN", add_on=""):
#     index = original_path.find(target_path)
#     without_foward_slash = original_path[:index + len(target_path)] if index != -1 else None
#     return without_foward_slash + add_on



def image_generation_API(prompt, output_file, model="stable-diffusion-2-1-finetuned"):

    import requests # Import the 'requests' module to make HTTP requests
    # hf_api_key = open(r"D:\ALL JARVIS\JARVIS Main\keys\huggingface").readline() # Importing the 'api_key' module to access the API key
    hf_api_key="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"
    '''Preffered Image Format is PNG. Dont Try any other format
    MODEL LIST - stable-diffusion-v1-5, stable-diffusion-xl-base-1.0, stable-diffusion-2-1-finetuned'''

    # API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"  # VERY FAST BUT NOT STABLE
    # API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"  # GOOD AND STABLE BUT SLOW
    # API_URL = "https://api-inference.huggingface.co/models/ARDICAI/stable-diffusion-2-1-finetuned"  # MOST RECENT

    API_URL = f"https://api-inference.huggingface.co/models/ARDICAI/{model}"  # GOOD AND STABLE BUT SLOW
    headers = {"Authorization": f"Bearer {hf_api_key}"} # Set the authorization token in the headers

    # Define a function called 'query' that sends a POST request to the API with a payload
    def query(payload):
        # Make a POST request to the API URL with the provided payload and headers
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content # Return the content of the response (image bytes)
    
    print(f"Generating...", end="\r", flush=True)

    image_bytes = query({
        "inputs": prompt,
    })

    # Save the image content to a file named "image_gen.png"
    with open(output_file, "wb") as f:
        f.write(image_bytes)

    img = Image.open(output_file)
    img.show()
    class Show_Image:
        def __init__(self,li:list) -> None:
            self.listd=li
        def open(self,no):
            try:
                img = Image.open(output_file)
                img.show()
            except:
                print("image was not good")
                self.open(no+1)
        def close(self,no):
            #TODO
            pass
    # print(end="\r", flush=True)

# Check if the script is being run as the main program
if __name__ == "__main__":
    import time
    # Example usage of the 'img_gen' function
    start = time.time()
    image_generation_API("Craft a surreal portrait of a woman with a cosmic aura. Her face should be off-center, with sharp features, large, expressive eyes, and a contemplative gaze. Surround her visage with a nebula-like composition, blending deep blues, purples, and fiery red to symbolize the birth of stars and galaxies. Silhouette of translucent mathematical and geometrical equations, symbols, and lines to represent the fusion of human thought with the infinite universe. The overall image should evoke a daily sense of wonder, intelligence, and the mysterious beauty of the cosmos. (((Double exposure))), bioluminescence, High detail, high quality, high resolution", "generated_image.png")
    
    end = time.time()
    print(f"TIME TAKEN : {end-start} sec")