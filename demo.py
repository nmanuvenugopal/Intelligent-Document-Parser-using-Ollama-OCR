from ollama_ocr import OCRProcessor

ocr = OCRProcessor(model_name="granite3.2-vision")

result  = ocr.process_image(
    image_path='/Users/manuvenugopalan/Documents/Programming/Ollama_OCR/Input/img.png',
    format_type='text',
    language='eng'
)

print(result)