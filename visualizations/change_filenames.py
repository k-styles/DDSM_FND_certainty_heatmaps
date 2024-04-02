import os

folder_path = "./BPC-FND/predictions_at_0.3"
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        image_id, _, _, _, _ = filename.split("-")
        new_filename = f"{image_id}-bpcfnd_pred.png"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
