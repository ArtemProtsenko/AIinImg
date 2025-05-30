from imageai.Detection import ObjectDetection

import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_virtual_device_configuration(
            gpus[0],
            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=2048)])
    except RuntimeError as e:
        print(e)


model_path = "./models/yolo-tiny.h5"
input_path = "./input/img4.png"
output_path = "./output/new_image.jpg"

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()

detector.setModelPath(model_path)
detector.loadModel()
detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

for item in detection:
    print(f"{item['name']}:{item['percentage_probability']}%")
