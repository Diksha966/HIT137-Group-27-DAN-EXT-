from model_text import TextModelHandler
from model_image import ImageModelHandler

def main():
    # Text example
    text_handler = TextModelHandler()
    result_text = text_handler.run("I enjoy studying and building small projects.")
    print("Text result:", result_text)

    # Image example
    image_handler = ImageModelHandler()
    result_image = image_handler.run("sample_inputs/cat.jpg")
    print("Image result:", result_image)

if __name__ == "__main__":
    main()