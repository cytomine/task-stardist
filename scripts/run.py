import sys
import os

from imageio import imread
from typing import Callable, Any, Iterable

import numpy as np
from stardist.models import StarDist2D
from csbdeep.utils import normalize

import geojson
import yaml


INPUT_DIR = "/inputs"
OUTPUT_DIR = "/outputs"
MODEL_DATA_DIR = "/models/"


def from_stardist_to_geojson_string(stardist_polygroup: np.ndarray):
  """
  """
  coordinates = np.vstack(stardist_polygroup[::-1]).transpose().tolist()
  coordinates.append(coordinates[0])
  return geojson.dumps(geojson.Polygon([coordinates], validate=True))


def read_parameter(path: str, cast_fn: Callable[[str], Any], default: Any=None, raise_if_missing: bool=False):
  """
  """
  if not os.path.isfile(path):
    if raise_if_missing:
      raise FileNotFoundError(f"could not find parameter file '{path}'")
    else:
      return default
  with open(path, "r", encoding="utf8") as file:
    content = file.read()
    return cast_fn(content)


def write_array(array_path: str, array_data: Iterable[Any], format_fn: Callable[[Any], str]):
  """
  """
  os.makedirs(array_path, exist_ok=True)
  # writing array metadata
  with open(os.path.join(array_path, "array.yml"), "w+", encoding="utf8") as file:
    yaml.dump({"size": len(array_data)}, file)
  # writing array data content
  for i, data_item in enumerate(array_data):
    with open(os.path.join(array_path, f"{i}"), "w+", encoding="utf8") as file:
      file.write(format_fn(data_item))


def main():
  # Red inputs
  stardist_norm_perc_low = read_parameter(os.path.join(INPUT_DIR, "stardist_norm_perc_low"), cast_fn=float, default=1.0)
  stardist_norm_perc_high = read_parameter(os.path.join(INPUT_DIR, "stardist_norm_perc_high"), cast_fn=float, default=99.0) 
  stardist_prob_t = read_parameter(os.path.join(INPUT_DIR, "stardist_prob_t"), cast_fn=float, default=0.5)
  stardist_nms_t = read_parameter(os.path.join(INPUT_DIR, "stardist_nms_t"), cast_fn=float, default=0.5)
  image_path = os.path.join(INPUT_DIR, "image")

  # use local model file in ~/models/2D_versatile_HE/
  model = StarDist2D(None, name='2D_versatile_HE', basedir=MODEL_DATA_DIR)

  # processing image
  img = normalize(
    imread(image_path),
    stardist_norm_perc_low,
    stardist_norm_perc_high,
    axis=(0, 1)  # normalize channels independently
  )

  # Stardist model prediction with thresholds
  _, details = model.predict_instances(
    img,
    prob_thresh=stardist_prob_t,
    nms_thresh=stardist_nms_t,
    n_tiles=model._guess_n_tiles(img)
  )

  # writing ouputs
  write_array(array_path=os.path.join(OUTPUT_DIR, "nuclei"), array_data=details['coord'], format_fn=from_stardist_to_geojson_string)
  write_array(array_path=os.path.join(OUTPUT_DIR, "probs"), array_data=details['prob'].tolist(), format_fn=str)
    

if __name__ == "__main__":
  main()
