import os
from io import BytesIO

import numpy as np
from PIL import Image
import cv2
import tensorflow as tf
import sys
import datetime


class DeepLabModel(object):
  INPUT_TENSOR_NAME = 'ImageTensor:0'
  OUTPUT_TENSOR_NAME = 'SemanticPredictions:0'
  INPUT_SIZE = 513
  FROZEN_GRAPH_NAME = 'frozen_inference_graph'

  def __init__(self, tarball_path):
    
    self.graph = tf.Graph()

    graph_def = None
    graph_def = tf.GraphDef.FromString(open(tarball_path + "/frozen_inference_graph.pb", "rb").read()) 

    if graph_def is None:
      raise RuntimeError('Cannot find inference graph in tar archive.')

    with self.graph.as_default():
      tf.import_graph_def(graph_def, name='')

    self.sess = tf.Session(graph=self.graph)

  def run(self, image):
    start = datetime.datetime.now()

    width, height = image.size
    resize_ratio = 1.0 * self.INPUT_SIZE / max(width, height)
    target_size = (int(resize_ratio * width), int(resize_ratio * height))
    resized_image = image.convert('RGB').resize(target_size, Image.ANTIALIAS)
    batch_seg_map = self.sess.run(
        self.OUTPUT_TENSOR_NAME,
        feed_dict={self.INPUT_TENSOR_NAME: [np.asarray(resized_image)]})
    seg_map = batch_seg_map[0]

    end = datetime.datetime.now()

    diff = end - start
    #print("Time taken to evaluate segmentation is : " + str(diff))

    return resized_image, seg_map


def show_image(img,title):
    img = cv2.imread('output.png')
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title, 450,450)
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def drawSegment(baseImg, matImg):
  width, height = baseImg.size
  dummyImg = np.zeros([height, width, 4], dtype=np.uint8)
  for x in range(width):
            for y in range(height):
                color = matImg[y,x]
                (r,g,b) = baseImg.getpixel((x,y))
                if color == 0:
                    dummyImg[y,x,3] = 0
                else :
                    dummyImg[y,x] = [r,g,b,255]
  img = Image.fromarray(dummyImg)
  img.save("output.png")
  show_image(img,"ads")

modelType = "mobile_net_model"
if len(sys.argv) > 3 and sys.argv[3] == "1":
  modelType = "xception_model"

MODEL = DeepLabModel(modelType)
print('model loaded successfully : ' + modelType)

imgPath='yavru-kopek.jpg'






#cv2.imread('img/yavru-kopek.jpg', cv2.IMREAD_GRAYSCALE)

def run_visualization(filepath):
  jpeg_str = open(filepath, "rb").read()
  img = Image.open(BytesIO(jpeg_str))
  orignal_im = Image.open(BytesIO(jpeg_str))
  print('running deeplab on image %s...' % filepath)
  resized_im, seg_map = MODEL.run(orignal_im)

  # vis_segmentation(resized_im, seg_map)
  drawSegment(resized_im, seg_map)

run_visualization(imgPath)

