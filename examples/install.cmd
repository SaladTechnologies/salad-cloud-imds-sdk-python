python -m venv .venv
call .venv\Scripts\activate
pip install build
python -m build --outdir dist ..\
pip install dist\salad_cloud_imds_sdk-0.9.0-alpha.3-py3-none-any.whl --force-reinstall
