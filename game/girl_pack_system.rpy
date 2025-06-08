init python:
    import os, json, random 

    selected_json_data = None  # This will hold the content of the selected JSON

    def load_random_json():
        mods_path = os.path.join(config.gamedir, "girl_packs")
        json_files = []
        # Folder(s) to exclude
        excluded_folders = {"original_premiun_slaves_pack"}

        for root, dirs, files in os.walk(mods_path):
            # Remove excluded folders from dirs to avoid walking into them
            dirs[:] = [d for d in dirs if d not in excluded_folders]

            for file in files:
                if file.lower().endswith(".json"):
                    json_path = os.path.join(root, file)
                    json_files.append(json_path)

        if json_files:
            chosen_path = random.choice(json_files)
            try:
                with open(chosen_path, "r", encoding="utf-8") as f:
                    global selected_json_data
                    selected_json_data = json.load(f)
                    renpy.log(f"Loaded JSON file: {chosen_path}")
            except Exception as e:
                renpy.log(f"Error loading JSON: {chosen_path} → {e}")
        else:
            renpy.log("No JSON files found.")
    load_random_json()
    def load_json(filename):
        try:
            with renpy.loader.load(filename) as f:
                return json.load(f)
        except Exception as e:
            renpy.log(f"Failed to load {filename}: {e}")
            return None
    next_id = 0 # Initialize counter

    def add_slave(slave):
        global next_id       # Tell Python we want to use the external variable
        all_girls_list[next_id] = slave
        next_id += 1         # Increase the counter
    def reduce_check(x,a):
        if all_girls_list[girl_index]["experience"][x][a] <= attributes_min_threshold[all_girls_list[girl_index][x][a]] and all_girls_list[girl_index][x][a] > 0:
            all_girls_list[girl_index]["experience"][x][a] -= attributes_min_threshold[all_girls_list[girl_index][x][a]]
            all_girls_list[girl_index][x][a] = all_girls_list[girl_index][x][a] - 1
    def increase_check(x,a):
        if all_girls_list[girl_index]["experience"][x][a] >= attributes_max_threshold[all_girls_list[girl_index][x][a]] and all_girls_list[girl_index][x][a] < 5:
            all_girls_list[girl_index]["experience"][x][a] -= attributes_max_threshold[all_girls_list[girl_index][x][a]]
            all_girls_list[girl_index][x][a] = all_girls_list[girl_index][x][a] + 1
    def msg(x):
        renpy.call_screen("msg", msg_text=x)
    def meat_evaluation():
        base_meat_gain = all_girls_list[girl_index]["attributes"]["physical"] + 2
        if all_girls_list[girl_index]["age"] == 0:
            base_meat_gain = base_meat_gain*2
        elif all_girls_list[girl_index]["age"] == 2:
            base_meat_gain = base_meat_gain*3
        mince_gain = all_girls_list[girl_index]["attributes"]["physical"] * all_girls_list[girl_index]["boobs"]
        meat_max = 1 + all_girls_list[girl_index]["attributes"]["endurance"]
        if all_girls_list[girl_index]["age"] == 0:
            meat_max = meat_max*2
        elif all_girls_list[girl_index]["age"] == 2:
            meat_max = meat_max*3
        if base_meat_gain > meat_max:
            meat_gain = meat_max
            mince_bonus = base_meat_gain - meat_max
        else:
            meat_gain = base_meat_gain
            mince_gain += mince_bonus
        if all_girls_list[girl_index]["age"] == 1 or ( all_girls_list[girl_index]["age"] == 0 and all_girls_list[girl_index]["vaginal_tightness"] == 0):
            virgin_meat_gain = meat_gain
            meat_gain = 0
        else:
            virgin_meat_gain = 0
        meat_price = mince_gain + meat_gain*2 + virgin_meat_gain*4
        return(meat_price)


            