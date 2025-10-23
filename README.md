# Stardist Nuclei Segmentation



## How to run it manually ?

### Get the docker image

#### From the task bundle

Either from an existing task bundle

```bash
$> unzip com.cytomine.nuclei.segmentation.stardist-0.1.0.zip
Archive:  ./com.cytomine.nuclei-segmentation.stardist-0.1.0.zip
  inflating: com.cytomine.nuclei.segmentation.stardist-0.1.0.tar
  inflating: descriptor.yml
$> docker image load --input image.tar
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
Loaded image: com/cytomine/nuclei-segmentation/stardist:0.1.0

```

### Build the docker image yourself

```
docker build -t com/cytomine/nuclei-segmentation/stardist:0.1.0 .
```

## Run on data

From this repository, run :

```bash
docker run -v ./examples/inputs:/inputs -v ./local-outputs:/outputs --rm -it com/cytomine/nuclei-segmentation/stardist:0.1.0
```

You can then explore the results in the `./local-outputs` directory.

## Build bundle to upload on Cytomine

1. Build the docker image as described above
2. Build the bundle
```bash
zip com.cytomine.nuclei.segmentation.stardist-0.1.0.zip descriptor.yml com.cytomine.nuclei.segmentation.stardist-0.1.0.tar
```
3. Upload the bundle on Cytomine