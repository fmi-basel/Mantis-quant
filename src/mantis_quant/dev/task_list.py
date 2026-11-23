from fractal_task_tools.task_models import CompoundTask, ParallelTask

AUTHORS = "Nicole Repina, Enrico Tagliavini, Tim-Oliver Buchholz, Joel Luethi"
DOCS_LINK = "https://github.com/fmi-basel/Mantis-quant"
INPUT_MODELS = [["fractal_tasks_core", "channels.py", "ChannelInputModel"]]
TASK_LIST = [
CompoundTask(
        name="Spherical Harmonics from Label Image",
        executable_init="fractal/init_select_reference_knowing_all.py",
        executable="fractal/spherical_harmonics_from_labelimage.py",
        meta_init={"cpus_per_task": 1, "mem": 1000},
        meta={"cpus_per_task": 4, "mem": 16000},
        category="Measurement",
        modality="HCS",
        tags=["3D"],
        docs_info="file:task_info/spherical_harmonics_from_label_image.md",
    ),
ParallelTask(
        name="Feature Measurements",
        executable="fractal/feature_measurements.py",
        meta={"cpus_per_task": 4, "mem": 16000},
        category="Measurement",
        tags=["regionprops", "morphology", "intensity"],
        docs_info="file:task_info/feature_measurements.md",
    ),
ParallelTask(
        name="Surface Mesh Multiscale",
        executable="fractal/surface_mesh_multiscale.py",
        meta={"cpus_per_task": 4, "mem": 16000},
        category="Image Processing",
        modality="HCS",
        tags=["3D", "mesh"],
        docs_info="file:task_info/surface_mesh_multiscale.md",
    ),
ParallelTask(
        name="Mesh Measurements",
        executable="fractal/mesh_measurements.py",
        meta={"cpus_per_task": 4, "mem": 16000},
        category="Measurement",
        modality="HCS",
        tags=["3D", "mesh", "morphology"],
        docs_info="file:task_info/mesh_measurements.md",
    ),
CompoundTask(
        name="Annotate Mesh by Child Features",
        executable_init="fractal/init_select_reference_knowing_all.py",
        executable="fractal/annotate_mesh_by_child_features.py",
        meta_init={"cpus_per_task": 1, "mem": 1000},
        meta={"cpus_per_task": 4, "mem": 12000},
        category="Image Processing",
        modality="HCS",
        tags=["3D", "mesh"],
        docs_info="file:task_info/annotate_mesh_by_child_features.md",
        input_types=dict(is_3D=True),
    ),
CompoundTask(
        name="Annotate Child Mesh",
        executable_init="fractal/init_select_reference_knowing_all.py",
        executable="fractal/annotate_child_mesh.py",
        meta_init={"cpus_per_task": 1, "mem": 1000},
        meta={"cpus_per_task": 4, "mem": 12000},
        category="Image Processing",
        modality="HCS",
        tags=["3D", "mesh"],
        docs_info="file:task_info/annotate_child_mesh.md",
        input_types=dict(is_3D=True),
    ),
ParallelTask(
        name="Pixel Measurements",
        executable="fractal/pixel_measurements.py",
        meta={"cpus_per_task": 4, "mem": 16000},
        category="Measurement",
        modality="HCS",
        tags=["2D", "3D", "intensity"],
        docs_info="file:task_info/pixel_measurements.md",
    )
]
