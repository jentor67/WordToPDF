#!/usr/bin/python3
import subprocess

input_path = "Input/sample.doc"
output_path = "Output/libre_output.pdf"

subprocess.run(["unoconv", "-f", "pdf", "-o", output_path, input_path])

