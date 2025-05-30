from imageai.Detection import VideoObjectDetection

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
input_path = "./input/vid.mp4"
output_path = "./output/detected_vid"

detector = VideoObjectDetection()
detector.setModelTypeAsTinyYOLOv3()

detector.setModelPath(model_path)
detector.loadModel()

detection = detector.detectObjectsFromVideo(input_file_path=input_path, output_file_path=output_path, frames_per_second=20)
