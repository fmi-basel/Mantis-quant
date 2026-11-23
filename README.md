# Mantis-quant

Independent Fractal task package extracted from [Mantis-plex](https://github.com/fmi-basel/Mantis-plex).

## Tasks

- `annotate_child_mesh`
- `annotate_mesh_by_child_features`
- `mesh_measurements`
- `pixel_measurements`
- `feature_measurements`
- `spherical_harmonics_from_labelimage`
- `surface_mesh_multiscale`

## Installation and task manifest

```bash
pip install -e ".[test]"
python -m mantis_quant.dev.task_info.create_manifest
pytest tests
```

The original Mantis-plex repository has not been modified. Internal helper modules are duplicated to avoid runtime dependencies on other Mantis packages.
