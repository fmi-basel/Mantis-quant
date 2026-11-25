<img width="4616" height="2094" alt="Asset 25@600x" src="https://github.com/user-attachments/assets/76e2a7c7-6af2-4ae1-aa83-c03707f78635" />

<br> `Mantis-quant` is a Python package for quantitative analysis of 3D microscopy images and segmented objects, developed as part of the [Mantis ecosystem](https://github.com/fmi-basel/Mantis) for high-content, multiplexed, and volumetric microscopy image analysis.

`Mantis-quant` provides [Fractal](https://fractal-analytics-platform.github.io/) tasks for 3D surface mesh generation, quantification of morphological and intensity features, spherical harmonics-based shape analysis, and spatial annotation of surface meshes. It operates on OME-Zarr datasets and supports region-of-interest (ROI)-based processing.

## Functionality

### 1. Feature measurements

The `feature_measurements` task extracts quantitative features from segmented objects and their corresponding microscopy images, enabling characterization of object morphology and intensity distributions.

<img width="1336" height="345" alt="Screenshot 2026-11-25 at 14 51 23" src="https://github.com/user-attachments/assets/76a99208-6943-4bc9-aaa5-927950b10f65" />

- **Input:** Raw channel image and segmentation label(s)
- **Output:** Table of quantitative object-level features, including:
  - **Spatial features:** centroid coordinates (XY or XYZ).
  - **Shape features:** area/volume, perimeter/surface area, equivalent diameter, bounding box and convex hull measurements, major and minor axis lengths, axis ratio, aspect ratio, extent, solidity, eccentricity, circularity, concavity, and asymmetry.
  - **Intensity features:** mean, minimum, maximum, standard deviation, skewness, kurtosis, and intensity percentiles (25th, 50th, 75th, 90th, 95th, and 99th).
  - **Spatial intensity features:** intensity-weighted centroid and displacement of the intensity-weighted centroid relative to the geometric centroid.
  - **Quality control features:** image border contact (XY and Z) and presence of disconnected components.

### 2. Pixel-based measurements

The `pixel_measurements` task quantifies the number and cumulative intensity of pixels exceeding a user-specified intensity threshold within segmented objects per channel.

<img width="1334" height="344" alt="Screenshot 2026-11-25 at 14 51 33" src="https://github.com/user-attachments/assets/b64f02cc-5755-4565-a92e-bf63d104b9f8" />

- **Input:** Raw channel image, segmentation label(s), and intensity threshold(s).
- **Output:** Table of quantitative object-level measurements, including:
  - **Spatial features:** centroid coordinates (XY or XYZ).
  - **Size measurements:** total number of pixels/voxels within each object.
  - **Threshold-based measurements:** number of pixels/voxels above the intensity threshold and sum of intensities above the threshold.

### 3. Surface mesh generation

The `surface_mesh_multiscale` task generates 3D surface meshes from segmentation label images with configurable smoothing and decimation. These meshes provide a geometric representation of segmented objects, such as cells, organoids, or tissue regions, for downstream morphological analysis and visualization.

<img width="1337" height="339" alt="Screenshot 2026-11-25 at 14 51 46" src="https://github.com/user-attachments/assets/d5f37273-7994-4f7f-b710-5d3cb081a5fe" />


- **Input:** 3D segmentation label image and mesh generation, smoothing, and decimation parameters.
- **Output:** 3D surface meshes (.STL or .VTP).

### 4. Mesh-based measurements

The `mesh_measurements` task quantifies geometric and morphological properties of segmented objects based on their 3D surface meshes, enabling quantitative characterization of object shape and size.

<img width="1339" height="275" alt="Screenshot 2026-11-25 at 14 51 12" src="https://github.com/user-attachments/assets/879b0102-3f1a-442d-8d00-dacafd6de464" />

- **Input:** 3D surface meshes of segmented objects.
- **Output:** Table of mesh-derived morphological features, including:
  - **Shape features:** volume, surface area, sphericity, extent, solidity, concavity, asymmetry, aspect ratio, and normalized surface area-to-volume ratio.

### 5. Annotation of child meshes

The `annotate_child_mesh` task annotates surface meshes of child objects (e.g., individual cells within an organoid or tissue) with extracted intensity or shape features. This enables visualization and spatial analysis of features in their 3D tissue context.

<img width="1328" height="337" alt="Screenshot 2026-11-25 at 14 51 01" src="https://github.com/user-attachments/assets/6a2f1464-9901-4021-a726-35d5b12e1475" />


- **Input:** Surface mesh of child objects and corresponding feature tables.
- **Output:** Surface mesh with vertices annotated with the corresponding child object features (.VTP).

### 6. Annotation of parent meshes with child features

The `annotate_mesh_by_child_features` task maps features of segmented child objects onto the surface mesh of their parent object using projection and tessellation. This enables visualization and spatial analysis of the distribution of child object features across the parent surface.

<img width="1338" height="353" alt="Screenshot 2026-11-25 at 14 50 46" src="https://github.com/user-attachments/assets/3eb5ab91-a7db-441c-9843-020062c3a3bd" />

- **Input:** Parent surface mesh, segmented child objects, and corresponding child feature tables.
- **Output:** Parent surface mesh with vertices annotated with spatially mapped child features (.VTP).

### 7. Spherical harmonic decomposition

The `spherical_harmonics_from_labelimage` task computes spherical harmonics representations of segmented 3D objects assuming star-convex objects.

<img width="1337" height="292" alt="Screenshot 2026-11-25 at 14 51 56" src="https://github.com/user-attachments/assets/f0da1380-2090-44c7-814d-c05cb5fed4a6" />


- **Input:** 3D segmentation label image and spherical harmonics parameters.
- **Output:** Spherical harmonics coefficients, reconstruction error, and optional reconstructed meshes.
  
## Installation

Mantis-quant uses Python 3.11.

A Conda-based installation workflow is:

```bash
conda create -n mantis-quant python=3.11
conda activate mantis-quant

git clone https://github.com/fmi-basel/Mantis-quant.git
cd Mantis-quant
pip install -e .
```

## License

Mantis-quant is distributed under the BSD 3-Clause License, with the exception of bundled third-party code.

Spherical harmonic decomposition uses a modified version of [aics-shparam](https://github.com/AllenCell/aics-shparam), developed by the Allen Institute for Cell Science. The bundled code retains its original Allen Institute Software License, provided in `src/mantis_quant/aics_shparam/LICENSE`.

## Contributors

Developed by [@nrepina](https://github.com/nrepina) in the Liberali Lab at the Friedrich Miescher Institute for Biomedical Research (FMI), Basel, Switzerland, with development support from [@jluethi](https://github.com/jluethi), [@lorenzocerrone](https://github.com/lorenzocerrone), and [@enricotagliavini](https://github.com/enricotagliavini).
