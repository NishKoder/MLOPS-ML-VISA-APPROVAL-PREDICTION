from pathlib import Path


def create_project_structure(proj_name: str) -> None:
    base_paths = [
        Path(f"{proj_name}/components"),
        Path(f"{proj_name}/configuration"),
        Path(f"{proj_name}/constants"),
        Path(f"{proj_name}/entity"),
        Path(f"{proj_name}/exception"),
        Path(f"{proj_name}/logger"),
        Path(f"{proj_name}/pipeline"),
        Path(f"{proj_name}/utils"),
        Path("research"),
        Path("config"),
        Path("flowchart"),
    ]

    files_with_paths = [
        Path(f"{proj_name}/__init__.py"),
        Path(f"{proj_name}/components/__init__.py"),
        Path(f"{proj_name}/components/data_ingestion.py"),
        Path(f"{proj_name}/components/data_transformation.py"),
        Path(f"{proj_name}/components/data_validation.py"),
        Path(f"{proj_name}/components/model_evaluation.py"),
        Path(f"{proj_name}/components/model_trainer.py"),
        Path(f"{proj_name}/components/model_pusher.py"),
        Path(f"{proj_name}/configuration/__init__.py"),
        Path(f"{proj_name}/constants/__init__.py"),
        Path(f"{proj_name}/entity/__init__.py"),
        Path(f"{proj_name}/entity/artifact_entity.py"),
        Path(f"{proj_name}/entity/config_entity.py"),
        Path(f"{proj_name}/exception/__init__.py"),
        Path(f"{proj_name}/logger/__init__.py"),
        Path(f"{proj_name}/pipeline/__init__.py"),
        Path(f"{proj_name}/pipeline/training_pipeline.py"),
        Path(f"{proj_name}/pipeline/prediction_pipeline.py"),
        Path(f"{proj_name}/utils/__init__.py"),
        Path(f"{proj_name}/utils/main_utils.py"),
        Path("research/trials.ipynb"),
        Path("config/model.yaml"),
        Path("config/schema.yaml"),
        Path("app.py"),
        Path("requirements.txt"),
        Path("Dockerfile"),
        Path("demo.py"),
        Path("setup.py"),
        Path(".dockerignore")
    ]

    [
        path.mkdir(
            parents=True,
            exist_ok=True
        ) if path not in files_with_paths else
        (path.parent.mkdir(parents=True, exist_ok=True), path.touch())
        for path in base_paths + files_with_paths
    ]

    print(f"Project structure for '{proj_name}' created successfully.")


if __name__ == "__main__":
    project_name = "us_visa"  # Set your project name here
    create_project_structure(
        proj_name=project_name
    )
