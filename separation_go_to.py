import os

def go_to_mix(mainpath):
    path = mainpath + '\mix'
    os.chdir(path)
    return path

def go_to_mix_folder(mainpath,foldname):
    path = go_to_mix(mainpath) + f'\{foldname}'
    os.chdir(path)
    return path

def go_to_mix_folder_activedir(mainpath, foldname, activedir):
    path = go_to_mix_folder(mainpath,foldname) + f'\{activedir}'
    os.chdir(path)
    return path

def go_to_separation(mainpath):
    path = mainpath + '\separation'
    os.chdir(path)
    return path