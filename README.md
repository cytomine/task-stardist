# Stardist Nuclei Segmentation

This repository packages the [StarDist](https://github.com/stardist/stardist) algorithm into a Cytomine Task compatible with the Cytomine App Engine. It detects and segments cell nuclei in H&E stained histology images using the pre-trained `2D_versatile_HE` model, producing nucleus outlines as GeoJSON polygons along with a per-nucleus detection probability score for each input image.

## GPU Support

GPU acceleration is supported but limited to NVIDIA GPUs only (via CUDA). AMD and other GPU vendors are not supported.

## ROI Support

Each input image may optionally be paired with a GeoJSON file defining a region of interest (ROI). When provided, only nuclei whose centroid falls inside that region are included in the output. To use it, place a file named `<index>.geojson` alongside the image file in the `images/` input array directory (e.g. `images/0.geojson` for the first image).

## How to run it manually

### Get the docker image from a task bundle

```bash
$> unzip com.cytomine.nuclei.segmentation.stardist-1.1.0.zip
Archive:  ./com.cytomine.nuclei-segmentation.stardist-1.1.0.zip
  inflating: com.cytomine.nuclei.segmentation.stardist-1.1.0.tar
  inflating: descriptor.yml
$> docker image load --input com.cytomine.nuclei.segmentation.stardist-1.1.0.tar
0949773899cf: Loading layer [==================================================>]   84.2MB/84.2MB
95c8f57bd29d: Loading layer [==================================================>]  3.405MB/3.405MB
95ce64f868d0: Loading layer [==================================================>]  30.56MB/30.56MB
eca2faa8f0ea: Loading layer [==================================================>]   5.12kB/5.12kB
d6bd5066234c: Loading layer [==================================================>]  12.91MB/12.91MB
631efc3b95e1: Loading layer [==================================================>]  1.536kB/1.536kB
c70e485b159b: Loading layer [==================================================>]   2.56kB/2.56kB
84cc4f8d1ed4: Loading layer [==================================================>]  2.087GB/2.087GB
e05ca7daf251: Loading layer [==================================================>]   5.78MB/5.78MB
987f4b5a221e: Loading layer [==================================================>]  6.656kB/6.656kB
Loaded image: com/cytomine/nuclei-segmentation/stardist:1.1.0
```

### Build the docker image yourself

```bash
docker build -t com/cytomine/nuclei-segmentation/stardist:1.1.0 .
```

## Run on data

From this repository, run:

```bash
docker run --gpus all -v ./examples/inputs:/inputs -v ./local-outputs:/outputs --rm -it com/cytomine/nuclei-segmentation/stardist:1.1.0
```

You can then explore the results in the `./local-outputs` directory.

## Build bundle to upload on Cytomine

1. Build the docker image as described above
2. Save it as a `tar` archive:
```bash
docker save -o com.cytomine.nuclei.segmentation.stardist-1.1.0.tar com/cytomine/nuclei-segmentation/stardist:1.1.0
```
3. Build the bundle:
```bash
zip com.cytomine.nuclei.segmentation.stardist-1.1.0.zip descriptor.yml com.cytomine.nuclei.segmentation.stardist-1.1.0.tar
```
4. Upload the bundle on Cytomine
