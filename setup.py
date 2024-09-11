from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6", "shiboken6"],
    "includes": ["jinja2", "jinja2.ext"],
    "bin_path_includes": ["templates"]
}

setup(
    name="RTMPServer",
    version="0.1",
    description="Servidor de Streaming RTMP!",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py", base="console", icon="icon.ico")],
)