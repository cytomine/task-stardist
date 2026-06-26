# Stardist Nuclei Segmentation

This repository packages the [StarDist](https://github.com/stardist/stardist) algorithm into a Cytomine Task compatible with the Cytomine App Engine. It detects and segments cell nuclei in H&E stained histology images using the pre-trained `2D_versatile_HE` model, producing nucleus outlines as GeoJSON polygons along with a per-nucleus detection probability score for each input image.

## GPU Support

GPU acceleration is supported but limited to NVIDIA GPUs only (via CUDA). AMD and other GPU vendors are not supported.

## ROI Support

Each input image may optionally be paired with a GeoJSON file defining a region of interest (ROI). When provided, only nuclei whose centroid falls inside that region are included in the output. To use it, place a file named `<index>.geojson` alongside the image file in the `images/` input array directory (e.g. `images/0.geojson` for the first image).

## How to run it manually

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
