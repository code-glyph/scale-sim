from scalesim.scale_sim import scalesim

topo_path = "scale-sim-v2/topologies/conv_nets/"
configs = "scale-sim-v2/configs"
models = ["custom"]
dataflows = ["ws","os","is"]
sizes = [72, 18]
for model in models:
    for s in sizes:
        for j in dataflows:
            topo = topo_path + f"{model}.csv"
            filepath = f"{model}"
            #config = configs + f"/{s}_{s}_{j}_1.cfg"
            config = configs + f"/{s}_{j}.cfg"
            #print(config)
            runsim = scalesim(save_disk_space=False, verbose=True,
                  config=config,
                  topology=topo)
            runsim.run_scale(top_path=filepath)