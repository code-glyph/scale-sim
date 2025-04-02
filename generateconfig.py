
def generate_cfg_file(filename, architecture_presets, run_presets, general):
    with open(filename, 'w') as file:
        # Writing architecture_presets section
        file.write("[architecture_presets]\n")
        for key, value in architecture_presets.items():
            file.write(f"{key}: {value}\n")

        # Writing run_presets section
        file.write("\n[run_presets]\n")
        for key, value in run_presets.items():
            file.write(f"{key}: {value}\n")

        # Writing general section
        file.write("\n[general]\n")
        for key, value in general.items():
            file.write(f"{key} = {value}\n")


# Input data
array_values = [32] # Range of values for ArrayHeight and ArrayWidth
SRAM_values = [18, 72]

architecture_presets_template = {
    "IfmapSramSzkB": 36,
    "FilterSramSzkB": 36,
    "OfmapSramSzkB": 36,
    "IfmapOffset": 0,
    "FilterOffset": 10000000,
    "OfmapOffset": 20000000,
    "Bandwidth": 10,
    "MemoryBanks": 1,
}

run_presets = {
    "InterfaceBandwidth": "CALC",
}

general_template = {
    "run_name": "{Size}_{Dataflow}",
}

dataflows = ["ws", "os", "is"]
for df in dataflows:
    for height in array_values:
        for SRAM in SRAM_values:
            architecture_presets = architecture_presets_template.copy()
            general = general_template.copy()

            # Update ArrayHeight and ArrayWidth
            architecture_presets["ArrayHeight"] = height
            architecture_presets["ArrayWidth"] = height
            architecture_presets["Dataflow"] = df
            architecture_presets["IfmapSramSzkB"] = SRAM
            architecture_presets["FilterSramSzkB"] = SRAM
            architecture_presets["OfmapSramSzkB"] = SRAM
            # Update run_name in general section
            general["run_name"] = general_template["run_name"].format(Size=SRAM, Dataflow = df)

            # Generate the file name
            filename = f"scale-sim-v2/configs/{SRAM}_{df}.cfg"
            print(filename)
            # Create the .cfg file
            generate_cfg_file(filename, architecture_presets, run_presets, general)

print("Configuration files generated successfully!")